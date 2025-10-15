#!/usr/bin/env python3
"""
Verify ACC color consistency across all HTML one-pagers.
Official ACC colors: Purple #512698, Gold #FDB913
"""

import os
import glob
import re

print("=" * 70)
print("PHASE 4: ACC COLOR CONSISTENCY CHECK")
print("=" * 70)
print("Verifying official ACC colors in all HTML one-pagers...\n")

# Official ACC colors
ACC_PURPLE = "#512698"
ACC_GOLD = "#FDB913"

html_files = glob.glob("department-one-pagers/*.html")
all_colors_correct = True
files_checked = 0

for filepath in html_files:
    filename = os.path.basename(filepath)
    print(f"[FILE] {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for ACC color variables in :root
    purple_found = ACC_PURPLE.lower() in content.lower()
    gold_found = ACC_GOLD.lower() in content.lower()

    # Also check for CSS variable definitions
    has_purple_var = '--acc-purple:' in content
    has_gold_var = '--acc-gold:' in content

    if purple_found and gold_found:
        print(f"   [OK] ACC Purple ({ACC_PURPLE}) - Found")
        print(f"   [OK] ACC Gold ({ACC_GOLD}) - Found")

        # Verify correct hex codes
        if ACC_PURPLE in content:
            print(f"   [OK] Exact purple match")
        if ACC_GOLD in content:
            print(f"   [OK] Exact gold match")

        if has_purple_var and has_gold_var:
            print(f"   [OK] CSS variables defined")

        files_checked += 1
    else:
        print(f"   [WARNING] Missing ACC colors!")
        if not purple_found:
            print(f"      - ACC Purple ({ACC_PURPLE}) NOT FOUND")
        if not gold_found:
            print(f"      - ACC Gold ({ACC_GOLD}) NOT FOUND")
        all_colors_correct = False

    # Check for any incorrect color variations
    incorrect_colors = []

    # Common variations that might be wrong
    wrong_purples = re.findall(r'#5[0-2][0-9][0-9][0-9][0-9]', content)
    for color in wrong_purples:
        if color.lower() != ACC_PURPLE.lower() and color not in incorrect_colors:
            incorrect_colors.append(color)

    wrong_golds = re.findall(r'#FD[A-F][0-9][0-9][0-9]', content, re.IGNORECASE)
    for color in wrong_golds:
        if color.upper() != ACC_GOLD and color not in incorrect_colors:
            incorrect_colors.append(color)

    if incorrect_colors:
        print(f"   [WARNING] Found possibly incorrect colors: {', '.join(incorrect_colors)}")
        all_colors_correct = False

    print()

print("=" * 70)
print("PHASE 4 COMPLETE: ACC Color Consistency Check")
print("=" * 70)
print(f"\n[OK] Files checked: {files_checked}/{len(html_files)}")

if all_colors_correct:
    print("[OK] All files use correct ACC colors!")
    print(f"     - ACC Purple: {ACC_PURPLE}")
    print(f"     - ACC Gold: {ACC_GOLD}")
else:
    print("[WARNING] Some files may have color inconsistencies")
    print("           Review warnings above")

print("\nNext: Phase 5 - Final automated QA checks\n")
