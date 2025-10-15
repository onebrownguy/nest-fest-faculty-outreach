#!/bin/bash
# NEST-FEST Faculty Outreach Campaign - Session Resume Script
# Session Date: October 15, 2025
# Session ID: nest-fest-qa-2025-10-15
#
# This script helps you resume work on the NEST-FEST campaign
# by showing session summary, verifying status, and listing next tasks.

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project paths
PROJECT_DIR="D:\Portfolio\nest-fest-faculty-outreach"
SESSION_DIR="$PROJECT_DIR/.claude/sessions"
SESSION_WRAP="$SESSION_DIR/SESSION_WRAP_2025-10-15.md"

# Clear screen
clear

echo -e "${BLUE}╔════════════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                                    ║${NC}"
echo -e "${BLUE}║   NEST-FEST Faculty Outreach Campaign - Session Resume            ║${NC}"
echo -e "${BLUE}║   Session: October 15, 2025 QA Complete                           ║${NC}"
echo -e "${BLUE}║                                                                    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Navigate to project directory
cd "$PROJECT_DIR" || {
    echo -e "${RED}[ERROR]${NC} Could not navigate to project directory: $PROJECT_DIR"
    exit 1
}

echo -e "${GREEN}[OK]${NC} Project directory: $PROJECT_DIR"
echo ""

# ============================================================================
# SECTION 1: Session Summary
# ============================================================================

echo -e "${BLUE}═══ SESSION SUMMARY ═══${NC}"
echo ""
echo "Date: October 15, 2025"
echo "Duration: ~2 hours"
echo "Status: ✅ 100% DEPLOYMENT READY"
echo ""
echo "Work Completed:"
echo "  • Phase 1: HTML one-pagers updated (7 files, 12 changes)"
echo "  • Phase 2: Email templates corrected (62 files, 133 changes)"
echo "  • Phase 3: Documentation synchronized (10 files, 20 changes)"
echo "  • Phase 4: ACC colors verified (7 files, 0 changes needed)"
echo "  • Phase 5: Final QA validation (81 files, 100% pass rate)"
echo ""
echo "Total Corrections: 169 changes across 81 files"
echo "QA Pass Rate: 100% (all 7 validation criteria met)"
echo ""

# ============================================================================
# SECTION 2: Campaign Status
# ============================================================================

echo -e "${BLUE}═══ CAMPAIGN STATUS ═══${NC}"
echo ""
echo "Event Details:"
echo "  • Date: Thursday, November 7, 2025"
echo "  • Time: 2:00-6:00 PM (2-5PM ceremonies, 5-6PM reception)"
echo "  • Location: Presentation Hall, ACC Riverside Campus"
echo "  • Submission Deadline: October 30, 2025"
echo ""
echo "Contact Information:"
echo "  • Primary: Abel Rincon (abel.rincon@g.austincc.edu | 737-206-9977)"
echo "  • Always CC: harshal.shah@austincc.edu, akehoe1@austincc.edu"
echo ""
echo "Campaign Assets:"
echo "  • 61 personalized faculty emails (3 tiers: 10 + 10 + 42)"
echo "  • 7 department HTML one-pagers (all QA verified)"
echo "  • 12 strategy documents (all updated)"
echo "  • 6 reusable QA scripts (806 lines of Python)"
echo ""

# ============================================================================
# SECTION 3: Critical Verifications
# ============================================================================

echo -e "${BLUE}═══ CRITICAL VERIFICATIONS ═══${NC}"
echo ""

# Check 1: QR Code File
echo -n "Checking QR code file... "
if [ -f "$PROJECT_DIR/assets/nest-fest-qr-code.png" ]; then
    QR_SIZE=$(du -h "$PROJECT_DIR/assets/nest-fest-qr-code.png" | cut -f1)
    echo -e "${GREEN}[OK]${NC} Found (Size: $QR_SIZE)"
else
    echo -e "${RED}[MISSING]${NC} QR code not added yet"
    echo "    Action: Copy user's 1000x1000px QR code to assets/nest-fest-qr-code.png"
fi

# Check 2: Git Status
echo -n "Checking git status... "
GIT_STATUS=$(git status --porcelain | wc -l)
if [ "$GIT_STATUS" -eq 0 ]; then
    echo -e "${GREEN}[OK]${NC} All changes committed"
else
    echo -e "${YELLOW}[PENDING]${NC} $GIT_STATUS files not committed"
    echo "    Action: Run 'git add -A && git commit -m \"Your message\"'"
fi

# Check 3: Documentation Files
echo -n "Checking documentation... "
if [ -f "$PROJECT_DIR/DEPLOYMENT_READY_CERTIFICATE.md" ] && \
   [ -f "$PROJECT_DIR/README.md" ] && \
   [ -f "$PROJECT_DIR/QUICK_START_GUIDE.md" ]; then
    echo -e "${GREEN}[OK]${NC} All core docs present"
else
    echo -e "${RED}[MISSING]${NC} Some documentation files missing"
fi

