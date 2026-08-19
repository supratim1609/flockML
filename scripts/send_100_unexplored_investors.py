import os
import sys
import time
import csv
import json
import smtplib
from email.message import EmailMessage
from collections import defaultdict

CSV_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML_100_High_Response_Unexplored_Global_Investors - Sheet1.csv'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'
LOG_PATH = '/Users/supratim/Desktop/flockml-sovereign/scripts/sent_100_investors_log.json'

GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

GENERIC_CATEGORIES = {'Open-Source Angel', 'Micro Angel', 'Indie Hacker', 'Angel', 'Angel Investor'}

def load_sent_log():
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_sent_log(sent_dict):
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(sent_dict, f, indent=2)

def generate_email_content(target):
    name = target['name']
    firm = target['firm']
    hook = target['hook'].strip().rstrip('.')
    
    first_name = name.split()[0] if name else "there"
    is_angel = firm in GENERIC_CATEGORIES
    
    if is_angel:
        intro_hook = f"Following your work and contributions in {hook.lower()}"
        salutation = f"Hi {first_name}"
    else:
        intro_hook = f"Following {firm}'s focus on {hook.lower()}"
        salutation = f"Hi {first_name}"

    body = f"""{salutation},

{intro_hook}:

I am Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We have engineered a zero-install WebGPU and WebAssembly execution engine that turns ordinary consumer & enterprise devices into a Decentralized AI Inference Cloud - executing 70B & 405B LLM workloads at ~70% lower cost than AWS/Azure with zero data egress.

Key Highlights:
• Commercial Wedge: 1-line OpenAI/OpenRouter drop-in API (`baseURL: api.flockml.com/v1`) delivering 70% cheaper token pricing on Llama-3.2, Gemma-2B & DeepSeek-R1 with 78%+ software gross margins.
• Sovereign Pilot Validation: Under 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across national headquarters.
• Zero-CapEx Compute Supply: Monetizing idle enterprise hardware and domestic silicon with zero datacenter leases or server CapEx.
• Deep Tech Moats: BitNet 1.58-bit ternary quantization (80.2% VRAM reduction), dynamic layer sharding across local networks, and sub-5ms self-healing failover.
• Seed Round Allocation: Raising our $20.0M Seed round ($80M Pre / $100M Post) to scale developer onboarding and enterprise pilots.

I have attached our Seed Investment Presentation (PDF). I would welcome 10 minutes with you this week to share our live benchmarks and technical blueprint.

Live Overview: https://supratimdev.qzz.io/flock-ml

Best regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
    # Scrub em dashes
    body = body.replace('—', '-').replace('–', '-')
    return body

def main():
    if not os.path.exists(PDF_PATH):
        print(f"Error: PDF not found at {PDF_PATH}")
        return

    with open(PDF_PATH, 'rb') as f:
        pdf_data = f.read()

    print(f"Loaded PDF: {len(pdf_data)} bytes")

    # Read CSV
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    targets = []
    for r in rows:
        email = r.get('Direct Email / Open Pitch Portal', '').strip()
        firm = r.get('Firm / Platform / Company Name', '').strip()
        name = r.get('Investor Name', '').strip()
        hook = r.get('Custom Cold Pitch Hook for FlockML', '').strip()
        if '@' in email and not email.startswith('http'):
            targets.append({
                'name': name,
                'email': email,
                'firm': firm,
                'hook': hook
            })

    print(f"Total valid investor targets to dispatch: {len(targets)}")
    sent_log = load_sent_log()
    print(f"Already sent previously: {len(sent_log)}")

    pending = [t for t in targets if t['email'] not in sent_log]
    print(f"Pending to send in this run: {len(pending)}\n")

    if not pending:
        print("All targets have already been sent!")
        return

    for idx, target in enumerate(pending, 1):
        email = target['email']
        name = target['name']
        firm = target['firm']

        print(f"[{idx}/{len(pending)}] Connecting to SMTP to send to {name} at {firm} ({email})...")
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=25)
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

            msg = EmailMessage()
            msg['Subject'] = "FlockML: Decentralized AI Inference Cloud (70% Cheaper than AWS)"
            msg['From'] = f"Supratim Dhara | FlockML <{GMAIL_USER}>"
            msg['To'] = email

            body = generate_email_content(target)
            msg.set_content(body)

            msg.add_attachment(
                pdf_data,
                maintype='application',
                subtype='pdf',
                filename='FlockML - Seed Investment Presentation.pdf'
            )

            server.send_message(msg)
            server.quit()

            sent_log[email] = {
                'name': name,
                'firm': firm,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            save_sent_log(sent_log)

            print(f"  ✓ Successfully sent to {email}")

            if idx < len(pending):
                print(f"  ⏳ Waiting 2 minutes (120s) before next dispatch...\n")
                time.sleep(120)

        except Exception as e:
            print(f"  ✗ Error sending to {email}: {e}")
            time.sleep(10)

    print("\n==================================================")
    print(f"  Completed dispatching all {len(pending)} investors!")
    print("==================================================")

if __name__ == '__main__':
    main()
