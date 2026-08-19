teleprompter_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FlockML - Anicut Capital Master Pitch Script (15 Slides)</title>
  <style>
    :root {
      --bg: #09090B;
      --card-bg: #18181B;
      --border: #27272A;
      --accent: #3B82F6;
      --accent-glow: rgba(59, 130, 246, 0.15);
      --text-main: #F4F4F5;
      --text-muted: #A1A1AA;
      --text-gold: #FBBF24;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding: 40px 20px;
      display: flex;
      justify-content: center;
    }

    .container {
      max-width: 900px;
      width: 100%;
    }

    header {
      margin-bottom: 40px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 20px;
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

    .meta {
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--accent);
      background: var(--accent-glow);
      padding: 6px 12px;
      border-radius: 4px;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }

    .slide-block {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 24px;
      transition: border-color 0.2s ease;
    }

    .slide-block:hover {
      border-color: var(--accent);
    }

    .slide-label {
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
      margin-bottom: 4px;
    }

    .slide-title {
      font-size: 20px;
      font-weight: 600;
      color: #FFF;
      margin-bottom: 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      padding-bottom: 8px;
    }

    .script-text {
      font-size: 16px;
      color: #D4D4D8;
      margin-bottom: 16px;
    }

    .script-text strong {
      color: #FFF;
    }

    .pro-tip {
      background: rgba(251, 191, 36, 0.05);
      border-left: 3px solid var(--text-gold);
      padding: 10px 14px;
      font-size: 13px;
      color: #FDE68A;
      font-family: var(--font-mono);
    }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div>
        <h1>FlockML - Anicut Capital Master Pitch Script</h1>
        <p style="color: var(--text-muted); font-size: 14px; margin-top: 4px;">15-Slide Master Deck Presentation Guide</p>
      </div>
      <div class="meta">15 SLIDES · 10:00 AM IST</div>
    </header>

    <!-- SLIDE 01 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 01 / 15</div>
      <div class="slide-title">The Decentralized AI Compute Grid</div>
      <div class="script-text">
        "Good morning everyone. I am Supratim Dhara, founder of FlockML.<br><br>
        Today, AI is bottlenecked by one single factor: centralized cloud compute. FlockML is the decentralized execution layer that turns millions of idle consumer, telecom, and enterprise devices into a high-performance, cost-effective distributed compute grid."
      </div>
      <div class="pro-tip">TIP: Speak with steady confidence. Anchor yourself as a systems architect.</div>
    </div>

    <!-- SLIDE 02 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 02 / 15</div>
      <div class="slide-title">AI Compute Is Becoming a Bottleneck</div>
      <div class="script-text">
        "Three structural crises are hitting AI today:<br><br>
        First, extreme centralization: three hyperscalers control pricing and supply quotas.<br><br>
        Second, exponential CapEx: running models in specialized datacenters requires billions in cooling, real estate, and hardware depreciation.<br><br>
        Third, sovereign risk: nations and companies are sending proprietary datasets overseas because they lack domestic compute infrastructure."
      </div>
      <div class="pro-tip">TIP: Emphasize that the cloud datacenter buildout is hitting physical power limits.</div>
    </div>

    <!-- SLIDE 03 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 03 / 15</div>
      <div class="slide-title">Why Now? Three Structural Shifts</div>
      <div class="script-text">
        "Why is this possible today when it was impossible 3 years ago?<br><br>
        1. WebGPU & Wasm SIMD: Browsers and edge runtimes now expose bare-metal GPU acceleration without installing native drivers.<br><br>
        2. BitNet 1.58-Bit Quantization: We replace heavy floating-point multiplications with lightweight integer additions, slashing VRAM needs by 80.2%.<br><br>
        3. Silicon Saturation: Millions of laptops, fiber modems, and set-top boxes sit idle on gigabit connections 18+ hours a day."
      </div>
    </div>

    <!-- SLIDE 04 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 04 / 15</div>
      <div class="slide-title">A Cloud Experience Over a Distributed Compute Grid</div>
      <div class="script-text">
        "Here is our core thesis: Developers do not want to manage distributed nodes. They want a cloud API.<br><br>
        To the developer, FlockML looks exactly like an OpenAI or PyTorch endpoint. Under the hood, our runtime orchestrates dynamic discovery, tensor sharding, and sub-5ms failover across our global mesh.<br><br>
        The developer thinks about the workload. FlockML handles the infrastructure."
      </div>
      <div class="pro-tip">TIP: Emphasize zero learning curve for developers.</div>
    </div>

    <!-- SLIDE 05 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 05 / 15</div>
      <div class="slide-title">How the System Works: The Execution Layer</div>
      <div class="script-text">
        "Our architecture has 4 purpose-built pillars:<br><br>
        1. The FlockML Worker: Zero-install Wasm/WebGPU sandbox running on any OS.<br>
        2. Distributed Coordinator: High-speed ring topology that shards 70B/405B tensors.<br>
        3. Cryptographic Verification: Sub-0.1ms zk-SNARK commitments that reject malicious updates without re-running weights.<br>
        4. Fault-Tolerant Failover: Dynamic work-stealing that catches dropped nodes in under 5ms with zero token loss."
      </div>
    </div>

    <!-- SLIDE 06 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 06 / 15</div>
      <div class="slide-title">Technical Proof: BitNet 1.58-Bit Quantization</div>
      <div class="script-text">
        "Here is the mathematical breakthrough: with 1.58-bit ternary weights {-1, 0, +1}, we pack 16 parameters into a single 32-bit register.<br><br>
        A 70-Billion parameter model that normally demands a $30,000 GPU cluster fits into standard consumer RAM, executing matrix math with simple integer additions."
      </div>
    </div>

    <!-- SLIDE 07 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 07 / 15</div>
      <div class="slide-title">The Economics: Hyperscale vs. Decentralized Compute</div>
      <div class="script-text">
        "Look at the unit economics: On AWS, running a large model forces you into an 8x A100 instance costing ~$32.00/hour because of datacenter CapEx and power overhead.<br><br>
        On FlockML, developers run the equivalent distributed workload for ~$10.00/hour: saving 70% while FlockML captures a 78%+ software gross margin because our hardware CapEx is zero."
      </div>
      <div class="pro-tip">TIP: Explain the 78% software gross margin clearly.</div>
    </div>

    <!-- SLIDE 08 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 08 / 15</div>
      <div class="slide-title">Developer Value & Incremental Migration</div>
      <div class="script-text">
        "How do we overcome enterprise switching inertia? We use a 4-step Trojan-horse adoption funnel:<br><br>
        Step 1: Developers add FlockML as a secondary target with 1 line of code.<br>
        Step 2: They offload batch fine-tuning, embeddings, and synthetic evaluations.<br>
        Step 3: Our SDK automatically routes traffic to wherever compute is cheapest.<br>
        Step 4: Over time, production inference organically shifts to FlockML."
      </div>
    </div>

    <!-- SLIDE 09 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 09 / 15</div>
      <div class="slide-title">The Execution Layer for Distributed Compute</div>
      <div class="script-text">
        "This slide defines our moat: Legacy clouds own server racks. Marketplaces rent raw SSH machines. FlockML is a pure software orchestration layer.<br><br>
        We do not need to own the world's compute. We become the software layer through which the world's available compute is executed."
      </div>
    </div>

    <!-- SLIDE 10 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 10 / 15</div>
      <div class="slide-title">Where FlockML Sits (Competitive Matrix)</div>
      <div class="script-text">
        "Against competitors, we sit in the sweet spot:<br><br>
        Unlike AWS, we have zero datacenter CapEx and 70% cheaper pricing.<br>
        Unlike raw marketplaces, we provide automated sharding with zero manual SSH.<br>
        Unlike crypto DePIN networks, we have no volatile tokens or Web3 friction: enterprises pay in standard USD/INR via credit card or invoice."
      </div>
    </div>

    <!-- SLIDE 11 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 11 / 15</div>
      <div class="slide-title">The Compute Supply Engine: Office Laptops to 100M Telecom Boxes</div>
      <div class="script-text">
        "Where does our compute supply come from? We unlock two massive tiers:<br><br>
        First, enterprise fleets: government and bank laptops sitting idle 7 PM to 7 AM for air-gapped sovereign training.<br><br>
        Second, Indian telecom set-top boxes: Reliance Jio and Airtel have over 30 Million 4K boxes wired to fiber and wall power, sitting idle 20 hours a day. With an over-the-air Wasm update, 10 Million boxes create a 150 PFLOPs national supercomputer.<br><br>
        And providers earn yield strictly on active cycles: zero idle burn."
      </div>
    </div>

    <!-- SLIDE 12 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 12 / 15</div>
      <div class="slide-title">A Compute Cloud Business Model</div>
      <div class="script-text">
        "We monetize through 3 high-margin channels:<br><br>
        1. Usage-based compute API with a 78% software gross margin.<br>
        2. Enterprise Private Grids: $100k-$500k ARR software licenses for banks and defense.<br>
        3. Sovereign AI Deployments: Multi-million dollar national AI infrastructure contracts."
      </div>
    </div>

    <!-- SLIDE 13 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 13 / 15</div>
      <div class="slide-title">The Next 24 Months: Roadmap</div>
      <div class="script-text">
        "Over the next 24 months, our execution path is clear:<br><br>
        Phase 1: Pilot 500-node MeitY and enterprise private grids.<br>
        Phase 2: Launch 50,000 telecom set-top box pilot and public developer API.<br>
        Phase 3: Scale to 20+ enterprise customers and $3M ARR.<br>
        Phase 4: Expand sovereign grids across the Gulf and global markets."
      </div>
    </div>

    <!-- SLIDE 14 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 14 / 15</div>
      <div class="slide-title">The Ask: Seed Capital Allocation</div>
      <div class="script-text">
        "We are raising a $20M - $30M Seed round at a $90M Pre / $120M Post valuation to give us a 24 to 30 month runway.<br><br>
        45% of capital goes to core distributed systems engineering, 25% to telecom and enterprise BD, 20% to developer ecosystem, and 10% to operations and compliance."
      </div>
    </div>

    <!-- SLIDE 15 -->
    <div class="slide-block">
      <div class="slide-label">SLIDE 15 / 15</div>
      <div class="slide-title">The Future of Sovereign Compute (Closing)</div>
      <div class="script-text">
        "AI should not belong to three data center monopolies. We are building the sovereign compute layer for the next billion devices.<br><br>
        Thank you, and I am excited to open the floor to your questions."
      </div>
      <div class="pro-tip">TIP: Pause, smile, and invite questions. You hold all the technical and economic cards.</div>
    </div>

  </div>

</body>
</html>
"""

# Scrub all em dashes
teleprompter_html = teleprompter_html.replace('—', '-').replace('–', '-')

with open('/Users/supratim/Desktop/flockml-sovereign/docs/Preparation_Playbooks/Anicut_Teleprompter_Script.html', 'w', encoding='utf-8') as f:
    f.write(teleprompter_html)

print('Updated Anicut Teleprompter Script for 15 slides.')
