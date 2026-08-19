import os
import time
import smtplib
from email.message import EmailMessage

PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'
GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

INVESTORS = [
    {
        "name": "GVFL Investment Team",
        "email": "investmentdesk2@gvfl.com",
        "firm": "GVFL",
        "hook": "pioneering Indian deeptech and strategic AI compute infrastructure"
    },
    {
        "name": "Sanjay",
        "email": "sanjay@100x.vc",
        "firm": "100X.VC",
        "hook": "100X.VC's focus on foundational deeptech moats and AI infrastructure"
    },
    {
        "name": "Aviral",
        "email": "aviral@ajuniorvc.com",
        "firm": "AJVC",
        "hook": "AJVC's thesis on Indian deeptech, sovereign compute, and developer ecosystems"
    },
    {
        "name": "Ashley",
        "email": "ashley@capital6.com",
        "firm": "Capital6",
        "hook": "Capital6's investments in early-stage deeptech and next-generation software architecture"
    },
    {
        "name": "Joy",
        "email": "jgrant@canaan.com",
        "firm": "Canaan Partners",
        "hook": "Canaan's frontier computing, enterprise AI infrastructure, and developer platforms"
    },
    {
        "name": "Brian",
        "email": "brian@mtechcapital.com",
        "firm": "MTech Capital",
        "hook": "MTech Capital's strategic software and enterprise AI infrastructure investments"
    },
    {
        "name": "Marina",
        "email": "marina@davidovs.com",
        "firm": "Davidovs VC",
        "hook": "Davidovs VC's focus on deeptech, developer tools, and decentralized AI systems"
    },
    {
        "name": "Brandon",
        "email": "brandon@sunsetventures.xyz",
        "firm": "Sunset Ventures",
        "hook": "Sunset Ventures' early-stage investments in AI infrastructure and distributed compute"
    }
]

def generate_email(inv):
    name = inv["name"]
    firm = inv["firm"]
    hook = inv["hook"]
    
    salutation = f"Hi {name}" if name != f"{firm} Investment Team" else f"Hi {firm} Team"
    
    body = f"""{salutation},

Following {firm}'s focus on {hook}:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary consumer & enterprise devices into a Decentralized AI Inference Cloud - executing 70B & 405B LLM workloads at ~70% lower cost than AWS/Azure with zero data egress.

Key Highlights:
• Commercial Wedge: 1-line OpenAI/OpenRouter drop-in API (`baseURL: api.flockml.com/v1`) providing 70% cheaper token pricing on Llama-3.2, Gemma-2B & DeepSeek-R1 with 78%+ software gross margins.
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Compute Supply: Monetizing idle enterprise hardware and domestic silicon with zero datacenter leases or server CapEx.
• Deep Tech Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), dynamic layer sharding across local networks, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising our Seed round to accelerate developer onboarding and enterprise pilots.

I have attached our Seed Investment Presentation (PDF). I would welcome 10 minutes with the {firm} team this week to share our live benchmarks and technical blueprint.

Live Overview: https://supratimdev.qzz.io/flock-ml

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
    # Strict scrub of em dashes
    body = body.replace('—', '-').replace('–', '-')
    return body

def main():
    if not os.path.exists(PDF_PATH):
        print(f"Error: PDF not found at {PDF_PATH}")
        return

    with open(PDF_PATH, 'rb') as f:
        pdf_data = f.read()

    print(f"Loaded PDF: {len(pdf_data)} bytes")
    print(f"Connecting to SMTP server as {GMAIL_USER}...")
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    print("SMTP Authentication Successful.\n")

    for idx, inv in enumerate(INVESTORS, 1):
        msg = EmailMessage()
        subject = f"FlockML: Decentralized AI Inference Cloud (70% Cheaper than AWS)"
        msg['Subject'] = subject
        msg['From'] = f"Supratim Dhara | FlockML <{GMAIL_USER}>"
        msg['To'] = inv["email"]
        
        body = generate_email(inv)
        msg.set_content(body)
        
        msg.add_attachment(
            pdf_data,
            maintype='application',
            subtype='pdf',
            filename='FlockML - Seed Investment Presentation.pdf'
        )
        
        print(f"[{idx}/{len(INVESTORS)}] Sending to {inv['name']} at {inv['firm']} ({inv['email']})...")
        server.send_message(msg)
        print(f"  ✓ Successfully sent to {inv['email']}")
        time.sleep(1.5)

    server.quit()
    print("\n==================================================")
    print(f"  All {len(INVESTORS)} VC pitches successfully delivered!")
    print("==================================================")

if __name__ == '__main__':
    main()
