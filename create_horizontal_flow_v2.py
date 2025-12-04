#!/usr/bin/env python3
"""
Create horizontal version of AR Makeup User Flow with better layout
"""
from graphviz import Digraph

def create_horizontal_user_flow():
    # Create a new directed graph with left-to-right layout
    dot = Digraph(comment='AR Makeup User Flow - Horizontal', format='png')
    dot.attr(rankdir='LR')  # Left to Right layout
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='11')
    dot.attr('graph', splines='spline', nodesep='0.8', ranksep='1.2', pad='0.8', dpi='150')

    # Define node styles
    action_style = {'fillcolor': '#FFD4A3', 'shape': 'box', 'style': 'rounded,filled', 'width': '1.3', 'height': '0.6'}
    system_style = {'fillcolor': '#C8E6C9', 'shape': 'ellipse', 'style': 'filled', 'width': '1.3', 'height': '0.6'}
    decision_style = {'fillcolor': '#BBDEFB', 'shape': 'diamond', 'style': 'filled', 'width': '1.3', 'height': '0.8'}

    # Start
    dot.node('start', 'Start', **system_style)
    dot.node('open_app', 'Open App', **action_style)
    dot.node('welcome', 'Welcome\nScreen', **action_style)
    dot.node('splash', 'Splash\nScreen', **system_style)
    dot.node('perm_req', 'Permission\nRequest', **action_style)
    dot.node('cam_access', 'Camera\nAccess', **system_style)
    dot.node('first_time', 'First Time\nUser?', **decision_style)

    # Tutorial path
    dot.node('tutorial', 'Tutorial\n(Optional)', **action_style)
    dot.node('skip_tut', 'Skip\nTutorial', **action_style)
    dot.node('view_tut', 'View\nTutorial', **action_style)
    dot.node('tut_shown', 'Tutorial\nShown', **system_style)
    dot.node('tut_comp', 'Tutorial\nComplete', **system_style)
    dot.node('nav_home', 'Navigate to\nHome', **action_style)

    # Direct to home
    dot.node('home', 'Home\nScreen', **system_style)

    # Main AR Experience
    dot.node('ar_home', 'Home\nScreen', **system_style)
    dot.node('try_on', 'Try On', **system_style)
    dot.node('select_cat', 'Select\nCategory', **action_style)
    dot.node('cat_shown', 'Categories\nShown', **system_style)
    dot.node('select_prod', 'Select\nProduct', **action_style)
    dot.node('prod_list', 'Product List\nShown', **system_style)
    dot.node('face_detect', 'Face Detection\n& Tracking', **action_style)
    dot.node('apply_makeup', 'Apply Makeup\nEffect', **action_style)
    dot.node('real_time', 'Real-time\nAR View', **system_style)

    # Adjustment loop
    dot.node('adjust', 'Adjust?', **decision_style)
    dot.node('intensity', 'Adjust\nIntensity', **action_style)
    dot.node('color', 'Change\nColor', **action_style)
    dot.node('updated', 'Effect\nUpdated', **system_style)

    # Satisfaction check
    dot.node('satisfied', 'Satisfied?', **decision_style)
    dot.node('back_prod', 'Back to\nProduct', **action_style)

    # Capture flow
    dot.node('capture', 'Capture/\nRecord?', **decision_style)
    dot.node('take_photo', 'Take\nPhoto', **action_style)
    dot.node('record_video', 'Record\nVideo', **action_style)
    dot.node('photo_saved', 'Photo\nSaved', **system_style)
    dot.node('video_saved', 'Video\nSaved', **system_style)

    # Share flow
    dot.node('share_q', 'Share?', **decision_style)
    dot.node('share_opts', 'Share\nOptions', **action_style)
    dot.node('shared', 'Shared to\nSocial Media', **system_style)
    dot.node('save_gal', 'Save to\nGallery', **action_style)
    dot.node('saved_gal', 'Saved to\nDevice', **system_style)

    # Purchase flow
    dot.node('add_cart', 'Add to\nCart', **action_style)
    dot.node('view_prod', 'View Product\nDetails', **action_style)
    dot.node('prod_detail', 'Product Info\nShown', **system_style)
    dot.node('buy_q', 'Purchase?', **decision_style)
    dot.node('checkout', 'Checkout\nProcess', **action_style)
    dot.node('payment', 'Payment\nGateway', **action_style)
    dot.node('confirm', 'Order\nConfirmation', **action_style)
    dot.node('order_placed', 'Order\nPlaced', **system_style)

    # Continue browsing
    dot.node('continue_q', 'Continue\nBrowsing?', **decision_style)
    dot.node('back_home', 'Back to\nHome', **action_style)

    # Exit
    dot.node('exit', 'Exit App', **action_style)
    dot.node('end', 'End', **system_style)

    # Connect the nodes - Onboarding
    dot.edge('start', 'open_app')
    dot.edge('open_app', 'welcome')
    dot.edge('welcome', 'splash')
    dot.edge('splash', 'perm_req')
    dot.edge('perm_req', 'cam_access')
    dot.edge('cam_access', 'first_time')

    dot.edge('first_time', 'tutorial', xlabel='Yes')
    dot.edge('first_time', 'home', xlabel='No')
    dot.edge('tutorial', 'skip_tut')
    dot.edge('tutorial', 'view_tut')
    dot.edge('skip_tut', 'tut_comp')
    dot.edge('view_tut', 'tut_shown')
    dot.edge('tut_shown', 'tut_comp')
    dot.edge('tut_comp', 'nav_home')
    dot.edge('nav_home', 'ar_home')
    dot.edge('home', 'ar_home')

    # AR Experience connections
    dot.edge('ar_home', 'try_on')
    dot.edge('try_on', 'select_cat')
    dot.edge('select_cat', 'cat_shown')
    dot.edge('cat_shown', 'select_prod')
    dot.edge('select_prod', 'prod_list')
    dot.edge('prod_list', 'face_detect')
    dot.edge('face_detect', 'apply_makeup')
    dot.edge('apply_makeup', 'real_time')
    dot.edge('real_time', 'adjust')

    dot.edge('adjust', 'intensity', xlabel='Yes')
    dot.edge('adjust', 'satisfied', xlabel='No')
    dot.edge('intensity', 'color')
    dot.edge('color', 'updated')
    dot.edge('updated', 'real_time')

    dot.edge('satisfied', 'back_prod', xlabel='No')
    dot.edge('satisfied', 'capture', xlabel='Yes')
    dot.edge('back_prod', 'select_prod')

    dot.edge('capture', 'take_photo', xlabel='Photo')
    dot.edge('capture', 'record_video', xlabel='Video')
    dot.edge('capture', 'add_cart', xlabel='Skip')

    dot.edge('take_photo', 'photo_saved')
    dot.edge('record_video', 'video_saved')
    dot.edge('photo_saved', 'share_q')
    dot.edge('video_saved', 'share_q')

    dot.edge('share_q', 'share_opts', xlabel='Yes')
    dot.edge('share_q', 'save_gal', xlabel='No')
    dot.edge('share_opts', 'shared')
    dot.edge('shared', 'save_gal')
    dot.edge('save_gal', 'saved_gal')
    dot.edge('saved_gal', 'add_cart')

    dot.edge('add_cart', 'view_prod')
    dot.edge('view_prod', 'prod_detail')
    dot.edge('prod_detail', 'buy_q')

    dot.edge('buy_q', 'checkout', xlabel='Yes')
    dot.edge('buy_q', 'continue_q', xlabel='No')

    dot.edge('checkout', 'payment')
    dot.edge('payment', 'confirm')
    dot.edge('confirm', 'order_placed')
    dot.edge('order_placed', 'continue_q')

    dot.edge('continue_q', 'back_home', xlabel='Yes')
    dot.edge('continue_q', 'exit', xlabel='No')
    dot.edge('back_home', 'ar_home')

    dot.edge('exit', 'end')

    return dot

if __name__ == '__main__':
    dot = create_horizontal_user_flow()
    dot.render('/home/user/ui/ar_makeup_user_flow_horizontal', cleanup=True)
    print("Horizontal user flow generated: ar_makeup_user_flow_horizontal.png")
