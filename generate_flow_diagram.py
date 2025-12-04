#!/usr/bin/env python3
from graphviz import Digraph

# Create the main user flow diagram
def create_ar_makeup_flow():
    dot = Digraph(comment='AR Makeup App User Flow', format='png')
    dot.attr(rankdir='TB', size='16,20', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='11')
    dot.attr('edge', fontname='Arial', fontsize='9')

    # Define node styles
    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2'}

    # ONBOARDING FLOW
    dot.node('start', 'Open app', **action_style)
    dot.node('splash', 'Splash\nscreen', **screen_style)
    dot.node('welcome', 'Welcome\nscreen', **screen_style)
    dot.node('get_started', 'Tap Get\nStarted', **action_style)
    dot.node('lang', 'Language\nselection', **screen_style)
    dot.node('select_lang', 'Select\nlanguage', **action_style)
    dot.node('privacy', 'Privacy\nnotice', **screen_style)
    dot.node('accept_privacy', 'Accept\nprivacy', **action_style)
    dot.node('cam_perm', 'Camera\npermission?', **decision_style)
    dot.node('quiz', 'Onboarding\nquiz', **screen_style)
    dot.node('perm_warn', 'Permission\nwarning', **screen_style)
    dot.node('go_settings', 'Go to\nsettings', **action_style)
    dot.node('answer_quiz', 'Answer\nquestions', **action_style)
    dot.node('save_pref', 'Save\npreferences', **action_style)
    dot.node('home', 'Home\nscreen', **screen_style)

    # Onboarding edges
    dot.edge('start', 'splash')
    dot.edge('splash', 'welcome')
    dot.edge('welcome', 'get_started')
    dot.edge('get_started', 'lang')
    dot.edge('lang', 'select_lang')
    dot.edge('select_lang', 'privacy')
    dot.edge('privacy', 'accept_privacy')
    dot.edge('accept_privacy', 'cam_perm')
    dot.edge('cam_perm', 'quiz', label='Allow')
    dot.edge('cam_perm', 'perm_warn', label='Deny')
    dot.edge('perm_warn', 'go_settings')
    dot.edge('go_settings', 'cam_perm', style='dashed')
    dot.edge('quiz', 'answer_quiz')
    dot.edge('answer_quiz', 'save_pref')
    dot.edge('save_pref', 'home')

    # HOME NAVIGATION
    dot.node('start_ar', 'Tap Start\nAR Makeup', **action_style)
    dot.node('view_tutorials', 'Open\ntutorials', **action_style)
    dot.node('view_saved', 'Open saved\nlooks', **action_style)
    dot.node('open_store', 'Open\nstore', **action_style)

    dot.edge('home', 'start_ar')
    dot.edge('home', 'view_tutorials')
    dot.edge('home', 'view_saved')
    dot.edge('home', 'open_store')

    # AR CORE FLOW
    dot.node('cam_activate', 'Camera\nactivation', **screen_style)
    dot.node('face_guide', 'Face alignment\nguide', **screen_style)
    dot.node('align_face', 'Align face\nwith guide', **action_style)
    dot.node('face_detect', 'Face\ndetected?', **decision_style)
    dot.node('retry_warn', 'Retry\nwarning', **screen_style)
    dot.node('retry', 'Retry\ndetection', **action_style)
    dot.node('scene', 'Scene\nselection', **screen_style)

    dot.edge('start_ar', 'cam_activate')
    dot.edge('cam_activate', 'face_guide')
    dot.edge('face_guide', 'align_face')
    dot.edge('align_face', 'face_detect')
    dot.edge('face_detect', 'scene', label='Y')
    dot.edge('face_detect', 'retry_warn', label='N')
    dot.edge('retry_warn', 'retry')
    dot.edge('retry', 'align_face', style='dashed')

    # SCENE SELECTION
    dot.node('select_scene', 'Select scene:\nDaily/Date/\nInterview/Creative', **action_style)
    dot.node('look_lib', 'Look\nlibrary', **screen_style)
    dot.node('choose_look_type', 'Choose\ntemplate or\ncustom?', **decision_style)
    dot.node('select_template', 'Select\ntemplate', **action_style)
    dot.node('start_custom', 'Start\ncustom', **action_style)

    dot.edge('scene', 'select_scene')
    dot.edge('select_scene', 'look_lib')
    dot.edge('look_lib', 'choose_look_type')
    dot.edge('choose_look_type', 'select_template', label='Template')
    dot.edge('choose_look_type', 'start_custom', label='Custom')

    # AR MAKEUP STEPS
    dot.node('ar_flow', 'AR makeup\nflow', **screen_style)
    dot.node('step0', 'Step 0:\nPreparation', **screen_style)
    dot.node('step1', 'Step 1:\nBase', **screen_style)
    dot.node('step2', 'Step 2:\nBrows', **screen_style)
    dot.node('step3', 'Step 3:\nEyes', **screen_style)
    dot.node('step4', 'Step 4:\nBlush', **screen_style)
    dot.node('step5', 'Step 5:\nLips', **screen_style)
    dot.node('step6', 'Step 6:\nFinal touch', **screen_style)
    dot.node('apply_makeup', 'Apply makeup\nat each step', **action_style)

    dot.edge('select_template', 'ar_flow')
    dot.edge('start_custom', 'ar_flow')
    dot.edge('ar_flow', 'step0')
    dot.edge('step0', 'step1')
    dot.edge('step1', 'step2')
    dot.edge('step2', 'step3')
    dot.edge('step3', 'step4')
    dot.edge('step4', 'step5')
    dot.edge('step5', 'step6')
    dot.edge('step6', 'apply_makeup')

    # FINAL PREVIEW
    dot.node('final_preview', 'Final\npreview', **screen_style)
    dot.node('before_after', 'Before/After\nslider', **screen_style)
    dot.node('choose_action', 'Choose\naction?', **decision_style)

    dot.edge('apply_makeup', 'final_preview')
    dot.edge('final_preview', 'before_after')
    dot.edge('before_after', 'choose_action')

    # FINAL ACTIONS
    dot.node('save_look', 'Tap Save\nLook', **action_style)
    dot.node('share_look', 'Tap Share', **action_style)
    dot.node('view_products', 'Tap View\nProducts', **action_style)
    dot.node('try_another', 'Tap Try\nAnother Look', **action_style)

    dot.edge('choose_action', 'save_look')
    dot.edge('choose_action', 'share_look')
    dot.edge('choose_action', 'view_products')
    dot.edge('choose_action', 'try_another')

    # SAVE FLOW
    dot.node('save_screen', 'Save look\nscreen', **screen_style)
    dot.node('name_look', 'Enter look\nname', **action_style)
    dot.node('add_tags', 'Add tags', **action_style)
    dot.node('confirm_save', 'Tap Save', **action_style)
    dot.node('auth_check', 'Authenticated?', **decision_style)
    dot.node('auth_screen', 'Auth\nscreen', **screen_style)
    dot.node('save_success', 'Save\nsuccessful', **screen_style)

    dot.edge('save_look', 'save_screen')
    dot.edge('save_screen', 'name_look')
    dot.edge('name_look', 'add_tags')
    dot.edge('add_tags', 'confirm_save')
    dot.edge('confirm_save', 'auth_check')
    dot.edge('auth_check', 'save_success', label='Y')
    dot.edge('auth_check', 'auth_screen', label='N')
    dot.edge('auth_screen', 'save_success', style='dashed')
    dot.edge('save_success', 'home', style='dashed')

    # SHARE FLOW
    dot.node('share_screen', 'Share\noptions', **screen_style)
    dot.node('media_type', 'Image or\nvideo?', **decision_style)
    dot.node('gen_image', 'Generate\nimage', **action_style)
    dot.node('gen_video', 'Generate\nvideo', **action_style)
    dot.node('share_panel', 'Share\npanel', **screen_style)
    dot.node('share_to', 'Share to\nplatform', **action_style)

    dot.edge('share_look', 'share_screen')
    dot.edge('share_screen', 'media_type')
    dot.edge('media_type', 'gen_image', label='Image')
    dot.edge('media_type', 'gen_video', label='Video')
    dot.edge('gen_image', 'share_panel')
    dot.edge('gen_video', 'share_panel')
    dot.edge('share_panel', 'share_to')
    dot.edge('share_to', 'home', style='dashed')

    # PRODUCT FLOW
    dot.node('product_list', 'Product\nlist', **screen_style)
    dot.node('select_product', 'Select\nproduct', **action_style)
    dot.node('product_detail', 'Product\ndetail', **screen_style)
    dot.node('product_action', 'Try in AR\nor purchase?', **decision_style)
    dot.node('try_ar', 'Tap Try\nin AR', **action_style)
    dot.node('add_cart', 'Add to\ncart', **action_style)
    dot.node('checkout', 'Checkout\nscreen', **screen_style)
    dot.node('payment', 'Payment', **action_style)
    dot.node('order_confirm', 'Order\nconfirmation', **screen_style)

    dot.edge('view_products', 'product_list')
    dot.edge('open_store', 'product_list')
    dot.edge('product_list', 'select_product')
    dot.edge('select_product', 'product_detail')
    dot.edge('product_detail', 'product_action')
    dot.edge('product_action', 'try_ar', label='Try AR')
    dot.edge('product_action', 'add_cart', label='Purchase')
    dot.edge('try_ar', 'step1', style='dashed')
    dot.edge('add_cart', 'checkout')
    dot.edge('checkout', 'payment')
    dot.edge('payment', 'order_confirm')
    dot.edge('order_confirm', 'home', style='dashed')

    # TRY ANOTHER
    dot.edge('try_another', 'scene', style='dashed')

    # TUTORIALS FLOW
    dot.node('tutorial_list', 'Tutorial\nlist', **screen_style)
    dot.node('select_tutorial', 'Select\ntutorial', **action_style)
    dot.node('tutorial_type', 'Video or\nAR tutorial?', **decision_style)
    dot.node('video_tutorial', 'Video\ntutorial', **screen_style)
    dot.node('ar_tutorial', 'AR\ntutorial', **screen_style)
    dot.node('try_this_look', 'Try this\nlook', **action_style)

    dot.edge('view_tutorials', 'tutorial_list')
    dot.edge('tutorial_list', 'select_tutorial')
    dot.edge('select_tutorial', 'tutorial_type')
    dot.edge('tutorial_type', 'video_tutorial', label='Video')
    dot.edge('tutorial_type', 'ar_tutorial', label='AR')
    dot.edge('video_tutorial', 'try_this_look')
    dot.edge('ar_tutorial', 'try_this_look')
    dot.edge('try_this_look', 'scene', style='dashed')

    # SAVED LOOKS
    dot.node('auth_check2', 'Authenticated?', **decision_style)
    dot.node('my_saved', 'My saved\nlooks', **screen_style)
    dot.node('select_saved', 'Select\nsaved look', **action_style)
    dot.node('reapply', 'Tap Reapply\nLook', **action_style)

    dot.edge('view_saved', 'auth_check2')
    dot.edge('auth_check2', 'my_saved', label='Y')
    dot.edge('auth_check2', 'auth_screen', label='N')
    dot.edge('my_saved', 'select_saved')
    dot.edge('select_saved', 'reapply')
    dot.edge('reapply', 'ar_flow', style='dashed')

    return dot

