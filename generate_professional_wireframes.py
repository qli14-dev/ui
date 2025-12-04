#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Professional wireframe settings
SCREEN_WIDTH = 375
SCREEN_HEIGHT = 812
DEVICE_PADDING = 20
SCREEN_RADIUS = 40
BG_COLOR = '#FFFFFF'
DEVICE_COLOR = '#E8E8E8'
LINE_COLOR = '#333333'
FILL_COLOR = '#F5F5F5'
TEXT_COLOR = '#333333'
LIGHT_TEXT = '#999999'

def draw_device_frame(draw, x, y, width, height):
    """Draw iPhone device frame with rounded corners"""
    # Outer device frame
    padding = 15
    draw.rounded_rectangle(
        [(x - padding, y - padding), (x + width + padding, y + height + padding)],
        radius=SCREEN_RADIUS,
        fill=DEVICE_COLOR,
        outline='#CCCCCC',
        width=2
    )

    # Screen area
    draw.rounded_rectangle(
        [(x, y), (x + width, y + height)],
        radius=SCREEN_RADIUS - 5,
        fill=BG_COLOR,
        outline=LINE_COLOR,
        width=1
    )

    # Notch
    notch_width = 120
    notch_height = 25
    notch_x = x + (width - notch_width) // 2
    draw.rounded_rectangle(
        [(notch_x, y), (notch_x + notch_width, y + notch_height)],
        radius=12,
        fill=DEVICE_COLOR
    )

    # Home indicator
    indicator_width = 120
    indicator_height = 5
    indicator_x = x + (width - indicator_width) // 2
    draw.rounded_rectangle(
        [(indicator_x, y + height - 15), (indicator_x + indicator_width, y + height - 10)],
        radius=3,
        fill='#CCCCCC'
    )

def draw_text(draw, x, y, text, size='normal', color=TEXT_COLOR):
    """Draw text with proper sizing"""
    draw.text((x, y), text, fill=color)

def draw_box(draw, x, y, width, height, fill=FILL_COLOR, outline=LINE_COLOR, radius=0):
    """Draw a box element"""
    if radius > 0:
        draw.rounded_rectangle([(x, y), (x + width, y + height)], radius=radius, fill=fill, outline=outline, width=1)
    else:
        draw.rectangle([(x, y), (x + width, y + height)], fill=fill, outline=outline, width=1)

def draw_button(draw, x, y, width, height, text, primary=False):
    """Draw a button"""
    fill = LINE_COLOR if primary else FILL_COLOR
    text_color = BG_COLOR if primary else TEXT_COLOR
    draw.rounded_rectangle([(x, y), (x + width, y + height)], radius=8, fill=fill, outline=LINE_COLOR, width=2)
    text_x = x + width // 2 - len(text) * 3
    text_y = y + height // 2 - 5
    draw_text(draw, text_x, text_y, text, color=text_color)

