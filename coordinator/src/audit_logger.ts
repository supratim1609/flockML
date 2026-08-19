import crypto from 'crypto';

export type SecurityEventType = 
  | 'SECURITY_NODE_JOIN'
  | 'SECURITY_NODE_DISCONNECT'
  | 'SECURITY_GRADIENT_ACCEPTED'
  | 'SECURITY_POISON_REJECT'
  | 'SECURITY_RATE_LIMIT_EXCEEDED'
  | 'SECURITY_OOB_PAYLOAD_DROP'
  | 'SECURITY_OVERSIZED_PAYLOAD_DROP'
  | 'SECURITY_TEST_AUDIT';

export interface AuditLogEntry {
  timestamp: string;
  eventType: SecurityEventType;
  ipAddress?: string;
  nodeId?: string;
  details: string;
  bftPassed?: boolean;
  logHash?: string;
}

export class CertInAuditLogger {
  private static lastHash: string = 'GENESIS_SECURE_HASH_CHAIN_0000000000000000';
  private static recentLogs: AuditLogEntry[] = [];

  /**
   * Format ISO 8601 timestamp compliant with CERT-In Directive Section 4 (NTP Synchronized Log Format).
   */
  private static getTimestamp(): string {
    return new Date().toISOString();
  }

  /**
   * Emit structured audit log entry to standard log stream with SHA-256 hash chaining.
   */
  public static log(eventType: SecurityEventType, nodeId: string, details: string, extra?: Partial<AuditLogEntry>): AuditLogEntry {
    const timestamp = this.getTimestamp();
    const hashData = `${this.lastHash}|${timestamp}|${eventType}|${nodeId}|${details}`;
    const logHash = crypto.createHash('sha256').update(hashData).digest('hex');
    this.lastHash = logHash;

    const entry: AuditLogEntry = {
      timestamp,
      eventType,
      nodeId,
      details,
      logHash,
      ...extra
    };

    this.recentLogs.push(entry);
    if (this.recentLogs.length > 100) this.recentLogs.shift();

    const logLine = `[CERT-In AUDIT] [${entry.timestamp}] [${entry.eventType}] [Hash:${logHash.substring(0, 8)}] Node:${entry.nodeId || 'UNKNOWN'} - ${entry.details}`;
    
    if (eventType.includes('REJECT') || eventType.includes('DROP') || eventType.includes('EXCEEDED')) {
      console.warn(logLine);
    } else {
      console.log(logLine);
    }

    return entry;
  }

  public static getRecentLogs(count: number = 10): AuditLogEntry[] {
    return this.recentLogs.slice(-count);
  }
}

