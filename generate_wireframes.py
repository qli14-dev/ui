#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Canvas size (iPhone 14 Pro proportions: 390×844)
WIDTH = 390
HEIGHT = 844
BG_COLOR = '#FFFFFF'
LINE_COLOR = '#333333'
FILL_COLOR = '#F0F0F0'
TEXT_COLOR = '#000000'

def create_base_canvas():
    """Create base wireframe canvas"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    return img, draw

def draw_app_bar(draw, title="", left_icon=False, right_icon=False):
    """Draw standard app bar"""
    # App bar background
    draw.rectangle([(0, 0), (WIDTH, 60)], fill=FILL_COLOR, outline=LINE_COLOR)

    # Left icon (back button or menu)
    if left_icon:
        draw.text((20, 25), "←", fill=TEXT_COLOR, font=None)

    # Title
    draw.text((WIDTH//2 - 50, 25), title, fill=TEXT_COLOR, font=None)

    # Right icon (settings/more)
    if right_icon:
        draw.text((WIDTH - 35, 25), "⚙", fill=TEXT_COLOR, font=None)

def draw_bottom_nav(draw):
    """Draw bottom navigation"""
    draw.rectangle([(0, HEIGHT-70), (WIDTH, HEIGHT)], fill=FILL_COLOR, outline=LINE_COLOR)

    nav_items = ["🏠", "📚", "🛍️", "👤"]
    nav_labels = ["Home", "Learn", "Store", "Profile"]

    spacing = WIDTH // 4
    for i, (icon, label) in enumerate(zip(nav_items, nav_labels)):
        x = spacing * i + spacing // 2
        draw.text((x - 10, HEIGHT - 55), icon, fill=TEXT_COLOR)
        draw.text((x - 15, HEIGHT - 30), label, fill=TEXT_COLOR, font=None)

def draw_button(draw, x, y, width, height, text):
    """Draw a button"""
    draw.rectangle([(x, y), (x+width, y+height)], fill=FILL_COLOR, outline=LINE_COLOR, width=2)
    text_x = x + width//2 - len(text)*3
    text_y = y + height//2 - 5
    draw.text((text_x, text_y), text, fill=TEXT_COLOR)

def draw_card(draw, x, y, width, height, label=""):
    """Draw a card element"""
    draw.rectangle([(x, y), (x+width, y+height)], fill=FILL_COLOR, outline=LINE_COLOR)
    if label:
        draw.text((x+10, y+10), label, fill=TEXT_COLOR)

def draw_input_field(draw, x, y, width, height, placeholder=""):
    """Draw an input field"""
    draw.rectangle([(x, y), (x+width, y+height)], fill='#FFFFFF', outline=LINE_COLOR)
    if placeholder:
        draw.text((x+10, y+height//2-5), placeholder, fill='#999999')

# ========================================
# 1. HOME SCREEN
# ========================================
def create_home_screen():
    img, draw = create_base_canvas()

    # App bar
    draw_app_bar(draw, "AR Makeup Studio", left_icon=True, right_icon=True)

    # Greeting
    draw.text((20, 80), "Hi, Isabella 👋", fill=TEXT_COLOR, font=None)
    draw.text((20, 100), "Ready for your next look?", fill='#666666', font=None)

    # Scene pills
    pills = ["Daily", "Date", "Work", "Party", "Creative"]
    x = 20
    for pill in pills:
        draw.rectangle([(x, 130), (x+60, 160)], fill=FILL_COLOR, outline=LINE_COLOR)
        draw.text((x+8, 140), pill[:4], fill=TEXT_COLOR)
        x += 70

    # Main CTA
    draw_card(draw, 20, 180, WIDTH-40, 140, "[Camera Icon]")
    draw_button(draw, 80, 260, 230, 40, "START AR MAKEUP")

    # Recommended looks
    draw.text((20, 340), "Recommended Looks", fill=TEXT_COLOR)
    draw.text((WIDTH-30, 340), ">", fill=TEXT_COLOR)

    for i in range(3):
        x_pos = 20 + i * 120
        draw_card(draw, x_pos, 365, 110, 140, "")
        draw.text((x_pos+10, 510), f"Look {i+1}", fill=TEXT_COLOR)

    # List items
    draw_card(draw, 20, 550, WIDTH-40, 60, "📚 Tutorials & Tips")
    draw.text((WIDTH-30, 575), ">", fill=TEXT_COLOR)

    draw_card(draw, 20, 620, WIDTH-40, 60, "💾 Saved Looks")
    draw.text((WIDTH-30, 645), ">", fill=TEXT_COLOR)

    # Bottom nav
    draw_bottom_nav(draw)

    return img

# ========================================
# 2. SCENE SELECTION SCREEN
# ========================================
def create_scene_selection():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Choose Your Scene", left_icon=True)

    draw.text((20, 80), "Select the occasion for your makeup", fill='#666666')

    scenes = [
        ("DAILY", "Perfect for everyday wear"),
        ("DATE", "Romantic and elegant"),
        ("INTERVIEW", "Professional & polished"),
        ("PARTY", "Bold and glamorous"),
        ("CREATIVE", "Artistic and unique")
    ]

    y_pos = 120
    for title, desc in scenes:
        draw_card(draw, 20, y_pos, WIDTH-40, 100, "")
        draw.text((WIDTH//2-30, y_pos+25), title, fill=TEXT_COLOR)
        draw.text((40, y_pos+55), desc, fill='#666666', font=None)
        y_pos += 115

    draw_button(draw, 120, 720, 150, 50, "CONTINUE")

    return img

# ========================================
# 3. LOOK LIBRARY SCREEN
# ========================================
def create_look_library():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Look Library", left_icon=True, right_icon=True)

    # Tabs
    tabs = ["Recommend'd", "Trending", "Natural", "Party"]
    tab_width = WIDTH // 4
    for i, tab in enumerate(tabs):
        x = i * tab_width
        draw.rectangle([(x, 60), (x+tab_width, 100)], fill=FILL_COLOR, outline=LINE_COLOR)
        draw.text((x+10, 75), tab[:8], fill=TEXT_COLOR, font=None)

    # Grid of looks
    y_pos = 120
    for row in range(3):
        for col in range(2):
            x_pos = 20 + col * 185
            draw_card(draw, x_pos, y_pos, 170, 180, "[IMG]")
            draw.text((x_pos+10, y_pos+140), f"Look Style", fill=TEXT_COLOR)
            draw_button(draw, x_pos+30, y_pos+155, 110, 20, "Try Look")
        y_pos += 200

    draw_bottom_nav(draw)

    return img

# ========================================
# 4. AR CAMERA SCREEN
# ========================================
def create_ar_camera():
    img, draw = create_base_canvas()

    # Close button
    draw.text((20, 20), "×", fill=TEXT_COLOR, font=None)

    # Camera view
    draw_card(draw, 30, 100, WIDTH-60, 500, "CAMERA VIEW")

    # Face outline (oval)
    center_x = WIDTH // 2
    center_y = 350
    draw.ellipse([(center_x-80, center_y-120), (center_x+80, center_y+120)],
                 outline=LINE_COLOR, width=2)

    draw.text((center_x-80, 500), "Align your face inside the frame", fill=TEXT_COLOR)

    # Continue button
    draw_button(draw, 120, 650, 150, 50, "CONTINUE")

    # Camera controls
    draw_card(draw, 40, 730, 60, 60, "📷")
    draw_card(draw, 290, 730, 60, 60, "🔄")

    return img

# ========================================
# 5. STEP 0: PREPARATION
# ========================================
def create_step0_preparation():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Step 0: Preparation", left_icon=True, right_icon=True)

    # Illustration area
    draw_card(draw, 40, 80, WIDTH-80, 120, "[ILLUSTRATION]\nTips & Best Practices")

    # Tips list
    tips = [
        "✓ Find good lighting",
        "  Natural light works best",
        "",
        "✓ Position 30-40cm away",
        "  Keep face centered",
        "",
        "✓ Remove glasses",
        "  For better detection",
        "",
        "✓ Tie back hair",
        "  Expose full face"
    ]

    y_pos = 220
    draw.text((20, y_pos), "Before You Begin:", fill=TEXT_COLOR)
    y_pos += 25

    for tip in tips:
        draw.text((20, y_pos), tip, fill=TEXT_COLOR if tip.startswith("✓") else '#666666', font=None)
        y_pos += 20

    # Lighting check card
    draw_card(draw, 20, 480, WIDTH-40, 80, "")
    draw.text((30, 495), "💡 Lighting Check", fill=TEXT_COLOR)
    draw.text((30, 515), "Current lighting: Good", fill='#666666')
    draw.rectangle([(30, 540), (330, 550)], fill='#CCCCCC', outline=LINE_COLOR)
    draw.rectangle([(30, 540), (270, 550)], fill='#4CAF50')
    draw.text((340, 535), "80%", fill=TEXT_COLOR)

    # Start button
    draw_button(draw, 120, 620, 150, 50, "START MAKEUP")
    draw.text((WIDTH//2-30, 680), "Skip Tips", fill='#666666')

    return img

# ========================================
# 6. STEP 1: BASE
# ========================================
def create_step1_base():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Step 1: Base (1/6)", left_icon=True, right_icon=True)

    # Camera preview
    draw_card(draw, 20, 80, WIDTH-40, 250, "CAMERA PREVIEW\n(Live AR Makeup)")

    # Controls
    draw.text((20, 350), "Foundation & Concealer", fill=TEXT_COLOR)

    # Skin tone slider
    draw.text((20, 380), "Skin Tone", fill=TEXT_COLOR, font=None)
    draw.rectangle([(20, 405), (340, 415)], outline=LINE_COLOR)
    draw.ellipse([(140, 400), (160, 420)], fill=LINE_COLOR)
    draw.text((345, 400), "Light-Med", fill='#666666', font=None)

    # Coverage slider
    draw.text((20, 440), "Coverage", fill=TEXT_COLOR, font=None)
    draw.rectangle([(20, 465), (340, 475)], outline=LINE_COLOR)
    draw.ellipse([(200, 460), (220, 480)], fill=LINE_COLOR)
    draw.text((345, 460), "Medium", fill='#666666', font=None)

    # Finish options
    draw.text((20, 500), "Finish", fill=TEXT_COLOR, font=None)
    finishes = ["Matte", "Natural", "Dewy"]
    x_pos = 20
    for finish in finishes:
        draw_card(draw, x_pos, 525, 110, 40, finish)
        x_pos += 120

    # Before/After toggle
    draw_card(draw, 20, 590, WIDTH-40, 60, "Before / After Toggle")
    draw.rectangle([(100, 610), (280, 630)], fill=FILL_COLOR, outline=LINE_COLOR)
    draw.ellipse([(240, 605), (275, 635)], fill=LINE_COLOR)

    # Navigation buttons
    draw_button(draw, 120, 700, 150, 50, "NEXT")
    draw.text((WIDTH//2-25, 760), "Skip Step", fill='#666666')

    return img

# ========================================
# 7. STEP 3: EYES
# ========================================
def create_step3_eyes():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Step 3: Eyes (3/6)", left_icon=True, right_icon=True)

    # Tabs
    tabs = ["Eyeshadow", "Eyeliner", "Mascara"]
    tab_width = WIDTH // 3
    for i, tab in enumerate(tabs):
        x = i * tab_width
        draw.rectangle([(x, 60), (x+tab_width, 95)], fill=FILL_COLOR if i==0 else '#FFFFFF', outline=LINE_COLOR)
        draw.text((x+tab_width//2-30, 72), tab, fill=TEXT_COLOR, font=None)

    # Camera preview
    draw_card(draw, 20, 105, WIDTH-40, 200, "CAMERA PREVIEW\n(Live AR Makeup)")

    # Eyeshadow palette
    draw.text((20, 320), "Eyeshadow Palette", fill=TEXT_COLOR)
    y_pos = 345
    for row in range(2):
        x_pos = 20
        for col in range(6):
            draw.rectangle([(x_pos, y_pos), (x_pos+50, y_pos+50)], fill='#CCCCCC', outline=LINE_COLOR, width=2)
            x_pos += 60
        y_pos += 60

    # Style presets
    draw.text((20, 470), "Style Presets", fill=TEXT_COLOR)
    presets = ["Nat.", "Smky", "Glam", "Cut"]
    x_pos = 20
    for preset in presets:
        draw_card(draw, x_pos, 495, 80, 60, preset)
        x_pos += 90

    # Intensity slider
    draw.text((20, 575), "Intensity", fill=TEXT_COLOR, font=None)
    draw.rectangle([(20, 600), (340, 610)], outline=LINE_COLOR)
    draw.ellipse([(180, 595), (200, 615)], fill=LINE_COLOR)
    draw.text((345, 595), "65%", fill='#666666', font=None)

    # Navigation
    draw_button(draw, 40, 680, 130, 45, "BACK")
    draw_button(draw, 220, 680, 130, 45, "NEXT")

    return img

# ========================================
# 8. FINAL LOOK SCREEN
# ========================================
def create_final_look():
    img, draw = create_base_canvas()

    # Close and more buttons
    draw.text((20, 20), "×", fill=TEXT_COLOR, font=None)
    draw.text((WIDTH-30, 20), "⋮", fill=TEXT_COLOR, font=None)

    # Final preview
    draw_card(draw, 20, 70, WIDTH-40, 350, "FINAL PREVIEW\n(AR Result)")

    # Before/After slider
    draw_card(draw, 20, 440, WIDTH-40, 60, "")
    draw.text((40, 460), "Before", fill=TEXT_COLOR)
    draw.rectangle([(110, 465), (270, 475)], fill=FILL_COLOR, outline=LINE_COLOR)
    draw.ellipse([(240, 460), (260, 480)], fill=LINE_COLOR)
    draw.text((280, 460), "After", fill=TEXT_COLOR)

    # Action buttons (2x2 grid)
    draw_button(draw, 20, 530, 170, 60, "SAVE LOOK")
    draw_button(draw, 200, 530, 170, 60, "SHARE")
    draw_button(draw, 20, 600, 170, 60, "VIEW PRODUCTS")
    draw_button(draw, 200, 600, 170, 60, "TRY ANOTHER")

    # Edit steps link
    draw.text((WIDTH//2-40, 680), "Edit Steps >", fill='#666666')

    return img

# ========================================
# 9. SAVE LOOK SCREEN
# ========================================
def create_save_look():
    img, draw = create_base_canvas()

    draw_app_bar(draw, "Save Your Look", left_icon=True, right_icon=True)

    # Thumbnail
    draw_card(draw, 120, 80, 150, 150, "[THUMBNAIL]\nLook Preview")

    # Name input
    draw.text((20, 250), "Name Your Look", fill=TEXT_COLOR)
    draw_input_field(draw, 20, 275, WIDTH-40, 45, "Evening Glam Look")

    # Tags input
    draw.text((20, 340), "Add Tags (optional)", fill=TEXT_COLOR)
    draw_input_field(draw, 20, 365, WIDTH-40, 45, "glam, date night, smokey...")

    # Suggested tags
    draw.text((20, 430), "Suggested Tags:", fill=TEXT_COLOR)
    tags = ["Evening", "Glam", "Party", "Dramatic", "Bold"]
    x_pos = 20
    y_pos = 455
    for i, tag in enumerate(tags):
        if i == 3:
            x_pos = 20
            y_pos = 505
        draw_card(draw, x_pos, y_pos, 100, 35, tag)
        x_pos += 110

    # Checkboxes
    draw.rectangle([(20, 565), (35, 580)], outline=LINE_COLOR)
    draw.text((45, 565), "Make this look public", fill=TEXT_COLOR, font=None)

    draw.rectangle([(20, 595), (35, 610)], outline=LINE_COLOR)
    draw.text((45, 595), "Save products to wishlist", fill=TEXT_COLOR, font=None)

    # Save button
    draw_button(draw, 120, 660, 150, 50, "SAVE LOOK")
    draw.text((WIDTH//2-25, 720), "Cancel", fill='#666666')

    return img

# ========================================
# 10. PRODUCT DETAIL SCREEN
# ========================================
def create_product_detail():
    img, draw = create_base_canvas()

    # Top bar with icons
    draw.text((20, 20), "←", fill=TEXT_COLOR)
    draw.text((WIDTH-80, 20), "♡", fill=TEXT_COLOR)
    draw.text((WIDTH-50, 20), "🔗", fill=TEXT_COLOR)
    draw.text((WIDTH-25, 20), "⋮", fill=TEXT_COLOR)

    # Product image
    draw_card(draw, 20, 60, WIDTH-40, 250, "PRODUCT IMAGE\n(Large Preview)")

    # Image dots
    dots_x = WIDTH//2 - 30
    for i in range(4):
        fill = LINE_COLOR if i == 0 else '#CCCCCC'
        draw.ellipse([(dots_x + i*20, 320), (dots_x + i*20 + 10, 330)], fill=fill)

    # Product info
    draw.text((20, 350), "Foundation Pro HD", fill=TEXT_COLOR, font=None)
    draw.text((20, 370), "Brand Name", fill='#666666', font=None)
    draw.text((20, 390), "★★★★☆ 4.3 (234 reviews)", fill='#666666', font=None)
    draw.text((20, 420), "$32.00", fill=TEXT_COLOR, font=None)

    # Action buttons
    draw_button(draw, 20, 460, 170, 50, "TRY IN AR")
    draw_button(draw, 200, 460, 170, 50, "BUY NOW")

    # Description
    draw.text((20, 530), "Description", fill=TEXT_COLOR)
    draw.text((WIDTH-20, 530), "▼", fill='#666666')
    draw_card(draw, 20, 555, WIDTH-40, 60, "Long-lasting, full coverage\nfoundation for all skin types...")

    # Shades
    draw.text((20, 635), "Shades", fill=TEXT_COLOR)
    draw.text((WIDTH-20, 635), "▼", fill='#666666')
    x_pos = 20
    for i in range(5):
        draw.rectangle([(x_pos, 660), (x_pos+50, 690)], fill='#CCCCCC', outline=LINE_COLOR)
        x_pos += 60
    draw.text((x_pos, 670), "→", fill=TEXT_COLOR)

    # Other sections
    draw.text((20, 710), "Ingredients", fill=TEXT_COLOR)
    draw.text((WIDTH-20, 710), "▼", fill='#666666')

    draw.text((20, 750), "Reviews (234)", fill=TEXT_COLOR)
    draw.text((WIDTH-20, 750), "▼", fill='#666666')

    return img

# ========================================
# 11. LOGIN SCREEN
# ========================================
def create_login_screen():
    img, draw = create_base_canvas()

    # Close button
    draw.text((20, 20), "×", fill=TEXT_COLOR)

    # Logo area
    draw_card(draw, 155, 80, 80, 80, "🎭")
    draw.text((WIDTH//2-70, 180), "AR Makeup Studio", fill=TEXT_COLOR)
    draw.text((WIDTH//2-80, 210), "Welcome back! Please login", fill='#666666', font=None)

    # Email field
    draw.text((20, 260), "Email or Phone", fill=TEXT_COLOR)
    draw_input_field(draw, 20, 285, WIDTH-40, 45, "")

    # Password field
    draw.text((20, 350), "Password", fill=TEXT_COLOR)
    draw_input_field(draw, 20, 375, WIDTH-40, 45, "")

    draw.text((WIDTH-150, 430), "Forgot password?", fill='#666666', font=None)

    # Login button
    draw_button(draw, 120, 470, 150, 50, "LOGIN")

    # Divider
    draw.text((WIDTH//2-20, 540), "OR", fill='#666666')
    draw.line([(20, 550), (150, 550)], fill='#CCCCCC')
    draw.line([(240, 550), (370, 550)], fill='#CCCCCC')

    # Social login buttons
    draw_button(draw, 20, 580, WIDTH-40, 45, "[G] Continue with Google")
    draw_button(draw, 20, 635, WIDTH-40, 45, "[f] Continue with Facebook")
    draw_button(draw, 20, 690, WIDTH-40, 45, "[🍎] Continue with Apple")

    # Sign up link
    draw.text((WIDTH//2-90, 760), "Don't have an account? Sign up", fill='#666666', font=None)
    draw.text((WIDTH//2-60, 790), "Continue as Guest", fill='#666666', font=None)

    return img

# ========================================
# 12. ERROR SCREEN: CAMERA DISABLED
# ========================================
def create_camera_error():
    img, draw = create_base_canvas()

    # Icon
    draw_card(draw, 155, 180, 80, 80, "📷❌")

    # Title
    draw.text((WIDTH//2-80, 290), "Camera Access Disabled", fill=TEXT_COLOR)

    # Message
    message = [
        "This app requires camera access",
        "to provide AR makeup features",
        "",
        "Please enable camera permission",
        "in your device settings"
    ]

    y_pos = 330
    for line in message:
        draw.text((WIDTH//2-len(line)*3, y_pos), line, fill='#666666', font=None)
        y_pos += 25

    # Buttons
    draw_button(draw, 95, 500, 200, 50, "OPEN SETTINGS")
    draw.text((WIDTH//2-30, 570), "Not Now", fill='#666666')

    return img

# ========================================
# 13. PROFILE SCREEN
# ========================================
def create_profile_screen():
    img, draw = create_base_canvas()

    # Settings icon
    draw.text((WIDTH-30, 20), "⚙️", fill=TEXT_COLOR)

    # Avatar
    draw.ellipse([(145, 60), (245, 160)], fill=FILL_COLOR, outline=LINE_COLOR, width=2)
    draw.text((185, 105), "(○)", fill=TEXT_COLOR)

    # Name
    draw.text((WIDTH//2-50, 180), "Isabella Chen", fill=TEXT_COLOR)
    draw.text((WIDTH//2-60, 200), "@isabella_makeup", fill='#666666', font=None)

    # Edit profile button
    draw_button(draw, 95, 230, 200, 40, "EDIT PROFILE")

    # Menu items
    menu_items = [
        ("Preferences", "Edit quiz answers & settings"),
        ("My Looks", "24 saved looks"),
        ("History", "View all past looks"),
        ("Wishlist", "12 saved products"),
        ("Settings", "App preferences & privacy")
    ]

    y_pos = 300
    for title, subtitle in menu_items:
        draw_card(draw, 20, y_pos, WIDTH-40, 70, "")
        draw.text((30, y_pos+15), title, fill=TEXT_COLOR)
        draw.text((30, y_pos+35), subtitle, fill='#666666', font=None)
        draw.text((WIDTH-35, y_pos+25), ">", fill=TEXT_COLOR)
        y_pos += 80

    draw_bottom_nav(draw)

    return img

# ========================================
# Generate all wireframes
# ========================================
def generate_all_wireframes():
    wireframes = {
        '01_home': create_home_screen(),
        '02_scene_selection': create_scene_selection(),
        '03_look_library': create_look_library(),
        '04_ar_camera': create_ar_camera(),
        '05_step0_preparation': create_step0_preparation(),
        '06_step1_base': create_step1_base(),
        '07_step3_eyes': create_step3_eyes(),
        '08_final_look': create_final_look(),
        '09_save_look': create_save_look(),
        '10_product_detail': create_product_detail(),
        '11_login': create_login_screen(),
        '12_camera_error': create_camera_error(),
        '13_profile': create_profile_screen()
    }

    # Create output directory
    output_dir = '/home/user/ui/wireframes'
    os.makedirs(output_dir, exist_ok=True)

    # Save all wireframes
    for name, img in wireframes.items():
        filepath = f'{output_dir}/{name}_wireframe.png'
        img.save(filepath)
        print(f'✓ Generated: {name}_wireframe.png')

    print(f'\n✅ All wireframes generated in {output_dir}/')
    print(f'Total screens: {len(wireframes)}')

if __name__ == '__main__':
    print('🎨 Generating AR Makeup App Wireframes...\n')
    generate_all_wireframes()
