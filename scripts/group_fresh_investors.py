import csv
from collections import defaultdict

CSV_FILE = '/Users/supratim/Desktop/flockml-sovereign/docs/FlockML_100_Fresh_Investors_Excluding_Prior_Rejections - Sheet1.csv'

firms = defaultdict(list)

with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        firm = row.get('Firm / Fund / Company Name', '').strip()
        name = row.get('Investor Name', '').strip()
        title = row.get('Executive Title / Role', '').strip()
        email = row.get('Direct Corporate Email / Contact', '').strip()
        location = row.get('Location / Office', '').strip()
        focus = row.get('Primary Investment Focus', '').strip()
        hook = row.get('Custom Strategic Pitch Hook for FlockML', '').strip()
        
        if email and '@' in email:
            firms[firm].append({
                'name': name,
                'title': title,
                'email': email,
                'location': location,
                'focus': focus,
                'hook': hook
            })

print(f"Total Unique Firms / Entities: {len(firms)}")
total_emails = sum(len(members) for members in firms.values())
print(f"Total Individual Contacts: {total_emails}\n")

for i, (firm, members) in enumerate(list(firms.items())[:8], 1):
    names = ", ".join(m['name'] for m in members)
    emails = ", ".join(m['email'] for m in members)
    print(f"{i}. {firm} ({len(members)} partners)")
    print(f"   Names: {names}")
    print(f"   Emails: {emails}\n")