# ============================================
# 1. HOME SCREEN
# ============================================
def create_home_screen():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Status bar
    draw_text(draw, x_base + 25, y_base + 10, "9:41", color=TEXT_COLOR)
    draw_box(draw, x_base + SCREEN_WIDTH - 80, y_base + 8, 60, 15, fill=None, outline=None)

    # App bar
    draw_box(draw, x_base, y_base + 40, SCREEN_WIDTH, 60, fill=BG_COLOR)
    draw_text(draw, x_base + 20, y_base + 60, "☰", size='large')
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 60, y_base + 60, "AR Makeup Studio")
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 60, "⚙")

    # Greeting
    draw_text(draw, x_base + 20, y_base + 120, "Hi, Isabella 👋", size='large')
    draw_text(draw, x_base + 20, y_base + 145, "Ready for your next look?", color=LIGHT_TEXT)

    # Scene pills
    pills = ["Daily", "Date", "Work", "Party", "Create"]
    x_pill = x_base + 20
    for pill in pills:
        draw_box(draw, x_pill, y_base + 175, 65, 35, radius=18)
        draw_text(draw, x_pill + 12, y_base + 185, pill)
        x_pill += 70

    # Main CTA card
    draw_box(draw, x_base + 20, y_base + 230, SCREEN_WIDTH - 40, 160, radius=12)
    draw_box(draw, x_base + SCREEN_WIDTH // 2 - 40, y_base + 255, 80, 80, radius=40)
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 35, y_base + 285, "📷")
    draw_button(draw, x_base + 90, y_base + 350, 195, 45, "START AR MAKEUP", primary=True)

    # Recommended looks
    draw_text(draw, x_base + 20, y_base + 420, "Recommended Looks")
    draw_text(draw, x_base + SCREEN_WIDTH - 35, y_base + 420, ">", color=LIGHT_TEXT)

    for i in range(3):
        x_card = x_base + 20 + i * 115
        draw_box(draw, x_card, y_base + 450, 105, 140, radius=8)
        draw_box(draw, x_card + 10, y_base + 460, 85, 85, fill='#E0E0E0')
        draw_text(draw, x_card + 10, y_base + 555, f"Look {i+1}")
        draw_box(draw, x_card + 10, y_base + 575, 85, 10, fill='#CCCCCC')

    # List items
    draw_box(draw, x_base + 20, y_base + 620, SCREEN_WIDTH - 40, 60, radius=12)
    draw_text(draw, x_base + 30, y_base + 645, "📚 Tutorials & Tips")
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 645, ">")

    draw_box(draw, x_base + 20, y_base + 690, SCREEN_WIDTH - 40, 60, radius=12)
    draw_text(draw, x_base + 30, y_base + 715, "💾 Saved Looks")
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 715, ">")

    # Bottom nav
    draw.line([(x_base, y_base + 770), (x_base + SCREEN_WIDTH, y_base + 770)], fill='#E0E0E0', width=1)
    nav_items = [("🏠", "Home"), ("📚", "Learn"), ("🛍️", "Store"), ("👤", "Profile")]
    spacing = SCREEN_WIDTH // 4
    for i, (icon, label) in enumerate(nav_items):
        x_nav = x_base + spacing * i + spacing // 2
        draw_text(draw, x_nav - 8, y_base + 775, icon)
        draw_text(draw, x_nav - 12, y_base + 795, label, size='small', color=LIGHT_TEXT)

    return img

# ============================================
# 2. AR CAMERA SCREEN
# ============================================
def create_ar_camera():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Full screen camera view
    draw_box(draw, x_base + 20, y_base + 50, SCREEN_WIDTH - 40, 600, fill='#E8E8E8')

    # Face outline
    center_x = x_base + SCREEN_WIDTH // 2
    center_y = y_base + 300
    draw.ellipse([(center_x - 80, center_y - 120), (center_x + 80, center_y + 120)], outline=LINE_COLOR, width=3)

    # Guide text
    draw_text(draw, center_x - 90, center_y + 140, "Align your face inside the frame", color=TEXT_COLOR)

    # Continue button
    draw_button(draw, x_base + 95, y_base + 680, 185, 50, "CONTINUE", primary=True)

    # Camera controls
    draw_box(draw, x_base + 30, y_base + 750, 60, 60, radius=30)
    draw_text(draw, x_base + 50, y_base + 772, "📷")

    draw_box(draw, x_base + SCREEN_WIDTH - 90, y_base + 750, 60, 60, radius=30)
    draw_text(draw, x_base + SCREEN_WIDTH - 70, y_base + 772, "🔄")

    return img