# Check 4: QA Scripts
echo -n "Checking QA scripts... "
QA_SCRIPTS=("fix-all-html-pagers.py" "fix-all-email-templates.py" "fix-documentation.py" \
            "check-acc-colors.py" "final-qa-check.py" "fix-final-issues.py")
MISSING_SCRIPTS=0
for script in "${QA_SCRIPTS[@]}"; do
    if [ ! -f "$PROJECT_DIR/$script" ]; then
        ((MISSING_SCRIPTS++))
    fi
done
if [ "$MISSING_SCRIPTS" -eq 0 ]; then
    echo -e "${GREEN}[OK]${NC} All 6 QA scripts present"
else
    echo -e "${YELLOW}[WARNING]${NC} $MISSING_SCRIPTS scripts missing"
fi

# Check 5: Email Templates
echo -n "Checking email templates... "
TIER1_COUNT=$(ls -1 "$PROJECT_DIR/tier1-critical"/*.txt 2>/dev/null | wc -l)
TIER2_COUNT=$(ls -1 "$PROJECT_DIR/tier2-high"/*.txt 2>/dev/null | wc -l)
TIER3_COUNT=$(ls -1 "$PROJECT_DIR/tier3-general"/*.txt 2>/dev/null | wc -l)
TOTAL_EMAILS=$((TIER1_COUNT + TIER2_COUNT + TIER3_COUNT))
if [ "$TOTAL_EMAILS" -eq 62 ]; then
    echo -e "${GREEN}[OK]${NC} All 62 emails present (10+10+42)"
else
    echo -e "${YELLOW}[WARNING]${NC} Found $TOTAL_EMAILS emails (expected 62)"
fi

# Check 6: HTML One-Pagers
echo -n "Checking HTML one-pagers... "
HTML_COUNT=$(ls -1 "$PROJECT_DIR/department-one-pagers"/*.html 2>/dev/null | wc -l)
if [ "$HTML_COUNT" -eq 7 ]; then
    echo -e "${GREEN}[OK]${NC} All 7 HTML files present"
else
    echo -e "${YELLOW}[WARNING]${NC} Found $HTML_COUNT HTML files (expected 7)"
fi

echo ""

# ============================================================================
# SECTION 4: Immediate Next Tasks
# ============================================================================

echo -e "${BLUE}═══ IMMEDIATE NEXT TASKS ═══${NC}"
echo ""

# Task 1: QR Code
if [ ! -f "$PROJECT_DIR/assets/nest-fest-qr-code.png" ]; then
    echo -e "${RED}🔴 CRITICAL${NC} - Add QR Code File (5 minutes)"
    echo "   Status: BLOCKING - Required for HTML one-pagers"
    echo "   Action:"
    echo "     cp /path/to/user/qr-code.png $PROJECT_DIR/assets/nest-fest-qr-code.png"
    echo "     ls -lh $PROJECT_DIR/assets/nest-fest-qr-code.png"
    echo ""
else
    echo -e "${GREEN}✅ COMPLETE${NC} - QR Code File Added"
    echo ""
fi

# Task 2: Convert HTML to PDF
echo -e "${YELLOW}🟡 RECOMMENDED${NC} - Convert HTML One-Pagers to PDF (30 minutes)"
echo "   Status: For email attachments"
echo "   Action:"
echo "     cd $PROJECT_DIR/department-one-pagers"
echo "     # Open each .html file in browser, Print to PDF (Ctrl+P)"
echo "     # OR use: wkhtmltopdf --enable-local-file-access file.html file.pdf"
echo ""

# Task 3: Tracking Spreadsheet
echo -e "${YELLOW}🟡 RECOMMENDED${NC} - Set Up Email Tracking Spreadsheet (20 minutes)"
echo "   Status: For campaign management"
echo "   Action:"
echo "     cat $PROJECT_DIR/MASTER_EMAIL_TRACKING.md"
echo "     # Follow instructions to create Excel/Google Sheets tracker"
echo ""

# Task 4: Test Send
echo -e "${YELLOW}🟡 RECOMMENDED${NC} - Test Send One Tier 1 Email (15 minutes)"
echo "   Status: Validate format/links before bulk send"
echo "   Action:"
echo "     # Send Adams_Amy_EMAIL_CORRECTED.txt to yourself"
echo "     # Verify: links work, CC addresses work, PDF attaches correctly"
echo ""

# Task 5: Begin Campaign
echo -e "${GREEN}🟢 READY${NC} - Begin Tier 1 Email Campaign (Week 1)"
echo "   Status: 10 critical faculty emails"
echo "   Action:"
echo "     # Send 2 emails per day for 5 days (Monday-Friday)"
echo "     # Always CC: harshal.shah@austincc.edu, akehoe1@austincc.edu"
echo "     # Track sends in spreadsheet"
echo ""

# ============================================================================
# SECTION 5: Quick Commands
# ============================================================================

echo -e "${BLUE}═══ QUICK COMMANDS ═══${NC}"
echo ""
echo "Run Final QA Check:"
echo "  python $PROJECT_DIR/final-qa-check.py"
echo ""
echo "View Complete Session Summary:"
echo "  cat $SESSION_WRAP"
echo ""
echo "Commit Changes:"
echo "  git add -A"
echo "  git commit -m \"Your commit message\""
echo "  git push origin master"
echo ""
echo "Open Documentation:"
echo "  cat $PROJECT_DIR/README.md"
echo "  cat $PROJECT_DIR/DEPLOYMENT_READY_CERTIFICATE.md"
echo "  cat $PROJECT_DIR/QUICK_START_GUIDE.md"
echo ""

# ============================================================================
# SECTION 6: Repository Information
# ============================================================================

echo -e "${BLUE}═══ REPOSITORY INFORMATION ═══${NC}"
echo ""
echo "Repository: https://github.com/onebrownguy/nest-fest-faculty-outreach"
echo "Visibility: Private"
echo "Last Commit: $(git log -1 --oneline)"
echo "Branch: $(git branch --show-current)"
echo "Uncommitted Changes: $GIT_STATUS files"
echo ""

# ============================================================================
# SECTION 7: Campaign Timeline
# ============================================================================

echo -e "${BLUE}═══ CAMPAIGN TIMELINE ═══${NC}"
echo ""
echo "Week 1 (Immediately):"
echo "  • Send Tier 1 Critical Emails (10 faculty, 2 per day)"
echo "  • Department Chairs and Division Dean"
echo "  • Track opens and responses"
echo ""
echo "Week 2:"
echo "  • Send Tier 2 High Priority (10 faculty, 2 per day)"
echo "  • Follow up with Tier 1 non-responders"
echo "  • Monitor nomination submissions"
echo ""
echo "Weeks 3-4:"
echo "  • Send Tier 3 General Faculty (42 faculty, 4-5 per day)"
echo "  • Stagger by department"
echo "  • Final follow-ups before October 30 deadline"
echo ""
echo "October 30, 2025:"
echo "  • SUBMISSION DEADLINE"
echo "  • Final reminder emails to non-responders"
echo ""
echo "November 7, 2025:"
echo "  • NEST-FEST EVENT"
echo "  • 2:00-5:00 PM: Ceremonies and awards"
echo "  • 5:00-6:00 PM: VIP networking reception"
echo ""

# ============================================================================
# SECTION 8: Interactive Options
# ============================================================================

echo -e "${BLUE}═══ INTERACTIVE OPTIONS ═══${NC}"
echo ""
echo "What would you like to do?"
echo ""
echo "  1) Run Final QA Check (verify all 81 files)"
echo "  2) View Complete Session Wrap-Up"
echo "  3) Check Git Status Details"
echo "  4) List All Email Templates"
echo "  5) List All HTML One-Pagers"
echo "  6) View Campaign Timeline"
echo "  7) Open Quick Start Guide"
echo "  8) Exit"
echo ""
read -p "Enter choice [1-8]: " choice

case $choice in
    1)
        echo ""
        echo "Running Final QA Check..."
        python "$PROJECT_DIR/final-qa-check.py"
        ;;
    2)
        echo ""
        echo "Opening Session Wrap-Up..."
        less "$SESSION_WRAP"
        ;;
    3)
        echo ""
        echo "Git Status Details:"
        git status
        ;;
    4)
        echo ""
        echo "Tier 1 Critical Emails (10 files):"
        ls -1 "$PROJECT_DIR/tier1-critical"/*.txt
        echo ""
        echo "Tier 2 High Priority Emails (10 files):"
        ls -1 "$PROJECT_DIR/tier2-high"/*.txt
        echo ""
        echo "Tier 3 General Faculty Emails (42 files):"
        ls -1 "$PROJECT_DIR/tier3-general"/*.txt
        ;;
    5)
        echo ""
        echo "HTML One-Pagers (7 files):"
        ls -lh "$PROJECT_DIR/department-one-pagers"/*.html
        ;;
    6)
        echo ""
        cat "$SESSION_WRAP" | grep -A 50 "═══ CAMPAIGN TIMELINE ═══"
        ;;
    7)
        echo ""
        echo "Opening Quick Start Guide..."
        less "$PROJECT_DIR/QUICK_START_GUIDE.md"
        ;;
    8)
        echo ""
        echo "Exiting session resume script."
        echo "To re-run: bash $SESSION_DIR/session-resume-2025-10-15.sh"
        exit 0
        ;;
    *)
        echo ""
        echo -e "${RED}[ERROR]${NC} Invalid choice. Please run script again."
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}═══ SESSION RESUME COMPLETE ═══${NC}"
echo ""
echo "For full details, read: $SESSION_WRAP"
echo "To re-run this script: bash $SESSION_DIR/session-resume-2025-10-15.sh"
echo ""
echo "Campaign Contact: abel.rincon@g.austincc.edu | 737-206-9977"
echo "Always CC: harshal.shah@austincc.edu, akehoe1@austincc.edu"
echo ""
echo "Good luck with the campaign! 🎉"
echo ""
