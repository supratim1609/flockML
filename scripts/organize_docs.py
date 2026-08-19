import os
import shutil

DOCS_DIR = '/Users/supratim/Desktop/flockml-sovereign/docs'

# Destination Folders
FOLDERS = {
    '01_Pitch_Decks': os.path.join(DOCS_DIR, '01_Pitch_Decks'),
    '02_CESC_RPSG_Enterprise': os.path.join(DOCS_DIR, '02_CESC_RPSG_Enterprise'),
    '03_MeitY_Sovereign_Pilot': os.path.join(DOCS_DIR, '03_MeitY_Sovereign_Pilot'),
    '04_Architecture_and_Whitepaper': os.path.join(DOCS_DIR, '04_Architecture_and_Whitepaper'),
    '05_Investor_Lists': os.path.join(DOCS_DIR, '05_Investor_Lists'),
    '06_Preparation_Playbooks': os.path.join(DOCS_DIR, '06_Preparation_Playbooks'),
    'Archive': os.path.join(DOCS_DIR, 'Archive')
}

for folder in FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

# 1. Pitch Decks
pitch_files = [
    'investment_pitch.html',
    'investment_pitch.pdf',
    'FlockML_Seed_Investment_Pitch_Deck.html',
    'FlockML_Seed_Investment_Pitch_Deck.pdf',
    'FlockML — Seed Investment Presentation.pdf',
    'FlockML - Seed Investment Pitch Deck ($20M Raise).pdf'
]
for f in pitch_files:
    src = os.path.join(DOCS_DIR, f)
    if os.path.exists(src):
        dst = os.path.join(FOLDERS['01_Pitch_Decks'], f)
        shutil.copy2(src, dst)
        print(f"Copied to 01_Pitch_Decks: {f}")

# 2. CESC / RPSG Enterprise
cesc_files = [
    'CESC_RPSG_Executive_Pitch_Deck.html',
    'CESC_RPSG_Executive_Pitch_Deck.pdf',
    'CESC_Executive_Briefing_and_Pilot_Proposal.html',
    'CESC_Executive_Briefing_and_Pilot_Proposal.pdf',
    'CESC_RPSG_Master_Strategic_Plan.html',
    'CESC_RPSG_National_IndiaAI_Platform.html',
    'CESC_RPSG_Pilot_Protocol.html',
    'CESC_RPSG_Pilot_Requirements.html',
    'CESC_RPSG_Deliverables_and_Architecture.html'
]
for f in cesc_files:
    src = os.path.join(DOCS_DIR, f)
    if os.path.exists(src):
        dst = os.path.join(FOLDERS['02_CESC_RPSG_Enterprise'], f)
        shutil.copy2(src, dst)
        print(f"Copied to 02_CESC_RPSG_Enterprise: {f}")

# Copy CESC Playbook from Preparation_Playbooks
cesc_playbook_src = os.path.join(DOCS_DIR, 'Preparation_Playbooks', 'CESC_RPSG_Executive_Meeting_Playbook.html')
if os.path.exists(cesc_playbook_src):
    shutil.copy2(cesc_playbook_src, os.path.join(FOLDERS['02_CESC_RPSG_Enterprise'], 'CESC_RPSG_Executive_Meeting_Playbook.html'))

# 3. MeitY Sovereign Pilot
meity_files = [
    'MeitY_14_Day_Pilot_Approval_Memorandum.html',
    'MeitY Empirical Field Test & Benchmark Validation Report.pdf',
    'MeitY Sovereign AI Pilot Proposal & Detailed SOP.pdf',
    'MeitY Technical Architecture & Detailed Component Specification.pdf'
]
for f in meity_files:
    src = os.path.join(DOCS_DIR, f)
    if os.path.exists(src):
        dst = os.path.join(FOLDERS['03_MeitY_Sovereign_Pilot'], f)
        shutil.copy2(src, dst)
        print(f"Copied to 03_MeitY_Sovereign_Pilot: {f}")

# 4. Architecture and Whitepaper
arch_files = [
    'FlockML_Whitepaper.html',
    'FlockML_Whitepaper.pdf',
    'FlockML_System_Architecture.html',
    'FlockML_Decentralized_Inference_MVP_Master_Plan.html',
    'FlockML_Strategic_Opportunity_and_Inference_Analysis.html',
    'FlockML - Strategic Opportunity & Dual-Track Roadmap Analysis.pdf'
]
for f in arch_files:
    src = os.path.join(DOCS_DIR, f)
    if os.path.exists(src):
        dst = os.path.join(FOLDERS['04_Architecture_and_Whitepaper'], f)
        shutil.copy2(src, dst)
        print(f"Copied to 04_Architecture_and_Whitepaper: {f}")

# 5. Investor Lists
csv_files = [
    'FlockML_100_High_Response_Unexplored_Global_Investors - Sheet1.csv',
    'FlockML_100_Fresh_Investors_Excluding_Prior_Rejections - Sheet1.csv'
]
for f in csv_files:
    src = os.path.join(DOCS_DIR, f)
    if os.path.exists(src):
        dst = os.path.join(FOLDERS['05_Investor_Lists'], f)
        shutil.copy2(src, dst)
        print(f"Copied to 05_Investor_Lists: {f}")

# 6. Preparation Playbooks
playbook_src_dir = os.path.join(DOCS_DIR, 'Preparation_Playbooks')
if os.path.exists(playbook_src_dir):
    for f in os.listdir(playbook_src_dir):
        src = os.path.join(playbook_src_dir, f)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(FOLDERS['06_Preparation_Playbooks'], f))
            print(f"Copied to 06_Preparation_Playbooks: {f}")

# 7. Move legacy redundant duplicate Anicut deck to Archive
legacy_anicut = os.path.join(DOCS_DIR, 'Anicut_Capital_Pitch_Deck.html')
if os.path.exists(legacy_anicut):
    shutil.move(legacy_anicut, os.path.join(FOLDERS['Archive'], 'Anicut_Capital_Pitch_Deck.html'))
    print("Archived legacy Anicut_Capital_Pitch_Deck.html")

print("\n✓ Directory cleanup complete! Created clean organized subfolders.")
