#!/usr/bin/env python3
import sys
import re
from css_styles import get_css
from slides_act1 import get_slides_act1
from slides_act2 import get_slides_act2
from slides_act3 import get_slides_act3
from slides_act4 import get_slides_act4
from slides_act5 import get_slides_act5
from nav_and_scripts import get_header_and_drawer, get_footer, get_script

def build_index_html():
    head_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Madeira Island Alpine & Coastal Expedition | Master Field Guide</title>
  <meta name="description" content="Comprehensive 8-day / 7-night expedition guide across Madeira Island, Portugal. Featuring high volcanic ridges (PR1), UNESCO Laurissilva levadas (PR9, PR6), dragon-tail sea cliffs (PR8), volcanic ocean pools, authentic 3★/4★ lodging, and mountain driving logistics.">
  <meta name="theme-color" content="#b47b2c">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='46' fill='%230f172a' stroke='%23b47b2c' stroke-width='6'/><polygon points='50,18 58,45 85,50 58,55 50,82 42,55 15,50 42,45' fill='%23b47b2c'/></svg>">
  <meta property="og:title" content="Madeira Island Alpine & Coastal Expedition | Master Field Guide">
  <meta property="og:description" content="Comprehensive 8-day / 7-night expedition guide across Madeira Island, Portugal. Soaring volcanic ridges, primordial rainforest levadas, and dramatic Atlantic cliffs.">
  <meta property="og:image" content="https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&w=1200&q=80">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Madeira Island Alpine & Coastal Expedition | Master Field Guide">
  <meta name="twitter:description" content="Comprehensive 8-day / 7-night expedition guide across Madeira Island, Portugal. High peaks above clouds, emerald levadas, and ocean lava pools.">
  <meta name="twitter:image" content="https://images.unsplash.com/photo-1542332213-9b5a5a3fad35?auto=format&fit=crop&w=1200&q=80">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

"""

    css = get_css()
    
    body_start = """
</head>
<body>

  <div class="viewport-ambient"></div>

  <!-- Main 16:9 Presentation Frame -->
  <main class="deck-container" id="presentationContainer">
"""

    header_and_drawer = get_header_and_drawer()

    slides_wrapper_start = """
    <!-- Slide Content Track (30 De-Cluttered, Large-Font Slides) -->
    <div class="slides-wrapper">
"""

    act1 = get_slides_act1()
    act2 = get_slides_act2()
    act3 = get_slides_act3()
    act4 = get_slides_act4()
    act5 = get_slides_act5()

    slides_wrapper_end = """
    </div><!-- /slides-wrapper -->
"""

    footer = get_footer()
    main_end = """
  </main>
"""
    script = get_script()

    full_html = (
        head_start +
        css +
        body_start +
        header_and_drawer +
        slides_wrapper_start +
        act1 +
        act2 +
        act3 +
        act4 +
        act5 +
        slides_wrapper_end +
        footer +
        main_end +
        script
    )

    return full_html

def validate(html_content):
    print("Validating generated HTML...")
    
    # Check slide count
    slides = re.findall(r'<section\s+class="slide[^"]*"\s+data-slide="(\d+)"', html_content)
    print(f"Found {len(slides)} slides: {slides}")
    assert len(slides) == 30, f"Expected 30 slides, found {len(slides)}"
    assert slides == [str(i) for i in range(1, 31)], "Slides are not numbered 1 through 30 sequentially"

    # Check slide 1 is active
    assert '<section class="slide active" data-slide="1">' in html_content, "Slide 1 is not marked active"

    # Check key element IDs
    required_ids = [
        'presentationContainer', 'deckDrawerTrigger', 'nativeSlidePicker', 'themeBtn',
        'slideCounter', 'fullscreenBtn', 'drawerOverlay', 'drawerBackdrop', 'drawerSheet',
        'drawerCloseBtn', 'drawerSearchInput', 'drawerSearchClear', 'drawerFilterPills',
        'drawerList', 'dotsContainer', 'mobileSlideIndicator', 'footerSlidePicker',
        'prevBtn', 'nextBtn', 'interactiveTrailSvg', 'inspectorContent', 'transitDetailCard-5'
    ]
    for req_id in required_ids:
        assert f'id="{req_id}"' in html_content, f"Missing required ID: {req_id}"

    # Check for per-person divisions (user constraint: zero per-person division)
    budget_section = html_content[html_content.find('data-slide="29"'):html_content.find('data-slide="30"')]
    assert 'per person' not in budget_section.lower() or 'zero per-person' in budget_section.lower(), "Budget slide should not divide costs per person"

    print("All validations PASSED!")

if __name__ == '__main__':
    html = build_index_html()
    validate(html)

    output_path = '/Users/luisechegorri/Documents/madeira/index.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Successfully generated {output_path} ({len(html)} bytes)")
