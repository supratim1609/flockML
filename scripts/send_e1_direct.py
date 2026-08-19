import os
import smtplib
from email.message import EmailMessage

PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'
GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

def main():
    if not os.path.exists(PDF_PATH):
        print(f"Error: PDF not found at {PDF_PATH}")
        return

    with open(PDF_PATH, 'rb') as f:
        pdf_data = f.read()

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

    targets = [
        {"name": "Ana", "email": "ana@e1.vc"},
        {"name": "E1 Ventures Team", "email": "team@e1.vc"},
        {"name": "E1 Ventures Team", "email": "hello@e1.vc"}
    ]

    for target in targets:
        name = target["name"]
        email = target["email"]
        salutation = f"Hi {name}" if name == "Ana" else "Hi E1 Ventures Team"

        body = f"""{salutation},

Following E1 Ventures' investment thesis on deeptech, frontier computing, and next-gen AI infrastructure:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary consumer & enterprise devices into a Decentralized AI Inference Cloud - executing 70B & 405B LLM workloads at ~70% lower cost than AWS/Azure with zero data egress.

Key Highlights:
• Commercial Wedge: 1-line OpenAI/OpenRouter drop-in API (`baseURL: api.flockml.com/v1`) providing 70% cheaper token pricing on Llama-3.2, Gemma-2B & DeepSeek-R1 with 78%+ software gross margins.
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Compute Supply: Monetizing idle enterprise hardware and domestic silicon with zero datacenter leases or server CapEx.
• Deep Tech Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), dynamic layer sharding across local networks, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising our Seed round to accelerate developer onboarding and enterprise pilots.

I have attached our Seed Investment Presentation (PDF). I would welcome 10 minutes with you this week to share our live benchmarks and technical blueprint.

Live Overview: https://supratimdev.qzz.io/flock-ml

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
        body = body.replace('—', '-').replace('–', '-')

        msg = EmailMessage()
        msg['Subject'] = "FlockML: Decentralized AI Inference Cloud (70% Cheaper than AWS)"
        msg['From'] = f"Supratim Dhara | FlockML <{GMAIL_USER}>"
        msg['To'] = email
        msg.set_content(body)
        msg.add_attachment(
            pdf_data,
            maintype='application',
            subtype='pdf',
            filename='FlockML - Seed Investment Presentation.pdf'
        )

        try:
            print(f"Sending pitch to {name} ({email})...")
            server.send_message(msg)
            print(f"  ✓ Successfully sent to {email}")
        except Exception as e:
            print(f"  ✗ Error sending to {email}: {e}")

    server.quit()

if __name__ == '__main__':
    main()
