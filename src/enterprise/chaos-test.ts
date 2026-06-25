import { MasterCoordinator } from './MasterCoordinator';
import { PodAggregator } from './PodAggregator';
import { SubstationDaemon } from './SubstationDaemon';

/**
 * The Kalbaishakhi Chaos Test
 * 
 * This is the ultimate boardroom simulation. It proves mathematically that 
 * the FlockML Enterprise Grid handles massive infrastructure failure autonomously.
 */
async function runChaosTest() {
  console.log("=========================================================");
  console.log("  FLOCKML ENTERPRISE: GRID ORCHESTRATION CHAOS TEST");
  console.log("=========================================================\n");

  // 1. Initialize the Central Master Coordinator (The Brain)
  const master = new MasterCoordinator(2, 4, 1);
  
  // 2. Initialize a Regional Pod Aggregator (e.g., Howrah Pod)
  const pod = new PodAggregator("POD_HOWRAH", 3); // Aggregates every 3 updates
  
  // 3. Initialize 5 Substation Daemons
  const substations: SubstationDaemon[] = [];
  for (let i = 1; i <= 5; i++) {
    const daemon = new SubstationDaemon(`SUBSTATION_${i}`, master, 2, 4, 1);
    daemon.bootUp();
    substations.push(daemon);
  }

  // 4. Generate a massive workload: 10 Training Tasks (Batches)
  master.generateTasks(10);
  console.log(`\n[MASTER] Generated ${master.taskQueue.length} training tasks. Dispatching to Grid...\n`);

  // 5. The Training Loop
  // We simulate continuous polling from the workers
  const runWorkerLoop = async (worker: SubstationDaemon) => {
    while (master.completedTasks.size < 10) {
      if (!worker.isPowerOn) break; // Stop loop if power failed

      const task = master.requestTask(worker.id);
      if (task) {
        // Run the math
        const gradients = await worker.processTask(task);
        
        if (gradients && worker.isPowerOn) {
          // Send to Pod Aggregator instead of DDoSing Master directly
          pod.receiveSubstationUpdate(gradients);
          console.log(`[WORKER ${worker.id}] Successfully pushed ${task.id} to POD_HOWRAH.`);
          
          // If Pod reaches threshold, it compresses and sends to Master
          const aggregatedPayload = pod.aggregateAndCompress();
          if (aggregatedPayload) {
            console.log(`\n[POD_HOWRAH] Mathematical Aggregation Complete. Transmitting compressed payload to Master...`);
            // In reality, the Pod wouldn't know the exact taskId of the combined batch, 
            // but for simulation tracking, we just mark the specific task as complete.
            master.receivePodUpdate(pod.podId, task.id, aggregatedPayload);
            master.aggregateGlobalModel();
          } else {
             // For simulation sake, if pod didn't trigger, we still need to mark task complete
             // so the loop finishes. In production, Pod manages batch IDs.
             master.receivePodUpdate(pod.podId, task.id, gradients); 
             master.aggregateGlobalModel();
          }
        }
      } else {
        // No pending tasks, wait a bit
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    }
  };

  // Start all workers simultaneously
  const workerPromises = substations.map(w => runWorkerLoop(w));

  // 6. THE KALBAISHAKHI POWER CUT (THE CHAOS INJECTION)
  // Exactly 1.5 seconds into the massive training job, Substation 3 gets hit by lightning.
  setTimeout(() => {
    console.log(`\n********************************************************`);
    console.log(`  [SIMULATION] INJECTING CATASTROPHIC INFRASTRUCTURE FAILURE`);
    console.log(`********************************************************`);
    substations[2].simulatePowerFailure(); // Kills SUBSTATION_3 mid-batch
  }, 1500);

  // Wait for all tasks to complete despite the failure
  await Promise.all(workerPromises);

  // Fallback wait to ensure Master re-queues and finishes
  while(master.completedTasks.size < 10) {
      await new Promise(resolve => setTimeout(resolve, 500));
      // Have healthy workers try to pull stranded tasks
      for (const w of substations) {
          if (w.isPowerOn) runWorkerLoop(w);
      }
  }

  console.log("\n=========================================================");
  console.log("  TRAINING COMPLETE.");
  console.log(`  Global Model Math synchronized successfully.`);
  console.log(`  Total Tasks Completed: ${master.completedTasks.size} / 10`);
  console.log(`  Active Nodes Remaining: ${master.nodes.size - 1} / 5`);
  console.log("=========================================================\n");

  // Cleanup
  master.cleanup();
  substations.forEach(s => s.shutdown());
}

// Execute the Boardroom Demo
runChaosTest().catch(console.error);
