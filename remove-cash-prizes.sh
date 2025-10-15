#!/bin/bash

# Script to remove cash prize guarantees from all faculty outreach emails
# Critical correction - cannot guarantee cash prizes in communications

echo "=== REMOVING CASH PRIZE GUARANTEES FROM FACULTY OUTREACH EMAILS ==="
echo ""

# Counter for tracking changes
total_files=0
files_modified=0
total_replacements=0

# Find all .txt files in the three tier directories
for file in tier1-critical/*.txt tier2-high/*.txt tier3-general/*.txt; do
    # Skip if file doesn't exist (glob expansion safety)
    [ -e "$file" ] || continue

    # Skip CORRECTED files (already processed)
    if [[ "$file" == *"_CORRECTED.txt" ]]; then
        continue
    fi

    total_files=$((total_files + 1))
    replacements_in_file=0

    # Create backup
    cp "$file" "$file.backup"

    # Replacement 1: Event details emoji line
    if grep -q "🏆 Cash Prizes for Pitch Competition Winners" "$file"; then
        sed -i 's/🏆 Cash Prizes for Pitch Competition Winners/🏆 Recognition and Awards for Top Pitches/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 2: "Cash prizes to fund..."
    if grep -q "Cash prizes to fund" "$file"; then
        sed -i 's/Cash prizes to fund/Recognition and awards to support/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 3: "win cash prizes"
    if grep -q "win cash prizes" "$file"; then
        sed -i 's/win cash prizes/win recognition and awards/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 4: "Cash prizes for"
    if grep -q "Cash prizes for" "$file"; then
        sed -i 's/Cash prizes for/Awards and recognition for/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 5: "with cash prizes"
    if grep -q "with cash prizes" "$file"; then
        sed -i 's/with cash prizes/with awards and recognition/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 6: "Free to attend, cash prizes for competitors"
    if grep -q "Free to attend, cash prizes for competitors" "$file"; then
        sed -i 's/Free to attend, cash prizes for competitors/Free to attend, recognition and awards for top pitches/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 7: "cash prizes" (catch remaining lowercase)
    if grep -q "cash prizes" "$file"; then
        sed -i 's/cash prizes/recognition and awards/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 8: "Cash prizes" (catch remaining uppercase)
    if grep -q "Cash prizes" "$file"; then
        sed -i 's/Cash prizes/Recognition and awards/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 9: "compete for cash prizes"
    if grep -q "compete for cash prizes" "$file"; then
        sed -i 's/compete for cash prizes/compete for recognition/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 10: "Cash prize opportunities"
    if grep -q "Cash prize opportunities" "$file"; then
        sed -i 's/Cash prize opportunities/Recognition opportunities/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 11: "prize money"
    if grep -q "prize money" "$file"; then
        sed -i 's/prize money/recognition and support/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Replacement 12: "FREE for all ACC students | Cash prizes"
    if grep -q "FREE for all ACC students | Cash prizes" "$file"; then
        sed -i 's/FREE for all ACC students | Cash prizes/FREE for all ACC students | Recognition and awards for top pitches/g' "$file"
        replacements_in_file=$((replacements_in_file + 1))
    fi

    # Track modified files
    if [ $replacements_in_file -gt 0 ]; then
        files_modified=$((files_modified + 1))
        total_replacements=$((total_replacements + replacements_in_file))
        echo "✓ Updated: $file ($replacements_in_file replacement patterns matched)"
    fi
done

echo ""
echo "=== UPDATE COMPLETE ==="
echo "Total files processed: $total_files"
echo "Total files modified: $files_modified"
echo "Total replacement patterns matched: $total_replacements"
echo ""

# Verify no cash prize references remain
echo "=== VERIFICATION: CHECKING FOR REMAINING CASH PRIZE REFERENCES ==="
remaining_count=$(grep -i "cash prize" tier1-critical/*.txt tier2-high/*.txt tier3-general/*.txt 2>/dev/null | grep -v ".backup:" | wc -l)

if [ "$remaining_count" -eq 0 ]; then
    echo "✓ SUCCESS: Zero 'cash prize' references remaining!"
else
    echo "⚠ WARNING: Found $remaining_count remaining 'cash prize' references:"
    grep -i "cash prize" tier1-critical/*.txt tier2-high/*.txt tier3-general/*.txt 2>/dev/null | grep -v ".backup:"
fi

echo ""
echo "Backups created with .backup extension"
echo "Review changes and delete .backup files when satisfied"
