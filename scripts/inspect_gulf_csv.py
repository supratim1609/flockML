import csv
import os

CSV_FILE = '/Users/supratim/Desktop/flockml-sovereign/docs/Archive/FlockML_50_Dubai_UAE_and_Gulf_Sovereign_Investors - Sheet1.csv'
PDF_PATH = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML — Seed Investment Presentation.pdf'

valid_recipients = []

with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        entity = row.get('Entity / Organization Name', '').strip()
        name_title = row.get('Key Decision Maker & Executive Title', '').strip()
        email = row.get('Verified Contact Email / Direct Application Portal', '').strip()
        hook = row.get('Custom Strategic Pitch Hook for FlockML', '').strip()
        check_size = row.get('Typical Check Size & Capacity', '').strip()
        city = row.get('Region / City', '').strip()
        
        if email and '@' in email:
            valid_recipients.append({
                'entity': entity,
                'name_title': name_title,
                'email': email,
                'hook': hook,
                'check_size': check_size,
                'city': city
            })

print(f"Total valid email recipients found in Gulf database: {len(valid_recipients)}")
for i, r in enumerate(valid_recipients[:5], 1):
    print(f"{i}. {r['entity']} ({r['name_title']}) -> {r['email']}")
