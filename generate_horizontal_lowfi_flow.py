#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Large horizontal flowchart settings
CANVAS_WIDTH = 4800
CANVAS_HEIGHT = 1200
BG_COLOR = '#FFFFFF'
BOX_COLOR = '#333333'
FILL_COLOR = '#F5F5F5'
TEXT_COLOR = '#000000'
ARROW_COLOR = '#333333'

def draw_box(draw, x, y, width, height, text, fill=FILL_COLOR):
    """Draw a flowchart box"""
    draw.rectangle([(x, y), (x + width, y + height)], fill=fill, outline=BOX_COLOR, width=2)

    # Center text
    lines = text.split('\n')
    line_height = 20
    total_height = len(lines) * line_height
    start_y = y + (height - total_height) // 2

    for i, line in enumerate(lines):
        text_width = len(line) * 6
        text_x = x + (width - text_width) // 2
        text_y = start_y + i * line_height
        draw.text((text_x, text_y), line, fill=TEXT_COLOR)

def draw_decision(draw, x, y, size, text):
    """Draw a diamond decision box"""
    half = size // 2
    center_x = x + half
    center_y = y + half

    points = [
        (center_x, y),           # top
        (x + size, center_y),    # right
        (center_x, y + size),    # bottom
        (x, center_y)            # left
    ]

    draw.polygon(points, fill=FILL_COLOR, outline=BOX_COLOR, width=2)

    # Center text
    lines = text.split('\n')
    line_height = 20
    total_height = len(lines) * line_height
    start_y = center_y - total_height // 2

    for i, line in enumerate(lines):
        text_width = len(line) * 6
        text_x = center_x - text_width // 2
        text_y = start_y + i * line_height
        draw.text((text_x, text_y), line, fill=TEXT_COLOR)

def draw_arrow(draw, x1, y1, x2, y2, label=''):
    """Draw an arrow between two points"""
    draw.line([(x1, y1), (x2, y2)], fill=ARROW_COLOR, width=2)

    # Arrow head
    if x2 > x1:  # horizontal right
        draw.polygon([(x2, y2), (x2-10, y2-5), (x2-10, y2+5)], fill=ARROW_COLOR)
    elif x2 < x1:  # horizontal left
        draw.polygon([(x2, y2), (x2+10, y2-5), (x2+10, y2+5)], fill=ARROW_COLOR)
    elif y2 > y1:  # vertical down
        draw.polygon([(x2, y2), (x2-5, y2-10), (x2+5, y2-10)], fill=ARROW_COLOR)
    elif y2 < y1:  # vertical up
        draw.polygon([(x2, y2), (x2-5, y2+10), (x2+5, y2+10)], fill=ARROW_COLOR)

    # Label
    if label:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2 - 10
        draw.text((mid_x, mid_y), label, fill=TEXT_COLOR)

