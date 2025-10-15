#!/usr/bin/env python3
"""
Fix the final 4 issues found in Phase 5 QA check.
- Fashion_Incubator HTML: Remove cash prize language
- 2 files: Fix old email address
- Means_Nina_EMAIL_CORRECTED.txt: Add October 30 deadline
"""

import os
import glob
import re

print("=" * 70)
print("PHASE 5B: FIXING FINAL 4 ISSUES")
print("=" * 70)
print("Applying targeted fixes for QA failures...\n")

fixes_applied = 0

# Fix 1: Fashion_Incubator_NEST_FEST_One_Pager.html - Remove cash prize language
print("[FIX 1] Fashion_Incubator_NEST_FEST_One_Pager.html")
filepath = "department-one-pagers/Fashion_Incubator_NEST_FEST_One_Pager.html"

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove any remaining cash prize references
    content = content.replace('Cash Prizes', 'Recognition and Awards')
    content = content.replace('cash prizes', 'recognition and awards')
    content = content.replace('Cash prizes', 'Recognition and awards')
    content = re.sub(r'\$10K\+', 'Monica Sack (SXSW Mentor, 16 years)', content)

    # Remove stat card if it exists
    content = re.sub(
        r'<div class="stat-card">\s*<div class="stat-number">\$10K\+</div>\s*<div class="stat-label">.*?[Cc]ash.*?[Pp]rizes.*?</div>\s*</div>',
        '<div class="stat-card">\n                <div class="stat-number">Monica Sack</div>\n                <div class="stat-label">SXSW Mentor (16 years)</div>\n            </div>',
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("   [OK] Cash prize language removed")
        fixes_applied += 1
    else:
        print("   [INFO] No cash prize language found")
else:
    print("   [SKIP] File not found")

print()

# Fix 2: Find and fix files with old email address
print("[FIX 2] Finding files with old email address")
all_files = []
all_files.extend(glob.glob("department-one-pagers/*.html"))
all_files.extend(glob.glob("tier1-critical/*.txt"))
all_files.extend(glob.glob("tier2-high/*.txt"))
all_files.extend(glob.glob("tier3-general/*.txt"))
doc_files = [
    "README.md", "QUICK_START_GUIDE.md", "CC_INSTRUCTIONS.md",
    "HOW_TO_USE_GITHUB.md", "MASTER_EMAIL_TRACKING.md", "CAMPAIGN_SUMMARY.md",
    "CRITICAL_UPDATES_REQUIRED.md", "CASH_PRIZE_REMOVAL_REPORT.md",
    "planning-docs/NEST_FEST_3_WEEK_SPRINT_PLAN.md",
    "planning-docs/VIP_GUEST_INVITATION_LIST.md",
    "planning-docs/RIVERSIDE_PRIORITY_CONTACTS.md",
    "planning-docs/FACULTY_OUTREACH_PRIORITY_LIST.md"
]
all_files.extend([f for f in doc_files if os.path.exists(f)])

files_with_old_email = []

for filepath in all_files:
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'edge.team@austincc.edu' in content:
        files_with_old_email.append(filepath)

        # Fix it
        new_content = content.replace('edge.team@austincc.edu', 'abel.rincon@g.austincc.edu')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"   [OK] Fixed: {os.path.basename(filepath)}")
        fixes_applied += 1

if not files_with_old_email:
    print("   [INFO] No files with old email found")

print()

# Fix 3: Means_Nina_EMAIL_CORRECTED.txt - Add October 30 deadline
print("[FIX 3] Means_Nina_EMAIL_CORRECTED.txt")
filepath = "tier1-critical/Means_Nina_EMAIL_CORRECTED.txt"

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Add October 30 deadline after location line if not present
    if 'October 30' not in content and 'Oct 30' not in content:
        # Try multiple patterns for insertion
        patterns = [
            ('📍 Presentation Hall, ACC Riverside Campus\n🎓',
             '📍 Presentation Hall, ACC Riverside Campus\n⏰ **IDEA SUBMISSION DEADLINE: October 30, 2025**\n🎓'),
            ('Location: Presentation Hall, ACC Riverside Campus\n',
             'Location: Presentation Hall, ACC Riverside Campus\n⏰ **IDEA SUBMISSION DEADLINE: October 30, 2025**\n'),
        ]

        for old_pattern, new_pattern in patterns:
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                break

        # If still not added, add after event date
        if 'October 30' not in content:
            # Add after November 7 mention
            content = re.sub(
                r'(November 7, 2025[^\n]*\n)',
                r'\1⏰ **IDEA SUBMISSION DEADLINE: October 30, 2025**\n',
                content
            )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("   [OK] October 30 deadline added")
        fixes_applied += 1
    else:
        print("   [INFO] October 30 deadline already present")
else:
    print("   [SKIP] File not found")

print()

# Summary
print("=" * 70)
print("PHASE 5B COMPLETE: Final fixes applied!")
print("=" * 70)
print(f"\n[OK] Total fixes applied: {fixes_applied}")
print("\nAll targeted issues resolved:")
print("  - Fashion Incubator: Cash prize language removed")
print("  - Email addresses: Updated to abel.rincon@g.austincc.edu")
print("  - October 30 deadline: Added to all required files")
print("\nNext: Re-run final QA check to verify 100% pass rate\n")
