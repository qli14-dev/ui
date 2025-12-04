#!/usr/bin/env python3
from graphviz import Digraph

# Create horizontal onboarding flow
def create_onboarding_horizontal():
    dot = Digraph(comment='AR Makeup Onboarding Flow', format='png')
    dot.attr(rankdir='LR', size='20,8', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='11')
    dot.attr('edge', fontname='Arial', fontsize='9')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2', 'width': '1.3', 'height': '0.8'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2', 'width': '1.3', 'height': '0.8'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2', 'width': '1.5', 'height': '1.5'}

    dot.node('start', 'Open\napp', **action_style)
    dot.node('splash', 'Splash\nscreen', **screen_style)
    dot.node('welcome', 'Welcome\nscreen', **screen_style)
    dot.node('get_started', 'Tap Get\nStarted', **action_style)
    dot.node('lang', 'Language\nselection', **screen_style)
    dot.node('privacy', 'Privacy\nnotice', **screen_style)
    dot.node('cam_perm', 'Camera\npermission?', **decision_style)
    dot.node('quiz', 'Onboarding\nquiz', **screen_style)
    dot.node('q1', 'Q1:\nSkin type', **action_style)
    dot.node('q2', 'Q2:\nSkin tone', **action_style)
    dot.node('q3', 'Q3:\nMakeup freq', **action_style)
    dot.node('q4', 'Q4:\nFav style', **action_style)
    dot.node('q5', 'Q5:\nMain goal', **action_style)
    dot.node('save', 'Save\npreferences', **action_style)
    dot.node('home', 'Home\nscreen', **screen_style)

    # Error path
    dot.node('perm_warn', 'Permission\nwarning', **screen_style)
    dot.node('settings', 'Go to\nsettings', **action_style)

    # Main path
    dot.edge('start', 'splash')
    dot.edge('splash', 'welcome')
    dot.edge('welcome', 'get_started')
    dot.edge('get_started', 'lang')
    dot.edge('lang', 'privacy')
    dot.edge('privacy', 'cam_perm')
    dot.edge('cam_perm', 'quiz', label='Allow')
    dot.edge('quiz', 'q1')
    dot.edge('q1', 'q2')
    dot.edge('q2', 'q3')
    dot.edge('q3', 'q4')
    dot.edge('q4', 'q5')
    dot.edge('q5', 'save')
    dot.edge('save', 'home')

    # Error handling
    dot.edge('cam_perm', 'perm_warn', label='Deny')
    dot.edge('perm_warn', 'settings')
    dot.edge('settings', 'cam_perm', style='dashed')

    return dot

# Create horizontal AR core flow
def create_ar_core_horizontal():
    dot = Digraph(comment='AR Makeup Core Flow', format='png')
    dot.attr(rankdir='LR', size='24,10', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='11')
    dot.attr('edge', fontname='Arial', fontsize='9')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2', 'width': '1.3', 'height': '0.8'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2', 'width': '1.3', 'height': '0.8'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2', 'width': '1.5', 'height': '1.5'}

    # Main flow nodes
    dot.node('home', 'Home\nscreen', **screen_style)
    dot.node('start_ar', 'Start AR\nMakeup', **action_style)
    dot.node('cam', 'Camera\nactivation', **screen_style)
    dot.node('face_guide', 'Face\nalignment', **screen_style)
    dot.node('align', 'Align\nface', **action_style)
    dot.node('detect', 'Face\ndetected?', **decision_style)
    dot.node('scene', 'Scene\nselection', **screen_style)
    dot.node('choose_scene', 'Select\nscene', **action_style)
    dot.node('look_lib', 'Look\nlibrary', **screen_style)
    dot.node('look_type', 'Template\nor custom?', **decision_style)
    dot.node('select_look', 'Select\nlook', **action_style)
    dot.node('step0', 'Step 0:\nPreparation', **screen_style)
    dot.node('step1', 'Step 1:\nBase', **screen_style)
    dot.node('step2', 'Step 2:\nBrows', **screen_style)
    dot.node('step3', 'Step 3:\nEyes', **screen_style)
    dot.node('step4', 'Step 4:\nBlush', **screen_style)
    dot.node('step5', 'Step 5:\nLips', **screen_style)
    dot.node('step6', 'Step 6:\nFinal touch', **screen_style)
    dot.node('preview', 'Final\npreview', **screen_style)
    dot.node('before_after', 'Before/After\nslider', **screen_style)
    dot.node('actions', 'Choose\naction?', **decision_style)

    # Action outcomes
    dot.node('save_action', 'Save\nlook', **action_style)
    dot.node('share_action', 'Share\nlook', **action_style)
    dot.node('products_action', 'View\nproducts', **action_style)
    dot.node('retry_action', 'Try\nanother', **action_style)

    dot.node('save_screen', 'Save\nscreen', **screen_style)
    dot.node('share_screen', 'Share\nscreen', **screen_style)
    dot.node('products_screen', 'Products\nscreen', **screen_style)

    dot.node('done', 'Done', **action_style)

    # Error path
    dot.node('retry_warn', 'Retry\nwarning', **screen_style)
    dot.node('retry', 'Retry\ndetection', **action_style)

    # Main edges
    dot.edge('home', 'start_ar')
    dot.edge('start_ar', 'cam')
    dot.edge('cam', 'face_guide')
    dot.edge('face_guide', 'align')
    dot.edge('align', 'detect')
    dot.edge('detect', 'scene', label='Y')
    dot.edge('scene', 'choose_scene')
    dot.edge('choose_scene', 'look_lib')
    dot.edge('look_lib', 'look_type')
    dot.edge('look_type', 'select_look', label='Template/Custom')
    dot.edge('select_look', 'step0')
    dot.edge('step0', 'step1')
    dot.edge('step1', 'step2')
    dot.edge('step2', 'step3')
    dot.edge('step3', 'step4')
    dot.edge('step4', 'step5')
    dot.edge('step5', 'step6')
    dot.edge('step6', 'preview')
    dot.edge('preview', 'before_after')
    dot.edge('before_after', 'actions')

    dot.edge('actions', 'save_action', label='Save')
    dot.edge('actions', 'share_action', label='Share')
    dot.edge('actions', 'products_action', label='Products')
    dot.edge('actions', 'retry_action', label='Retry')

    dot.edge('save_action', 'save_screen')
    dot.edge('share_action', 'share_screen')
    dot.edge('products_action', 'products_screen')

    dot.edge('save_screen', 'done')
    dot.edge('share_screen', 'done')
    dot.edge('products_screen', 'done')

    dot.edge('done', 'home', style='dashed')
    dot.edge('retry_action', 'scene', style='dashed')

    # Error handling
    dot.edge('detect', 'retry_warn', label='N')
    dot.edge('retry_warn', 'retry')
    dot.edge('retry', 'align', style='dashed')

    return dot

