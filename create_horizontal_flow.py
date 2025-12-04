#!/usr/bin/env python3
"""
Create horizontal version of AR Makeup User Flow
"""
from graphviz import Digraph

def create_horizontal_user_flow():
    # Create a new directed graph with left-to-right layout
    dot = Digraph(comment='AR Makeup User Flow - Horizontal', format='png')
    dot.attr(rankdir='LR')  # Left to Right layout
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')
    dot.attr('graph', splines='ortho', nodesep='0.5', ranksep='0.8', pad='0.5')

    # Define node styles
    action_style = {'fillcolor': '#FFD4A3', 'shape': 'box', 'style': 'rounded,filled'}
    system_style = {'fillcolor': '#C8E6C9', 'shape': 'ellipse', 'style': 'filled'}
    decision_style = {'fillcolor': '#BBDEFB', 'shape': 'diamond', 'style': 'filled'}

    # Start
    dot.node('start', 'Start', **system_style)

    # Onboarding flow
    dot.node('open_app', 'Open App', **action_style)
    dot.node('welcome', 'Welcome\nScreen', **action_style)
    dot.node('splash', 'Splash Screen', **system_style)
    dot.node('perm_req', 'Permission\nRequest', **action_style)
    dot.node('cam_access', 'Camera\nAccess', **system_style)
    dot.node('tutorial', 'Tutorial\n(Optional)', **action_style)
    dot.node('home', 'Home Screen', **system_style)

    # Decision: First time user
    dot.node('first_time', 'First Time\nUser?', **decision_style)

    # Branches
    dot.node('skip_tut', 'Skip Tutorial', **action_style)
    dot.node('view_tut', 'View Tutorial', **action_style)
    dot.node('tut_shown', 'Tutorial\nShown', **system_style)
    dot.node('tut_comp', 'Tutorial\nComplete', **system_style)
    dot.node('nav_home', 'Navigate to\nHome', **action_style)

    # Main AR Experience (will be in a subgraph/cluster)
    with dot.subgraph(name='cluster_ar_exp') as ar:
        ar.attr(label='AR Makeup Experience', style='dashed', color='gray')

        ar.node('ar_home', 'Home Screen', **system_style)
        ar.node('try_on', 'Try On', **system_style)
        ar.node('select_cat', 'Select\nCategory', **action_style)
        ar.node('select_prod', 'Select\nProduct', **action_style)
        ar.node('cat_shown', 'Categories\nShown', **system_style)
        ar.node('prod_list', 'Product List\nShown', **system_style)

        ar.node('face_detect', 'Face Detection\n& Tracking', **action_style)
        ar.node('apply_makeup', 'Apply Makeup\nEffect', **action_style)
        ar.node('real_time', 'Real-time AR\nView', **system_style)

        ar.node('adjust', 'Adjust?', **decision_style)
        ar.node('intensity', 'Adjust\nIntensity', **action_style)
        ar.node('color', 'Change\nColor', **action_style)
        ar.node('updated', 'Effect\nUpdated', **system_style)

        ar.node('satisfied', 'Satisfied?', **decision_style)
        ar.node('back_prod', 'Back to Product\nSelection', **action_style)

        ar.node('capture', 'Capture/Record?', **decision_style)
        ar.node('take_photo', 'Take Photo', **action_style)
        ar.node('record_video', 'Record Video', **action_style)
        ar.node('photo_saved', 'Photo Saved', **system_style)
        ar.node('video_saved', 'Video Saved', **system_style)

        ar.node('share_q', 'Share?', **decision_style)
        ar.node('share_opts', 'Share Options', **action_style)
        ar.node('shared', 'Shared to\nSocial Media', **system_style)

        ar.node('save_gal', 'Save to\nGallery', **action_style)
        ar.node('saved_gal', 'Saved to\nDevice', **system_style)

        ar.node('add_cart', 'Add to Cart', **action_style)
        ar.node('view_prod', 'View Product\nDetails', **action_style)
        ar.node('prod_detail', 'Product Info\nShown', **system_style)
        ar.node('buy_q', 'Purchase?', **decision_style)

        ar.node('checkout', 'Checkout\nProcess', **action_style)
        ar.node('payment', 'Payment\nGateway', **action_style)
        ar.node('confirm', 'Order\nConfirmation', **action_style)
        ar.node('order_placed', 'Order Placed', **system_style)

        ar.node('continue_q', 'Continue\nBrowsing?', **decision_style)
        ar.node('back_home', 'Back to Home', **action_style)

    dot.node('exit', 'Exit App', **action_style)
    dot.node('end', 'End', **system_style)

    # Connect the nodes - Onboarding
    dot.edge('start', 'open_app')
    dot.edge('open_app', 'welcome')
    dot.edge('welcome', 'splash')
    dot.edge('splash', 'perm_req')
    dot.edge('perm_req', 'cam_access')
    dot.edge('cam_access', 'first_time')

    dot.edge('first_time', 'tutorial', label='Yes')
    dot.edge('first_time', 'home', label='No')
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

    dot.edge('adjust', 'intensity', label='Yes')
    dot.edge('adjust', 'satisfied', label='No')
    dot.edge('intensity', 'color')
    dot.edge('color', 'updated')
    dot.edge('updated', 'real_time')

    dot.edge('satisfied', 'back_prod', label='No')
    dot.edge('satisfied', 'capture', label='Yes')
    dot.edge('back_prod', 'select_prod')

    dot.edge('capture', 'take_photo', label='Photo')
    dot.edge('capture', 'record_video', label='Video')
    dot.edge('capture', 'add_cart', label='Skip')

    dot.edge('take_photo', 'photo_saved')
    dot.edge('record_video', 'video_saved')
    dot.edge('photo_saved', 'share_q')
    dot.edge('video_saved', 'share_q')

    dot.edge('share_q', 'share_opts', label='Yes')
    dot.edge('share_q', 'save_gal', label='No')
    dot.edge('share_opts', 'shared')
    dot.edge('shared', 'save_gal')
    dot.edge('save_gal', 'saved_gal')
    dot.edge('saved_gal', 'add_cart')

    dot.edge('add_cart', 'view_prod')
    dot.edge('view_prod', 'prod_detail')
    dot.edge('prod_detail', 'buy_q')

    dot.edge('buy_q', 'checkout', label='Yes')
    dot.edge('buy_q', 'continue_q', label='No')

    dot.edge('checkout', 'payment')
    dot.edge('payment', 'confirm')
    dot.edge('confirm', 'order_placed')
    dot.edge('order_placed', 'continue_q')

    dot.edge('continue_q', 'back_home', label='Yes')
    dot.edge('continue_q', 'exit', label='No')
    dot.edge('back_home', 'ar_home')

    dot.edge('exit', 'end')

    return dot

if __name__ == '__main__':
    dot = create_horizontal_user_flow()
    dot.render('/home/user/ui/ar_makeup_user_flow_horizontal', cleanup=True)
    print("Horizontal user flow generated: ar_makeup_user_flow_horizontal.png")
