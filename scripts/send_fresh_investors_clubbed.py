import csv
import time
import os
import smtplib
from email.message import EmailMessage
from collections import defaultdict

CSV_FILE = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML_100_Fresh_Investors_Excluding_Prior_Rejections - Sheet1.csv'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

def generate_clubbed_body(firm, members):
    # Format names: "Nivas, Byron, Sameer, Mary, and Anant"
    first_names = [m['name'].split()[0] for m in members if m['name']]
    if len(first_names) == 1:
        salutation = f"Hi {first_names[0]}"
    elif len(first_names) == 2:
        salutation = f"Hi {first_names[0]} and {first_names[1]}"
    elif len(first_names) > 2:
        salutation = f"Hi {', '.join(first_names[:-1])}, and {first_names[-1]}"
    else:
        salutation = f"Hi {firm} Investment Team"
        
    # Get primary strategic hook
    hooks = [m['hook'].strip().rstrip('.') for m in members if m['hook']]
    primary_hook = hooks[0] if hooks else "AI infrastructure and decentralized compute"

    body = f"""{salutation},

Following {firm}'s focus on {primary_hook.lower()}:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary edge and enterprise hardware into a Sovereign AI Inference & Compute Grid - executing 70B and 405B LLM workloads at ~70% lower cost than centralized hyperscale clouds with zero offshore data egress.

Key Highlights:
• Commercial Wedge (Sovereign Inference): 1-line OpenAI drop-in API (`baseURL: api.flockml.com/v1`) providing 70% cheaper token pricing on Llama-3 70B & DeepSeek-R1 with 78%+ software gross margins.
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Compute Supply: Monetizing idle corporate fleets (7 PM - 7 AM) and 100M telecom set-top boxes (150 PFLOPs capacity) with zero datacenter leases.
• Deep Tech Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), sub-0.1ms zk-SNARK cryptographic verification, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising $20.0M USD Seed round for 20% equity ($80M Pre / $100M Post-Money Valuation).

I have attached our Seed Investment Presentation (PDF). I would welcome 10 minutes with the {firm} team this week to share our technical blueprint and benchmarks.

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
    # Scrub em dashes
    body = body.replace('—', '-').replace('–', '-')
    return body

def main():
    print(f"Reading CSV: {CSV_FILE}")
    firms = defaultdict(list)

    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            firm = row.get('Firm / Fund / Company Name', '').strip()
            name = row.get('Investor Name', '').strip()
            title = row.get('Executive Title / Role', '').strip()
            email = row.get('Direct Corporate Email / Contact', '').strip()
            hook = row.get('Custom Strategic Pitch Hook for FlockML', '').strip()
            
            if email and '@' in email and firm:
                firms[firm].append({
                    'name': name,
                    'title': title,
                    'email': email,
                    'hook': hook
                })

    print(f"Total unique firms to contact: {len(firms)}")
    total_contacts = sum(len(m) for m in firms.values())
    print(f"Total individual partners covered: {total_contacts}\n")

    # Read PDF
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

    for idx, (firm, members) in enumerate(firms.items(), 1):
        to_emails = list(set([m['email'] for m in members]))
        names = ", ".join([m['name'] for m in members])
        
        subject = f"FlockML: Sovereign Decentralized AI Compute Grid ($20M Seed Allocation) - {firm}"
        subject = subject.replace('—', '-').replace('–', '-')
        
        body = generate_clubbed_body(firm, members)
        
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = f"Supratim Dhara <{GMAIL_USER}>"
        msg['To'] = ", ".join(to_emails)
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
            print(f"[{idx}/{len(firms)}] SUCCESS -> Sent to {firm} ({len(to_emails)} partners: {', '.join(to_emails)})")
        except Exception as e:
            failed_sends += 1
            print(f"[{idx}/{len(firms)}] FAILED -> {firm}: {e}")
            
        # Pacing delay between firms
        if idx < len(firms):
            time.sleep(5)

    server.quit()
    print(f"\n==========================================")
    print(f"DISPATCH COMPLETE: {successful_sends} firms sent successfully, {failed_sends} failed.")
    print(f"Covered {total_contacts} total investors.")
    print(f"==========================================")

if __name__ == '__main__':
    main()
