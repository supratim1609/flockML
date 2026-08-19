# Generate comprehensive 15-slide institutional teleprompter script (12-14 min master pitch)

teleprompter_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FlockML - Anicut Capital Master Pitch Script (15 Slides)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #000000;
      --surface: #0A0A0A;
      --card-bg: #111111;
      --border: #222222;
      --border-accent: #333333;
      --text-main: #EEEEEE;
      --text-muted: #888888;
      --text-gold: #FBBF24;
      --text-blue: #3B82F6;
      --text-green: #34D399;
      --text-purple: #818CF8;
      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: var(--bg);
      color: var(--text-main);
      font-family: var(--font-main);
      line-height: 1.6;
      padding: 40px 20px;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
    }

    header {
      border-bottom: 1px solid var(--border);
      padding-bottom: 24px;
      margin-bottom: 36px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }

    h1 {
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.5px;
      color: #FFF;
    }

    .meta-badge {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-gold);
      background: rgba(251, 191, 36, 0.1);
      border: 1px solid rgba(251, 191, 36, 0.2);
      padding: 4px 10px;
      border-radius: 4px;
    }

    .timing-bar {
      background: #0E0E0E;
      border: 1px solid var(--border);
      border-left: 3px solid var(--text-blue);
      padding: 14px 18px;
      margin-bottom: 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 13px;
      color: #CCC;
    }

    .slide-block {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 24px 28px;
      margin-bottom: 28px;
      transition: border-color 0.2s ease;
    }

    .slide-block:hover {
      border-color: #444;
    }

    .slide-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding-bottom: 10px;
    }

    .slide-label {
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-blue);
      font-weight: 700;
    }

    .slide-time {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
    }

    .slide-title {
      font-size: 20px;
      font-weight: 600;
      color: #FFF;
      margin-bottom: 16px;
    }

    .script-text {
      font-size: 15.5px;
      color: #D4D4D8;
      line-height: 1.75;
      margin-bottom: 16px;
    }

    .script-text strong {
      color: #FFF;
    }

    .script-text .highlight {
      color: var(--text-gold);
      font-weight: 600;
    }

    .pro-tip {
      background: rgba(251, 191, 36, 0.04);
      border-left: 3px solid var(--text-gold);
      padding: 10px 14px;
      font-size: 12.5px;
      color: #FDE68A;
      font-family: var(--font-mono);
      line-height: 1.5;
    }

    .section-divider {
      text-align: center;
      margin: 40px 0 24px;
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--text-muted);
      position: relative;
    }

    .section-divider::before,
    .section-divider::after {
      content: "";
      position: absolute;
      top: 50%;
      width: 35%;
      height: 1px;
      background: var(--border);
    }

    .section-divider::before { left: 0; }
    .section-divider::after { right: 0; }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div>
        <h1>FlockML - Master Pitch Teleprompter Script</h1>
        <p style="color: var(--text-muted); font-size: 14px; margin-top: 4px;">15-Slide Institutional Master Deck Guide · Anicut Capital Pitch</p>
      </div>
      <div class="meta-badge">12-14 MIN PITCH · $20M SEED</div>
    </header>

    <div class="timing-bar">
      <div><strong>PRESENTATION PACE:</strong> ~45 - 55 SECONDS PER SLIDE</div>
      <div><strong>TOTAL RUNTIME:</strong> ~13 MINUTES + 25 MIN Q&amp;A</div>
    </div>

    <!-- ========================================================= -->
    <!-- ACT I: THE HOOK & THE CRISIS -->
    <!-- ========================================================= -->

    <div class="section-divider">ACT I: THE HOOK &amp; THE STRUCTURAL CRISIS</div>

    <!-- SLIDE 01 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 01 / 15 · COVER</span>
        <span class="slide-time">DURATION: 45 SEC</span>
      </div>
      <div class="slide-title">FlockML: Distributed Compute for Sovereign AI Workloads</div>
      <div class="script-text">
        "Good morning, partners. I am Supratim Dhara, Founder and Chief Systems Architect of FlockML.<br><br>
        If you look at the artificial intelligence landscape today, we are in the middle of the greatest technological wave in human history, but it is entirely choked by a single bottleneck: <span class="highlight">centralized compute</span>.<br><br>
        Today, three American hyperscale cloud providers control who gets access to AI hardware, what they pay, and where their data lives. FlockML is the decentralized execution layer that turns billions of dollars of existing, idle consumer, telecom, and enterprise hardware into a high-performance, sovereign compute grid. We are building the compute layer for the next billion devices."
      </div>
      <div class="pro-tip">DELIVERY: Speak with calm, absolute technical authority. Anchor yourself as a systems engineer building fundamental infrastructure, not a wrapper app.</div>
    </div>

    <!-- SLIDE 02 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 02 / 15 · THE PROBLEM</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">AI Compute Is Becoming a Bottleneck</div>
      <div class="script-text">
        "To understand why FlockML exists, we have to look at the three structural crises hitting the cloud today:<br><br>
        First, <strong>Extreme Centralization:</strong> Developers and enterprises are trapped in rigid datacenter contracts. If you want to train or fine-tune a model, you are forced to rent rigid 8-GPU nodes with multi-month lock-ins and arbitrary quota limits.<br><br>
        Second, <strong>Exponential CapEx &amp; Power Limits:</strong> Building multi-billion dollar datacenters is hitting physical power grid constraints and massive cooling overheads that get passed directly down to software companies as inflated hourly bills.<br><br>
        And third, <strong>Sovereign Data Risk:</strong> Indian enterprises, banks, and government agencies are forced to route their proprietary corporate data offshore because domestic sovereign GPU clusters simply do not exist at scale."
      </div>
      <div class="pro-tip">DELIVERY: Emphasize that the centralized datacenter model cannot physically scale to meet exponential inference demand.</div>
    </div>

    <!-- SLIDE 03 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 03 / 15 · WHY NOW</span>
        <span class="slide-time">DURATION: 55 SEC</span>
      </div>
      <div class="slide-title">Why Now? Three Structural Shifts</div>
      <div class="script-text">
        "Why is a distributed compute grid possible today when it was technically impossible just three years ago? It comes down to three simultaneous technological convergences:<br><br>
        Number one: <strong>WebGPU and WebAssembly SIMD.</strong> Every modern browser and edge runtime now gives developers direct, bare-metal access to GPU shaders and 128-bit vector registers without installing native Nvidia CUDA drivers.<br><br>
        Number two: <strong>1.58-Bit Ternary Quantization.</strong> Breakthroughs like BitNet b1.58 prove that models can run on ternary weights (-1, 0, +1), replacing power-hungry 16-bit floating point multiplications with lightweight integer additions. This reduces model memory footprints by over 80%.<br><br>
        Number three: <strong>Silicon Saturation.</strong> Billions of consumer laptops, Apple Silicon M-series chips, and telecom set-top boxes sit plugged into wall power and gigabit fiber, completely idle 18 to 20 hours a day. The hardware is already paid for."
      </div>
      <div class="pro-tip">DELIVERY: Make the point that this convergence makes decentralized compute technically and economically inevitable.</div>
    </div>

    <!-- ========================================================= -->
    <!-- ACT II: THE ARCHITECTURE & TECHNICAL MOAT -->
    <!-- ========================================================= -->

    <div class="section-divider">ACT II: ARCHITECTURE &amp; TECHNICAL PROOF</div>

    <!-- SLIDE 04 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 04 / 15 · CORE THESIS</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">A Cloud Experience Over a Distributed Compute Grid</div>
      <div class="script-text">
        "Our core thesis is simple: <span class="highlight">The developer thinks about the workload; FlockML thinks about the infrastructure.</span><br><br>
        From the developer's perspective, FlockML looks and feels exactly like AWS or OpenAI. They do not manage clusters, they do not configure SSH keys, and they do not worry about device topology. They simply submit a standard API request or PyTorch training job.<br><br>
        Underneath that standard API, the FlockML Runtime dynamically discovers active nodes across our mesh, automatically shards model weights across heterogeneous device memory pools, and uses sub-5 millisecond work-stealing failover to ensure execution never stalls. We turn untrusted, noisy edge devices into a Tier-1 virtual supercomputer."
      </div>
      <div class="pro-tip">DELIVERY: Contrast the developer simplicity with the deep systems orchestration happening underneath.</div>
    </div>

    <!-- SLIDE 05 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 05 / 15 · ARCHITECTURE</span>
        <span class="slide-time">DURATION: 55 SEC</span>
      </div>
      <div class="slide-title">How the System Works: The Execution Layer</div>
      <div class="script-text">
        "Let us look under the hood at how our four specialized subsystems operate:<br><br>
        1. <strong>The FlockML Worker:</strong> A zero-install sandboxed runtime executing inside WebAssembly SIMD and WebGPU. It executes tensor operations in a secure browser sandbox with zero host privileges.<br><br>
        2. <strong>The Distributed Coordinator:</strong> Our high-throughput orchestration engine that continuously monitors node telemetry, network latency, and available RAM, dynamically slicing 70-billion parameter models across the active network topology.<br><br>
        3. <strong>zk-Proof Verification:</strong> We solve the Byzantine node problem mathematically. Using lightweight zero-knowledge commitments, we verify tensor computations in sub-0.1 milliseconds without having to wastefully re-execute weights.<br><br>
        4. <strong>Sub-5ms Failover:</strong> If a household laptop closes its lid or an office set-top box turns off, neighboring nodes automatically steal and resume the pipeline stage with zero token loss."
      </div>
      <div class="pro-tip">DELIVERY: The zk-verification and sub-5ms failover are your deepest technical moats. State them with precision.</div>
    </div>

    <!-- SLIDE 06 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 06 / 15 · TECHNICAL PROOF</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">Technical Proof: BitNet 1.58-Bit Quantization</div>
      <div class="script-text">
        "Here is the mathematical breakthrough that unlocks edge AI: BitNet 1.58-bit ternary quantization.<br><br>
        Traditionally, running a 70B parameter model requires 140 Gigabytes of expensive datacenter VRAM. With ternary representation {-1, 0, +1}, we pack 16 parameters into a single 32-bit register. That slashes the required memory by <strong>80.2%</strong>.<br><br>
        More importantly, ternary math eliminates power-hungry matrix floating-point multiplications entirely. They become simple integer additions. This slashes energy draw by 85%, allowing standard consumer CPUs and integrated GPUs to run high-speed inference without thermal throttling."
      </div>
      <div class="pro-tip">DELIVERY: Highlight that 80% VRAM reduction is why models fit on ordinary edge devices without $30,000 datacenter GPUs.</div>
    </div>

    <!-- ========================================================= -->
    <!-- ACT III: THE ECONOMICS & ADOPTION FUNNEL -->
    <!-- ========================================================= -->

    <div class="section-divider">ACT III: UNIT ECONOMICS &amp; GO-TO-MARKET</div>

    <!-- SLIDE 07 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 07 / 15 · UNIT ECONOMICS</span>
        <span class="slide-time">DURATION: 55 SEC</span>
      </div>
      <div class="slide-title">The Economics: Hyperscale vs. Decentralized Compute</div>
      <div class="script-text">
        "Now let us look at why this is an unstoppable commercial wedge.<br><br>
        On traditional hyperscale clouds, developers pay roughly <strong>$32.00 an hour</strong> (about ₹2,650) because they are forced to rent rigid 8x A100 nodes, paying for datacenter real estate, cooling, and massive corporate margin stacking.<br><br>
        On FlockML, developers access a flexible distributed cluster for <strong>$10.00 flat per hour</strong> (₹830). That is a direct <span class="highlight">~70% cost reduction</span>.<br><br>
        And because FlockML has zero hardware CapEx, zero cooling bills, and zero datacenter leases, we capture a <strong>78% pure software gross margin</strong> while paying node providers attractive yields on their sunk-cost hardware."
      </div>
      <div class="pro-tip">DELIVERY: Emphasize that $10/hr gives developers huge savings while leaving FlockML with pure SaaS gross margins.</div>
    </div>

    <!-- SLIDE 08 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 08 / 15 · ADOPTION FUNNEL</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">Developer Value &amp; Incremental Migration</div>
      <div class="script-text">
        "We do not ask enterprises or developers to rip and replace their existing cloud stack on Day 1. We use a 4-step Trojan-horse adoption funnel:<br><br>
        Step 1: <strong>Add Secondary Target.</strong> Keep your existing AWS stack completely intact. Plug in the FlockML API key in 5 minutes.<br><br>
        Step 2: <strong>Route Batch Workloads.</strong> Offload non-critical offline fine-tuning, embeddings, and synthetic data evals to FlockML to immediately see 70% savings.<br><br>
        Step 3: <strong>Dynamic Economic Routing.</strong> Our SDK automatically routes traffic to wherever compute is cheapest across the mesh.<br><br>
        Step 4: <strong>Scale Production.</strong> As confidence builds, enterprise production inference organically migrates onto FlockML."
      </div>
      <div class="pro-tip">DELIVERY: Frame this as zero enterprise switching risk: start with batch eval, then expand into production.</div>
    </div>

    <!-- SLIDE 09 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 09 / 15 · POSITIONING</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">The Execution Layer for Distributed Compute</div>
      <div class="script-text">
        "To understand our positioning: <span class="highlight">FlockML is not a hardware owner; we are the software execution layer.</span><br><br>
        Hyperscalers own physical datacenters and rent rigid instances. GPU marketplaces aggregate fragmented servers, but force developers into painful manual SSH management and fragile setups.<br><br>
        FlockML is a pure software orchestration layer. Developers interact with a standard API, while our runtime handles dynamic tensor sharding, cryptographic verification, and sub-5ms failover underneath. We do not need to buy the world's compute; we become the software protocol through which the world's compute executes."
      </div>
      <div class="pro-tip">DELIVERY: This is the 'Windows/Android of Distributed Compute' analogy. You are the operating system layer.</div>
    </div>

    <!-- SLIDE 10 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 10 / 15 · COMPETITIVE LANDSCAPE</span>
        <span class="slide-time">DURATION: 45 SEC</span>
      </div>
      <div class="slide-title">Where FlockML Sits: The Competitive Matrix</div>
      <div class="script-text">
        "When comparing the competitive landscape across four models:<br><br>
        Hyperscale clouds offer standard APIs, but are wildly expensive ($32/hr minimums) with rigid minimums.<br><br>
        GPU marketplaces offer spot pricing, but require complex manual SSH and lack automated sharding.<br><br>
        Crypto DePIN networks suffer from volatile token gas fees, cryptic Web3 wallets, and high failure rates that enterprises reject.<br><br>
        FlockML sits alone at the intersection: <span class="highlight">Enterprise Tier-1 developer usability with disruptive $10/hr pricing, sub-5ms failover, and standard USD/INR invoicing.</span>"
      </div>
      <div class="pro-tip">DELIVERY: Emphasize that we have zero crypto token nonsense. Real software, real enterprise invoicing, real fiat billing.</div>
    </div>

    <!-- ========================================================= -->
    <!-- ACT IV: SCALE, BUSINESS MODEL & ROADMAP -->
    <!-- ========================================================= -->

    <div class="section-divider">ACT IV: SUPPLY SCALE, ROADMAP &amp; CAPITAL ALLOCATION</div>

    <!-- SLIDE 11 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 11 / 15 · COMPUTE SUPPLY</span>
        <span class="slide-time">DURATION: 55 SEC</span>
      </div>
      <div class="slide-title">The Compute Supply Engine: Enterprise Fleets to 100M Telecom Boxes</div>
      <div class="script-text">
        "Where does our compute supply come from? We unlock two massive, high-margin supply tiers with zero CapEx:<br><br>
        Tier 1: <strong>Enterprise Fleets.</strong> Thousands of corporate and government laptops (MeitY, state power utilities, banks) sit idle from 7 PM to 7 AM. Organizations run internal AI workloads across their own machines with zero data leaving the building.<br><br>
        Tier 2: <strong>Telecom Set-Top Boxes.</strong> Reliance Jio and Bharti Airtel have over 30 Million 4K Android boxes wired to fiber and wall power, sitting idle 20 hours a day. With a single over-the-air Wasm update, 10 Million boxes create a <span class="highlight">150 PFLOPs national supercomputer</span>. Telcos earn high-margin enterprise revenue, consumers receive broadband bill credits, and FlockML pays strictly for active compute cycles."
      </div>
      <div class="pro-tip">DELIVERY: The 100M telecom set-top box angle is a massive eye-opener for Indian VC partners. Emphasize the 150 PFLOPs scale.</div>
    </div>

    <!-- SLIDE 12 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 12 / 15 · BUSINESS MODEL</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">A Compute Cloud Business Model</div>
      <div class="script-text">
        "We monetize through three distinct, high-margin revenue streams:<br><br>
        1. <strong>Usage-Based Compute API:</strong> Developers pay per compute-second or token ($10/hr cluster equivalent). FlockML retains a 78% software gross margin after node provider payouts.<br><br>
        2. <strong>Enterprise Private Grids:</strong> Annual recurring software licenses ($100k to $500k ARR) for banks and defense agencies deploying air-gapped sovereign clusters on internal hardware.<br><br>
        3. <strong>Sovereign AI Deployments:</strong> Multi-million dollar government and national infrastructure contracts (IndiaAI, MeitY) delivering 100% domestic data sovereignty."
      </div>
      <div class="pro-tip">DELIVERY: Reinforce that we have pure software margins because we never purchase, house, or depreciate physical servers.</div>
    </div>

    <!-- SLIDE 13 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 13 / 15 · 24-MONTH ROADMAP</span>
        <span class="slide-time">DURATION: 50 SEC</span>
      </div>
      <div class="slide-title">The Next 24 Months: Proof → Product → Network → Scale</div>
      <div class="script-text">
        "Our execution roadmap is disciplined and milestone-driven:<br><br>
        <strong>Months 1 to 6 (Phase 1):</strong> Expand WebGPU/Wasm kernels for Llama-3 70B and DeepSeek-R1; pilot 500-node MeitY and enterprise private grids; launch developer SDK.<br><br>
        <strong>Months 7 to 12 (Phase 2):</strong> Deploy 50,000 set-top box pilot with Indian telecom partners; launch public developer API with automated usage billing; scale to 10,000 active nodes.<br><br>
        <strong>Months 13 to 18 (Phase 3):</strong> Sign 20+ enterprise private grid customers; expand telecom footprint to 1M+ connected living rooms; reach $3M ARR with positive unit economics.<br><br>
        <strong>Months 19 to 24 (Phase 4):</strong> Deploy sovereign AI infrastructure across the Gulf and global markets, scaling beyond 10M active edge devices."
      </div>
      <div class="pro-tip">DELIVERY: Demonstrate that every phase derisks the next: protocol validation leads to telecom pilots, which leads to enterprise ARR.</div>
    </div>

    <!-- SLIDE 14 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 14 / 15 · THE ASK</span>
        <span class="slide-time">DURATION: 55 SEC</span>
      </div>
      <div class="slide-title">The Ask: Seed Round Capital Allocation</div>
      <div class="script-text">
        "We are raising a <strong>$20.0 Million USD Seed round</strong>: exactly <span class="highlight">₹168 Crore</span> at an $80M Pre / $100M Post valuation (~₹670 Cr Pre / ~₹840 Cr Post). This gives us a 24 to 30 month runway to Series A and sovereign scale.<br><br>
        Our capital deployment is disciplined across 5 core buckets:<br><br>
        • <strong>40% ($8.0M / ₹67.2 Cr) to Core Distributed Systems Engineering:</strong> Wasm SIMD kernels, WebGPU pipelines, and zk-SNARK verifiers.<br>
        • <strong>20% ($4.0M / ₹33.6 Cr) to Telecom &amp; Enterprise BD:</strong> Deploying set-top box rollouts and MeitY pilots.<br>
        • <strong>15% ($3.0M / ₹25.2 Cr) to Developer Ecosystem:</strong> Global SDKs, documentation, hackathons, and grants.<br>
        • <strong>10% ($2.0M / ₹16.8 Cr) to Security &amp; Compliance:</strong> SOC 2 Type II, DPDP Act 2023 compliance, and audits.<br>
        • <strong>15% ($3.0M / ₹25.2 Cr) to Treasury &amp; Contingency Buffer:</strong> Ensuring an extended runway and operational liquidity safety cushion."
      </div>
      <div class="pro-tip">DELIVERY: State the valuation and numbers clearly with zero hesitation. The 15% buffer highlights your capital prudence.</div>
    </div>

    <!-- SLIDE 15 -->
    <div class="slide-block">
      <div class="slide-header">
        <span class="slide-label">SLIDE 15 / 15 · CLOSING &amp; SUMMARY</span>
        <span class="slide-time">DURATION: 45 SEC</span>
      </div>
      <div class="slide-title">Why FlockML Wins: Investment Summary &amp; Q&amp;A</div>
      <div class="script-text">
        "To summarize why FlockML is the defining infrastructure investment of this cycle:<br><br>
        1. <strong>Zero-CapEx Scale:</strong> 78% software gross margins monetizing idle corporate laptops and 100M telecom set-top boxes.<br>
        2. <strong>Mathematical Moat:</strong> BitNet 1.58-bit quantization slashing VRAM by 80.2%, paired with sub-0.1ms zk-verification and sub-5ms failover.<br>
        3. <strong>Low-Friction Adoption:</strong> Drop-in OpenAI API saving developers ~70% on compute with zero architecture rewrites.<br>
        4. <strong>Sovereign Defense:</strong> 100% on-soil air-gapped data localization for India and global governments.<br><br>
        Artificial intelligence should not belong to three data center monopolies. We are building the sovereign compute layer for the next billion devices.<br><br>
        Thank you, and I am excited to open the floor to your questions."
      </div>
      <div class="pro-tip">DELIVERY: Conclude with a strong, confident pause, look at the lead partner, and smile. You hold all the cards.</div>
    </div>

  </div>

</body>
</html>
"""

# Scrub any possible em dashes
teleprompter_content = teleprompter_content.replace('—', '-').replace('–', '-')

with open('/Users/supratim/Desktop/flockml-sovereign/docs/Preparation_Playbooks/Anicut_Teleprompter_Script.html', 'w', encoding='utf-8') as f:
    f.write(teleprompter_content)

print("Updated teleprompter script successfully with full 12-14 minute master pitch narrative.")