# Create complete horizontal flow with sections
def create_complete_horizontal():
    dot = Digraph(comment='AR Makeup Complete Flow', format='png')
    dot.attr(rankdir='LR', size='28,16', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='10')
    dot.attr('edge', fontname='Arial', fontsize='8')
    dot.attr(splines='ortho', nodesep='0.5', ranksep='0.8')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2', 'width': '1.2', 'height': '0.7'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2', 'width': '1.2', 'height': '0.7'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2', 'width': '1.3', 'height': '1.3'}

    # Section 0: Launch
    dot.node('s0_1', 'Open\napp', **action_style)
    dot.node('s0_2', 'Splash', **screen_style)
    dot.node('s0_3', 'Welcome', **screen_style)
    dot.node('s0_4', 'Get Started', **action_style)

    # Section 1: Permissions
    dot.node('s1_1', 'Language', **screen_style)
    dot.node('s1_2', 'Privacy', **screen_style)
    dot.node('s1_3', 'Camera\npermission?', **decision_style)

    # Section 2: Quiz
    dot.node('s2_1', 'Quiz', **screen_style)
    dot.node('s2_2', 'Answer\n5 questions', **action_style)
    dot.node('s2_3', 'Save\nprefs', **action_style)

    # Section 3: Home
    dot.node('s3_1', 'Home', **screen_style)
    dot.node('s3_2', 'Start AR', **action_style)

    # Section 4: Face Detection
    dot.node('s4_1', 'Camera', **screen_style)
    dot.node('s4_2', 'Align\nface', **action_style)
    dot.node('s4_3', 'Detected?', **decision_style)

    # Section 5: Scene & Look
    dot.node('s5_1', 'Scene\nselection', **screen_style)
    dot.node('s5_2', 'Look\nlibrary', **screen_style)
    dot.node('s5_3', 'Choose\nlook', **action_style)

    # Section 6: AR Steps
    dot.node('s6_1', 'Steps\n0-6', **screen_style)
    dot.node('s6_2', 'Apply\nmakeup', **action_style)

    # Section 7: Preview
    dot.node('s7_1', 'Final\npreview', **screen_style)
    dot.node('s7_2', 'Before/\nAfter', **screen_style)
    dot.node('s7_3', 'Actions?', **decision_style)

    # Section 8: Outcomes
    dot.node('s8_1', 'Save', **screen_style)
    dot.node('s8_2', 'Share', **screen_style)
    dot.node('s8_3', 'Products', **screen_style)
    dot.node('s8_4', 'Retry', **action_style)

    # Section 9: Additional features
    dot.node('s9_1', 'Tutorials', **screen_style)
    dot.node('s9_2', 'Saved\nlooks', **screen_style)
    dot.node('s9_3', 'Profile', **screen_style)

    # Main flow
    dot.edge('s0_1', 's0_2')
    dot.edge('s0_2', 's0_3')
    dot.edge('s0_3', 's0_4')
    dot.edge('s0_4', 's1_1')
    dot.edge('s1_1', 's1_2')
    dot.edge('s1_2', 's1_3')
    dot.edge('s1_3', 's2_1', label='Allow')
    dot.edge('s2_1', 's2_2')
    dot.edge('s2_2', 's2_3')
    dot.edge('s2_3', 's3_1')

    dot.edge('s3_1', 's3_2')
    dot.edge('s3_2', 's4_1')
    dot.edge('s4_1', 's4_2')
    dot.edge('s4_2', 's4_3')
    dot.edge('s4_3', 's5_1', label='Y')
    dot.edge('s5_1', 's5_2')
    dot.edge('s5_2', 's5_3')
    dot.edge('s5_3', 's6_1')
    dot.edge('s6_1', 's6_2')
    dot.edge('s6_2', 's7_1')
    dot.edge('s7_1', 's7_2')
    dot.edge('s7_2', 's7_3')

    dot.edge('s7_3', 's8_1', label='Save')
    dot.edge('s7_3', 's8_2', label='Share')
    dot.edge('s7_3', 's8_3', label='Products')
    dot.edge('s7_3', 's8_4', label='Retry')

    # Return paths
    dot.edge('s8_1', 's3_1', style='dashed')
    dot.edge('s8_2', 's3_1', style='dashed')
    dot.edge('s8_3', 's3_1', style='dashed')
    dot.edge('s8_4', 's5_1', style='dashed')

    # Additional features
    dot.edge('s3_1', 's9_1', style='dotted')
    dot.edge('s3_1', 's9_2', style='dotted')
    dot.edge('s3_1', 's9_3', style='dotted')

    dot.edge('s9_1', 's5_1', style='dashed')
    dot.edge('s9_2', 's6_1', style='dashed')

    # Error path
    dot.edge('s4_3', 's4_2', label='N', style='dashed')

    return dot