def create_complete_horizontal_flow():
    """Create complete AR Makeup App horizontal flowchart"""
    img = Image.new('RGB', (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Box dimensions
    box_width = 160
    box_height = 100
    spacing_x = 200
    spacing_y = 150

    # Starting position
    start_x = 50
    y_top = 100
    y_middle = 400
    y_bottom = 700

    # Title
    draw.text((20, 20), "AR Interactive Makeup App - Complete User Flow", fill=TEXT_COLOR, font=None)

    # ======================================
    # SECTION 0: ONBOARDING
    # ======================================
    x = start_x

    draw_box(draw, x, y_middle, box_width, box_height, "App\nLaunch")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Splash\nScreen")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Welcome\nScreen")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Language\nSelection")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Privacy\nNotice")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_decision(draw, x, y_middle, box_height, "Camera\nPermission?")

    # Permission denied branch
    draw_arrow(draw, x + 50, y_middle - 10, x + 50, y_bottom, "Deny")
    draw_box(draw, x, y_bottom, box_width, box_height, "Permission\nWarning")
    draw_arrow(draw, x - 30, y_bottom + 50, x + 50, y_middle + box_height + 10, "")

    # Permission allowed - continue
    x += spacing_x
    draw_arrow(draw, x - 140, y_middle + 50, x, y_middle + 50, "Allow")
    draw_box(draw, x, y_middle, box_width, box_height, "Onboarding\nQuiz\n(5 questions)")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Save\nPreferences")
    x += spacing_x

    # ======================================
    # SECTION 1: HOME SCREEN
    # ======================================
    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "HOME\nSCREEN", fill='#E0E0E0')

    # Multiple exits from home
    draw_arrow(draw, x + 80, y_middle, x + 80, y_top)
    draw_box(draw, x, y_top, box_width, box_height, "Tutorials")

    draw_arrow(draw, x + 80, y_middle + box_height, x + 80, y_bottom)
    draw_box(draw, x, y_bottom, box_width, box_height, "Saved\nLooks")

    x += spacing_x

    # ======================================
    # SECTION 2: AR CORE FLOW
    # ======================================
    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Start AR\nMakeup")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Camera\nActivation")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Face\nAlignment")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_decision(draw, x, y_middle, box_height, "Face\nDetected?")

    # Face detection failed
    draw_arrow(draw, x + 50, y_middle + box_height + 10, x + 50, y_bottom, "No")
    draw_box(draw, x, y_bottom, box_width, box_height, "Retry\nWarning")
    draw_arrow(draw, x - 30, y_bottom + 50, x - 150, y_middle + 50, "")

    # Face detected - continue
    x += spacing_x
    draw_arrow(draw, x - 140, y_middle + 50, x, y_middle + 50, "Yes")
    draw_box(draw, x, y_middle, box_width, box_height, "Scene\nSelection")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Look\nLibrary")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Select\nLook")
    x += spacing_x

    # ======================================
    # SECTION 3: AR MAKEUP STEPS
    # ======================================
    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 0:\nPreparation", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 1:\nBase", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 2:\nBrows", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 3:\nEyes", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 4:\nBlush", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 5:\nLips", fill='#F0F0F0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Step 6:\nFinal Touch", fill='#F0F0F0')
    x += spacing_x

    # ======================================
    # SECTION 4: FINAL PREVIEW
    # ======================================
    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Final\nPreview", fill='#D0D0D0')
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_box(draw, x, y_middle, box_width, box_height, "Before/After\nSlider")
    x += spacing_x

    draw_arrow(draw, x - 40, y_middle + 50, x, y_middle + 50)
    draw_decision(draw, x, y_middle, box_height, "Choose\nAction?")

    # ======================================
    # SECTION 5: FINAL ACTIONS
    # ======================================
    x += spacing_x

    # Save branch
    draw_arrow(draw, x - 140, y_middle - 50, x, y_top + 50, "Save")
    draw_box(draw, x, y_top, box_width, box_height, "Save Look\nScreen")
    x_save = x + spacing_x
    draw_arrow(draw, x + box_width, y_top + 50, x_save, y_top + 50)
    draw_decision(draw, x_save, y_top, box_height, "Auth?")
    x_save += spacing_x
    draw_arrow(draw, x_save - 40, y_top + 50, x_save, y_top + 50, "Yes")
    draw_box(draw, x_save, y_top, box_width, box_height, "Save to\nCloud")

    # Share branch
    draw_arrow(draw, x - 140, y_middle + 50, x, y_middle + 50, "Share")
    draw_box(draw, x, y_middle, box_width, box_height, "Share\nOptions")
    x_share = x + spacing_x
    draw_arrow(draw, x + box_width, y_middle + 50, x_share, y_middle + 50)
    draw_box(draw, x_share, y_middle, box_width, box_height, "Share\nPanel")

    # Products branch
    draw_arrow(draw, x - 140, y_middle + 150, x, y_bottom + 50, "Products")
    draw_box(draw, x, y_bottom, box_width, box_height, "Product\nList")
    x_prod = x + spacing_x
    draw_arrow(draw, x + box_width, y_bottom + 50, x_prod, y_bottom + 50)
    draw_box(draw, x_prod, y_bottom, box_width, box_height, "Product\nDetail")
    x_prod += spacing_x
    draw_arrow(draw, x_prod - 40, y_bottom + 50, x_prod, y_bottom + 50)
    draw_box(draw, x_prod, y_bottom, box_width, box_height, "Try AR /\nBuy")

    # Try Another branch
    x_retry = x + spacing_x * 2 + 100
    draw_arrow(draw, x - 100, y_middle - 80, x_retry, y_top - 20, "Retry")
    draw.line([(x_retry, y_top - 20), (x_retry, 50), (start_x + spacing_x * 13, 50),
               (start_x + spacing_x * 13, y_middle - 50)], fill=ARROW_COLOR, width=2)
    draw.text((x_retry + 10, y_top - 40), "(Back to Scene)", fill=TEXT_COLOR)

    # ======================================
    # DONE indicators
    # ======================================
    x_end = x_save + spacing_x
    draw_arrow(draw, x_save + box_width, y_top + 50, x_end, y_top + 50)
    draw_box(draw, x_end, y_top, box_width, box_height, "DONE", fill='#C0C0C0')

    x_end2 = x_share + spacing_x
    draw_arrow(draw, x_share + box_width, y_middle + 50, x_end2, y_middle + 50)
    draw_box(draw, x_end2, y_middle, box_width, box_height, "DONE", fill='#C0C0C0')

    # Add legend
    legend_x = 50
    legend_y = 1050
    draw.text((legend_x, legend_y), "LEGEND:", fill=TEXT_COLOR)
    draw_box(draw, legend_x, legend_y + 25, 100, 50, "Screen")
    draw.text((legend_x + 120, legend_y + 40), "= Screen/Process", fill=TEXT_COLOR)

    draw_decision(draw, legend_x + 250, legend_y + 25, 50, "?")
    draw.text((legend_x + 320, legend_y + 40), "= Decision Point", fill=TEXT_COLOR)

    draw_box(draw, legend_x + 500, legend_y + 25, 100, 50, "Key Flow", fill='#E0E0E0')
    draw.text((legend_x + 620, legend_y + 40), "= Important Step", fill=TEXT_COLOR)

    return img