# ============================================
# 3. STEP 1: BASE
# ============================================
def create_step_base():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # App bar
    draw_text(draw, x_base + 20, y_base + 60, "←")
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 50, y_base + 60, "Step 1: Base (1/6)")
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 60, "?")

    # Camera preview
    draw_box(draw, x_base + 20, y_base + 100, SCREEN_WIDTH - 40, 280, radius=12, fill='#E8E8E8')
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 55, y_base + 230, "CAMERA PREVIEW")

    # Controls section
    draw_text(draw, x_base + 20, y_base + 400, "Foundation & Concealer", color=TEXT_COLOR)

    # Skin Tone slider
    draw_text(draw, x_base + 20, y_base + 430, "Skin Tone", size='small')
    draw_box(draw, x_base + 20, y_base + 455, 300, 4, fill='#CCCCCC', outline=None)
    draw.ellipse([(x_base + 130, y_base + 445), (x_base + 150, y_base + 465)], fill=LINE_COLOR)
    draw_text(draw, x_base + 325, y_base + 450, "Light", color=LIGHT_TEXT, size='small')

    # Coverage slider
    draw_text(draw, x_base + 20, y_base + 490, "Coverage", size='small')
    draw_box(draw, x_base + 20, y_base + 515, 300, 4, fill='#CCCCCC', outline=None)
    draw.ellipse([(x_base + 180, y_base + 505), (x_base + 200, y_base + 525)], fill=LINE_COLOR)
    draw_text(draw, x_base + 325, y_base + 510, "Medium", color=LIGHT_TEXT, size='small')

    # Finish options
    draw_text(draw, x_base + 20, y_base + 550, "Finish", size='small')
    finishes = ["Matte", "Natural", "Dewy"]
    x_finish = x_base + 20
    for i, finish in enumerate(finishes):
        fill = LINE_COLOR if i == 1 else FILL_COLOR
        text_color = BG_COLOR if i == 1 else TEXT_COLOR
        draw_box(draw, x_finish, y_base + 575, 105, 40, radius=8, fill=fill)
        draw_text(draw, x_finish + 25, y_base + 590, finish, color=text_color)
        x_finish += 115

    # Before/After toggle
    draw_box(draw, x_base + 20, y_base + 640, SCREEN_WIDTH - 40, 60, radius=12)
    draw_text(draw, x_base + 30, y_base + 665, "Before / After")
    draw_box(draw, x_base + 200, y_base + 660, 140, 30, radius=15, fill='#CCCCCC')
    draw.ellipse([(x_base + 300, y_base + 655), (x_base + 335, y_base + 690)], fill=LINE_COLOR)

    # Navigation buttons
    draw_button(draw, x_base + 95, y_base + 730, 185, 50, "NEXT", primary=True)

    return img

# ============================================
# 4. FINAL LOOK SCREEN
# ============================================
def create_final_look():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Top bar
    draw_text(draw, x_base + 20, y_base + 60, "×", size='large')
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 60, "⋮")

    # Large preview
    draw_box(draw, x_base + 20, y_base + 100, SCREEN_WIDTH - 40, 380, radius=12, fill='#E8E8E8')
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 55, y_base + 280, "FINAL PREVIEW")

    # Before/After slider
    draw_box(draw, x_base + 20, y_base + 500, SCREEN_WIDTH - 40, 60, radius=12)
    draw_text(draw, x_base + 30, y_base + 525, "Before")
    draw_box(draw, x_base + 100, y_base + 520, 160, 4, fill='#CCCCCC', outline=None)
    draw.ellipse([(x_base + 230, y_base + 510), (x_base + 250, y_base + 530)], fill=LINE_COLOR)
    draw_text(draw, x_base + 270, y_base + 525, "After")

    # Action buttons (2x2 grid)
    buttons = [
        ("SAVE LOOK", 20, 580),
        ("SHARE", 200, 580),
        ("VIEW PRODUCTS", 20, 645),
        ("TRY ANOTHER", 200, 645)
    ]

    for text, x_offset, y_offset in buttons:
        draw_button(draw, x_base + x_offset, y_base + y_offset, 160, 50, text, primary=(text == "SAVE LOOK"))

    # Edit link
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 35, y_base + 720, "Edit Steps >", color=LIGHT_TEXT)

    return img

