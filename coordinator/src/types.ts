export interface QuantizedPayload {
  min: number;
  max: number;
  rows: number;
  cols: number;
  data: number[]; // 8-bit quantized values (0-255)
}

export interface ClientGradientUpdate {
  nodeId: string;
  roundId: number;
  timestamp?: number;
  weights_ih: QuantizedPayload;
  weights_ho: QuantizedPayload;
  bias_h: QuantizedPayload;
  bias_o: QuantizedPayload;
  hardwareConfig?: {
    deviceType: string;
    hasWebGPU: boolean;
    hasWasmSimd: boolean;
  };
}

export interface WebRtcSignalPacket {
  targetNodeId: string;
  senderNodeId: string;
  signalType: 'SDP_OFFER' | 'SDP_ANSWER' | 'ICE_CANDIDATE';
  signalData: any;
}

export interface WsMessage {
  type: 'JOIN_SWARM' | 'GRADIENT_SUBMIT' | 'HEARTBEAT' | 'REQUEST_WEIGHTS' | 'WEBRTC_SIGNAL';
  nodeId: string;
  payload?: any;
}

export interface SwarmStats {
  activeNodes: number;
  totalRoundsCompleted: number;
  totalGradientsAggregated: number;
  poisonedPayloadsRejected: number;
  bftFilterPassRate: number;
  globalEpsilonPrivacy: number;
  nodeTypes: { [key: string]: number };
  lastAggregationTimestamp: string | null;
}
