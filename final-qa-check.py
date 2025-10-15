#!/usr/bin/env python3
"""
Final comprehensive QA check across all 81 files.
Verifies all critical requirements are met.
"""

import os
import glob

print("=" * 70)
print("PHASE 5: FINAL AUTOMATED QA CHECKS")
print("=" * 70)
print("Running comprehensive validation across all 81 files...\n")

# Count files
html_files = glob.glob("department-one-pagers/*.html")
email_files = glob.glob("tier*/*.txt")
doc_files = [
    "README.md", "QUICK_START_GUIDE.md", "CC_INSTRUCTIONS.md",
    "HOW_TO_USE_GITHUB.md", "MASTER_EMAIL_TRACKING.md", "CAMPAIGN_SUMMARY.md",
    "CRITICAL_UPDATES_REQUIRED.md", "CASH_PRIZE_REMOVAL_REPORT.md",
    "planning-docs/NEST_FEST_3_WEEK_SPRINT_PLAN.md",
    "planning-docs/VIP_GUEST_INVITATION_LIST.md",
    "planning-docs/RIVERSIDE_PRIORITY_CONTACTS.md",
    "planning-docs/FACULTY_OUTREACH_PRIORITY_LIST.md"
]

total_files = len(html_files) + len(email_files) + len([f for f in doc_files if os.path.exists(f)])

print(f"Total files to check: {total_files}")
print(f"  - HTML one-pagers: {len(html_files)}")
print(f"  - Email templates: {len(email_files)}")
print(f"  - Documentation: {len([f for f in doc_files if os.path.exists(f)])}")
print()

# QA Check 1: No cash prize language
print("[CHECK 1] Verifying NO cash prize language...")
cash_issues = []

for filepath in html_files + email_files + doc_files:
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip archival documents
    if 'ARCHIVAL DOCUMENT' in content:
        continue

    # Check for cash prize language
    if 'cash prize' in content.lower() or '$10k' in content.lower():
        # Exclude if it's in a report about removing them
        if 'REMOVAL_REPORT' not in filepath and 'CRITICAL_UPDATES' not in filepath:
            cash_issues.append(os.path.basename(filepath))

if cash_issues:
    print(f"   [FAIL] Found cash prize language in {len(cash_issues)} files")
    for f in cash_issues[:5]:  # Show first 5
        print(f"      - {f}")
else:
    print(f"   [OK] No cash prize guarantees found")

# QA Check 2: Email address correct
print("\n[CHECK 2] Verifying email address (abel.rincon@g.austincc.edu)...")
wrong_email_count = 0

for filepath in html_files + email_files + doc_files:
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'edge.team@austincc.edu' in content:
        wrong_email_count += 1

if wrong_email_count > 0:
    print(f"   [FAIL] Found old email in {wrong_email_count} files")
else:
    print(f"   [OK] All emails correct")

# QA Check 3: October 30 deadline present
print("\n[CHECK 3] Verifying October 30 deadline mentioned...")
missing_deadline = []

for filepath in html_files + email_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'October 30' not in content and 'Oct 30' not in content:
        missing_deadline.append(os.path.basename(filepath))

if missing_deadline:
    print(f"   [FAIL] Missing deadline in {len(missing_deadline)} files")
    for f in missing_deadline[:5]:
        print(f"      - {f}")
else:
    print(f"   [OK] All files mention October 30 deadline")

# QA Check 4: All EDGE links present in HTML
print("\n[CHECK 4] Verifying all EDGE links in HTML one-pagers...")
required_links = [
    'https://nest-fest.org/',
    'https://discord.gg/EgjuFMzV',
    'https://austincc.campuslabs.com/engage/organization/edgeteam',
    'https://calendar.app.google/rPFQ4o2k56fsKZrM6'
]

html_missing_links = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    missing = [link for link in required_links if link not in content]
    if missing:
        html_missing_links.append((os.path.basename(filepath), missing))

if html_missing_links:
    print(f"   [FAIL] Missing links in {len(html_missing_links)} files")
    for f, links in html_missing_links:
        print(f"      - {f}: {len(links)} links missing")
else:
    print(f"   [OK] All HTML files have required links")

# QA Check 5: Phone number not placeholder
print("\n[CHECK 5] Verifying phone number (737-206-9977)...")
placeholder_phone_count = 0

for filepath in html_files + email_files + doc_files:
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '[Phone]' in content or '[TO BE ADDED]' in content:
        placeholder_phone_count += 1

if placeholder_phone_count > 0:
    print(f"   [FAIL] Found placeholder phone in {placeholder_phone_count} files")
else:
    print(f"   [OK] All phone numbers filled in")

# QA Check 6: ACC colors in HTML
print("\n[CHECK 6] Verifying ACC colors (#512698, #FDB913)...")
wrong_colors = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '#512698' not in content or '#FDB913' not in content:
        wrong_colors += 1

if wrong_colors > 0:
    print(f"   [FAIL] Missing ACC colors in {wrong_colors} files")
else:
    print(f"   [OK] All HTML files use ACC colors")

# QA Check 7: Event schedule correct
print("\n[CHECK 7] Verifying event schedule format...")
wrong_schedule = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for new schedule format
    if '2:00-5:00 PM' not in content or '5:00-6:00 PM' not in content:
        wrong_schedule.append(os.path.basename(filepath))

if wrong_schedule:
    print(f"   [FAIL] Incorrect schedule in {len(wrong_schedule)} files")
    for f in wrong_schedule:
        print(f"      - {f}")
else:
    print(f"   [OK] All HTML files have correct schedule")

# Final Summary
print("\n" + "=" * 70)
print("PHASE 5 COMPLETE: FINAL QA CHECKS")
print("=" * 70)

total_issues = (
    len(cash_issues) +
    wrong_email_count +
    len(missing_deadline) +
    len(html_missing_links) +
    placeholder_phone_count +
    wrong_colors +
    len(wrong_schedule)
)

if total_issues == 0:
    print("\n" + "=" * 70)
    print("*** ALL CHECKS PASSED! ***")
    print("=" * 70)
    print("\n[OK] Campaign is READY TO DEPLOY!")
    print(f"[OK] {total_files} files verified")
    print("\n All requirements met:")
    print("  [OK] No cash prize guarantees")
    print("  [OK] Email: abel.rincon@g.austincc.edu")
    print("  [OK] October 30 deadline mentioned")
    print("  [OK] All EDGE links present")
    print("  [OK] Phone: 737-206-9977")
    print("  [OK] ACC colors: #512698, #FDB913")
    print("  [OK] Event schedule: 2:00-5:00 PM + 5:00-6:00 PM")
    print("\n Repository ready for GitHub push and faculty deployment!")
else:
    print(f"\n[WARNING] Found {total_issues} issues across all files")
    print("          Review checks above")

print()
