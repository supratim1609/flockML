import pymupdf
import os

PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

def clean_rebuild_page16():
    doc = pymupdf.open(PDF_PATH)
    page16 = doc[15]
    rect = page16.rect

    # 1. Apply true redaction to completely remove old underlying text across the whole page body
    content_rect = pymupdf.Rect(20, 20, rect.width - 20, rect.height - 45)
    page16.add_redact_annot(content_rect, fill=(1, 1, 1))
    page16.apply_redactions()

    # Now redraw page 16 with pristine typography and styling
    # Heading
    page16.insert_text(pymupdf.Point(54, 100), "Seed Financing Terms: $20M Raise (Rs 169.0 Cr) at $80M Pre-Money.", fontsize=17, fontname="helv", color=(0.05, 0.05, 0.05))

    # Table Headers
    page16.insert_text(pymupdf.Point(54, 140), "TERM", fontsize=10, fontname="helv", color=(0.4, 0.4, 0.4))
    page16.insert_text(pymupdf.Point(260, 140), "USD ($)", fontsize=10, fontname="helv", color=(0.4, 0.4, 0.4))
    page16.insert_text(pymupdf.Point(400, 140), "INR (Rs)", fontsize=10, fontname="helv", color=(0.4, 0.4, 0.4))

    # Divider line
    page16.draw_line(pymupdf.Point(54, 148), pymupdf.Point(540, 148), color=(0.85, 0.85, 0.85), width=0.8)

    # Table rows
    rows = [
        ("Capital raise", "$20.0M", "Rs 169.0 Cr"),
        ("Pre-money valuation", "$80.0M", "Rs 676.0 Cr"),
        ("Post-money valuation", "$100.0M", "Rs 845.0 Cr"),
        ("Investor equity", "20.0%", "20.0%"),
        ("Founder retained", "80.0%", "80.0%")
    ]

    y = 170
    for term, usd, inr in rows:
        page16.insert_text(pymupdf.Point(54, y), term, fontsize=11, fontname="helv", color=(0.2, 0.2, 0.2))
        page16.insert_text(pymupdf.Point(260, y), usd, fontsize=11, fontname="helv", color=(0.05, 0.05, 0.05))
        page16.insert_text(pymupdf.Point(400, y), inr, fontsize=11, fontname="helv", color=(0.05, 0.05, 0.05))
        y += 22

    # Valuation basis text
    page16.draw_line(pymupdf.Point(54, y - 4), pymupdf.Point(540, y - 4), color=(0.85, 0.85, 0.85), width=0.8)
    y += 14
    basis_txt = "Valuation basis: Institutional DeepTech infrastructure bet. Working WebGPU implementation,\nactive MeitY pilot engagement, and structural sovereign compute tailwinds."
    page16.insert_textbox(pymupdf.Rect(54, y, 780, y + 36), basis_txt, fontsize=9.5, fontname="helv", color=(0.35, 0.35, 0.35))

    # Capital Deployment Section
    y_dep = 330
    page16.insert_text(pymupdf.Point(54, y_dep), "Capital Deployment ($20M / Rs 169.0 Cr Total)", fontsize=14, fontname="helv", color=(0.05, 0.05, 0.05))
    page16.draw_line(pymupdf.Point(54, y_dep + 8), pymupdf.Point(540, y_dep + 8), color=(0.85, 0.85, 0.85), width=0.8)

    allocations = [
        ("Engineering & Shader R&D (40%)", "$8.0M · Rs 67.6 Cr"),
        ("Network Liquidity & Incentives (25%)", "$5.0M · Rs 42.3 Cr"),
        ("Enterprise Sales & Sovereign GTM (20%)", "$4.0M · Rs 33.8 Cr"),
        ("Security Audits & ZK Proofs (10%)", "$2.0M · Rs 16.9 Cr"),
        ("Operations, IP & Legal (5%)", "$1.0M · Rs 8.5 Cr")
    ]

    y_alloc = y_dep + 32
    for cat, val in allocations:
        page16.insert_text(pymupdf.Point(54, y_alloc), cat, fontsize=10.5, fontname="helv", color=(0.2, 0.2, 0.2))
        page16.insert_text(pymupdf.Point(340, y_alloc), val, fontsize=10.5, fontname="helv", color=(0.05, 0.05, 0.05))
        y_alloc += 20

    tmp_path = PDF_PATH + '.clean.pdf'
    doc.save(tmp_path)
    doc.close()
    os.replace(tmp_path, PDF_PATH)
    print("✓ Pristine $20M PDF created successfully!")

if __name__ == '__main__':
    clean_rebuild_page16()
