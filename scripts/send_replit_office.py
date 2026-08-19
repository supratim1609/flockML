import os
import smtplib
from email.message import EmailMessage

PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'
GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

to_email = 'ceo-office@repl.it'
subject = 'FlockML: Sovereign Decentralized AI Compute Grid ($20M Seed Allocation) - Replit Office'

body = """Dear Office of Amjad Masad (Replit),

Following Amjad and Replit's leadership in browser-native execution and WebAssembly systems:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary edge and enterprise hardware into a Sovereign AI Inference & Compute Grid - executing 70B and 405B LLM workloads at ~70% lower cost than centralized hyperscale clouds with zero offshore data egress.

Key Highlights:
• Commercial Wedge (Sovereign Inference): 1-line OpenAI drop-in API (`baseURL: api.flockml.com/v1`) providing 70% cheaper token pricing on Llama-3 70B & DeepSeek-R1 with 78%+ software gross margins.
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Compute Supply: Monetizing idle corporate fleets (7 PM - 7 AM) and 100M telecom set-top boxes (150 PFLOPs capacity) with zero datacenter leases.
• Deep Tech Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), sub-0.1ms zk-SNARK cryptographic verification, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising $20.0M USD Seed round for 20% equity ($80M Pre / $100M Post-Money Valuation).

I have attached our Seed Investment Presentation (PDF). I would welcome 10 minutes with Amjad or the Replit team this week to share our technical blueprint and benchmarks.

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""

# Scrub em dashes
body = body.replace('—', '-').replace('–', '-')

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = f"Supratim Dhara <{GMAIL_USER}>"
msg['To'] = to_email
msg.set_content(body)

if os.path.exists(PDF_PATH):
    with open(PDF_PATH, 'rb') as f:
        pdf_data = f.read()
    msg.add_attachment(
        pdf_data, 
        maintype='application', 
        subtype='pdf', 
        filename='FlockML - Seed Investment Presentation.pdf'
    )

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
server.send_message(msg)
server.quit()
print(f"SUCCESS: Forwarded pitch to Amjad Masad's executive office -> {to_email}")
