import os
import smtplib
from email.message import EmailMessage

GMAIL_USER = 'supratimdhara0@gmail.com'
GMAIL_APP_PASSWORD = 'lmxq aovn whdl ckof'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

def send_cesc_email():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

    to_email = 'subir.verma@rpsg.in'
    cc_email = 'darlene.graham@rpsg.in'

    subject = "Reconnecting: Edge Compute Infrastructure for CESC Grid Telemetry & Forecasting"

    body = """Dear Subir Sir,

I hope you are doing well.

It has been about a year and a half since we met at CESC House (when I was finishing my final year of B.Tech). Since then, I have graduated and focused entirely on engineering deep-tech infrastructure.

I have built FlockML-a decentralized edge execution engine designed to coordinate local computing hardware into an on-premises compute grid.

In the context of CESC and RPSG Group's scale, this architecture provides immediate operational value:

1. Zero-CapEx Load Forecasting & Telemetry: Aggregates compute power from existing substation PCs, office machines, and SCADA edge terminals to run high-frequency smart meter analytics, fault detection, and load prediction-slashing expensive cloud GPU leasing costs on AWS/Azure by ~70%.
2. 100% On-Premises Air-Gapped Security: All model activations and grid telemetry stay strictly within CESC's local network, fully compliant with CEA and CERT-In critical infrastructure security mandates.
3. Zero-Install Deployment: Executes within sandboxed WebGPU/WASM browser runtimes on hardware CESC already owns, requiring no intrusive server overhauls.

Since I am based here in Kolkata, I would appreciate 10 minutes at CESC House to demonstrate the live 3-node execution cluster on local hardware.

(CC'd Darlene to help coordinate a brief slot on your calendar whenever convenient).

Live Overview: https://supratimdev.qzz.io/flock-ml

Warm regards,

Supratim Dhara
Founder & Chief Systems Architect, FlockML
+91 8240356758 | supratimdhara0@gmail.com
Kolkata, India
"""
    # Strict scrub of em dashes
    body = body.replace('—', '-').replace('–', '-')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = f"Supratim Dhara | FlockML <{GMAIL_USER}>"
    msg['To'] = to_email
    msg['Cc'] = cc_email
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

    recipients = [to_email, cc_email]
    print(f"Sending email to {to_email} (CC: {cc_email})...")
    server.send_message(msg, to_addrs=recipients)
    print("✓ Successfully delivered to Subir Verma and Darlene Graham!")
    server.quit()

if __name__ == '__main__':
    send_cesc_email()