# ============================================
# 5. SAVE LOOK SCREEN
# ============================================
def create_save_look():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # App bar
    draw_text(draw, x_base + 20, y_base + 60, "←")
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 50, y_base + 60, "Save Your Look")
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 60, "×")

    # Thumbnail preview
    draw_box(draw, x_base + 120, y_base + 110, 135, 180, radius=12, fill='#E0E0E0')
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 35, y_base + 190, "[PREVIEW]")

    # Name input
    draw_text(draw, x_base + 20, y_base + 310, "Name Your Look")
    draw_box(draw, x_base + 20, y_base + 335, SCREEN_WIDTH - 40, 45, radius=8, fill=BG_COLOR)
    draw_text(draw, x_base + 30, y_base + 352, "Evening Glam Look", color=LIGHT_TEXT)

    # Tags input
    draw_text(draw, x_base + 20, y_base + 400, "Add Tags")
    draw_box(draw, x_base + 20, y_base + 425, SCREEN_WIDTH - 40, 45, radius=8, fill=BG_COLOR)
    draw_text(draw, x_base + 30, y_base + 442, "glam, date night...", color=LIGHT_TEXT)

    # Suggested tags
    draw_text(draw, x_base + 20, y_base + 490, "Suggested:", size='small', color=LIGHT_TEXT)
    tags = ["Evening", "Glam", "Party", "Bold"]
    x_tag = x_base + 20
    for tag in tags:
        draw_box(draw, x_tag, y_base + 515, 80, 35, radius=18, fill='#E8E8E8')
        draw_text(draw, x_tag + 18, y_base + 527, tag, size='small')
        x_tag += 90

    # Checkboxes
    draw_box(draw, x_base + 20, y_base + 580, 20, 20, radius=4)
    draw_text(draw, x_base + 45, y_base + 582, "Make this public", size='small')

    draw_box(draw, x_base + 20, y_base + 615, 20, 20, radius=4)
    draw_text(draw, x_base + 45, y_base + 617, "Save products to wishlist", size='small')

    # Save button
    draw_button(draw, x_base + 95, y_base + 680, 185, 50, "SAVE LOOK", primary=True)
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 20, y_base + 745, "Cancel", color=LIGHT_TEXT)

    return img

# ============================================
# 6. PRODUCT DETAIL SCREEN
# ============================================
def create_product_detail():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Top bar
    draw_text(draw, x_base + 20, y_base + 60, "←")
    draw_text(draw, x_base + SCREEN_WIDTH - 100, y_base + 60, "♡")
    draw_text(draw, x_base + SCREEN_WIDTH - 60, y_base + 60, "🔗")
    draw_text(draw, x_base + SCREEN_WIDTH - 30, y_base + 60, "⋮")

    # Product image
    draw_box(draw, x_base + 20, y_base + 100, SCREEN_WIDTH - 40, 280, radius=12, fill='#E8E8E8')

    # Image dots
    dots_x = x_base + SCREEN_WIDTH // 2 - 25
    for i in range(4):
        fill_color = LINE_COLOR if i == 0 else '#CCCCCC'
        draw.ellipse([(dots_x + i * 18, y_base + 390), (dots_x + i * 18 + 8, y_base + 398)], fill=fill_color)

    # Product info
    draw_text(draw, x_base + 20, y_base + 420, "Foundation Pro HD")
    draw_text(draw, x_base + 20, y_base + 440, "Brand Name", color=LIGHT_TEXT, size='small')
    draw_text(draw, x_base + 20, y_base + 460, "★★★★☆ 4.3 (234)", color=LIGHT_TEXT, size='small')

    draw_text(draw, x_base + 20, y_base + 490, "$32.00", size='large')

    # Action buttons
    draw_button(draw, x_base + 20, y_base + 530, 160, 50, "TRY IN AR", primary=False)
    draw_button(draw, x_base + 195, y_base + 530, 160, 50, "BUY NOW", primary=True)

    # Description section
    draw_text(draw, x_base + 20, y_base + 605, "Description")
    draw_text(draw, x_base + SCREEN_WIDTH - 35, y_base + 605, "▼", color=LIGHT_TEXT)
    draw.line([(x_base + 20, y_base + 630), (x_base + SCREEN_WIDTH - 20, y_base + 630)], fill='#E0E0E0')

    # Shades
    draw_text(draw, x_base + 20, y_base + 650, "Shades")
    draw_text(draw, x_base + SCREEN_WIDTH - 35, y_base + 650, "▼", color=LIGHT_TEXT)
    x_shade = x_base + 20
    for i in range(5):
        draw_box(draw, x_shade, y_base + 675, 55, 55, radius=8, fill='#D0D0D0')
        x_shade += 65
    draw.line([(x_base + 20, y_base + 745), (x_base + SCREEN_WIDTH - 20, y_base + 745)], fill='#E0E0E0')

    # Reviews
    draw_text(draw, x_base + 20, y_base + 765, "Reviews (234)")
    draw_text(draw, x_base + SCREEN_WIDTH - 35, y_base + 765, "▼", color=LIGHT_TEXT)

    return img