def create_simplified_horizontal_flow():
    """Create simplified version"""
    img = Image.new('RGB', (3200, 800), BG_COLOR)
    draw = ImageDraw.Draw(img)

    box_width = 140
    box_height = 80
    spacing = 180

    y = 360
    x = 50

    # Title
    draw.text((20, 20), "AR Makeup App - Simplified User Flow", fill=TEXT_COLOR)

    steps = [
        ("Launch", FILL_COLOR),
        ("Onboarding", FILL_COLOR),
        ("Home", '#E0E0E0'),
        ("Face\nDetection", FILL_COLOR),
        ("Scene\nSelection", FILL_COLOR),
        ("AR Steps\n(0-6)", '#F0F0F0'),
        ("Final\nPreview", '#D0D0D0'),
        ("Actions", FILL_COLOR),
        ("Save", FILL_COLOR),
        ("Share", FILL_COLOR),
        ("Products", FILL_COLOR),
        ("Done", '#C0C0C0')
    ]

    for i, (text, fill) in enumerate(steps):
        draw_box(draw, x, y, box_width, box_height, text, fill=fill)

        if i < len(steps) - 1:
            draw_arrow(draw, x + box_width, y + box_height // 2,
                      x + spacing, y + box_height // 2)

        x += spacing

    # Add decision branches
    draw.text((50, 650), "Note: Multiple paths exist - Retry, Guest mode, Error handling not shown", fill=LIGHT_TEXT)

    return img

LIGHT_TEXT = '#666666'

# Generate both versions
print("🎨 Generating Horizontal Low-Fi Flowcharts...\n")

complete_flow = create_complete_horizontal_flow()
complete_flow.save('/home/user/ui/ar_makeup_horizontal_flow_complete.png')
print("✓ Generated: ar_makeup_horizontal_flow_complete.png (4800x1200)")

simplified_flow = create_simplified_horizontal_flow()
simplified_flow.save('/home/user/ui/ar_makeup_horizontal_flow_simplified.png')
print("✓ Generated: ar_makeup_horizontal_flow_simplified.png (3200x800)")

print("\n✅ Horizontal flowcharts generated successfully!")
print("\nFiles:")
print("  - ar_makeup_horizontal_flow_complete.png (detailed with all branches)")
print("  - ar_makeup_horizontal_flow_simplified.png (clean main path)")
