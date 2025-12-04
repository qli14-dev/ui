#!/usr/bin/env python3
"""
Create horizontal version of AR Makeup User Flow with multi-row layout
"""
from graphviz import Digraph

def create_horizontal_user_flow():
    # Create a new directed graph
    dot = Digraph(comment='AR Makeup User Flow - Horizontal', format='png')
    dot.attr(rankdir='LR')  # Left to Right layout
    dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='12')
    dot.attr('graph', splines='polyline', nodesep='0.6', ranksep='1.5', pad='0.5', dpi='150', size='20,10!')

    # Define node styles
    action_style = {'fillcolor': '#FFD4A3', 'shape': 'box', 'style': 'rounded,filled', 'width': '1.5', 'height': '0.7'}
    system_style = {'fillcolor': '#C8E6C9', 'shape': 'ellipse', 'style': 'filled', 'width': '1.5', 'height': '0.7'}
    decision_style = {'fillcolor': '#BBDEFB', 'shape': 'diamond', 'style': 'filled', 'width': '1.5', 'height': '0.9'}

    # Use subgraphs to control layout by rank (left to right position)

    # Rank 0: Start
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('start', 'Start', **system_style)

    # Rank 1: Onboarding begins
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('open_app', 'Open App', **action_style)

    # Rank 2
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('welcome', 'Welcome\nScreen', **action_style)

    # Rank 3
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('splash', 'Splash\nScreen', **system_style)

    # Rank 4
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('perm_req', 'Permission\nRequest', **action_style)

    # Rank 5
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('cam_access', 'Camera\nAccess', **system_style)

    # Rank 6
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('first_time', 'First Time\nUser?', **decision_style)

    # Rank 7 - Tutorial branch
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('tutorial', 'Tutorial\n(Optional)', **action_style)
        s.node('home', 'Home\nScreen', **system_style)

    # Rank 8
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('skip_tut', 'Skip\nTutorial', **action_style)
        s.node('view_tut', 'View\nTutorial', **action_style)

    # Rank 9
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('tut_comp', 'Tutorial\nComplete', **system_style)
        s.node('tut_shown', 'Tutorial\nShown', **system_style)

    # Rank 10
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('nav_home', 'Navigate\nto Home', **action_style)

    # Rank 11 - AR Experience begins
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('ar_home', 'Home\nScreen', **system_style)

    # Rank 12
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('try_on', 'Try On', **system_style)

    # Rank 13
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('select_cat', 'Select\nCategory', **action_style)

    # Rank 14
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('cat_shown', 'Categories\nShown', **system_style)

    # Rank 15
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('select_prod', 'Select\nProduct', **action_style)

    # Rank 16
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('prod_list', 'Product List\nShown', **system_style)

    # Rank 17
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('face_detect', 'Face Detection\n& Tracking', **action_style)

    # Rank 18
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('apply_makeup', 'Apply Makeup\nEffect', **action_style)

    # Rank 19
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('real_time', 'Real-time\nAR View', **system_style)

    # Rank 20
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('adjust', 'Adjust?', **decision_style)

    # Rank 21 - Adjustment path
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('intensity', 'Adjust\nIntensity', **action_style)
        s.node('satisfied', 'Satisfied?', **decision_style)

    # Rank 22
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('color', 'Change\nColor', **action_style)
        s.node('back_prod', 'Back to\nProduct', **action_style)
        s.node('capture', 'Capture/\nRecord?', **decision_style)

    # Rank 23
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('updated', 'Effect\nUpdated', **system_style)
        s.node('take_photo', 'Take\nPhoto', **action_style)
        s.node('record_video', 'Record\nVideo', **action_style)
        s.node('add_cart', 'Add to\nCart', **action_style)

    # Rank 24
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('photo_saved', 'Photo\nSaved', **system_style)
        s.node('video_saved', 'Video\nSaved', **system_style)

    # Rank 25
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('share_q', 'Share?', **decision_style)

    # Rank 26
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('share_opts', 'Share\nOptions', **action_style)
        s.node('save_gal', 'Save to\nGallery', **action_style)

    # Rank 27
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('shared', 'Shared to\nSocial Media', **system_style)

    # Rank 28
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('saved_gal', 'Saved to\nDevice', **system_style)

    # Rank 29
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('view_prod', 'View Product\nDetails', **action_style)

    # Rank 30
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('prod_detail', 'Product Info\nShown', **system_style)

    # Rank 31
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('buy_q', 'Purchase?', **decision_style)

    # Rank 32
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('checkout', 'Checkout\nProcess', **action_style)
        s.node('continue_q', 'Continue\nBrowsing?', **decision_style)

    # Rank 33
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('payment', 'Payment\nGateway', **action_style)
        s.node('back_home', 'Back to\nHome', **action_style)
        s.node('exit', 'Exit App', **action_style)

    # Rank 34
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('confirm', 'Order\nConfirmation', **action_style)

    # Rank 35
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('order_placed', 'Order\nPlaced', **system_style)

    # Rank 36
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node('end', 'End', **system_style)

    # Connect all nodes
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