# ============================================
# 7. LOGIN SCREEN
# ============================================
def create_login():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Close button
    draw_text(draw, x_base + 20, y_base + 60, "×", size='large')

    # Logo
    draw_box(draw, x_base + 140, y_base + 120, 95, 95, radius=48, fill='#E8E8E8')
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 15, y_base + 155, "🎭")

    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 65, y_base + 235, "AR Makeup Studio")
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 75, y_base + 260, "Welcome back! Please login", size='small', color=LIGHT_TEXT)

    # Email input
    draw_text(draw, x_base + 20, y_base + 310, "Email or Phone", size='small')
    draw_box(draw, x_base + 20, y_base + 335, SCREEN_WIDTH - 40, 50, radius=8, fill=BG_COLOR)

    # Password input
    draw_text(draw, x_base + 20, y_base + 405, "Password", size='small')
    draw_box(draw, x_base + 20, y_base + 430, SCREEN_WIDTH - 40, 50, radius=8, fill=BG_COLOR)

    draw_text(draw, x_base + SCREEN_WIDTH - 130, y_base + 490, "Forgot password?", size='small', color=LIGHT_TEXT)

    # Login button
    draw_button(draw, x_base + 95, y_base + 530, 185, 50, "LOGIN", primary=True)

    # Divider
    draw.line([(x_base + 30, y_base + 615), (x_base + 155, y_base + 615)], fill='#CCCCCC', width=1)
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 10, y_base + 607, "OR", color=LIGHT_TEXT)
    draw.line([(x_base + 220, y_base + 615), (x_base + 345, y_base + 615)], fill='#CCCCCC', width=1)

    # Social login buttons
    socials = ["[G] Continue with Google", "[f] Continue with Facebook", "[🍎] Continue with Apple"]
    y_social = y_base + 645
    for social in socials:
        draw_button(draw, x_base + 20, y_social, SCREEN_WIDTH - 40, 45, social, primary=False)
        y_social += 55

    # Sign up link
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 90, y_base + 785, "Don't have an account? Sign up", size='small', color=LIGHT_TEXT)

    return img

