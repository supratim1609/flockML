import os

DOCS_DIR = '/Users/supratim/Desktop/flockml-sovereign/docs'

# Shared minimal CSS header
def get_html_wrapper(title, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #000000;
      --surface: #080808;
      --raised: #040404;
      --border: #1A1A1A;
      --border-s: #111111;
      --t1: #FFFFFF;
      --t2: #999999;
      --t3: #666666;
      --t4: #444444;
      --blue: #3B82F6;
      --green: #34D399;
      --gold: #FBBF24;
      --red: #F87171;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--t1);
      font-family: 'Inter', -apple-system, sans-serif;
      line-height: 1.6;
      padding: 40px 24px;
      max-width: 1040px;
      margin: 0 auto;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
      margin-bottom: 32px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }}
    .brand {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }}
    .subhead {{
      font-size: 14px;
      color: var(--t2);
      margin-top: 4px;
    }}
    .tag {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--t3);
      padding: 4px 10px;
      border: 1px solid var(--border);
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}
    h2 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 19px;
      font-weight: 700;
      color: var(--t1);
      margin: 28px 0 12px;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border-s);
      letter-spacing: -0.3px;
    }}
    p {{
      color: var(--t2);
      font-size: 14.5px;
      margin-bottom: 14px;
      line-height: 1.65;
    }}
    p strong, li strong {{ color: var(--t1); }}
    .g2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin: 16px 0; }}
    .g3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin: 16px 0; }}
    .g4 {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 12px; margin: 16px 0; }}
    .c {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .c-t {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--t3);
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    .c-v {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 26px;
      font-weight: 700;
      color: var(--t1);
      margin-bottom: 4px;
    }}
    .c-vs {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--t3);
      margin-bottom: 8px;
    }}
    .c-b {{
      font-size: 13px;
      color: var(--t2);
      line-height: 1.55;
    }}
    .mono-box {{
      background: var(--raised);
      border: 1px solid var(--border);
      padding: 16px 20px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      color: #E2E8F0;
      line-height: 1.7;
      margin: 16px 0;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0;
      font-size: 13.5px;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 12px 14px;
      text-align: left;
    }}
    th {{
      background: var(--surface);
      color: var(--t3);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    td {{ color: var(--t2); }}
    ul, ol {{ margin-left: 20px; margin-bottom: 16px; color: var(--t2); font-size: 14px; }}
    li {{ margin-bottom: 8px; }}
    .quote-block {{
      border-left: 2px solid var(--t1);
      padding-left: 16px;
      font-size: 15px;
      color: var(--t1);
      margin: 18px 0;
      line-height: 1.6;
    }}
    .footer {{
      border-top: 1px solid var(--border-s);
      padding-top: 16px;
      margin-top: 40px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--t4);
      display: flex;
      justify-content: space-between;
    }}
    @media print {{
      body {{ background: #000000 !important; color: #FFFFFF !important; padding: 20px; }}
      .c, .mono-box, th {{ background: #080808 !important; border-color: #222 !important; }}
    }}
  </style>
</head>
<body>

{content}

</body>
</html>"""

def build_html_1():
    # 1. Master Strategic Plan & Economics
    content = """
  <header>
    <div>
      <div class="brand">FLOCKML &times; CESC / RPSG GROUP</div>
      <div class="subhead">Master Strategic Plan: Energy-Compute Arbitrage &amp; Sovereign AI Cloud Monetization</div>
    </div>
    <div class="tag">STRATEGIC BLUEPRINT</div>
  </header>

  <h2>1. The Strategic Opportunity: Energy-to-Compute Arbitrage</h2>
  <p>
    Artificial intelligence infrastructure worldwide is constrained by a single physical bottleneck: <strong>electricity availability and power cost</strong>. Public cloud datacenters (AWS, Microsoft, Google) pay commercial electricity rates (Rs 12–14 per kWh) and spend billions building datacenters.
  </p>
  <p>
    <strong>CESC holds the ultimate unfair advantage:</strong> raw electricity at generation cost (<strong>Rs 3.50/kWh</strong>), 100+ secure substation locations across Kolkata, optical ground wire (OPGW) dark fiber, and 5,000+ workstations sitting idle every night.
  </p>

  <div class="g3">
    <div class="c">
      <div class="c-t">ARBITRAGE FACTOR 01</div>
      <div class="c-v">Rs 3.50</div>
      <div class="c-vs">POWER COST / KWH</div>
      <div class="c-b">Electricity constitutes 60%+ of AI datacenter operating costs. CESC operates at generation-level energy margins.</div>
    </div>
    <div class="c">
      <div class="c-t">ARBITRAGE FACTOR 02</div>
      <div class="c-v">100+ Hubs</div>
      <div class="c-vs">SUBSTATION SITES</div>
      <div class="c-b">Physical real estate across Kolkata &amp; Howrah equipped with power step-downs, cooling, and high-security perimeters.</div>
    </div>
    <div class="c">
      <div class="c-t">ARBITRAGE FACTOR 03</div>
      <div class="c-v">80%+</div>
      <div class="c-vs">SOFTWARE GROSS MARGIN</div>
      <div class="c-b">Transitions CESC from tariff-capped electricity distribution to unregulated, high-margin AI compute token sales.</div>
    </div>
  </div>

  <h2>2. The Revenue Model: Rs 50–100 Crore / Year New Business Line</h2>
  <p>
    By pooling idle substation PCs and night workstations via FlockML's WebGPU orchestration engine, CESC launches <strong>Bengal's First Sovereign AI Compute Cloud</strong>.
  </p>

  <div class="mono-box">
    <strong>COMMERCIAL REVENUE-SHARE MODEL (80 / 20 SPLIT):</strong><br>
    &bull; Total AI Compute Token Sales: <strong>Rs 60.0 Crores / year</strong><br>
    &bull; <strong>CESC Revenue Share (80%):</strong> <strong>Rs 48.0 Crores / year</strong> (Pure new unregulated P&amp;L profit)<br>
    &bull; <strong>FlockML Software Share (20%):</strong> <strong>Rs 12.0 Crores / year</strong> (Platform maintenance, shaders, ZK verification)
  </div>

  <h2>3. RPSG Conglomerate Synergies: Keeping AI Spend In-House</h2>
  <table>
    <thead>
      <tr>
        <th>RPSG Subsidiary</th>
        <th>Current Problem / Spend</th>
        <th>FlockML Sovereign Solution</th>
        <th>Annual Financial Impact</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>CESC Power</strong></td>
        <td>Smart meter cloud ingestion &amp; transformer thermal overload risk.</td>
        <td>Local on-premises telemetry inference across 100+ substations.</td>
        <td><strong style="color: var(--green);">Saves Rs 3–5 Cr/yr</strong> + 0% CEA risk.</td>
      </tr>
      <tr>
        <td><strong>Firstsource</strong></td>
        <td>$1B+ BPO spending millions on third-party OpenAI/AWS support bots.</td>
        <td>Private on-soil LLM inference grid powered by CESC substations.</td>
        <td><strong style="color: var(--blue);">Cuts AI OpEx by ~70%</strong> across contact centers.</td>
      </tr>
      <tr>
        <td><strong>Woodlands Hospital</strong></td>
        <td>Patient healthcare data cannot legally be sent to foreign clouds.</td>
        <td>100% on-premises clinical diagnostics and radiology NLP.</td>
        <td><strong style="color: var(--gold);">100% On-soil</strong> patient data compliance.</td>
      </tr>
      <tr>
        <td><strong>Spencer's Retail</strong></td>
        <td>Inventory forecasting and in-store computer vision across 150+ stores.</td>
        <td>Edge vision models running on store backoffice PCs with 0 CapEx.</td>
        <td>Eliminates server hardware procurement.</td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    <span>FLOCKML &times; CESC / RPSG GROUP</span>
    <span>CONFIDENTIAL &middot; MASTER STRATEGIC PLAN</span>
  </div>
"""
    with open(os.path.join(DOCS_DIR, 'CESC_RPSG_Master_Strategic_Plan.html'), 'w', encoding='utf-8') as f:
        f.write(get_html_wrapper("FlockML x CESC — Master Strategic Plan & Economics", content))
    print("✓ Created: docs/CESC_RPSG_Master_Strategic_Plan.html")

def build_html_2():
    # 2. Pilot Protocol (7-Day / 14-Day)
    content = """
  <header>
    <div>
      <div class="brand">FLOCKML &times; CESC / RPSG GROUP</div>
      <div class="subhead">Technical Pilot Protocol: 7-Day &amp; 14-Day Zero-Risk Substation Evaluation</div>
    </div>
    <div class="tag">PILOT PROTOCOL</div>
  </header>

  <h2>1. Scope &amp; Safety Guarantees</h2>
  <p>
    The pilot is engineered to run in <strong>passive, read-only shadow mode</strong> on 5 to 10 idle office/substation PCs across Kolkata (e.g. Chowringhee HQ, Salt Lake Sector V, Howrah). It requires <strong>zero new hardware</strong> and has <strong>zero write-access to live electrical breakers or SCADA actuation controls</strong>.
  </p>

  <div class="quote-block">
    <strong>Zero-Interference Guarantee:</strong> FlockML runs inside memory-safe WebGPU/WASM browser workers. It does not install kernel drivers, does not alter operating system files, and consumes less than 15% CPU during active daytime operator shifts.
  </div>

  <h2>2. Day-by-Day Pilot Execution Roadmap</h2>
  <table>
    <thead>
      <tr>
        <th>Timeline</th>
        <th>Phase Name</th>
        <th>Operational Action Items</th>
        <th>Success Metric / Output</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Days 1 – 2</strong></td>
        <td>Zero-Risk Setup</td>
        <td>Deploy FlockML lightweight worker on 5–10 idle test PCs across internal LAN. Establish read-only telemetry mirror connection.</td>
        <td>100% node registration, zero firewall or network interference.</td>
      </tr>
      <tr>
        <td><strong>Days 3 – 5</strong></td>
        <td>Telemetry Ingestion</td>
        <td>Ingest sample smart meter streams / transformer thermal telemetry. Run localized peak load forecast and phase balancing inference.</td>
        <td>Telemetry forward pass latency &lt; 700ms; forecast accuracy &gt; 98.5%.</td>
      </tr>
      <tr>
        <td><strong>Day 6</strong></td>
        <td>Chaos &amp; Resilience Test</td>
        <td>Intentionally disconnect 1 substation PC to simulate fiber cut / power outage. Verify work-stealing topology rebalance.</td>
        <td>Sub-5ms automatic failover with <strong>zero dropped packets</strong>.</td>
      </tr>
      <tr>
        <td><strong>Day 7</strong></td>
        <td>Executive Audit Presentation</td>
        <td>Generate and present complete <strong>Executive Audit &amp; Cost Reduction Report</strong> to Subir Verma and Group CTO.</td>
        <td>Formal decision gate to initiate commercial contract / group rollout.</td>
      </tr>
    </tbody>
  </table>

  <h2>3. Verified Benchmark Targets</h2>
  <div class="g3">
    <div class="c">
      <div class="c-t">TARGET 01 &middot; SPEED</div>
      <div class="c-v">&lt; 700 ms</div>
      <div class="c-vs">LOCALIZED INFERENCE PASS</div>
      <div class="c-b">Processes 50,000 telemetry readings across distributed substation hardware in under 1 second.</div>
    </div>
    <div class="c">
      <div class="c-t">TARGET 02 &middot; FAILOVER</div>
      <div class="c-v">&lt; 5.0 ms</div>
      <div class="c-vs">SUBSTATION WORK-STEALING</div>
      <div class="c-b">Guarantees high-availability fault tolerance during unexpected hardware or fiber drops.</div>
    </div>
    <div class="c">
      <div class="c-t">TARGET 03 &middot; COST</div>
      <div class="c-v">~70%</div>
      <div class="c-vs">OPEX REDUCTION VS AWS</div>
      <div class="c-b">Proves tangible cost elimination vs. equivalent centralized cloud GPU hosting.</div>
    </div>
  </div>

  <div class="footer">
    <span>FLOCKML &times; CESC / RPSG GROUP</span>
    <span>CONFIDENTIAL &middot; PILOT PROTOCOL</span>
  </div>
"""
    with open(os.path.join(DOCS_DIR, 'CESC_RPSG_Pilot_Protocol.html'), 'w', encoding='utf-8') as f:
        f.write(get_html_wrapper("FlockML x CESC — 7-Day & 14-Day Pilot Protocol", content))
    print("✓ Created: docs/CESC_RPSG_Pilot_Protocol.html")

def build_html_3():
    # 3. What is Needed From CESC
    content = """
  <header>
    <div>
      <div class="brand">FLOCKML &times; CESC / RPSG GROUP</div>
      <div class="subhead">Pilot Requirements: Exact Permissions, Clearances &amp; Resources Needed from CESC</div>
    </div>
    <div class="tag">REQUIREMENTS &amp; CLEARANCES</div>
  </header>

  <h2>1. What FlockML Requires from CESC (Low-Friction Checklist)</h2>
  <p>
    To ensure zero administrative burden on CESC's engineering team, the pilot requires only three basic clearances:
  </p>

  <div class="g3">
    <div class="c">
      <div class="c-t">REQUIREMENT 01 &middot; HARDWARE</div>
      <div class="c-v">5 – 10 PCs</div>
      <div class="c-vs">IDLE OFFICE / SUBSTATION PCS</div>
      <div class="c-b">Standard desktop computers (Intel Core i5/i7, 8GB–16GB RAM) in a non-critical test lab or zonal office.</div>
    </div>
    <div class="c">
      <div class="c-t">REQUIREMENT 02 &middot; DATA</div>
      <div class="c-v">Read-Only</div>
      <div class="c-vs">PASSIVE TELEMETRY MIRROR</div>
      <div class="c-b">Sample/historical smart meter stream, transformer thermal log, or CSV/MQTT mirror. Zero SCADA write access.</div>
    </div>
    <div class="c">
      <div class="c-t">REQUIREMENT 03 &middot; PEOPLE</div>
      <div class="c-v">1 SPOC</div>
      <div class="c-vs">DESIGNATED TECHNICAL LIAISON</div>
      <div class="c-b">One Executive Engineer / IT coordinator assigned to facilitate network pairing and review test outputs.</div>
    </div>
  </div>

  <h2>2. What CESC Does NOT Need to Provide</h2>
  <ul>
    <li><strong>Zero Financial Investment:</strong> The 7-day pilot is executed at <strong>₹0 cost to CESC</strong>.</li>
    <li><strong>Zero Hardware Procurement:</strong> No new GPU servers, racks, or specialized hardware required.</li>
    <li><strong>Zero SCADA Interference:</strong> No write permissions, breaker commands, or operational changes to live power distribution.</li>
    <li><strong>Zero Network Egress:</strong> No outbound internet connectivity required; executes entirely within CESC's local subnet.</li>
  </ul>

  <h2>3. Governance &amp; Decision Gate</h2>
  <div class="mono-box">
    <strong>THE DAY-7 DECISION GATE:</strong><br>
    &bull; Subir Verma (CHRO / Executive Leadership) &amp; Group CTO receive the formal <strong>Executive Savings &amp; Latency Audit</strong>.<br>
    &bull; If benchmarks exceed targets (&gt;70% cloud cost reduction, &lt;5ms failover), parties proceed to formalize the commercial contract or group rollout structure.
  </div>

  <div class="footer">
    <span>FLOCKML &times; CESC / RPSG GROUP</span>
    <span>CONFIDENTIAL &middot; PILOT REQUIREMENTS</span>
  </div>
"""
    with open(os.path.join(DOCS_DIR, 'CESC_RPSG_Pilot_Requirements.html'), 'w', encoding='utf-8') as f:
        f.write(get_html_wrapper("FlockML x CESC — Pilot Requirements & Clearances", content))
    print("✓ Created: docs/CESC_RPSG_Pilot_Requirements.html")

def build_html_4():
    # 4. What We Ship (Deliverables & Architecture)
    content = """
  <header>
    <div>
      <div class="brand">FLOCKML &times; CESC / RPSG GROUP</div>
      <div class="subhead">System Architecture &amp; Enterprise Deliverables: The Sovereign Edge Software Suite</div>
    </div>
    <div class="tag">SYSTEM DELIVERABLES</div>
  </header>

  <h2>1. What FlockML Ships to CESC</h2>
  <p>
    FlockML delivers a complete, production-grade enterprise software suite designed specifically for on-premises utility grids:
  </p>

  <div class="g2">
    <div class="c">
      <div class="c-t">DELIVERABLE 01 &middot; RUNTIME</div>
      <div class="c-v">Zero-Install Node Agent</div>
      <div class="c-vs">WEBGPU &amp; WASM COMPUTE WORKER</div>
      <div class="c-b">Lightweight 38KB execution worker that runs inside standard browser workers across Intel, AMD, and ARM silicon without requiring OS kernel drivers.</div>
    </div>
    <div class="c">
      <div class="c-t">DELIVERABLE 02 &middot; CONTROL PLANE</div>
      <div class="c-v">On-Premises Gateway</div>
      <div class="c-vs">OPENAI-COMPATIBLE API (PORT 8080)</div>
      <div class="c-b">Centralized coordination gateway (`api.cesc-ai.local/v1`) providing dynamic transformer layer sharding, work-stealing failover, and hardware telemetry.</div>
    </div>
    <div class="c">
      <div class="c-t">DELIVERABLE 03 &middot; SHADERS</div>
      <div class="c-v">BitNet 1.58-bit Shaders</div>
      <div class="c-vs">80.2% VRAM REDUCTION</div>
      <div class="c-b">Custom WGSL shader kernels that compress 7B/70B model weights into ternary {-1, 0, +1} precision, enabling large model execution on standard 8GB RAM PCs.</div>
    </div>
    <div class="c">
      <div class="c-t">DELIVERABLE 04 &middot; SECURITY</div>
      <div class="c-v">CEA Compliance Audit Suite</div>
      <div class="c-vs">100% AIR-GAPPED VERIFICATION</div>
      <div class="c-b">Cryptographic zero-knowledge proof (zk-SNARK) verification layer proving that 100% of telemetry and model activations remained strictly on domestic soil.</div>
    </div>
  </div>

  <h2>2. System Architecture Flow</h2>
  <div class="mono-box">
    <strong>ON-PREMISES SUBSTATION ARCHITECTURE:</strong><br>
    [Smart Meters / SCADA Sensors] ──(Read-Only Telemetry)──► [Substation Local Hub]<br>
                                                                     │<br>
    ┌────────────────────────────────────────────────────────────────┴─────────────────────────────────┐<br>
    │                      FLOCKML ON-PREMISES DECENTRALIZED COMPUTE GRID                              │<br>
    │  [Chowringhee HQ Workstation]  ◄──►  [Salt Lake Sec V Hub]  ◄──►  [Howrah Industrial Feeder]    │<br>
    │  (Layers 00 - 10 Shard)             (Layers 11 - 20 Shard)        (Layers 21 - 31 Shard)        │<br>
    └────────────────────────────────────────────────────────────────┬─────────────────────────────────┘<br>
                                                                     │<br>
    [Real-Time Peak Load Predictions] ◄──────────────────────────────┴──► [Sub-5ms Work-Stealing Failover]
  </div>

  <div class="footer">
    <span>FLOCKML &times; CESC / RPSG GROUP</span>
    <span>CONFIDENTIAL &middot; DELIVERABLES &amp; ARCHITECTURE</span>
  </div>
"""
    with open(os.path.join(DOCS_DIR, 'CESC_RPSG_Deliverables_and_Architecture.html'), 'w', encoding='utf-8') as f:
        f.write(get_html_wrapper("FlockML x CESC — Deliverables & System Architecture", content))
    print("✓ Created: docs/CESC_RPSG_Deliverables_and_Architecture.html")

def build_html_5():
    # 5. National IndiaAI Platform & Commercialization (Selling to Tata, Adani, State DISCOMs)
    content = """
  <header>
    <div>
      <div class="brand">FLOCKML &times; CESC / RPSG GROUP</div>
      <div class="subhead">National IndiaAI Platform: How RPSG Leads the National Utility Compute Grid &amp; Licenses to Tata, Adani &amp; DISCOMs</div>
    </div>
    <div class="tag">NATIONAL EXPANSION</div>
  </header>

  <h2>1. The National IndiaAI Mandate (Rs 10,372 Crore Opportunity)</h2>
  <p>
    The Ministry of Electronics &amp; Information Technology (MeitY) and the Ministry of Power have launched the <strong>₹10,372 Crore IndiaAI Mission</strong> to build domestic, sovereign artificial intelligence compute infrastructure.
  </p>
  <p>
    By partnering with FlockML, <strong>RPSG does not just solve CESC's internal problems—RPSG becomes the National Flagship Champion</strong> delivering the sovereign utility compute blueprint for India.
  </p>

  <div class="g2">
    <div class="c">
      <div class="c-t">NATIONAL STRATEGY 01</div>
      <div class="c-v">Direct Govt Access</div>
      <div class="c-vs">MEITY &amp; MINISTRY OF POWER</div>
      <div class="c-b">RPSG presents the validated CESC deployment as the approved national standard for power grid telemetry and smart meter analytics.</div>
    </div>
    <div class="c">
      <div class="c-t">NATIONAL STRATEGY 02</div>
      <div class="c-v">DISCOM Consortium</div>
      <div class="c-vs">LICENSING TO TATA, ADANI, STATE GRIDS</div>
      <div class="c-b">RPSG and FlockML license the Sovereign Utility AI Platform to peer utilities (Tata Power, Adani Electricity, Torrent Power, Mahavitaran, UPPCL).</div>
    </div>
  </div>

  <h2>2. Licensing to Peer Utilities: The Multi-Hundred Crore Enterprise Market</h2>
  <table>
    <thead>
      <tr>
        <th>Target Power Utility</th>
        <th>Operational Scale</th>
        <th>RPSG / FlockML Solution</th>
        <th>Commercial Licensing Opportunity</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tata Power</strong></td>
        <td>12M+ consumers across Mumbai, Delhi, Odisha.</td>
        <td>On-premises smart grid load forecasting &amp; EV charger load balancing.</td>
        <td>Rs 15–25 Cr / year annual enterprise licensing contract.</td>
      </tr>
      <tr>
        <td><strong>Adani Electricity</strong></td>
        <td>Mumbai &amp; Gujarat smart grid distribution franchises.</td>
        <td>Substation anomaly detection &amp; 100% CEA air-gapped compliance.</td>
        <td>Rs 20–30 Cr / year enterprise contract.</td>
      </tr>
      <tr>
        <td><strong>State DISCOMs (UPPCL, Mahavitaran, WBSEDCL)</strong></td>
        <td>100M+ smart meters under national RDSS mandates.</td>
        <td>Central Government subsidized Sovereign AI Utility grid deployment.</td>
        <td>Multi-state consortium contracts funded via IndiaAI Mission grants.</td>
      </tr>
    </tbody>
  </table>

  <h2>3. The Ultimate Vision: From Power Utility to Sovereign AI Giant</h2>
  <div class="quote-block">
    "Reliance built Jio to dominate telecom and digital services. Tata built Tata Electronics and Tata Neu.  
    <strong>With FlockML, RPSG pioneers the National Sovereign AI Infrastructure Grid</strong>—turning power generation and electrical substations into Asia's most profitable, energy-efficient AI compute cloud."
  </div>

  <div class="footer">
    <span>FLOCKML &times; CESC / RPSG GROUP</span>
    <span>CONFIDENTIAL &middot; NATIONAL INDIAAI PLATFORM</span>
  </div>
"""
    with open(os.path.join(DOCS_DIR, 'CESC_RPSG_National_IndiaAI_Platform.html'), 'w', encoding='utf-8') as f:
        f.write(get_html_wrapper("FlockML x CESC — National IndiaAI Platform & Commercialization", content))
    print("✓ Created: docs/CESC_RPSG_National_IndiaAI_Platform.html")

if __name__ == '__main__':
    build_html_1()
    build_html_2()
    build_html_3()
    build_html_4()
    build_html_5()