# Create simplified horizontal flow
def create_simplified_horizontal():
    dot = Digraph(comment='AR Makeup Simplified Flow', format='png')
    dot.attr(rankdir='LR', size='22,6', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='12')
    dot.attr('edge', fontname='Arial', fontsize='10')

    action_style = {'shape': 'ellipse', 'style': 'filled', 'fillcolor': '#C8E6C9', 'color': '#2E7D32', 'penwidth': '2.5', 'width': '1.5', 'height': '1'}
    screen_style = {'shape': 'box', 'style': 'filled,rounded', 'fillcolor': '#FFE0B2', 'color': '#E65100', 'penwidth': '2.5', 'width': '1.5', 'height': '1'}
    decision_style = {'shape': 'diamond', 'style': 'filled', 'fillcolor': '#B3E5FC', 'color': '#01579B', 'penwidth': '2.5', 'width': '1.6', 'height': '1.6'}

    dot.node('1', 'Open\napp', **action_style)
    dot.node('2', 'Onboarding', **screen_style)
    dot.node('3', 'Home\nscreen', **screen_style)
    dot.node('4', 'Start AR', **action_style)
    dot.node('5', 'Face\ndetection', **screen_style)
    dot.node('6', 'Face OK?', **decision_style)
    dot.node('7', 'Scene &\nLook', **screen_style)
    dot.node('8', 'AR\nSteps 0-6', **screen_style)
    dot.node('9', 'Final\npreview', **screen_style)
    dot.node('10', 'Choose\naction?', **decision_style)
    dot.node('11', 'Save', **screen_style)
    dot.node('12', 'Share', **screen_style)
    dot.node('13', 'Products', **screen_style)
    dot.node('14', 'Done', **action_style)

    dot.edge('1', '2')
    dot.edge('2', '3')
    dot.edge('3', '4')
    dot.edge('4', '5')
    dot.edge('5', '6')
    dot.edge('6', '7', label='Y')
    dot.edge('6', '5', label='N', style='dashed')
    dot.edge('7', '8')
    dot.edge('8', '9')
    dot.edge('9', '10')
    dot.edge('10', '11', label='Save')
    dot.edge('10', '12', label='Share')
    dot.edge('10', '13', label='Products')
    dot.edge('10', '7', label='Retry', style='dashed')
    dot.edge('11', '14')
    dot.edge('12', '14')
    dot.edge('13', '14')
    dot.edge('14', '3', style='dashed')

    return dot

# Generate all diagrams
print("🎨 Generating horizontal flow diagrams...")

onboarding = create_onboarding_horizontal()
onboarding.render('/home/user/ui/flow_1_onboarding', cleanup=True)
print("✓ 1. Onboarding flow (horizontal)")

ar_core = create_ar_core_horizontal()
ar_core.render('/home/user/ui/flow_2_ar_core', cleanup=True)
print("✓ 2. AR core flow (horizontal)")

complete = create_complete_horizontal()
complete.render('/home/user/ui/flow_3_complete', cleanup=True)
print("✓ 3. Complete flow (horizontal)")

simplified = create_simplified_horizontal()
simplified.render('/home/user/ui/flow_4_simplified', cleanup=True)
print("✓ 4. Simplified flow (horizontal)")

print("\n✅ All horizontal diagrams generated!")
print("\nFiles created:")
print("  - flow_1_onboarding.png")
print("  - flow_2_ar_core.png")
print("  - flow_3_complete.png")
print("  - flow_4_simplified.png")
