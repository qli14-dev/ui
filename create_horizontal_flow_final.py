#!/usr/bin/env python3
"""
Create horizontal version of AR Makeup User Flow with wide canvas
"""
from graphviz import Digraph

def create_horizontal_user_flow():
    # Create a new directed graph
    dot = Digraph(comment='AR Makeup User Flow - Horizontal', format='png', engine='dot')
    dot.attr(rankdir='LR')  # Left to Right layout
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='14', margin='0.3,0.2')
    dot.attr('graph', splines='ortho', nodesep='1.0', ranksep='2.5', pad='1.0', dpi='96')
    dot.attr('edge', fontsize='11')

    # Define node styles with larger sizes
    action_style = {'fillcolor': '#FFD4A3', 'shape': 'box', 'style': 'rounded,filled', 'width': '2.0', 'height': '0.8'}
    system_style = {'fillcolor': '#C8E6C9', 'shape': 'ellipse', 'style': 'filled', 'width': '2.0', 'height': '0.8'}
    decision_style = {'fillcolor': '#BBDEFB', 'shape': 'diamond', 'style': 'filled', 'width': '2.2', 'height': '1.2'}

    # Create all nodes
    # Row 1 - Onboarding
    dot.node('start', 'Start', **system_style)
    dot.node('open_app', 'Open App', **action_style)
    dot.node('welcome', 'Welcome Screen', **action_style)
    dot.node('splash', 'Splash Screen', **system_style)
    dot.node('perm_req', 'Permission Request', **action_style)
    dot.node('cam_access', 'Camera Access', **system_style)
    dot.node('first_time', 'First Time User?', **decision_style)

    # Tutorial path
    dot.node('tutorial', 'Tutorial (Optional)', **action_style)
    dot.node('skip_tut', 'Skip Tutorial', **action_style)
    dot.node('view_tut', 'View Tutorial', **action_style)
    dot.node('tut_shown', 'Tutorial Shown', **system_style)
    dot.node('tut_comp', 'Tutorial Complete', **system_style)
    dot.node('nav_home', 'Navigate to Home', **action_style)
    dot.node('home', 'Home Screen', **system_style)

    # AR Experience
    dot.node('ar_home', 'Home Screen', **system_style)
    dot.node('try_on', 'Try On', **system_style)
    dot.node('select_cat', 'Select Category', **action_style)
    dot.node('cat_shown', 'Categories Shown', **system_style)
    dot.node('select_prod', 'Select Product', **action_style)
    dot.node('prod_list', 'Product List Shown', **system_style)
    dot.node('face_detect', 'Face Detection & Tracking', **action_style)
    dot.node('apply_makeup', 'Apply Makeup Effect', **action_style)
    dot.node('real_time', 'Real-time AR View', **system_style)

    # Adjustment
    dot.node('adjust', 'Adjust?', **decision_style)
    dot.node('intensity', 'Adjust Intensity', **action_style)
    dot.node('color', 'Change Color', **action_style)
    dot.node('updated', 'Effect Updated', **system_style)

    # Satisfaction
    dot.node('satisfied', 'Satisfied?', **decision_style)
    dot.node('back_prod', 'Back to Product', **action_style)

    # Capture
    dot.node('capture', 'Capture/Record?', **decision_style)
    dot.node('take_photo', 'Take Photo', **action_style)
    dot.node('record_video', 'Record Video', **action_style)
    dot.node('photo_saved', 'Photo Saved', **system_style)
    dot.node('video_saved', 'Video Saved', **system_style)

    # Share
    dot.node('share_q', 'Share?', **decision_style)
    dot.node('share_opts', 'Share Options', **action_style)
    dot.node('shared', 'Shared to Social Media', **system_style)
    dot.node('save_gal', 'Save to Gallery', **action_style)
    dot.node('saved_gal', 'Saved to Device', **system_style)

    # Purchase
    dot.node('add_cart', 'Add to Cart', **action_style)
    dot.node('view_prod', 'View Product Details', **action_style)
    dot.node('prod_detail', 'Product Info Shown', **system_style)
    dot.node('buy_q', 'Purchase?', **decision_style)
    dot.node('checkout', 'Checkout Process', **action_style)
    dot.node('payment', 'Payment Gateway', **action_style)
    dot.node('confirm', 'Order Confirmation', **action_style)
    dot.node('order_placed', 'Order Placed', **system_style)

    # Continue
    dot.node('continue_q', 'Continue Browsing?', **decision_style)
    dot.node('back_home', 'Back to Home', **action_style)

    # Exit
    dot.node('exit', 'Exit App', **action_style)
    dot.node('end', 'End', **system_style)

    # Connect nodes - Main flow
    edges = [
        ('start', 'open_app', ''),
        ('open_app', 'welcome', ''),
        ('welcome', 'splash', ''),
        ('splash', 'perm_req', ''),
        ('perm_req', 'cam_access', ''),
        ('cam_access', 'first_time', ''),
        ('first_time', 'tutorial', 'Yes'),
        ('first_time', 'home', 'No'),
        ('tutorial', 'skip_tut', ''),
        ('tutorial', 'view_tut', ''),
        ('skip_tut', 'tut_comp', ''),
        ('view_tut', 'tut_shown', ''),
        ('tut_shown', 'tut_comp', ''),
        ('tut_comp', 'nav_home', ''),
        ('nav_home', 'ar_home', ''),
        ('home', 'ar_home', ''),
        ('ar_home', 'try_on', ''),
        ('try_on', 'select_cat', ''),
        ('select_cat', 'cat_shown', ''),
        ('cat_shown', 'select_prod', ''),
        ('select_prod', 'prod_list', ''),
        ('prod_list', 'face_detect', ''),
        ('face_detect', 'apply_makeup', ''),
        ('apply_makeup', 'real_time', ''),
        ('real_time', 'adjust', ''),
        ('adjust', 'intensity', 'Yes'),
        ('adjust', 'satisfied', 'No'),
        ('intensity', 'color', ''),
        ('color', 'updated', ''),
        ('updated', 'real_time', ''),
        ('satisfied', 'back_prod', 'No'),
        ('satisfied', 'capture', 'Yes'),
        ('back_prod', 'select_prod', ''),
        ('capture', 'take_photo', 'Photo'),
        ('capture', 'record_video', 'Video'),
        ('capture', 'add_cart', 'Skip'),
        ('take_photo', 'photo_saved', ''),
        ('record_video', 'video_saved', ''),
        ('photo_saved', 'share_q', ''),
        ('video_saved', 'share_q', ''),
        ('share_q', 'share_opts', 'Yes'),
        ('share_q', 'save_gal', 'No'),
        ('share_opts', 'shared', ''),
        ('shared', 'save_gal', ''),
        ('save_gal', 'saved_gal', ''),
        ('saved_gal', 'add_cart', ''),
        ('add_cart', 'view_prod', ''),
        ('view_prod', 'prod_detail', ''),
        ('prod_detail', 'buy_q', ''),
        ('buy_q', 'checkout', 'Yes'),
        ('buy_q', 'continue_q', 'No'),
        ('checkout', 'payment', ''),
        ('payment', 'confirm', ''),
        ('confirm', 'order_placed', ''),
        ('order_placed', 'continue_q', ''),
        ('continue_q', 'back_home', 'Yes'),
        ('continue_q', 'exit', 'No'),
        ('back_home', 'ar_home', ''),
        ('exit', 'end', ''),
    ]

    for src, dst, label in edges:
        if label:
            dot.edge(src, dst, label=label)
        else:
            dot.edge(src, dst)

    return dot

if __name__ == '__main__':
    dot = create_horizontal_user_flow()
    # Save the source for inspection
    dot.save('/home/user/ui/ar_makeup_user_flow_horizontal.gv')
    # Render to PNG
    dot.render('/home/user/ui/ar_makeup_user_flow_horizontal', cleanup=True)
    print("Horizontal user flow generated: ar_makeup_user_flow_horizontal.png")
