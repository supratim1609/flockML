import fitz # PyMuPDF
import os
import shutil

PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'
HTML_SOURCE = '/Users/supratim/Desktop/flockml-sovereign/docs/Anicut_Capital_Pitch_Deck.html'
DOCS_DIR = '/Users/supratim/Desktop/flockml-sovereign/docs'

def update_html_decks():
    with open(HTML_SOURCE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic clean title and subtitle
    content = content.replace('FlockML - Decentralized Compute Cloud', 'FlockML - Seed Investment Pitch Deck ($20M Raise)')
    content = content.replace('ANICUT CAPITAL', 'SEED INVESTMENT PITCH')
    content = content.replace('Anicut Capital', 'Seed Investment Partners')
    
    targets = [
        os.path.join(DOCS_DIR, 'investment_pitch.html'),
        os.path.join(DOCS_DIR, 'Investment_Pitch.html'),
        os.path.join(DOCS_DIR, 'FlockML_Seed_Investment_Pitch_Deck.html')
    ]

    for target in targets:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created: {target}")

def update_pdf_slide_16():
    doc = fitz.open(PDF_PATH)
    page16 = doc[15] # 0-indexed page 16
    
    # Let's inspect page dimensions
    rect = page16.rect
    print(f"Page 16 dimensions: {rect.width} x {rect.height}")
    
    # In page 16, let's redact the specific lines and replace them with $20M figures
    # Let's find text instances to replace
    # 1. Heading
    instances_h = page16.search_for("Seed Financing Terms:")
    for inst in instances_h:
        # Cover the whole heading line
        r = fitz.Rect(inst.x0, inst.y0 - 2, rect.width - 50, inst.y1 + 4)
        page16.draw_rect(r, color=(1, 1, 1), fill=(1, 1, 1)) # White background
        page16.insert_text(fitz.Point(inst.x0, inst.y1), "Seed Financing Terms: $20M Raise ( ₹ 169.0 Cr) at $80M Pre-Money.", fontsize=15, fontname="helv", fontfile=None, color=(0, 0, 0))

    # 2. Table rows
    table_replacements = [
        ("Capital raise", "Capital raise", "$20.0M", "₹ 169.0 Cr"),
        ("Pre-m oney valuation", "Pre-money valuation", "$80.0M", "₹ 676.0 Cr"),
        ("Post-m oney valuation", "Post-money valuation", "$100.0M", "₹ 845.0 Cr"),
        ("Investor equity", "Investor equity", "20.0%", "20.0%"),
        ("Founder retained", "Founder retained", "80.0%", "80.0%"),
    ]

    # Let's search for table area
    t_start = page16.search_for("TERM")
    t_end = page16.search_for("Valuation basis:")
    if not t_end:
        t_end = page16.search_for("V aluation basis:")

    if t_start and t_end:
        table_rect = fitz.Rect(t_start[0].x0 - 5, t_start[0].y0 + 12, rect.width - 50, t_end[0].y0 - 4)
        page16.draw_rect(table_rect, color=(1, 1, 1), fill=(1, 1, 1))
        
        # Redraw table rows cleanly
        y = t_start[0].y0 + 26
        rows = [
            ("Capital raise", "$20.0M", "₹ 169.0 Cr"),
            ("Pre-money valuation", "$80.0M", "₹ 676.0 Cr"),
            ("Post-money valuation", "$100.0M", "₹ 845.0 Cr"),
            ("Investor equity", "20.0%", "20.0%"),
            ("Founder retained", "80.0%", "80.0%")
        ]
        for term, usd, inr in rows:
            page16.insert_text(fitz.Point(t_start[0].x0, y), term, fontsize=10.5, fontname="helv", color=(0.2, 0.2, 0.2))
            page16.insert_text(fitz.Point(t_start[0].x0 + 200, y), usd, fontsize=10.5, fontname="helv", color=(0, 0, 0))
            page16.insert_text(fitz.Point(t_start[0].x0 + 340, y), inr, fontsize=10.5, fontname="helv", color=(0, 0, 0))
            y += 18

    # 3. Capital Deployment breakdown
    dep_hdr = page16.search_for("Capital Deployment")
    dep_foot = page16.search_for("16 / 18")
    
    if dep_hdr and dep_foot:
        dep_rect = fitz.Rect(dep_hdr[0].x0 - 5, dep_hdr[0].y0 - 2, rect.width - 50, dep_foot[0].y0 - 10)
        page16.draw_rect(dep_rect, color=(1, 1, 1), fill=(1, 1, 1))

        # Title
        page16.insert_text(fitz.Point(dep_hdr[0].x0, dep_hdr[0].y0 + 10), "Capital Deployment ($20M / ₹ 169.0 Cr Total)", fontsize=13, fontname="helv", color=(0, 0, 0))

        # Items
        y = dep_hdr[0].y0 + 28
        allocations = [
            ("Engineering & Shader R&D (40%)", "$8.0M · ₹ 67.6 Cr"),
            ("Network Liquidity & Incentives (25%)", "$5.0M · ₹ 42.3 Cr"),
            ("Enterprise Sales & Sovereign GTM (20%)", "$4.0M · ₹ 33.8 Cr"),
            ("Security Audits & ZK Proofs (10%)", "$2.0M · ₹ 16.9 Cr"),
            ("Operations, IP & Legal (5%)", "$1.0M · ₹ 8.5 Cr")
        ]
        for cat, val in allocations:
            page16.insert_text(fitz.Point(dep_hdr[0].x0, y), cat, fontsize=10, fontname="helv", color=(0.2, 0.2, 0.2))
            page16.insert_text(fitz.Point(dep_hdr[0].x0 + 260, y), val, fontsize=10, fontname="helv", color=(0, 0, 0))
            y += 16

    tmp_path = PDF_PATH + '.tmp.pdf'
    doc.save(tmp_path)
    doc.close()
    os.replace(tmp_path, PDF_PATH)
    print(f"✓ Successfully updated PDF: {PDF_PATH} with $20M round parameters!")

if __name__ == '__main__':
    update_html_decks()
    update_pdf_slide_16()
