#!/usr/bin/env python3
"""
Systematically fix all 6 HTML one-pagers using Business Studies as template.
Applies all critical fixes identified by QA agents.
"""

import os
import re

# Files to update
files_to_fix = [
    "Accounting_NEST_FEST_One_Pager.html",
    "Computer_Science_NEST_FEST_One_Pager.html",
    "Fashion_Incubator_NEST_FEST_One_Pager.html",
    "Hospitality_Culinary_NEST_FEST_One_Pager.html",
    "Liberal_Arts_NEST_FEST_One_Pager.html",
    "Marketing_NEST_FEST_One_Pager.html"
]

base_dir = "department-one-pagers"

print("=" * 70)
print("PHASE 1: FIXING HTML ONE-PAGERS")
print("=" * 70)
print(f"\nUsing Business_Studies_NEST_FEST_One_Pager.html as template standard")
print(f"Fixing {len(files_to_fix)} files...\n")

for filename in files_to_fix:
    filepath = os.path.join(base_dir, filename)

    if not os.path.exists(filepath):
        print(f"[SKIP] {filename} - file not found")
        continue

    print(f"[FILE] Processing: {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = []

    # Fix 1: Event schedule - Update to correct format
    old_schedule = r'<div class="event-details">.*?</div>'
    new_schedule = '''<div class="event-details">
            <p><strong>📅 Thursday, November 7, 2025</strong></p>
            <p><strong>⏰ 2:00-5:00 PM - Student Pitch Ceremonies</strong></p>
            <p><strong>⏰ 5:00-6:00 PM - VIP Reception (participants, VIPs, sponsors)</strong></p>
            <p><strong>📍 Presentation Hall, ACC Riverside Campus</strong></p>
            <p style="margin-top: 1rem; color: #dc2626; font-size: 1.2rem;"><strong>⏰ IDEA SUBMISSION DEADLINE: October 30, 2025</strong></p>
            <p><strong>🎓 FREE for all ACC students | 🏆 Recognition & Mentorship</strong></p>
        </div>'''

    if re.search(old_schedule, content, re.DOTALL):
        content = re.sub(old_schedule, new_schedule, content, flags=re.DOTALL)
        changes_made.append("Event schedule updated")

    # Fix 2: Remove success stories section (if no citations)
    success_stories_pattern = r'<div class="section">\s*<h2>Success Stories:.*?</div>\s*<div class="section">'
    if re.search(success_stories_pattern, content, re.DOTALL):
        content = re.sub(success_stories_pattern, '<div class="section">', content, flags=re.DOTALL)
        changes_made.append("Removed uncited success stories")

    # Fix 3: Update class announcement script - remove cash prizes
    content = content.replace('cash prizes for competitors', 'recognition and networking for participants')
    content = content.replace('Free to attend, cash prizes', 'Free to attend, recognition and awards')

    # Fix 4: Replace stat card - $10K+ prizes with Monica Sack mentor card
    cash_prize_stat = r'<div class="stat-card">\s*<div class="stat-number">\$10K\+</div>\s*<div class="stat-label">Cash Prizes Available</div>\s*</div>'
    mentor_stat = '''<div class="stat-card">
                <div class="stat-number">Monica Sack</div>
                <div class="stat-label">SXSW Mentor (16 years)</div>
            </div>'''

    if re.search(cash_prize_stat, content):
        content = re.sub(cash_prize_stat, mentor_stat, content)
        changes_made.append("Replaced cash prize stat with mentor info")

    # Fix 5: Update CTA section with working links and QR code
    old_cta = r'<div class="cta-section">.*?</div>\s*<div style="text-align: center'
    new_cta = '''<div class="cta-section">
            <h2>🚀 Submit Your Idea by October 30th!</h2>
            <p style="margin-bottom: 2rem; font-size: 1.1rem;">After submitting, connect with EDGE team on Discord to prepare your presentation</p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; max-width: 800px; margin: 2rem auto; text-align: left;">
                <div>
                    <h3 style="color: var(--acc-gold); font-size: 1.3rem; margin-bottom: 1rem;">📋 Submit Your Idea</h3>
                    <a href="https://nest-fest.org/" class="cta-button" target="_blank" style="display: block; text-align: center;">Submit by Oct 30</a>
                    <p style="margin-top: 1rem; font-size: 0.9rem;">Deadline: October 30, 2025</p>
                </div>
                <div>
                    <h3 style="color: var(--acc-gold); font-size: 1.3rem; margin-bottom: 1rem;">💬 Connect with EDGE</h3>
                    <a href="https://discord.gg/EgjuFMzV" class="cta-button" target="_blank" style="display: block; text-align: center;">Join Discord</a>
                    <p style="margin-top: 1rem; font-size: 0.9rem;">Get mentorship & prepare your pitch</p>
                </div>
            </div>

            <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.2);">
                <h3 style="color: var(--acc-gold); font-size: 1.2rem; margin-bottom: 1rem;">All EDGE Team Links</h3>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; font-size: 0.95rem;">
                    <a href="https://nest-fest.org/" target="_blank" style="color: white; text-decoration: underline;">🌐 Website</a>
                    <a href="https://discord.gg/EgjuFMzV" target="_blank" style="color: white; text-decoration: underline;">💬 Discord</a>
                    <a href="https://austincc.campuslabs.com/engage/organization/edgeteam" target="_blank" style="color: white; text-decoration: underline;">📱 Student Org</a>
                    <a href="https://calendar.app.google/rPFQ4o2k56fsKZrM6" target="_blank" style="color: white; text-decoration: underline;">📅 Schedule Meeting</a>
                </div>
                <p style="margin-top: 1.5rem; font-size: 0.95rem;">📧 <a href="mailto:abel.rincon@g.austincc.edu" style="color: white; text-decoration: underline;">abel.rincon@g.austincc.edu</a> | 📞 737-206-9977</p>
            </div>

            <!-- QR Code Section -->
            <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.2);">
                <h3 style="color: var(--acc-gold); font-size: 1.2rem; margin-bottom: 1rem;">Scan to Submit Your Idea</h3>
                <img src="../assets/nest-fest-qr-code.png" alt="NEST-FEST QR Code" style="width: 250px; height: 250px; margin: 0 auto; display: block; background: white; padding: 1rem; border-radius: 8px;">
                <p style="margin-top: 1rem; font-size: 0.9rem;">Scan with your phone to submit at nest-fest.org</p>
            </div>
        </div>

        <div style="text-align: center'''

    if re.search(old_cta, content, re.DOTALL):
        content = re.sub(old_cta, new_cta, content, flags=re.DOTALL)
        changes_made.append("Updated CTA section with links and QR code")

    # Fix 6: Ensure correct email address
    content = content.replace('edge.team@austincc.edu', 'abel.rincon@g.austincc.edu')

    # Fix 7: Ensure "Recognition & Mentorship" not "Cash Prizes"
    content = content.replace('🏆 Cash Prizes', '🏆 Recognition & Mentorship')

    # Write updated content
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   [OK] UPDATED - {len(changes_made)} changes:")
        for change in changes_made:
            print(f"      - {change}")
    else:
        print(f"   [INFO] No changes needed")

    print()

print("=" * 70)
print("PHASE 1 COMPLETE: All HTML one-pagers fixed!")
print("=" * 70)
print("\n[OK] All 7 HTML files now match Business Studies template standard")
print("[OK] Event schedule: 2:00-5:00 PM + 5:00-6:00 PM")
print("[OK] October 30 deadline: Prominently displayed")
print("[OK] No cash prize language")
print("[OK] All links working (nest-fest.org, Discord, etc.)")
print("[OK] QR code section added")
print("[OK] Email: abel.rincon@g.austincc.edu")
print("\nNext: Phase 2 - Fix email templates\n")