# ============================================
# 8. PROFILE SCREEN
# ============================================
def create_profile():
    img = Image.new('RGB', (SCREEN_WIDTH + 30, SCREEN_HEIGHT + 30), '#FAFAFA')
    draw = ImageDraw.Draw(img)
    draw_device_frame(draw, 15, 15, SCREEN_WIDTH, SCREEN_HEIGHT)

    x_base = 15
    y_base = 15

    # Settings icon
    draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + 60, "⚙")

    # Avatar
    draw.ellipse([(x_base + 137, y_base + 100), (x_base + 237, y_base + 200)], fill='#E0E0E0', outline=LINE_COLOR, width=2)
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 10, y_base + 140, "IС")

    # Name
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 45, y_base + 220, "Isabella Chen")
    draw_text(draw, x_base + SCREEN_WIDTH // 2 - 55, y_base + 240, "@isabella_makeup", color=LIGHT_TEXT, size='small')

    # Edit button
    draw_button(draw, x_base + 95, y_base + 270, 185, 45, "EDIT PROFILE", primary=False)

    # Menu items
    menu_items = [
        ("Preferences", "Edit quiz answers & settings", 340),
        ("My Looks", "24 saved looks", 420),
        ("History", "View all past looks", 500),
        ("Wishlist", "12 saved products", 580),
        ("Settings", "App preferences & privacy", 660)
    ]

    for title, subtitle, y_pos in menu_items:
        draw_box(draw, x_base + 20, y_base + y_pos, SCREEN_WIDTH - 40, 70, radius=12)
        draw_text(draw, x_base + 30, y_base + y_pos + 18, title)
        draw_text(draw, x_base + 30, y_base + y_pos + 40, subtitle, color=LIGHT_TEXT, size='small')
        draw_text(draw, x_base + SCREEN_WIDTH - 40, y_base + y_pos + 28, ">", color=LIGHT_TEXT)

    # Bottom nav
    draw.line([(x_base, y_base + 770), (x_base + SCREEN_WIDTH, y_base + 770)], fill='#E0E0E0', width=1)
    nav_items = [("🏠", "Home"), ("📚", "Learn"), ("🛍️", "Store"), ("👤", "Profile")]
    spacing = SCREEN_WIDTH // 4
    for i, (icon, label) in enumerate(nav_items):
        x_nav = x_base + spacing * i + spacing // 2
        draw_text(draw, x_nav - 8, y_base + 775, icon)
        draw_text(draw, x_nav - 12, y_base + 795, label, size='small', color=TEXT_COLOR if i == 3 else LIGHT_TEXT)

    return img

# ============================================
# Generate all screens
# ============================================
def generate_all_screens():
    screens = {
        '01_Home': create_home_screen(),
        '02_AR_Camera': create_ar_camera(),
        '03_Step_Base': create_step_base(),
        '04_Final_Look': create_final_look(),
        '05_Save_Look': create_save_look(),
        '06_Product_Detail': create_product_detail(),
        '07_Login': create_login(),
        '08_Profile': create_profile()
    }

    output_dir = '/home/user/ui/wireframes_professional'
    os.makedirs(output_dir, exist_ok=True)

    # Save individual screens
    for name, img in screens.items():
        filepath = f'{output_dir}/{name}.png'
        img.save(filepath)
        print(f'✓ Generated: {name}.png')

    # Create composite images (2 rows x 4 columns)
    screen_list = list(screens.values())

    # First composite (screens 1-4)
    composite1_width = (SCREEN_WIDTH + 30) * 4 + 50
    composite1_height = (SCREEN_HEIGHT + 80) + 50
    composite1 = Image.new('RGB', (composite1_width, composite1_height), '#FAFAFA')

    for i in range(4):
        x_offset = 25 + i * (SCREEN_WIDTH + 30 + 10)
        composite1.paste(screen_list[i], (x_offset, 60))
        # Add title
        draw = ImageDraw.Draw(composite1)
        titles = ['Home', 'AR Camera', 'Step: Base', 'Final Look']
        draw_text(draw, x_offset + 140, 25, titles[i], color=TEXT_COLOR)

    composite1.save(f'{output_dir}/composite_1-4.png')
    print('✓ Generated: composite_1-4.png')

    # Second composite (screens 5-8)
    composite2 = Image.new('RGB', (composite1_width, composite1_height), '#FAFAFA')

    for i in range(4, 8):
        x_offset = 25 + (i - 4) * (SCREEN_WIDTH + 30 + 10)
        composite2.paste(screen_list[i], (x_offset, 60))
        # Add title
        draw = ImageDraw.Draw(composite2)
        titles = ['Save Look', 'Product Detail', 'Login', 'Profile']
        draw_text(draw, x_offset + 130, 25, titles[i - 4], color=TEXT_COLOR)

    composite2.save(f'{output_dir}/composite_5-8.png')
    print('✓ Generated: composite_5-8.png')

    print(f'\n✅ All wireframes generated in {output_dir}/')
    print(f'Total individual screens: {len(screens)}')
    print(f'Total composite images: 2')

if __name__ == '__main__':
    print('🎨 Generating Professional Wireframes...\n')
    generate_all_screens()
