#!/usr/bin/env python3
"""
Fix all documentation files based on QA agent findings.
"""

import os
import re

print("=" * 70)
print("PHASE 3: FIXING DOCUMENTATION FILES")
print("=" * 70)
print("Updating all documentation with correct information...\n")

# Documentation files to fix
docs_to_fix = [
    ("README.md", [
        "Add October 30 deadline",
        "Fix cash prize reference",
        "Update email address"
    ]),
    ("QUICK_START_GUIDE.md", [
        "Replace [Phone] placeholder",
        "Add October 30 deadline"
    ]),
    ("MASTER_EMAIL_TRACKING.md", [
        "Replace [Phone] placeholder",
        "Add October 30 deadline"
    ]),
    ("CAMPAIGN_SUMMARY.md", [
        "Remove cash prize references",
        "Add October 30 deadline"
    ]),
    ("planning-docs/NEST_FEST_3_WEEK_SPRINT_PLAN.md", [
        "Remove cash prize references",
        "Add date disclaimer"
    ]),
    ("planning-docs/VIP_GUEST_INVITATION_LIST.md", [
        "Add Dr. Kehoe email"
    ]),
    ("planning-docs/RIVERSIDE_PRIORITY_CONTACTS.md", [
        "Replace placeholder contact info"
    ]),
    ("planning-docs/FACULTY_OUTREACH_PRIORITY_LIST.md", [
        "Add Oct 30 to talking points"
    ]),
    ("CRITICAL_UPDATES_REQUIRED.md", [
        "Mark as ARCHIVAL"
    ]),
    ("CASH_PRIZE_REMOVAL_REPORT.md", [
        "Mark as ARCHIVAL"
    ])
]

files_updated = 0
total_changes = 0

for filename, planned_fixes in docs_to_fix:
    if not os.path.exists(filename):
        print(f"[SKIP] {filename} - file not found")
        continue

    print(f"[FILE] {filename}")

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    file_changes = 0

    # Global fixes for all docs
    # Fix 1: Email address
    if 'edge.team@austincc.edu' in content:
        content = content.replace('edge.team@austincc.edu', 'abel.rincon@g.austincc.edu')
        file_changes += 1
        print(f"   - Email address updated")

    # Fix 2: Phone placeholder
    if '[Phone]' in content or '[TO BE ADDED]' in content:
        content = content.replace('[Phone]', '737-206-9977')
        content = content.replace('[TO BE ADDED]', '737-206-9977')
        file_changes += 1
        print(f"   - Phone number added")

    # Fix 3: Cash prize language
    cash_replacements = 0
    if 'Cash Prizes' in content or 'cash prizes' in content or '$10K' in content:
        content = content.replace('Cash Prizes', 'Recognition and Awards')
        content = content.replace('cash prizes', 'recognition and awards')
        content = content.replace('$10K+', 'Monica Sack (SXSW Mentor, 16 years)')
        cash_replacements = original_content.count('Cash') + original_content.count('cash') - content.count('Cash') - content.count('cash')
        if cash_replacements > 0:
            file_changes += 1
            print(f"   - Cash prize language removed ({cash_replacements} instances)")

    # Fix 4: Dr. Andrea Kehoe email
    if '[Need to obtain]' in content and 'Andrea Kehoe' in content:
        # Find pattern like "Email: [Need to obtain]" near "Andrea Kehoe"
        content = re.sub(
            r'(Andrea Kehoe.*?Email:\s*)\[Need to obtain\]',
            r'\1akehoe1@austincc.edu',
            content,
            flags=re.DOTALL
        )
        if 'akehoe1@austincc.edu' in content and 'akehoe1@austincc.edu' not in original_content:
            file_changes += 1
            print(f"   - Dr. Kehoe email added")

    # File-specific fixes
    if filename == "README.md":
        # Add October 30 deadline to event details if not present
        if 'October 30' not in content and 'November 7, 2025' in content:
            content = content.replace(
                '**Date:** Thursday, November 7, 2025 | 2:00-6:00 PM',
                '**Date:** Thursday, November 7, 2025 | 2:00-6:00 PM\n**Pitch Submission Deadline:** October 30, 2025'
            )
            if 'October 30' in content:
                file_changes += 1
                print(f"   - October 30 deadline added")

    elif filename in ["CRITICAL_UPDATES_REQUIRED.md", "CASH_PRIZE_REMOVAL_REPORT.md"]:
        # Add archival banner if not present
        if '🗄️ ARCHIVAL DOCUMENT' not in content:
            archival_banner = """# 🗄️ ARCHIVAL DOCUMENT - HISTORICAL REFERENCE ONLY

**Status:** COMPLETED - Updates documented here have been implemented
**Purpose:** Historical record of campaign evolution

⚠️ DO NOT USE FOR CURRENT OPERATIONS

For current campaign information, see:
- README.md (campaign overview)
- QUICK_START_GUIDE.md (implementation guide)

---

"""
            # Insert at the beginning after any existing title
            if content.startswith('#'):
                # Find first blank line after title
                first_line_end = content.find('\n')
                if first_line_end > 0:
                    # Check if next line is blank or has markdown (##, -*)
                    next_line_start = first_line_end + 1
                    next_blank = content.find('\n\n', next_line_start)
                    if next_blank > 0:
                        content = content[:next_blank+2] + archival_banner + content[next_blank+2:]
                    else:
                        content = content[:first_line_end+1] + '\n' + archival_banner + content[first_line_end+1:]
                    file_changes += 1
                    print(f"   - Archival banner added")

    # Write updated content if changes were made
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        total_changes += file_changes
        print(f"   [OK] {file_changes} changes applied")
    else:
        print(f"   [INFO] No changes needed")

    print()

# Summary
print("=" * 70)
print("PHASE 3 COMPLETE: Documentation files fixed!")
print("=" * 70)
print(f"\n[OK] Files processed: {len(docs_to_fix)}")
print(f"[OK] Files updated: {files_updated}")
print(f"[OK] Total changes: {total_changes}")
print("\nFixes applied:")
print("  - Email addresses updated to abel.rincon@g.austincc.edu")
print("  - Phone placeholders replaced with 737-206-9977")
print("  - Cash prize language removed")
print("  - October 30 deadline added where applicable")
print("  - Archival documents marked clearly")
print("\nNext: Phase 4 - Verify ACC color consistency\n")
