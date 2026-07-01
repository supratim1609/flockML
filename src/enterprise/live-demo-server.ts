import { WebSocketServer } from 'ws';
import { LegacyNeuralNetwork as NeuralNetwork } from './legacy-network';
import { MasterCoordinator } from './MasterCoordinator';
import { SubstationDaemon } from './SubstationDaemon';

console.log("=========================================");
console.log(" flockML Live Demo Backend Started");
console.log("=========================================");

// 1. Initialize Master
const master = new MasterCoordinator(2, 3, 1);
master.generateTasks(1000); // Queue up 1000 tasks for a longer demo

let eventLogs: string[] = [];
function addLog(msg: string) {
  const time = new Date().toLocaleTimeString();
  eventLogs.unshift(`[${time}] ${msg}`);
  if (eventLogs.length > 20) eventLogs.pop();
}

addLog("Master Coordinator Initialized.");

// 2. Initialize 5 Substations
const daemons: SubstationDaemon[] = [];
for (let i = 1; i <= 5; i++) {
  const daemon = new SubstationDaemon(`SUB-${i}`, master, 2, 3, 1);
  daemon.bootUp();
  daemons.push(daemon);
}

// 3. Worker Loop (Substations continuously pulling tasks)
async function workerLoop(daemon: SubstationDaemon) {
  while (true) {
    if (daemon.isPowerOn) {
      const task = master.requestTask(daemon.id);
      if (task) {
        const payload = await daemon.processTask(task);
        if (payload) {
          master.receivePodUpdate(daemon.id, task.id, payload);
        }
      }
    }
    // Small delay before next request
    await new Promise(r => setTimeout(r, 200));
  }
}

// Start all worker loops
daemons.forEach(d => workerLoop(d));

// 4. WebSocket Server
const wss = new WebSocketServer({ port: 8080 });
console.log("[WSS] WebSocket Server running on ws://localhost:8080");

wss.on('connection', (ws) => {
  console.log("[WSS] UI Dashboard Connected!");
  
  // Listen for commands from the UI
  ws.on('message', (message) => {
    try {
      const command = JSON.parse(message.toString());
      if (command.type === 'KILL_NODE') {
        const daemon = daemons.find(d => d.id === command.nodeId);
        if (daemon && daemon.isPowerOn) {
          addLog(`⚡ MANUAL COMMAND: Operator initiated kill switch on ${daemon.id}.`);
          daemon.simulatePowerFailure();
          
          // Force the Master to instantly recognize the failure for the UI
          const masterNode = master.nodes.get(daemon.id);
          if (masterNode) {
             masterNode.lastHeartbeat = 0; // Triggers immediate rerouting on next 500ms tick
          }
          
          // Still revive it after 5 seconds for the demo loop
          setTimeout(() => {
            console.log(`[RECOVERY] Rebooting Substation ${daemon.id}...`);
            daemon.bootUp();
            addLog(`✅ RECOVERY: ${daemon.id} rebooted and reconnected to grid.`);
          }, 5000);
        }
      }
    } catch (e) {
      console.error("Invalid WS message");
    }
  });
});

// 4.5. Run FedAvg Aggregation periodically
setInterval(() => {
  if ((master as any).pendingUpdates.length > 0) {
    master.aggregateGlobalModel();
    addLog(`🧠 AI ENGINE: Executed FedAvg on pending node updates. Global Model optimized.`);
  }
}, 3000);

// 5. Broadcast State to UI
setInterval(() => {
  const nodesArr = Array.from(master.nodes.values());
  // Extract a small slice of the actual Neural Network weights to prove the math is real
  const rawMatrixRow = master.globalModel.weights_ho.data[0] || [];
  
  const payload = JSON.stringify({
    type: 'GRID_STATE',
    data: {
      nodes: nodesArr,
      tasks: master.taskQueue.slice(0, 15), // send top 15 tasks for the UI
      logs: eventLogs,
      matrixSnapshot: rawMatrixRow // The real math
    }
  });

  wss.clients.forEach(client => {
    if (client.readyState === 1) { // OPEN
      client.send(payload);
    }
  });
}, 200);

// 6. The Chaos Engine (Kalbaishakhi Simulation)
setInterval(() => {
  // Pick a random daemon
  const randomDaemon = daemons[Math.floor(Math.random() * daemons.length)];
  
  if (randomDaemon.isPowerOn) {
    randomDaemon.simulatePowerFailure();
    addLog(`⚠️ HARDWARE ALERT: ${randomDaemon.id} power failure! Node dead.`);
    
    // Revive it after 5 seconds
    setTimeout(() => {
      console.log(`[RECOVERY] Rebooting Substation ${randomDaemon.id}...`);
      randomDaemon.bootUp();
      addLog(`✅ RECOVERY: ${randomDaemon.id} rebooted and reconnected to grid.`);
    }, 5000);
  }
}, 8000);

// We also need to hack the master to log reroutes
const originalMonitor = (master as any).monitorGridHealth.bind(master);
(master as any).monitorGridHealth = () => {
  const before = [...master.taskQueue.map(t => ({id: t.id, status: t.status, retryCount: t.retryCount}))];
  originalMonitor();
  const after = master.taskQueue;
  for (let i = 0; i < before.length; i++) {
    if (before[i].status === 'RUNNING' && after[i].status === 'PENDING' && after[i].retryCount > before[i].retryCount) {
      addLog(`🔄 FAULT TOLERANCE: Rerouted stranded task ${after[i].id} back to DAG queue.`);
    }
  }
};
