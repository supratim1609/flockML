import csv
import time
import os
import smtplib
from email.message import EmailMessage

LIVE_MODE = True

CSV_FILE = '/Users/supratim/Desktop/flockml-sovereign/docs/Archive/FlockML_60_Quiet_Big_Check_Investors - Sheet1.csv'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'

def generate_standard_body(name, hook):
    first_name = name.split()[0] if name else "there"
    
    body = f"""Hi {first_name},

Following your focus on {hook.lower().strip('.')}

I'm Supratim Dhara, Founder & Chief Systems Architect at FlockML.

We've engineered a zero-install WebGPU/WASM execution engine that turns ordinary desktop PCs into a Sovereign AI Supercomputer Grid — executing 7B, 70B, and 405B LLM inference and fine-tuning at 1/3rd AWS GPU cost with zero data leakage.

Key Highlights:
• Currently in 50-node sovereign pilot review with the Indian IT Ministry (MeitY) across NIC Delhi HQ & Kolkata.
• Sharding Meta Llama 3.1 405B, DeepSeek-R1, and Bhashini models over 128-layer WebRTC pipeline rings.
• Raising $30M Seed for 25% equity ($90M Pre-Money / $120M Post-Money Valuation).
• Built 1-line Developer SDK, BitNet 1.58-bit WGSL shaders, and sub-0.1ms Zero-Knowledge Proof (zk-SNARK) verification.

I've attached our Pitch Deck (PDF). Would love 5 minutes to share our technical blueprint with you.

Best regards,
Supratim Dhara | Founder & Chief Systems Architect, FlockML
supratimdhara0@gmail.com | https://supratimdev.qzz.io/flock-ml
"""
    return body

def send_email(to_email, subject, body, pdf_path, live=False, server=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = GMAIL_USER
    msg['To'] = to_email
    msg.set_content(body)

    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()
        msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='FlockML — Seed Investment Presentation.pdf')

    try:
        server.send_message(msg)
        print(f"SUCCESS: Sent to {to_email}")
    except Exception as e:
        print(f"FAILED: Could not send to {to_email} - {str(e)}")


def main():
    print(f"Starting execution for Quiet Big Check Investors. LIVE_MODE = {LIVE_MODE}")
    emails_to_send = []
    
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('Name', '').strip()
                email = row.get('Verified Contact Email / Direct Portal', '').strip()
                hook = row.get('Custom Strategic Pitch Hook for FlockML', '').strip()
                
                if email and '@' in email:
                    subject = "FlockML — Sovereign WebGPU AI Compute Grid ($30M Seed)"
                    body = generate_standard_body(name, hook)
                    emails_to_send.append({'to': email, 'subject': subject, 'body': body})
    else:
        print(f"Error: Could not find CSV at {CSV_FILE}")
        return

    # LIVE MODE
    print(f"WARNING: LIVE MODE ENGAGED. Sending {len(emails_to_send)} emails with 30s delays...")
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        
        for idx, em in enumerate(emails_to_send):
            send_email(em['to'], em['subject'], em['body'], PDF_PATH, live=True, server=server)
            if idx < len(emails_to_send) - 1:
                print("Waiting 30 seconds to avoid spam filters...")
                time.sleep(30)
                
        server.quit()
        print("All emails dispatched successfully.")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to connect or authenticate with SMTP - {str(e)}")

if __name__ == "__main__":
    main()