# Generate the diagram
flow = create_ar_makeup_flow()
flow.render('/home/user/ui/ar_makeup_user_flow', cleanup=True)
print("✓ Main user flow diagram generated: ar_makeup_user_flow.png")

# Create a simplified core flow
def create_simplified_flow():
    dot = Digraph(comment='AR Makeup Core Flow', format='png')
    dot.attr(rankdir='TB', size='12,16', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='12')
    dot.attr('edge', fontname='Arial', fontsize='10')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2.5', 'width': '1.5'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2.5', 'width': '1.5', 'height': '0.8'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2.5', 'width': '1.8'}

    # Main flow
    dot.node('1', 'Open app', **action_style)
    dot.node('2', 'Splash &\nWelcome', **screen_style)
    dot.node('3', 'Accept privacy\n& camera', **action_style)
    dot.node('4', 'Onboarding\nquiz', **screen_style)
    dot.node('5', 'Answer\nquestions', **action_style)
    dot.node('6', 'Home screen', **screen_style)
    dot.node('7', 'Start AR\nMakeup', **action_style)
    dot.node('8', 'Face\ndetection', **screen_style)
    dot.node('9', 'Face found?', **decision_style)
    dot.node('10', 'Scene\nselection', **screen_style)
    dot.node('11', 'Select scene\n& look', **action_style)
    dot.node('12', 'AR makeup\nsteps 0-6', **screen_style)
    dot.node('13', 'Apply makeup\nstep by step', **action_style)
    dot.node('14', 'Final\npreview', **screen_style)
    dot.node('15', 'Choose\naction', **action_style)
    dot.node('16', 'Save', **screen_style)
    dot.node('17', 'Share', **screen_style)
    dot.node('18', 'Products', **screen_style)
    dot.node('19', 'Try another', **action_style)
    dot.node('20', 'Retry', **action_style)

    # Edges
    dot.edge('1', '2')
    dot.edge('2', '3')
    dot.edge('3', '4')
    dot.edge('4', '5')
    dot.edge('5', '6')
    dot.edge('6', '7')
    dot.edge('7', '8')
    dot.edge('8', '9')
    dot.edge('9', '10', label='Y')
    dot.edge('9', '20', label='N')
    dot.edge('20', '8', style='dashed')
    dot.edge('10', '11')
    dot.edge('11', '12')
    dot.edge('12', '13')
    dot.edge('13', '14')
    dot.edge('14', '15')
    dot.edge('15', '16')
    dot.edge('15', '17')
    dot.edge('15', '18')
    dot.edge('15', '19')
    dot.edge('16', '6', style='dashed', label='Done')
    dot.edge('17', '6', style='dashed', label='Done')
    dot.edge('18', '6', style='dashed', label='Done')
    dot.edge('19', '10', style='dashed')

    return dot

