import os
import shutil

DOCS_DIR = '/Users/supratim/Desktop/flockml-sovereign/docs'
ARCHIVE_DIR = os.path.join(DOCS_DIR, 'Archive')

# Files we keep in root as immediate shortcuts
KEEP_IN_ROOT = {
    'investment_pitch.html',
    'investment_pitch.pdf',
    'FlockML — Seed Investment Presentation.pdf',
    'CESC_RPSG_Executive_Pitch_Deck.html',
    'CESC_RPSG_Executive_Pitch_Deck.pdf',
    'CESC_Executive_Briefing_and_Pilot_Proposal.pdf'
}

for item in os.listdir(DOCS_DIR):
    item_path = os.path.join(DOCS_DIR, item)
    if os.path.isfile(item_path):
        if item not in KEEP_IN_ROOT:
            dst = os.path.join(ARCHIVE_DIR, item)
            # If exists in archive, overwrite
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(item_path, dst)
            print(f"Moved loose file to Archive: {item}")

print("✓ Root docs folder pristine clean!")
