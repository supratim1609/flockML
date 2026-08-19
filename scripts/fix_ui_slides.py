# Rebuild pitch deck with fixed UI on slides 1, 4, 5, 8, 13, 14
with open('/Users/supratim/Desktop/flockml-sovereign/docs/Anicut_Capital_Pitch_Deck.html', 'r', encoding='utf-8') as f:
    orig = f.read()

head = orig[:orig.find('<body>')]

deck_body = """<body>

  <div class="deck">

    <!-- ========================================================= -->
    <!-- SLIDE 01: COVER (RESTORED TO ORIGINAL CLEAN DESIGN) -->
    <!-- ========================================================= -->

    <div class="s cover active">
      <div class="s-num">01 / 15</div>
      <div class="cover-title">FlockML</div>
      <div class="cover-tag">Distributed compute infrastructure for sovereign artificial intelligence workloads.</div>
      <div class="cover-meta">
        Seed Investment Presentation<br>
        Supratim Dhara · Founder &amp; Chief Systems Architect<br>
        supratimdev.qzz.io/flock-ml
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>OVERVIEW</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 02: THE BOTTLENECK -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">02 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">AI Compute Is Becoming a Bottleneck</div>
          <div class="h-sub">
            The modern AI boom is encountering severe structural constraints across cost, access, and infrastructure centralization.
          </div>
        </div>

        <div class="g3">
          <div class="c">
            <div class="c-t">01. CENTRALIZATION</div>
            <div class="c-b">
              AI infrastructure is heavily concentrated in three hyperscale clouds. Developers face rigid pricing, forced minimum instance sizes, and arbitrary compute quotas.
            </div>
          </div>

          <div class="c">
            <div class="c-t">02. EXPONENTIAL COST</div>
            <div class="c-b">
              Running multi-billion parameter models in centralized data centers requires enormous CapEx for specialized cooling, power grids, and hardware depreciation.
            </div>
          </div>

          <div class="c">
            <div class="c-t">03. SOVEREIGN RISK</div>
            <div class="c-b">
              Nations and enterprises are sending sensitive proprietary datasets to offshore data centers, creating massive data sovereignty, security, and privacy vulnerabilities.
            </div>
          </div>
        </div>

        <div class="why-now-bottom">
          <span>THE CORE PROBLEM</span>
          Centralized data centers cannot sustainably scale to meet the exponential global demand for AI inference and training.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>PROBLEM DEFINITION</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 03: WHY NOW -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">03 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">Why Now? Three Structural Shifts</div>
          <div class="h-sub">
            Three technological convergence points make decentralized edge compute viable for the first time in history.
          </div>
        </div>

        <div class="g3">
          <div class="c">
            <div class="c-t">01. WEBGPU &amp; WASM SIMD</div>
            <div class="c-b">
              Modern browsers and edge runtimes now expose bare-metal GPU acceleration (WebGPU) and 128-bit vector math (Wasm SIMD) with zero native driver installation.
            </div>
          </div>

          <div class="c">
            <div class="c-t">02. 1.58-BIT QUANTIZATION</div>
            <div class="c-b">
              Ternary quantization (BitNet b1.58) replaces power-hungry floating-point multiplications with integer additions, reducing model memory footprints by 80.2%.
            </div>
          </div>

          <div class="c">
            <div class="c-t">03. SILICON SATURATION</div>
            <div class="c-b">
              Billions of consumer laptops, Apple Silicon chips, and telecom set-top boxes sit idle over 18 hours a day, wired to high-speed gigabit fiber and wall power.
            </div>
          </div>
        </div>

        <div class="why-now-bottom">
          <span>MARKET TIMING</span>
          The combination of WebGPU, BitNet quantization, and pervasive fiber makes a zero-CapEx decentralized compute grid technically and economically inevitable.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>MARKET TIMING</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 04: CORE THESIS & DEV EXPERIENCE (CLEAN SPACIOUS UI) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">04 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">A Cloud Experience Over a Distributed Compute Grid</div>
          <div class="h-sub">
            FlockML abstracts millions of heterogeneous devices into a single, programmable cloud API.
          </div>
        </div>

        <div class="g2" style="margin-top: 10px;">
          <div class="c" style="padding: 24px;">
            <div class="c-t">
              WHAT DEVELOPERS SEE
              <span class="badge">DEVELOPER API</span>
            </div>
            <div class="c-b" style="margin-top: 14px; line-height: 1.8; font-size: 14px;">
              • <strong>Drop-In API:</strong> Submit standard OpenAI or PyTorch requests and receive outputs instantly.<br>
              • <strong>Familiar Primitives:</strong> Deployments, inference endpoints, logs, and telemetry with standard SDKs.<br>
              • <strong>Zero Cluster Setup:</strong> No manual server management, SSH keys, or CUDA driver maintenance.
            </div>
          </div>

          <div class="c" style="padding: 24px; border-color: #3B82F6; background: rgba(59, 130, 246, 0.03);">
            <div class="c-t" style="color: #3B82F6;">
              WHAT FLOCKML ORCHESTRATES
              <span class="badge" style="color: #3B82F6; border-color: #3B82F6;">RUNTIME MESH</span>
            </div>
            <div class="c-b" style="margin-top: 14px; line-height: 1.8; font-size: 14px;">
              • <strong>Dynamic Discovery:</strong> Automatically matches workloads to active nodes across the network.<br>
              • <strong>Smart Tensor Sharding:</strong> Partitions large models across heterogeneous device RAM limits.<br>
              • <strong>Sub-5ms Failover:</strong> Dynamic work-stealing automatically reroutes dropped nodes with zero data loss.
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="margin-top: 24px;">
          <span>THE DEVELOPER PROMISE</span>
          The developer thinks about the workload. FlockML handles the infrastructure underneath.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>DEVELOPER EXPERIENCE &amp; THESIS</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 05: ARCHITECTURE (CRISP 4-CARD BALANCED UI) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">05 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">How the System Works: The Execution Layer</div>
          <div class="h-sub">
            Four specialized subsystems turn untrusted edge hardware into a fault-tolerant compute cluster.
          </div>
        </div>

        <div class="g2" style="gap: 16px;">
          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">01. FLOCKML WORKER <span class="badge">SANDBOX</span></div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.6; margin-top: 6px;">
              Zero-install runtime in WebAssembly SIMD and WebGPU. Executes tensor matrix math on consumer chips with zero host privilege.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">02. DISTRIBUTED COORDINATOR <span class="badge">TOPOLOGY</span></div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.6; margin-top: 6px;">
              High-throughput orchestration layer tracking node telemetry, latency, and RAM to shard model weights dynamically across the network.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">03. zk-VERIFICATION <span class="badge">SUB-0.1MS</span></div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.6; margin-top: 6px;">
              Zero-knowledge proof-of-compute commitments evaluate instantly without re-running weights, rejecting Byzantine or corrupt updates.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">04. FAULT-TOLERANT FAILOVER <span class="badge">SUB-5MS</span></div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.6; margin-top: 6px;">
              Work-stealing P2P ring scheduler. If a node drops, neighboring machines seamlessly pick up the pipeline stage with zero token loss.
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="margin-top: 20px;">
          <span>SYSTEM ARCHITECTURE</span>
          Untrusted edge devices are transformed into an enterprise-grade compute substrate through deterministic verification and sub-5ms failover.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>SYSTEM ARCHITECTURE</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 06: TECHNICAL PROOF (BITNET 1.58-BIT) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">06 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">Technical Proof: BitNet 1.58-Bit Quantization</div>
          <div class="h-sub">
            Mathematical breakthroughs in ternary weight representation make edge AI faster, cheaper, and radically efficient.
          </div>
        </div>

        <div class="g3">
          <div class="c">
            <div class="c-t">80.2% VRAM REDUCTION</div>
            <div class="c-b">
              Ternary weights {-1, 0, +1} pack 16 parameters into a single 32-bit register. A 70B parameter model that normally requires 140GB VRAM now fits comfortably across everyday edge memory pools.
            </div>
          </div>

          <div class="c">
            <div class="c-t">INTEGER ADDITIONS</div>
            <div class="c-b">
              Replaces energy-heavy floating-point matrix multiplications (FP16/FP32) with lightweight integer additions, slashing power consumption by 85% on standard consumer CPUs and integrated GPUs.
            </div>
          </div>

          <div class="c">
            <div class="c-t">SUB-0.1MS VERIFICATION</div>
            <div class="c-b">
              Coordinator validates mathematical integrity through coordinate-wise hash commitments without re-executing inference, maintaining line-rate execution across thousands of nodes.
            </div>
          </div>
        </div>

        <div class="why-now-bottom">
          <span>THE QUANTIZATION LEAP</span>
          BitNet 1.58-bit turns consumer chips into high-speed inference engines, eliminating the requirement for expensive $30,000 datacenter GPUs.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>QUANTIZATION &amp; BENCHMARKS</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 07: UNIT ECONOMICS ($32 VS $10) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">07 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">The Economics: Hyperscale vs. Decentralized Compute</div>
          <div class="h-sub">
            By eliminating data center CapEx, we fundamentally restructure the cost of AI compute while retaining software margins.
          </div>
        </div>

        <div class="g2">
          <div class="pricing-box">
            <div class="pricing-title" style="color: #F87171;">HYPERSCALE CLOUD</div>
            <div class="pricing-body">
              <div class="c-v">~$32.00 <span style="font-size: 16px; color: var(--t2);">(~₹2,650)</span></div>
              <div class="c-vs">MINIMUM HOURLY BILL (FORCED 8x A100 NODE)</div>
              <br>
              <strong>Why it is expensive:</strong><br>
              • Forced to rent massive 8-GPU nodes with rigid minimums<br>
              • Datacenter real estate, HVAC cooling, and power overhead<br>
              • Corporate margin stacking across infrastructure layers<br>
              • Continuous rapid hardware depreciation
            </div>
          </div>

          <div class="pricing-box" style="border-color: #34D399;">
            <div class="pricing-title" style="color: #34D399;">FLOCKML DECENTRALIZED</div>
            <div class="pricing-body">
              <div class="c-v">~$10.00 <span style="font-size: 16px; color: var(--t2);">(~₹830)</span></div>
              <div class="c-vs">PER HOUR (FLEXIBLE DISTRIBUTED CLUSTER)</div>
              <br>
              <strong>Why it is disruptive:</strong><br>
              • Developers save ~70% compared to legacy cloud minimums<br>
              • Zero hardware CapEx or datacenter cooling costs for FlockML<br>
              • Compute providers earn high yield on sunk-cost hardware<br>
              • <strong>78%+ Gross Margins (Pure software take-rate)</strong>
            </div>
          </div>
        </div>

        <div class="accent">
          When compute costs drop by 70%+, developers can deploy entirely new classes of AI applications that were previously economically unviable.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>UNIT ECONOMICS</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 08: DEVELOPER VALUE & ADOPTION FUNNEL (BALANCED 2-COL UI) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">08 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">Developer Value &amp; Incremental Migration</div>
          <div class="h-sub">
            We eliminate enterprise switching friction through a 4-step Trojan-horse adoption funnel.
          </div>
        </div>

        <div class="g2" style="gap: 20px;">
          <!-- Left: Value Drivers -->
          <div class="c" style="display: flex; flex-direction: column; justify-content: space-between; padding: 22px;">
            <div class="c-t" style="margin-bottom: 12px;">WHY DEVELOPERS MIGRATE <span class="badge">VALUE PILLARS</span></div>
            
            <div style="margin-bottom: 14px;">
              <strong style="color: #34D399; font-family: 'JetBrains Mono', monospace; font-size: 13px;">01. 70% COST REDUCTION</strong>
              <div class="c-b" style="font-size: 13.5px; margin-top: 2px;">Bypass forced 8-GPU cloud minimums and pay strictly for active matrix cycles executed.</div>
            </div>

            <div style="margin-bottom: 14px;">
              <strong style="color: #3B82F6; font-family: 'JetBrains Mono', monospace; font-size: 13px;">02. INSTANT CAPACITY</strong>
              <div class="c-b" style="font-size: 13.5px; margin-top: 2px;">Access millions of available edge and enterprise cores with zero GPU waitlists or quotas.</div>
            </div>

            <div>
              <strong style="color: #FBBF24; font-family: 'JetBrains Mono', monospace; font-size: 13px;">03. ZERO LOCK-IN</strong>
              <div class="c-b" style="font-size: 13.5px; margin-top: 2px;">Standard REST/OpenAI interfaces make routing workloads to FlockML take under 10 lines of code.</div>
            </div>
          </div>

          <!-- Right: 4-Step Funnel -->
          <div class="c" style="padding: 22px; border-color: #3B82F6; background: rgba(59, 130, 246, 0.03);">
            <div class="c-t" style="color: #3B82F6; margin-bottom: 14px;">THE 4-STEP ADOPTION FUNNEL <span class="badge" style="color: #3B82F6; border-color: #3B82F6;">LOW FRICTION</span></div>
            
            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: flex-start;">
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #3B82F6; background: rgba(59, 130, 246, 0.1); padding: 2px 6px; border-radius: 3px;">01</div>
              <div class="c-b" style="font-size: 13.5px; line-height: 1.4;"><strong>Add Secondary Target:</strong> Keep AWS stack intact; plug in FlockML API key in 5 minutes.</div>
            </div>

            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: flex-start;">
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #3B82F6; background: rgba(59, 130, 246, 0.1); padding: 2px 6px; border-radius: 3px;">02</div>
              <div class="c-b" style="font-size: 13.5px; line-height: 1.4;"><strong>Route Batch &amp; Eval:</strong> Offload non-critical offline fine-tuning, embeddings, and synthetic data tests.</div>
            </div>

            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: flex-start;">
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #3B82F6; background: rgba(59, 130, 246, 0.1); padding: 2px 6px; border-radius: 3px;">03</div>
              <div class="c-b" style="font-size: 13.5px; line-height: 1.4;"><strong>Dynamic Routing:</strong> SDK automatically routes traffic to wherever compute is cheapest.</div>
            </div>

            <div style="display: flex; gap: 12px; align-items: flex-start;">
              <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #3B82F6; background: rgba(59, 130, 246, 0.1); padding: 2px 6px; border-radius: 3px;">04</div>
              <div class="c-b" style="font-size: 13.5px; line-height: 1.4;"><strong>Scale Production:</strong> As confidence builds, production inference organically shifts onto FlockML.</div>
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="margin-top: 20px;">
          <span>MIGRATION PRINCIPLE</span>
          Do not ask developers to rewrite their world on Day 1. Give them a zero-risk, high-margin execution target.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>ADOPTION STRATEGY</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 09: THE EXECUTION LAYER POSITIONING -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">09 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">The Execution Layer for Distributed Compute</div>
          <div class="h-sub">
            FlockML abstracts millions of heterogeneous devices into a single, programmable cloud for AI workloads.
          </div>
        </div>

        <div class="g2">
          <div class="c">
            <div class="c-t">
              TRADITIONAL VS. FLOCKML
              <span class="badge">PARADIGM SHIFT</span>
            </div>
            <div class="c-b" style="margin-top: 14px; line-height: 1.8;">
              • <strong>Hyperscale Cloud:</strong> Own physical server racks → Rent expensive fixed instances.<br>
              • <strong>GPU Marketplaces:</strong> Aggregate individual servers → Manual SSH and fragmented hardware.<br>
              • <strong style="color: #3B82F6;">FlockML:</strong> Pure software orchestration layer → Developers interact with a standard API while our runtime handles sharding, failover, and execution underneath.
            </div>
          </div>

          <div class="c" style="border-color: #3B82F6; background: rgba(59, 130, 246, 0.03);">
            <div class="c-t" style="color: #3B82F6;">
              WHAT THE RUNTIME HANDLES
              <span class="badge" style="color: #3B82F6; border-color: #3B82F6;">ZERO OVERHEAD</span>
            </div>
            <div class="c-b" style="margin-top: 14px; line-height: 1.8;">
              • <strong>Dynamic Tensor Sharding:</strong> Automatically partitions 70B &amp; 405B models across varied device RAM limits.<br>
              • <strong>Cryptographic Verification:</strong> Sub-0.1ms zk-SNARK gates validate matrix computation.<br>
              • <strong>Self-Healing Failover:</strong> Sub-5ms rerouting ensures zero pipeline stall if a device disconnects.
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="font-family: 'JetBrains Mono', monospace; font-size: 13px;">
          <span style="color: #FBBF24;">CORE MOAT</span>
          FlockML does not need to own the world's compute. We become the software layer through which the world's available compute is executed.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>EXECUTION LAYER POSITIONING</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 10: COMPETITIVE LANDSCAPE -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">10 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">Where FlockML Sits</div>
          <div class="h-sub">
            Positioned at the intersection of enterprise cloud usability and zero-CapEx decentralized compute.
          </div>
        </div>

        <table class="tbl">
          <thead>
            <tr>
              <th>Model</th>
              <th>Infrastructure</th>
              <th>Pricing / CapEx</th>
              <th>Developer UX</th>
              <th>Fault Tolerance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Hyperscale Cloud</td>
              <td>Centralized Datacenters</td>
              <td>High ($32/hr minimums)</td>
              <td>Standard Cloud APIs</td>
              <td>Centralized Failover</td>
            </tr>
            <tr>
              <td>GPU Marketplaces</td>
              <td>Fragmented Servers</td>
              <td>Medium (Spot rates)</td>
              <td>Complex (Manual SSH)</td>
              <td>Manual Reconnect</td>
            </tr>
            <tr>
              <td>Crypto DePINs</td>
              <td>Consumer Rigs (Tokenized)</td>
              <td>Volatile Token Gas</td>
              <td>Cryptic Web3 Wallets</td>
              <td>High Failure Rates</td>
            </tr>
            <tr style="background: rgba(59, 130, 246, 0.08); font-weight: 600;">
              <td style="color: #3B82F6;">FlockML</td>
              <td style="color: #FFF;">Decentralized Edge Mesh</td>
              <td style="color: #34D399;">Disruptive ($10/hr Flat)</td>
              <td style="color: #FFF;">Standard REST / SDK</td>
              <td style="color: #34D399;">Sub-5ms Self-Healing</td>
            </tr>
          </tbody>
        </table>

        <div class="why-now-bottom" style="margin-top: 24px;">
          <span>STRATEGIC MOAT</span>
          We do not ask enterprises to manage crypto wallets or raw SSH keys. We offer a Tier-1 cloud developer experience on top of a zero-CapEx distributed compute grid.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>COMPETITIVE LANDSCAPE</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 11: THE COMPUTE SUPPLY ENGINE -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">11 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">The Compute Supply Engine: Office Laptops to 100M Telecom Boxes</div>
          <div class="h-sub">
            How FlockML aggregates petabytes of compute capacity with zero infrastructure capital expenditure.
          </div>
        </div>

        <div class="g3">
          <div class="c">
            <div class="c-t">
              01. ENTERPRISE FLEETS
              <span class="badge">B2B SUPPLY</span>
            </div>
            <div class="c-b">
              Thousands of corporate and government laptops (MeitY, CESC, banks) sit idle from 7 PM to 7 AM. Organizations run internal AI models across their own hardware grid with zero data leaving the perimeter.
            </div>
          </div>

          <div class="c" style="border-color: #3B82F6; background: rgba(59, 130, 246, 0.04);">
            <div class="c-t" style="color: #3B82F6;">
              02. TELECOM SET-TOP BOXES
              <span class="badge" style="color: #3B82F6; border-color: #3B82F6;">100M+ SCALE</span>
            </div>
            <div class="c-b">
              30M+ Reliance Jio &amp; Airtel 4K boxes connected to fiber and wall power, idle 20 hours/day. Single over-the-air Wasm injection creates a <strong>150 PFLOPs national living-room supercomputer</strong>.
            </div>
          </div>

          <div class="c">
            <div class="c-t">
              03. UTILIZATION-BASED YIELD
              <span class="badge">ZERO IDLE BURN</span>
            </div>
            <div class="c-b">
              FlockML pays providers strictly for active matrix cycles executed. Telcos earn new high-margin enterprise revenue, while consumers receive broadband bill credits.
            </div>
          </div>
        </div>

        <div class="why-now-bottom">
          <span>SCALE MULTIPLIER</span>
          10M Jio/Airtel Set-Top Boxes + Wasm SIMD = 10 Petabytes VRAM &amp; 150 PFLOPs Compute with $0 Cloud CapEx.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>COMPUTE SUPPLY ENGINE</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 12: BUSINESS MODEL -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">12 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">A Compute Cloud Business Model</div>
          <div class="h-sub">
            High software gross margins through usage-based compute billing and enterprise private deployments.
          </div>
        </div>

        <div class="g3">
          <div class="c">
            <div class="c-t">01. USAGE COMPUTE API</div>
            <div class="c-b">
              Developers pay per token or compute-second ($10/hr cluster equivalent). FlockML captures a 75% to 80% software margin after node provider payouts.
            </div>
          </div>

          <div class="c">
            <div class="c-t">02. ENTERPRISE PRIVATE GRID</div>
            <div class="c-b">
              Annual software licensing ($100k-$500k ARR) for enterprises and banks to turn internal office machines into a private, air-gapped sovereign AI training cluster.
            </div>
          </div>

          <div class="c">
            <div class="c-t">03. SOVEREIGN AI DEPLOYMENTS</div>
            <div class="c-b">
              Government and national AI grid contracts (IndiaAI, MeitY, Gulf Sovereigns) deploying national model training infrastructure with full data localization.
            </div>
          </div>
        </div>

        <div class="why-now-bottom">
          <span>HIGH-MARGIN SOFTWARE ECONOMICS</span>
          FlockML operates with pure software gross margins (78%+) because we never purchase, house, or depreciate physical server hardware.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>BUSINESS MODEL</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 13: 24-MONTH ROADMAP (CLEAN 4-PHASE PROGRESSION UI) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">13 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">The Next 24 Months: Proof → Product → Network → Scale</div>
          <div class="h-sub">
            A disciplined, milestone-driven execution plan focused on technical validation and enterprise distribution.
          </div>
        </div>

        <div class="g2" style="gap: 16px;">
          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">
              PHASE 1: PROTOCOL &amp; BENCHMARKS
              <span class="badge">MONTHS 1-6</span>
            </div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.7; margin-top: 8px;">
              • Deploy WebGPU &amp; Wasm SIMD kernels for Llama-3 70B.<br>
              • Complete 500-node MeitY &amp; enterprise private grid pilot.<br>
              • Release developer SDK &amp; CLI with drop-in OpenAI parity.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">
              PHASE 2: TELECOM PILOT &amp; PUBLIC API
              <span class="badge">MONTHS 7-12</span>
            </div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.7; margin-top: 8px;">
              • Partner with Indian telecom for 50,000 set-top box pilot.<br>
              • Launch public developer compute API with usage billing.<br>
              • Scale network to 10,000 active nodes with sub-5ms failover.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">
              PHASE 3: ENTERPRISE COMMERCIALIZATION
              <span class="badge">MONTHS 13-18</span>
            </div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.7; margin-top: 8px;">
              • Sign 20+ enterprise customers across banking and defense.<br>
              • Expand telecom footprint to 1M+ connected living rooms.<br>
              • Reach $3M ARR with positive software unit economics.
            </div>
          </div>

          <div class="c" style="padding: 18px 20px;">
            <div class="c-t">
              PHASE 4: GLOBAL SOVEREIGN GRIDS
              <span class="badge">MONTHS 19-24</span>
            </div>
            <div class="c-b" style="font-size: 13.5px; line-height: 1.7; margin-top: 8px;">
              • Deploy sovereign AI grid infrastructure in UAE &amp; Gulf markets.<br>
              • Scale network beyond 10M active edge devices globally.<br>
              • Establish FlockML as the global distributed execution layer.
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="margin-top: 18px;">
          <span>EXECUTION MILESTONES</span>
          From technical proof to millions of distributed nodes delivering sovereign AI compute.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>24-MONTH ROADMAP</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 14: THE ASK / CAPITAL ALLOCATION (SHARP HIGH-IMPACT UI) -->
    <!-- ========================================================= -->

    <div class="s">
      <div class="s-num">14 / 15</div>
      <div class="s-body">
        <div class="h-section">
          <div class="h1">The Ask: Seed Round Capital Allocation</div>
          <div class="h-sub">
            Raising $20M - $30M Seed to scale our distributed systems engineering team and accelerate telecom partnerships.
          </div>
        </div>

        <div class="g2" style="gap: 20px;">
          <!-- Left: Deal Terms -->
          <div class="c" style="padding: 24px; border-color: #3B82F6; background: rgba(59, 130, 246, 0.04); display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div class="c-t" style="color: #3B82F6; margin-bottom: 14px;">ROUND PARAMETERS <span class="badge" style="color: #3B82F6; border-color: #3B82F6;">SEED ROUND</span></div>
              
              <div style="margin-bottom: 14px;">
                <div class="c-v" style="font-size: 32px; color: #FFF;">$20M - $30M</div>
                <div class="c-vs" style="color: #A1A1AA;">TARGET ROUND SIZE</div>
              </div>

              <div style="margin-bottom: 14px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 18px; font-weight: 700; color: #FFF;">$90M Pre / $120M Post</div>
                <div class="c-vs" style="color: #A1A1AA;">VALUATION FRAMEWORK</div>
              </div>

              <div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 600; color: #34D399;">24 - 30 Months Runway</div>
                <div class="c-vs" style="color: #A1A1AA;">PATH TO SERIES A &amp; SOVEREIGN SCALE</div>
              </div>
            </div>

            <div class="c-vs" style="border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px; margin-top: 14px;">
              Co-investors: Deep Tech, Infrastructure &amp; Sovereign Funds
            </div>
          </div>

          <!-- Right: Capital Deployment -->
          <div class="c" style="padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
            <div class="c-t" style="margin-bottom: 14px;">CAPITAL ALLOCATION <span class="badge">DEPLOYMENT</span></div>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="padding-bottom: 8px; border-bottom: 1px solid var(--border);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                  <strong style="color: #FFF; font-size: 14px;">45% Core Distributed Engineering</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; color: #3B82F6; font-size: 13px; font-weight: 700;">$9.0M - $13.5M</span>
                </div>
                <div class="c-b" style="font-size: 12.5px;">Wasm SIMD kernels, WebGPU compute pipelines, zk-SNARK verifiers.</div>
              </div>

              <div style="padding-bottom: 8px; border-bottom: 1px solid var(--border);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                  <strong style="color: #FFF; font-size: 14px;">25% Telecom &amp; Enterprise BD</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; color: #34D399; font-size: 13px; font-weight: 700;">$5.0M - $7.5M</span>
                </div>
                <div class="c-b" style="font-size: 12.5px;">Telecom set-top box rollouts, MeitY pilots, enterprise private grids.</div>
              </div>

              <div style="padding-bottom: 8px; border-bottom: 1px solid var(--border);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                  <strong style="color: #FFF; font-size: 14px;">20% Developer Ecosystem</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; color: #FBBF24; font-size: 13px; font-weight: 700;">$4.0M - $6.0M</span>
                </div>
                <div class="c-b" style="font-size: 12.5px;">Global developer SDK, documentation, hackathons, and grants.</div>
              </div>

              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                  <strong style="color: #FFF; font-size: 14px;">10% Security &amp; Compliance</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; color: #A1A1AA; font-size: 13px; font-weight: 700;">$2.0M - $3.0M</span>
                </div>
                <div class="c-b" style="font-size: 12.5px;">SOC 2 Type II, DPDP Act 2023 compliance, cryptographic audits.</div>
              </div>
            </div>
          </div>
        </div>

        <div class="why-now-bottom" style="margin-top: 20px;">
          <span>INVESTMENT CATALYST</span>
          Capital will establish FlockML as the category leader in zero-CapEx distributed AI infrastructure.
        </div>
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>SEED CAPITAL ALLOCATION</span>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- SLIDE 15: CLOSING & VISION -->
    <!-- ========================================================= -->

    <div class="s cover">
      <div class="s-num">15 / 15</div>
      <div class="cover-title">FlockML</div>
      <div class="cover-tag">The Future of Sovereign AI Infrastructure. Building the compute layer for the next billion devices.</div>
      <div class="cover-meta">
        Supratim Dhara · Founder &amp; Chief Systems Architect<br>
        supratim@flockml.com · supratimdev.qzz.io/flock-ml<br>
        Bangalore · Kolkata · Dubai
      </div>
      <div class="s-foot">
        <span>FLOCKML - CONFIDENTIAL</span>
        <span>THANK YOU</span>
      </div>
    </div>

  </div>

  <!-- ========================================================= -->
  <!-- NAVIGATION JS -->
  <!-- ========================================================= -->

  <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.s');

    function showSlide(index) {
      if (index < 0) index = 0;
      if (index >= slides.length) index = slides.length - 1;

      slides.forEach(s => s.classList.remove('active'));
      slides[index].classList.add('active');
      currentSlide = index;
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
        e.preventDefault();
        showSlide(currentSlide + 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        showSlide(currentSlide - 1);
      }
    });

    document.body.addEventListener('click', (e) => {
      if (e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON') {
        if (currentSlide < slides.length - 1) {
          showSlide(currentSlide + 1);
        }
      }
    });

    showSlide(0);
  </script>

</body>
</html>
"""

full_deck = head + deck_body
full_deck = full_deck.replace('—', '-').replace('–', '-')

with open('/Users/supratim/Desktop/flockml-sovereign/docs/Anicut_Capital_Pitch_Deck.html', 'w', encoding='utf-8') as f:
    f.write(full_deck)

print('Updated pitch deck with pristine UI on slides 1, 4, 5, 8, 13, 14.')
