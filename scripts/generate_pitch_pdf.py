import os
import subprocess
import pymupdf

DOCS_DIR = '/Users/supratim/Desktop/flockml-sovereign/docs'
CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

PRINT_CSS = """
    @media print {
      @page {
        size: 1120px 660px;
        margin: 0;
      }
      *, *::before, *::after {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
        color-adjust: exact !important;
      }
      html, body {
        width: 1120px !important;
        height: auto !important;
        min-height: 100% !important;
        overflow: visible !important;
        background: #000000 !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
      }
      .deck {
        position: static !important;
        width: 1120px !important;
        height: auto !important;
        display: block !important;
        transform: none !important;
        margin: 0 !important;
        padding: 0 !important;
      }
      .s {
        position: relative !important;
        top: auto !important;
        left: auto !important;
        width: 1120px !important;
        height: 660px !important;
        max-height: 660px !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        border-radius: 0 !important;
        opacity: 1 !important;
        visibility: visible !important;
        display: flex !important;
        flex-direction: column !important;
        page-break-before: always !important;
        break-before: page !important;
        page-break-after: always !important;
        break-after: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }
      .s:first-child {
        page-break-before: avoid !important;
        break-before: avoid !important;
      }
      .s:last-child {
        page-break-after: avoid !important;
        break-after: avoid !important;
      }
    }
"""

def add_print_css_to_html_files():
    html_files = [
        os.path.join(DOCS_DIR, 'investment_pitch.html'),
        os.path.join(DOCS_DIR, 'Investment_Pitch.html'),
        os.path.join(DOCS_DIR, 'FlockML_Seed_Investment_Pitch_Deck.html'),
        os.path.join(DOCS_DIR, 'Anicut_Capital_Pitch_Deck.html'),
    ]

    for fpath in html_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing @media print if any
        if '@media print' in content:
            # clean replace
            pass
        
        # Inject right before </style>
        if '</style>' in content and '@media print' not in content:
            content = content.replace('</style>', f"{PRINT_CSS}\n  </style>")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added @media print styles to: {fpath}")

def generate_pdf_via_chrome():
    input_html = os.path.join(DOCS_DIR, 'investment_pitch.html')
    output_pdf = os.path.join(DOCS_DIR, 'FlockML — Seed Investment Presentation.pdf')
    alt_output_pdf = os.path.join(DOCS_DIR, 'FlockML_Seed_Investment_Pitch_Deck.pdf')
    alt2_output_pdf = os.path.join(DOCS_DIR, 'investment_pitch.pdf')

    cmd = [
        CHROME_PATH,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=5000',
        f'--print-to-pdf={output_pdf}',
        f'file://{input_html}'
    ]

    print(f"Generating PDF with Chrome from {input_html}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running Chrome: {res.stderr}")
        return

    print(f"✓ Created PDF at: {output_pdf}")
    
    # Copy to companion names
    import shutil
    shutil.copy2(output_pdf, alt_output_pdf)
    shutil.copy2(output_pdf, alt2_output_pdf)
    print(f"✓ Copied to: {alt_output_pdf} and {alt2_output_pdf}")

    # Verify with PyMuPDF
    doc = pymupdf.open(output_pdf)
    print(f"✓ PDF verified: {len(doc)} pages, file size: {os.path.getsize(output_pdf)} bytes")
    for i, page in enumerate(doc):
        text = page.get_text().strip().split('\\n')
        title = text[0] if text else "Blank"
        print(f"  Page {i+1}: {title[:50]}")
    doc.close()

if __name__ == '__main__':
    add_print_css_to_html_files()
    generate_pdf_via_chrome()
