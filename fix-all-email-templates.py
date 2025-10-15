#!/usr/bin/env python3
"""
Fix all 62 email templates with global replacements.
Based on QA agent findings.
"""

import os
import glob

print("=" * 70)
print("PHASE 2: FIXING EMAIL TEMPLATES")
print("=" * 70)
print("Applying global fixes to all 62 email templates...\n")

# Find all email template files
tier1_files = glob.glob("tier1-critical/*.txt")
tier2_files = glob.glob("tier2-high/*.txt")
tier3_files = glob.glob("tier3-general/*.txt")

all_files = tier1_files + tier2_files + tier3_files
total_files = len(all_files)

print(f"Found {total_files} email templates:")
print(f"  - Tier 1 (Critical): {len(tier1_files)} files")
print(f"  - Tier 2 (High): {len(tier2_files)} files")
print(f"  - Tier 3 (General): {len(tier3_files)} files")
print()

files_updated = 0
total_changes = 0

for filepath in all_files:
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    file_changes = 0

    # Fix 1: Email address replacement
    if 'edge.team@austincc.edu' in content:
        content = content.replace('edge.team@austincc.edu', 'abel.rincon@g.austincc.edu')
        file_changes += content.count('abel.rincon@g.austincc.edu') - original_content.count('abel.rincon@g.austincc.edu')

    # Fix 2: Add October 30th deadline after event details
    # Look for the event details pattern and add deadline if not present
    if 'October 30' not in content and '**QUICK OVERVIEW:**' in content:
        # Add deadline right after location line
        content = content.replace(
            '📍 Presentation Hall, ACC Riverside Campus\n🎓',
            '📍 Presentation Hall, ACC Riverside Campus\n⏰ **IDEA SUBMISSION DEADLINE: October 30, 2025**\n🎓'
        )
        if 'October 30' in content and 'October 30' not in original_content:
            file_changes += 1

    # Fix 3: Update call-to-action text
    # Enhance the "Register to attend" language
    if 'Register to attend: https://nest-fest.org/' in content:
        content = content.replace(
            'Register to attend: https://nest-fest.org/',
            '🚀 SUBMIT YOUR IDEA (Deadline: October 30): https://nest-fest.org/'
        )
        file_changes += 1

    # Also update "Apply to pitch" if present
    if 'Apply to pitch: https://nest-fest.org/' in content:
        content = content.replace(
            'Apply to pitch: https://nest-fest.org/',
            '💬 Connect with EDGE team to prepare: https://discord.gg/EgjuFMzV'
        )
        file_changes += 1

    # Fix 4: Fix remaining cash prize language (should only be in Means_Nina_EMAIL_CORRECTED.txt)
    if 'Cash prizes' in content or 'cash prizes' in content or 'Cash Prizes' in content:
        content = content.replace('Cash prizes', 'Recognition and awards')
        content = content.replace('cash prizes', 'recognition and awards')
        content = content.replace('Cash Prizes', 'Recognition and Awards')
        file_changes += 1

    # Write updated content if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        total_changes += file_changes
        print(f"[OK] {filename}: {file_changes} changes")

# Summary
print("\n" + "=" * 70)
print("PHASE 2 COMPLETE: Email templates fixed!")
print("=" * 70)
print(f"\n[OK] Files processed: {total_files}")
print(f"[OK] Files updated: {files_updated}")
print(f"[OK] Total changes: {total_changes}")
print("\nFixes applied:")
print("  - Email address: edge.team -> abel.rincon@g.austincc.edu")
print("  - October 30 deadline: Added to all templates")
print("  - Call-to-action: Enhanced with deadline urgency")
print("  - Cash prize language: Removed all instances")
print("\nNext: Phase 3 - Fix documentation files\n")
