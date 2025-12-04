#!/usr/bin/env python3
"""
Create horizontal multi-row version of AR Makeup User Flow
Using a layout similar to existing horizontal flows
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_horizontal_flow_image():
    # Canvas settings
    width = 5000
    height = 1200
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fallback to default
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_label = ImageFont.load_default()

    # Colors matching original
    action_color = '#FFD4A3'
    system_color = '#C8E6C9'
    decision_color = '#BBDEFB'
    line_color = '#333333'
    text_color = '#000000'

    # Convert hex to RGB
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    action_rgb = hex_to_rgb(action_color)
    system_rgb = hex_to_rgb(system_color)
    decision_rgb = hex_to_rgb(decision_color)
    line_rgb = hex_to_rgb(line_color)
    text_rgb = hex_to_rgb(text_color)

    # Node dimensions
    box_width = 120
    box_height = 60
    spacing_x = 160
    spacing_y = 150

    # Starting position
    start_x = 50
    y_row1 = 80
    y_row2 = 280
    y_row3 = 480
    y_row4 = 680
    y_row5 = 880

    # Draw rounded rectangle (box node)
    def draw_rounded_box(x, y, width, height, radius, fill_color, text, font):
        # Draw rounded rectangle
        draw.rectangle([x + radius, y, x + width - radius, y + height], fill=fill_color)
        draw.rectangle([x, y + radius, x + width, y + height - radius], fill=fill_color)
        draw.ellipse([x, y, x + radius * 2, y + radius * 2], fill=fill_color)
        draw.ellipse([x + width - radius * 2, y, x + width, y + radius * 2], fill=fill_color)
        draw.ellipse([x, y + height - radius * 2, x + radius * 2, y + height], fill=fill_color)
        draw.ellipse([x + width - radius * 2, y + height - radius * 2, x + width, y + height], fill=fill_color)
        # Draw border
        draw.arc([x, y, x + radius * 2, y + radius * 2], 180, 270, fill=line_rgb, width=2)
        draw.arc([x + width - radius * 2, y, x + width, y + radius * 2], 270, 360, fill=line_rgb, width=2)
        draw.arc([x, y + height - radius * 2, x + radius * 2, y + height], 90, 180, fill=line_rgb, width=2)
        draw.arc([x + width - radius * 2, y + height - radius * 2, x + width, y + height], 0, 90, fill=line_rgb, width=2)
        draw.line([x + radius, y, x + width - radius, y], fill=line_rgb, width=2)
        draw.line([x + radius, y + height, x + width - radius, y + height], fill=line_rgb, width=2)
        draw.line([x, y + radius, x, y + height - radius], fill=line_rgb, width=2)
        draw.line([x + width, y + radius, x + width, y + height - radius], fill=line_rgb, width=2)
        # Draw text
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (width - text_width) / 2
        text_y = y + (height - text_height) / 2
        draw.text((text_x, text_y), text, fill=text_rgb, font=font)
        return (x + width / 2, y + height / 2)

    # Draw ellipse node (system state)
    def draw_ellipse_node(x, y, width, height, fill_color, text, font):
        draw.ellipse([x, y, x + width, y + height], fill=fill_color, outline=line_rgb, width=2)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (width - text_width) / 2
        text_y = y + (height - text_height) / 2
        draw.text((text_x, text_y), text, fill=text_rgb, font=font)
        return (x + width / 2, y + height / 2)

    # Draw diamond node (decision)
    def draw_diamond_node(x, y, width, height, fill_color, text, font):
        cx, cy = x + width / 2, y + height / 2
        points = [(cx, y), (x + width, cy), (cx, y + height), (x, cy)]
        draw.polygon(points, fill=fill_color, outline=line_rgb)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = cx - text_width / 2
        text_y = cy - text_height / 2
        draw.text((text_x, text_y), text, fill=text_rgb, font=font)
        return (cx, cy)

    # Draw arrow
    def draw_arrow(x1, y1, x2, y2, label=''):
        draw.line([x1, y1, x2, y2], fill=line_rgb, width=2)
        # Arrowhead
        if x2 > x1:  # Right arrow
            draw.polygon([(x2, y2), (x2 - 10, y2 - 5), (x2 - 10, y2 + 5)], fill=line_rgb)
        elif x2 < x1:  # Left arrow
            draw.polygon([(x2, y2), (x2 + 10, y2 - 5), (x2 + 10, y2 + 5)], fill=line_rgb)
        elif y2 > y1:  # Down arrow
            draw.polygon([(x2, y2), (x2 - 5, y2 - 10), (x2 + 5, y2 - 10)], fill=line_rgb)
        elif y2 < y1:  # Up arrow
            draw.polygon([(x2, y2), (x2 - 5, y2 + 10), (x2 + 5, y2 + 10)], fill=line_rgb)
        # Label
        if label:
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            draw.text((mid_x, mid_y - 15), label, fill=text_rgb, font=font_label)

    # Add title
    draw.text((20, 20), "AR Makeup App - Complete User Flow (Horizontal Layout)", fill=text_rgb, font=font_title)

    # ROW 1: Onboarding Flow
    x = start_x
    nodes = {}

    nodes['start'] = draw_ellipse_node(x, y_row1, box_width, box_height, system_rgb, "Start", font_text)
    x += spacing_x
    nodes['open'] = draw_rounded_box(x, y_row1, box_width, box_height, 10, action_rgb, "Open App", font_text)
    x += spacing_x
    nodes['welcome'] = draw_rounded_box(x, y_row1, box_width, box_height, 10, action_rgb, "Welcome\nScreen", font_text)
    x += spacing_x
    nodes['splash'] = draw_ellipse_node(x, y_row1, box_width, box_height, system_rgb, "Splash\nScreen", font_text)
    x += spacing_x
    nodes['perm'] = draw_rounded_box(x, y_row1, box_width, box_height, 10, action_rgb, "Permission\nRequest", font_text)
    x += spacing_x
    nodes['camera'] = draw_ellipse_node(x, y_row1, box_width, box_height, system_rgb, "Camera\nAccess", font_text)
    x += spacing_x
    nodes['first_time'] = draw_diamond_node(x, y_row1 - 15, box_width, box_height + 30, decision_rgb, "First\nTime?", font_text)
    x += spacing_x
    nodes['tutorial'] = draw_rounded_box(x, y_row1, box_width, box_height, 10, action_rgb, "Tutorial\n(Optional)", font_text)
    x += spacing_x
    nodes['skip_tut'] = draw_rounded_box(x, y_row1 - 50, box_width, box_height, 10, action_rgb, "Skip\nTutorial", font_text)
    nodes['view_tut'] = draw_rounded_box(x, y_row1 + 50, box_width, box_height, 10, action_rgb, "View\nTutorial", font_text)
    x += spacing_x
    nodes['tut_shown'] = draw_ellipse_node(x, y_row1 + 50, box_width, box_height, system_rgb, "Tutorial\nShown", font_text)
    nodes['tut_comp'] = draw_ellipse_node(x, y_row1 - 50, box_width, box_height, system_rgb, "Tutorial\nComplete", font_text)
    x += spacing_x
    nodes['nav_home'] = draw_rounded_box(x, y_row1, box_width, box_height, 10, action_rgb, "Navigate\nto Home", font_text)
    x += spacing_x
    nodes['home'] = draw_ellipse_node(x, y_row1, box_width, box_height, system_rgb, "Home\nScreen", font_text)

    # Draw connections for row 1
    draw_arrow(nodes['start'][0], nodes['start'][1], nodes['open'][0], nodes['open'][1])
    draw_arrow(nodes['open'][0], nodes['open'][1], nodes['welcome'][0], nodes['welcome'][1])
    draw_arrow(nodes['welcome'][0], nodes['welcome'][1], nodes['splash'][0], nodes['splash'][1])
    draw_arrow(nodes['splash'][0], nodes['splash'][1], nodes['perm'][0], nodes['perm'][1])
    draw_arrow(nodes['perm'][0], nodes['perm'][1], nodes['camera'][0], nodes['camera'][1])
    draw_arrow(nodes['camera'][0], nodes['camera'][1], nodes['first_time'][0], nodes['first_time'][1])
    draw_arrow(nodes['first_time'][0], nodes['first_time'][1], nodes['tutorial'][0], nodes['tutorial'][1], 'Yes')
    draw_arrow(nodes['tutorial'][0], nodes['tutorial'][1], nodes['skip_tut'][0], nodes['skip_tut'][1])
    draw_arrow(nodes['tutorial'][0], nodes['tutorial'][1], nodes['view_tut'][0], nodes['view_tut'][1])
    draw_arrow(nodes['skip_tut'][0], nodes['skip_tut'][1], nodes['tut_comp'][0], nodes['tut_comp'][1])
    draw_arrow(nodes['view_tut'][0], nodes['view_tut'][1], nodes['tut_shown'][0], nodes['tut_shown'][1])
    draw_arrow(nodes['tut_shown'][0], nodes['tut_shown'][1], nodes['tut_comp'][0], nodes['tut_comp'][1])
    draw_arrow(nodes['tut_comp'][0], nodes['tut_comp'][1], nodes['nav_home'][0], nodes['nav_home'][1])
    draw_arrow(nodes['nav_home'][0], nodes['nav_home'][1], nodes['home'][0], nodes['home'][1])

    # ROW 2: AR Try-On Flow
    x = start_x
    nodes['ar_home'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Home\nScreen", font_text)
    draw_arrow(nodes['home'][0], nodes['home'][1], nodes['ar_home'][0], nodes['ar_home'][1])
    draw_arrow(nodes['first_time'][0], nodes['first_time'][1] + 40, nodes['ar_home'][0], nodes['ar_home'][1] - 40, 'No')

    x += spacing_x
    nodes['try_on'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Try On", font_text)
    x += spacing_x
    nodes['select_cat'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Select\nCategory", font_text)
    x += spacing_x
    nodes['cat_shown'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Categories\nShown", font_text)
    x += spacing_x
    nodes['select_prod'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Select\nProduct", font_text)
    x += spacing_x
    nodes['prod_list'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Product\nList", font_text)
    x += spacing_x
    nodes['face_detect'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Face\nDetection", font_text)
    x += spacing_x
    nodes['apply'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Apply\nMakeup", font_text)
    x += spacing_x
    nodes['realtime'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Real-time\nAR View", font_text)
    x += spacing_x
    nodes['adjust_q'] = draw_diamond_node(x, y_row2 - 15, box_width, box_height + 30, decision_rgb, "Adjust?", font_text)
    x += spacing_x
    nodes['intensity'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Adjust\nIntensity", font_text)
    x += spacing_x
    nodes['color'] = draw_rounded_box(x, y_row2, box_width, box_height, 10, action_rgb, "Change\nColor", font_text)
    x += spacing_x
    nodes['updated'] = draw_ellipse_node(x, y_row2, box_width, box_height, system_rgb, "Effect\nUpdated", font_text)

    # Draw connections for row 2
    draw_arrow(nodes['ar_home'][0], nodes['ar_home'][1], nodes['try_on'][0], nodes['try_on'][1])
    draw_arrow(nodes['try_on'][0], nodes['try_on'][1], nodes['select_cat'][0], nodes['select_cat'][1])
    draw_arrow(nodes['select_cat'][0], nodes['select_cat'][1], nodes['cat_shown'][0], nodes['cat_shown'][1])
    draw_arrow(nodes['cat_shown'][0], nodes['cat_shown'][1], nodes['select_prod'][0], nodes['select_prod'][1])
    draw_arrow(nodes['select_prod'][0], nodes['select_prod'][1], nodes['prod_list'][0], nodes['prod_list'][1])
    draw_arrow(nodes['prod_list'][0], nodes['prod_list'][1], nodes['face_detect'][0], nodes['face_detect'][1])
    draw_arrow(nodes['face_detect'][0], nodes['face_detect'][1], nodes['apply'][0], nodes['apply'][1])
    draw_arrow(nodes['apply'][0], nodes['apply'][1], nodes['realtime'][0], nodes['realtime'][1])
    draw_arrow(nodes['realtime'][0], nodes['realtime'][1], nodes['adjust_q'][0], nodes['adjust_q'][1])
    draw_arrow(nodes['adjust_q'][0], nodes['adjust_q'][1], nodes['intensity'][0], nodes['intensity'][1], 'Yes')
    draw_arrow(nodes['intensity'][0], nodes['intensity'][1], nodes['color'][0], nodes['color'][1])
    draw_arrow(nodes['color'][0], nodes['color'][1], nodes['updated'][0], nodes['updated'][1])
    draw_arrow(nodes['updated'][0], nodes['updated'][1], nodes['realtime'][0], nodes['realtime'][1])

    # ROW 3: Satisfaction & Capture Flow
    x = start_x
    nodes['satisfied_q'] = draw_diamond_node(x, y_row3 - 15, box_width, box_height + 30, decision_rgb, "Satisfied?", font_text)
    draw_arrow(nodes['adjust_q'][0], nodes['adjust_q'][1] + 50, nodes['satisfied_q'][0], nodes['satisfied_q'][1] - 50, 'No')

    x += spacing_x
    nodes['back_prod'] = draw_rounded_box(x, y_row3 - 60, box_width, box_height, 10, action_rgb, "Back to\nProduct", font_text)
    nodes['capture_q'] = draw_diamond_node(x, y_row3 + 30, box_width, box_height + 30, decision_rgb, "Capture?", font_text)
    x += spacing_x
    nodes['take_photo'] = draw_rounded_box(x, y_row3 - 50, box_width, box_height, 10, action_rgb, "Take\nPhoto", font_text)
    nodes['record'] = draw_rounded_box(x, y_row3 + 40, box_width, box_height, 10, action_rgb, "Record\nVideo", font_text)
    x += spacing_x
    nodes['photo_saved'] = draw_ellipse_node(x, y_row3 - 50, box_width, box_height, system_rgb, "Photo\nSaved", font_text)
    nodes['video_saved'] = draw_ellipse_node(x, y_row3 + 40, box_width, box_height, system_rgb, "Video\nSaved", font_text)
    x += spacing_x
    nodes['share_q'] = draw_diamond_node(x, y_row3 - 15, box_width, box_height + 30, decision_rgb, "Share?", font_text)
    x += spacing_x
    nodes['share_opts'] = draw_rounded_box(x, y_row3 - 50, box_width, box_height, 10, action_rgb, "Share\nOptions", font_text)
    nodes['save_gal'] = draw_rounded_box(x, y_row3 + 40, box_width, box_height, 10, action_rgb, "Save to\nGallery", font_text)
    x += spacing_x
    nodes['shared'] = draw_ellipse_node(x, y_row3 - 50, box_width, box_height, system_rgb, "Shared", font_text)
    x += spacing_x
    nodes['saved_gal'] = draw_ellipse_node(x, y_row3, box_width, box_height, system_rgb, "Saved to\nDevice", font_text)

    # Draw connections for row 3
    draw_arrow(nodes['satisfied_q'][0], nodes['satisfied_q'][1], nodes['back_prod'][0], nodes['back_prod'][1], 'No')
    draw_arrow(nodes['back_prod'][0], nodes['back_prod'][1], nodes['select_prod'][0], nodes['select_prod'][1])
    draw_arrow(nodes['satisfied_q'][0], nodes['satisfied_q'][1], nodes['capture_q'][0], nodes['capture_q'][1], 'Yes')
    draw_arrow(nodes['capture_q'][0], nodes['capture_q'][1], nodes['take_photo'][0], nodes['take_photo'][1], 'Photo')
    draw_arrow(nodes['capture_q'][0], nodes['capture_q'][1], nodes['record'][0], nodes['record'][1], 'Video')
    draw_arrow(nodes['take_photo'][0], nodes['take_photo'][1], nodes['photo_saved'][0], nodes['photo_saved'][1])
    draw_arrow(nodes['record'][0], nodes['record'][1], nodes['video_saved'][0], nodes['video_saved'][1])
    draw_arrow(nodes['photo_saved'][0], nodes['photo_saved'][1], nodes['share_q'][0], nodes['share_q'][1])
    draw_arrow(nodes['video_saved'][0], nodes['video_saved'][1], nodes['share_q'][0], nodes['share_q'][1])
    draw_arrow(nodes['share_q'][0], nodes['share_q'][1], nodes['share_opts'][0], nodes['share_opts'][1], 'Yes')
    draw_arrow(nodes['share_q'][0], nodes['share_q'][1], nodes['save_gal'][0], nodes['save_gal'][1], 'No')
    draw_arrow(nodes['share_opts'][0], nodes['share_opts'][1], nodes['shared'][0], nodes['shared'][1])
    draw_arrow(nodes['shared'][0], nodes['shared'][1], nodes['saved_gal'][0], nodes['saved_gal'][1])
    draw_arrow(nodes['save_gal'][0], nodes['save_gal'][1], nodes['saved_gal'][0], nodes['saved_gal'][1])

    # ROW 4: Purchase Flow
    x = start_x
    nodes['add_cart'] = draw_rounded_box(x, y_row4, box_width, box_height, 10, action_rgb, "Add to\nCart", font_text)
    draw_arrow(nodes['saved_gal'][0], nodes['saved_gal'][1], nodes['add_cart'][0], nodes['add_cart'][1])
    draw_arrow(nodes['capture_q'][0], nodes['capture_q'][1] + 50, nodes['add_cart'][0], nodes['add_cart'][1] - 50, 'Skip')

    x += spacing_x
    nodes['view_prod'] = draw_rounded_box(x, y_row4, box_width, box_height, 10, action_rgb, "View\nProduct", font_text)
    x += spacing_x
    nodes['prod_detail'] = draw_ellipse_node(x, y_row4, box_width, box_height, system_rgb, "Product\nInfo", font_text)
    x += spacing_x
    nodes['buy_q'] = draw_diamond_node(x, y_row4 - 15, box_width, box_height + 30, decision_rgb, "Purchase?", font_text)
    x += spacing_x
    nodes['checkout'] = draw_rounded_box(x, y_row4, box_width, box_height, 10, action_rgb, "Checkout", font_text)
    x += spacing_x
    nodes['payment'] = draw_rounded_box(x, y_row4, box_width, box_height, 10, action_rgb, "Payment", font_text)
    x += spacing_x
    nodes['confirm'] = draw_rounded_box(x, y_row4, box_width, box_height, 10, action_rgb, "Order\nConfirm", font_text)
    x += spacing_x
    nodes['order_placed'] = draw_ellipse_node(x, y_row4, box_width, box_height, system_rgb, "Order\nPlaced", font_text)
    x += spacing_x
    nodes['continue_q'] = draw_diamond_node(x, y_row4 - 15, box_width, box_height + 30, decision_rgb, "Continue?", font_text)

    # Draw connections for row 4
    draw_arrow(nodes['add_cart'][0], nodes['add_cart'][1], nodes['view_prod'][0], nodes['view_prod'][1])
    draw_arrow(nodes['view_prod'][0], nodes['view_prod'][1], nodes['prod_detail'][0], nodes['prod_detail'][1])
    draw_arrow(nodes['prod_detail'][0], nodes['prod_detail'][1], nodes['buy_q'][0], nodes['buy_q'][1])
    draw_arrow(nodes['buy_q'][0], nodes['buy_q'][1], nodes['checkout'][0], nodes['checkout'][1], 'Yes')
    draw_arrow(nodes['checkout'][0], nodes['checkout'][1], nodes['payment'][0], nodes['payment'][1])
    draw_arrow(nodes['payment'][0], nodes['payment'][1], nodes['confirm'][0], nodes['confirm'][1])
    draw_arrow(nodes['confirm'][0], nodes['confirm'][1], nodes['order_placed'][0], nodes['order_placed'][1])
    draw_arrow(nodes['order_placed'][0], nodes['order_placed'][1], nodes['continue_q'][0], nodes['continue_q'][1])
    draw_arrow(nodes['buy_q'][0], nodes['buy_q'][1] + 50, nodes['continue_q'][0], nodes['continue_q'][1] - 50, 'No')

    # ROW 5: Exit Flow
    x = start_x
    nodes['back_home2'] = draw_rounded_box(x, y_row5, box_width, box_height, 10, action_rgb, "Back to\nHome", font_text)
    draw_arrow(nodes['continue_q'][0], nodes['continue_q'][1], nodes['back_home2'][0], nodes['back_home2'][1], 'Yes')
    draw_arrow(nodes['back_home2'][0], nodes['back_home2'][1], nodes['ar_home'][0], nodes['ar_home'][1])

    x += spacing_x * 2
    nodes['exit'] = draw_rounded_box(x, y_row5, box_width, box_height, 10, action_rgb, "Exit App", font_text)
    draw_arrow(nodes['continue_q'][0] + 30, nodes['continue_q'][1] + 50, nodes['exit'][0], nodes['exit'][1] - 30, 'No')

    x += spacing_x
    nodes['end'] = draw_ellipse_node(x, y_row5, box_width, box_height, system_rgb, "End", font_text)
    draw_arrow(nodes['exit'][0], nodes['exit'][1], nodes['end'][0], nodes['end'][1])

    # Add legend
    legend_x = width - 400
    legend_y = 50
    draw.text((legend_x, legend_y), "Legend:", fill=text_rgb, font=font_title)
    draw_rounded_box(legend_x, legend_y + 30, 80, 40, 8, action_rgb, "Action", font_label)
    draw_ellipse_node(legend_x + 100, legend_y + 30, 80, 40, system_rgb, "System", font_label)
    draw_diamond_node(legend_x + 200, legend_y + 25, 80, 50, decision_rgb, "Decision", font_label)

    # Save image
    img = img.crop((0, 0, width, height))
    img.save('/home/user/ui/ar_makeup_user_flow_horizontal.png')
    print("Horizontal multi-row user flow generated successfully!")

if __name__ == '__main__':
    create_horizontal_flow_image()