simple_flow = create_simplified_flow()
simple_flow.render('/home/user/ui/ar_makeup_core_flow', cleanup=True)
print("✓ Simplified core flow diagram generated: ar_makeup_core_flow.png")

# Create onboarding flow
def create_onboarding_flow():
    dot = Digraph(comment='Onboarding Flow', format='png')
    dot.attr(rankdir='TB', size='10,12', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='12')
    dot.attr('edge', fontname='Arial', fontsize='10')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2.5', 'width': '1.8', 'height': '1'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2.5', 'width': '1.8', 'height': '1'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2.5', 'width': '2'}

    dot.node('start', 'Open app', **action_style)
    dot.node('splash', 'Splash screen', **screen_style)
    dot.node('welcome', 'Welcome screen', **screen_style)
    dot.node('get_started', 'Tap Get Started', **action_style)
    dot.node('lang', 'Language selection', **screen_style)
    dot.node('privacy', 'Privacy notice', **screen_style)
    dot.node('cam_perm', 'Camera\npermission?', **decision_style)
    dot.node('perm_warn', 'Permission warning', **screen_style)
    dot.node('settings', 'Go to settings', **action_style)
    dot.node('quiz', 'Onboarding quiz', **screen_style)
    dot.node('q1', 'Skin type', **action_style)
    dot.node('q2', 'Skin tone', **action_style)
    dot.node('q3', 'Makeup frequency', **action_style)
    dot.node('q4', 'Favorite style', **action_style)
    dot.node('q5', 'Main goal', **action_style)
    dot.node('save', 'Save preferences', **action_style)
    dot.node('home', 'Home screen', **screen_style)

    dot.edge('start', 'splash')
    dot.edge('splash', 'welcome')
    dot.edge('welcome', 'get_started')
    dot.edge('get_started', 'lang')
    dot.edge('lang', 'privacy')
    dot.edge('privacy', 'cam_perm')
    dot.edge('cam_perm', 'quiz', label='Allow')
    dot.edge('cam_perm', 'perm_warn', label='Deny')
    dot.edge('perm_warn', 'settings')
    dot.edge('settings', 'cam_perm', style='dashed')
    dot.edge('quiz', 'q1')
    dot.edge('q1', 'q2')
    dot.edge('q2', 'q3')
    dot.edge('q3', 'q4')
    dot.edge('q4', 'q5')
    dot.edge('q5', 'save')
    dot.edge('save', 'home')

    return dot

onboarding = create_onboarding_flow()
onboarding.render('/home/user/ui/ar_makeup_onboarding', cleanup=True)
print("✓ Onboarding flow diagram generated: ar_makeup_onboarding.png")

print("\n✅ All diagrams generated successfully!")
print("Files created:")
print("  - ar_makeup_user_flow.png (Complete flow)")
print("  - ar_makeup_core_flow.png (Simplified version)")
print("  - ar_makeup_onboarding.png (Onboarding detail)")
