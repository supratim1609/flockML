import re
import subprocess
import os

HTML_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/CESC_RPSG_Executive_Pitch_Deck.html'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/CESC_RPSG_Executive_Pitch_Deck.pdf'
CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

NEW_SLIDE_5_6 = """
  <!-- ========================================== -->
  <!-- SLIDE 05: THE RPSG NATIONAL AI PLAY -->
  <!-- ========================================== -->
  <div class="slide" id="s5">
    <div class="slide-hdr">
      <div>
        <span class="slide-badge electric">NATIONAL LEADERSHIP &amp; INDIAAI MISSION</span>
        <div class="slide-title">RPSG Group: The Sovereign AI Infrastructure Champion</div>
        <div class="slide-sub">
          How RPSG enters the AI sector and leads the ₹10,372 Crore IndiaAI National Sovereign Mandate.
        </div>
      </div>
      <div class="slide-num">05 / 10</div>
    </div>

    <div class="slide-body">
      <div class="grid-2">
        <div class="card highlight-gold">
          <div class="card-title" style="color: var(--accent-gold); font-size: 17px;">The RPSG National Strategic Moat</div>
          <div class="card-body" style="display: flex; flex-direction: column; gap: 10px;">
            <p>• <strong>The IndiaAI Sovereign Opportunity:</strong> The Government of India has committed <strong>₹10,372 Crores</strong> to build domestic AI compute infrastructure that does not depend on foreign cloud vendors (AWS/Microsoft).</p>
            <p>• <strong>The First-Mover Power Conglomerate:</strong> While other business houses build expensive imported GPU datacenters, RPSG can pioneer <strong>Asia's First Zero-CapEx Sovereign Utility Grid</strong>—transforming power substations into decentralized AI supercomputing nodes.</p>
            <p>• <strong>Direct National Influence:</strong> RPSG becomes the flagship partner presenting the national blueprint directly to the Ministry of Power, MeitY, and state DISCOMs across India.</p>
          </div>
        </div>

        <div class="card highlight-blue">
          <div class="card-title" style="color: var(--accent-blue); font-size: 17px;">The Unbeatable Conglomerate Advantage</div>
          <div class="card-body" style="display: flex; flex-direction: column; gap: 10px;">
            <p>• <strong>Energy Cost Monopoly:</strong> Power is 60%+ of AI datacenter OpEx. CESC has generation-cost power (₹3.50/kWh), creating a permanent cost moat that tech companies cannot match.</p>
            <p>• <strong>From Regional Utility to National AI Cloud:</strong> CESC transitions from a tariff-capped power distributor to an <strong>unregulated Sovereign AI Compute Cloud</strong> selling tokens to Indian banks, defense, and healthcare.</p>
            <p>• <strong>Institutional Clout:</strong> With RPSG's scale and executive relationships, bureaucratic hurdles vanish and national utility rollouts become immediate reality.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="slide-foot">
      <span>FLOCKML × CESC / RPSG GROUP</span>
      <span>05 / 10</span>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- SLIDE 06: RPSG GROUP SYNERGIES -->
  <!-- ========================================== -->
  <div class="slide" id="s6">
    <div class="slide-hdr">
      <div>
        <span class="slide-badge purple">GROUP-LEVEL ECOSYSTEM VALUE</span>
        <div class="slide-title">RPSG Group Synergies: Powering the Conglomerate</div>
        <div class="slide-sub">
          Keeping 100% of the group's AI compute expenditures inside the RPSG balance sheet.
        </div>
      </div>
      <div class="slide-num">06 / 10</div>
    </div>

    <div class="slide-body">
      <div class="grid-4">
        <div class="card highlight-green">
          <div class="slide-badge green">CESC POWER</div>
          <div class="card-title" style="font-size: 14.5px;">Sovereign Grid AI</div>
          <div class="card-body" style="font-size: 12px;">
            Saves ₹3–5 Cr/yr in smart meter cloud bills; prevents DSM penalties and distribution transformer burnouts.
          </div>
        </div>

        <div class="card highlight-blue">
          <div class="slide-badge">FIRSTSOURCE</div>
          <div class="card-title" style="font-size: 14.5px;">$1B+ BPO Arm</div>
          <div class="card-body" style="font-size: 12px;">
            Runs internal LLM call transcription &amp; customer automation at ~70% lower cost than OpenAI/AWS.
          </div>
        </div>

        <div class="card highlight-gold">
          <div class="slide-badge gold">WOODLANDS</div>
          <div class="card-title" style="font-size: 14.5px;">Healthcare AI</div>
          <div class="card-body" style="font-size: 12px;">
            100% private, on-premises radiology &amp; clinical diagnostics with zero patient data leakage.
          </div>
        </div>

        <div class="card highlight-blue">
          <div class="slide-badge electric">SPENCER'S</div>
          <div class="card-title" style="font-size: 14.5px;">Retail Analytics</div>
          <div class="card-body" style="font-size: 12px;">
            Real-time inventory computer vision and demand forecasting across 150+ stores with zero server CapEx.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-foot">
      <span>FLOCKML × CESC / RPSG GROUP</span>
      <span>06 / 10</span>
    </div>
  </div>
"""

def update_slides():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to replace slide 5 and 6
    pattern = r'<!-- =+ -->\s*<!-- SLIDE 05:.*?<!-- =+ -->\s*<!-- SLIDE 07:'
    replacement = NEW_SLIDE_5_6 + '\n  <!-- ==========================================\n  <!-- SLIDE 07:'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✓ Updated HTML Slides 5 & 6 with RPSG National IndiaAI Sovereign Vision!")

    # Re-render PDF
    cmd = [
        CHROME_PATH,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=5000',
        f'--print-to-pdf={PDF_PATH}',
        f'file://{HTML_PATH}'
    ]
    subprocess.run(cmd, check=True)
    print(f"✓ Re-rendered High-Res PDF: {PDF_PATH}")

if __name__ == '__main__':
    update_slides()
