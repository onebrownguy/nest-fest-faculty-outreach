#!/usr/bin/env python3
"""
Update all HTML one-pagers with consistent messaging:
1. Remove cash prize language
2. Update schedule to 2-5PM + 5-6PM
3. Add October 30th deadline
4. Update CTA with all links
5. Add QR code section
6. Update email to abel.rincon@g.austincc.edu
7. Ensure consistent ACC colors
"""

import os
import re

# Define the files to update
files = [
    "Accounting_NEST_FEST_One_Pager.html",
    "Computer_Science_NEST_FEST_One_Pager.html",
    "Fashion_Incubator_NEST_FEST_One_Pager.html",
    "Hospitality_Culinary_NEST_Pager.html",
    "Liberal_Arts_NEST_FEST_One_Pager.html",
    "Marketing_NEST_FEST_One_Pager.html"
]

base_dir = "department-one-pagers"

# Common replacements
replacements = [
    # Schedule update
    (r'<p><strong>📅 Thursday, November 7, 2025 \| 2:00-6:00 PM</strong></p>\s*<p><strong>📍 Presentation Hall, ACC Riverside Campus</strong></p>\s*<p><strong>🎓 FREE for all ACC students \| 🏆 Cash Prizes</strong></p>',
     '''<p><strong>📅 Thursday, November 7, 2025</strong></p>
            <p><strong>⏰ 2:00-5:00 PM - Student Pitch Ceremonies</strong></p>
            <p><strong>⏰ 5:00-6:00 PM - VIP Reception (participants, VIPs, sponsors)</strong></p>
            <p><strong>📍 Presentation Hall, ACC Riverside Campus</strong></p>
            <p style="margin-top: 1rem; color: #dc2626; font-size: 1.2rem;"><strong>⏰ IDEA SUBMISSION DEADLINE: October 30, 2025</strong></p>
            <p><strong>🎓 FREE for all ACC students | 🏆 Recognition & Mentorship</strong></p>'''),

    # Remove cash prizes stat card
    (r'<div class="stat-card">\s*<div class="stat-number">\$10K\+</div>\s*<div class="stat-label">Cash Prizes Available</div>\s*</div>',
     '''<div class="stat-card">
                <div class="stat-number">Monica Sack</div>
                <div class="stat-label">SXSW Mentor (16 years)</div>
            </div>'''),

    # Update CTA section (complex - will need to be more specific per file)
    (r'<div class="cta-section">.*?</div>\s*<div style="text-align: center',
     '''<div class="cta-section">
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

        <div style="text-align: center'''),
]

print("Starting HTML one-pager updates...")
print("=" * 60)

for filename in files:
    filepath = os.path.join(base_dir, filename)

    if not os.path.exists(filepath):
        print(f"⚠️  Skipping {filename} - file not found")
        continue

    print(f"\n📄 Processing: {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Apply replacements
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Additional simple replacements that were already done
    # (these should already be done, but ensuring they're applied)
    content = content.replace('edge.team@austincc.edu', 'abel.rincon@g.austincc.edu')
    content = content.replace('🏆 Cash Prizes', '🏆 Recognition & Mentorship')
    content = content.replace('cash prizes for competitors', 'recognition and networking for participants')

    # Write updated content
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {filename}")
    else:
        print(f"ℹ️  No changes needed for {filename}")

print("\n" + "=" * 60)
print("✅ All HTML one-pagers processed!")
print("\nPlease manually copy your QR code to:")
print("D:\\Portfolio\\nest-fest-faculty-outreach\\assets\\nest-fest-qr-code.png")
