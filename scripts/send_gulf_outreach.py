import csv
import time
import os
import smtplib
from email.message import EmailMessage

CSV_FILE = '/Users/supratim/Desktop/flockml-sovereign/docs/Archive/FlockML_50_Dubai_UAE_and_Gulf_Sovereign_Investors - Sheet1.csv'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

def generate_gulf_body(entity, name_title, hook):
    # Determine salutation
    if 'Sheikh' in name_title:
        salutation = f"Your Highness / Respected Leadership at {entity}"
    elif name_title and len(name_title.split()) > 0:
        first_part = name_title.split('(')[0].split('&')[0].strip()
        salutation = f"Dear {first_part} and Investment Leadership at {entity}"
    else:
        salutation = f"Dear Investment Team at {entity}"
        
    hook_clean = hook.strip().rstrip('.')
    
    body = f"""{salutation},

Following {entity}'s strategic focus on {hook_clean.lower()}:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary edge and enterprise hardware into a Sovereign AI Inference & Compute Grid - executing 70B and 405B LLM workloads at ~70% lower cost than centralized hyperscale clouds with zero offshore data egress.

Key Highlights:
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Scale: 78%+ software gross margins monetizing idle enterprise fleets and 100M telecom set-top boxes (150 PFLOPs capacity).
• Technical Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), sub-0.1ms zk-SNARK cryptographic verification, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising $20.0M USD (~AED 73.5M / ₹168 Crore) Seed round for 20% equity ($80M Pre / $100M Post-Money Valuation).

I have attached our Seed Investment Presentation (PDF). I would welcome a 10-minute briefing with your investment team this week to share our architectural blueprint and discuss sovereign compute grid deployment across the Gulf region.

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
    # Scrub em dashes
    body = body.replace('—', '-').replace('–', '-')
    return body

def main():
    print(f"Reading Gulf Investors CSV: {CSV_FILE}")
    recipients = []
    
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entity = row.get('Entity / Organization Name', '').strip()
            name_title = row.get('Key Decision Maker & Executive Title', '').strip()
            email = row.get('Verified Contact Email / Direct Application Portal', '').strip()
            hook = row.get('Custom Strategic Pitch Hook for FlockML', '').strip()
            
            if email and '@' in email:
                recipients.append({
                    'entity': entity,
                    'name_title': name_title,
                    'email': email,
                    'hook': hook
                })
                
    print(f"Total valid Gulf investor targets: {len(recipients)}")
    
    # Read PDF attachment
    if not os.path.exists(PDF_PATH):
        print(f"ERROR: PDF not found at {PDF_PATH}")
        return
        
    with open(PDF_PATH, 'rb') as f:
        pdf_data = f.read()
    print(f"Loaded PDF attachment ({len(pdf_data)} bytes).")

    # Connect to SMTP
    print("Connecting to Gmail SMTP server...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    print("SMTP authentication successful!\n")

    successful_sends = 0
    failed_sends = 0

    for idx, r in enumerate(recipients, 1):
        subject = f"FlockML: Sovereign Decentralized AI Compute Grid ($20M Seed Allocation) - {r['entity']}"
        subject = subject.replace('—', '-').replace('–', '-')
        body = generate_gulf_body(r['entity'], r['name_title'], r['hook'])
        
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = f"Supratim Dhara <{GMAIL_USER}>"
        msg['To'] = r['email']
        msg.set_content(body)
        
        msg.add_attachment(
            pdf_data, 
            maintype='application', 
            subtype='pdf', 
            filename='FlockML - Seed Investment Presentation.pdf'
        )

        try:
            server.send_message(msg)
            successful_sends += 1
            print(f"[{idx}/{len(recipients)}] SUCCESS -> Sent to {r['entity']} ({r['email']})")
        except Exception as e:
            failed_sends += 1
            print(f"[{idx}/{len(recipients)}] FAILED -> {r['entity']} ({r['email']}): {e}")
            
        # Pacing delay between emails
        if idx < len(recipients):
            time.sleep(4)

    server.quit()
    print(f"\n==========================================")
    print(f"DISPATCH COMPLETE: {successful_sends} sent successfully, {failed_sends} failed.")
    print(f"==========================================")

if __name__ == '__main__':
    main()
