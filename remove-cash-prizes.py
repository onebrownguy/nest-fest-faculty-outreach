#!/usr/bin/env python3
"""
Script to remove cash prize guarantees from all faculty outreach emails
Critical correction - cannot guarantee cash prizes in communications
"""

import os
import glob
import re

def main():
    print("=== REMOVING CASH PRIZE GUARANTEES FROM FACULTY OUTREACH EMAILS ===")
    print()

    # Counter for tracking changes
    total_files = 0
    files_modified = 0
    total_replacements = 0

    # Define all replacement patterns
    replacements = [
        # Specific patterns first (more specific to less specific)
        ("🏆 Cash Prizes for Pitch Competition Winners", "🏆 Recognition and Awards for Top Pitches"),
        ("🏆 Cash Prizes for Pitch Competition", "🏆 Recognition and Awards for Top Pitches"),
        ("FREE for all ACC students | Cash prizes | Professional networking", "FREE for all ACC students | Recognition and awards for top pitches | Professional networking"),
        ("FREE for all ACC students | Cash prizes | Professional mentorship | VIP reception", "FREE for all ACC students | Recognition and awards for top pitches | Professional mentorship | VIP reception"),
        ("FREE for all ACC students | Cash prizes", "FREE for all ACC students | Recognition and awards for top pitches"),
        ("Free to attend, cash prizes for competitors", "Free to attend, recognition and awards for top pitches"),
        ("Cash prizes to fund", "Recognition and awards to support"),
        ("cash prizes to fund", "recognition and awards to support"),
        ("win cash prizes", "win recognition and awards"),
        ("Cash prizes for", "Awards and recognition for"),
        ("cash prizes for", "awards and recognition for"),
        ("with cash prizes", "with awards and recognition"),
        ("compete for cash prizes", "compete for recognition"),
        ("Cash prize opportunities", "Recognition opportunities"),
        ("cash prize opportunities", "recognition opportunities"),
        ("prize money", "recognition and support"),
        # Generic catch-all patterns last
        ("cash prizes", "recognition and awards"),
        ("Cash prizes", "Recognition and awards"),
    ]

    # Find all .txt files in the three tier directories
    patterns = [
        "tier1-critical/*.txt",
        "tier2-high/*.txt",
        "tier3-general/*.txt"
    ]

    all_files = []
    for pattern in patterns:
        all_files.extend(glob.glob(pattern))

    # Process each file
    for filepath in all_files:
        # Skip CORRECTED files (old versions)
        if "_CORRECTED.txt" in filepath:
            continue

        # Skip backup files
        if filepath.endswith(".backup"):
            continue

        total_files += 1
        replacements_in_file = 0

        # Read file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Apply all replacements
        for old_text, new_text in replacements:
            if old_text in content:
                count = content.count(old_text)
                content = content.replace(old_text, new_text)
                replacements_in_file += count

        # If content changed, write back and create backup
        if content != original_content:
            # Create backup
            backup_path = filepath + ".backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)

            # Write updated content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            files_modified += 1
            total_replacements += replacements_in_file
            print(f"[OK] Updated: {filepath} ({replacements_in_file} replacements made)")

    print()
    print("=== UPDATE COMPLETE ===")
    print(f"Total files processed: {total_files}")
    print(f"Total files modified: {files_modified}")
    print(f"Total replacements made: {total_replacements}")
    print()

    # Verify no cash prize references remain
    print("=== VERIFICATION: CHECKING FOR REMAINING CASH PRIZE REFERENCES ===")
    remaining_files = []
    remaining_count = 0

    for filepath in all_files:
        # Skip CORRECTED and backup files
        if "_CORRECTED.txt" in filepath or filepath.endswith(".backup"):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Case-insensitive search for cash prize
        matches = re.findall(r'cash prize[s]?', content, re.IGNORECASE)
        if matches:
            remaining_files.append((filepath, len(matches)))
            remaining_count += len(matches)

    if remaining_count == 0:
        print("[SUCCESS] Zero 'cash prize' references remaining!")
    else:
        print(f"[WARNING] Found {remaining_count} remaining 'cash prize' references in {len(remaining_files)} files:")
        for filepath, count in remaining_files:
            print(f"  - {filepath}: {count} reference(s)")
            # Show the lines with references
            with open(filepath, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    if re.search(r'cash prize[s]?', line, re.IGNORECASE):
                        print(f"    Line {i}: {line.strip()}")

    print()
    print("Backups created with .backup extension")
    print("Review changes and delete .backup files when satisfied")

if __name__ == "__main__":
    main()
