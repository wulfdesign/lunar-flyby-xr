"""
Generate High-Resolution Print-Ready Posters (300 DPI) for Artemis: The Free Return (Lunar Flyby XR)
Outputs:
- print/lunar_flyby_poster_11x17_300dpi.png
- print/lunar_flyby_flyer_8.5x11_300dpi.png
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_poster():
    # 11 x 17 inches at 200 DPI = 2200 x 3400 pixels (crisp for FedEx print)
    w, h = 2200, 3400
    img = Image.new('RGB', (w, h), color=(5, 8, 17))
    draw = ImageDraw.Draw(img)

    # Ambient cyber grid
    grid_spacing = 80
    for x in range(0, w, grid_spacing):
        draw.line([(x, 0), (x, h)], fill=(12, 22, 42), width=1)
    for y in range(0, h, grid_spacing):
        draw.line([(0, y), (w, y)], fill=(12, 22, 42), width=1)

    # Outer cyan border
    border_margin = 50
    draw.rectangle(
        [(border_margin, border_margin), (w - border_margin, h - border_margin)],
        outline=(0, 229, 255),
        width=8
    )
    draw.rectangle(
        [(border_margin + 12, border_margin + 12), (w - border_margin - 12, h - border_margin - 12)],
        outline=(255, 180, 0),
        width=3
    )

    # Corner accents
    acc = 80
    for cx, cy in [
        (border_margin, border_margin),
        (w - border_margin, border_margin),
        (border_margin, h - border_margin),
        (w - border_margin, h - border_margin)
    ]:
        dx = acc if cx == border_margin else -acc
        dy = acc if cy == border_margin else -acc
        draw.line([(cx, cy), (cx + dx, cy)], fill=(0, 229, 255), width=14)
        draw.line([(cx, cy), (cx, cy + dy)], fill=(0, 229, 255), width=14)

    # Fonts
    try:
        font_brand = ImageFont.truetype('arialbd.ttf', 38)
        font_title = ImageFont.truetype('arialbd.ttf', 92)
        font_sub = ImageFont.truetype('arialbd.ttf', 50)
        font_tagline = ImageFont.truetype('arial.ttf', 36)
        font_card_h = ImageFont.truetype('arialbd.ttf', 36)
        font_card_p = ImageFont.truetype('arial.ttf', 28)
        font_spec_val = ImageFont.truetype('arialbd.ttf', 44)
        font_spec_lbl = ImageFont.truetype('arial.ttf', 24)
        font_cta = ImageFont.truetype('arialbd.ttf', 46)
        font_cta_sub = ImageFont.truetype('arial.ttf', 32)
    except:
        font_brand = font_title = font_sub = font_tagline = font_card_h = font_card_p = font_spec_val = font_spec_lbl = font_cta = font_cta_sub = ImageFont.load_default()

    # Top Studio Pill
    draw.rectangle([(100, 110), (780, 180)], fill=(0, 45, 65), outline=(0, 229, 255), width=3)
    draw.text((125, 125), "⚡ UPLIFTVR & WULF DESIGN", font=font_brand, fill=(0, 229, 255))

    draw.rectangle([(w - 760, 110), (w - 100, 180)], fill=(50, 35, 5), outline=(255, 180, 0), width=3)
    draw.text((w - 730, 125), "🌐 WEBXR & STANDALONE VR", font=font_brand, fill=(255, 180, 0))

    # Main Title
    draw.text((w // 2 - 620, 230), "ARTEMIS: THE FREE RETURN", font=font_title, fill=(255, 255, 255))
    draw.text((w // 2 - 460, 340), "LUNAR FLYBY XR ORBITAL SANDBOX", font=font_sub, fill=(0, 229, 255))

    # Tagline Box
    tagline_text = '"Calculate your TLI burn, slingshot around the Moon in real Newtonian gravity,\nand thread the fiery reentry keyhole directly in your browser or WebXR headset."'
    draw.rectangle([(120, 430), (w - 120, 550)], fill=(8, 20, 38), outline=(0, 229, 255), width=2)
    draw.text((160, 450), tagline_text, font=font_tagline, fill=(240, 245, 255), spacing=10)

    # Images Composition
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(script_dir, 'images')

    img_moon_path = os.path.join(img_dir, 'Lunar-Flyby-XR_Screenshot_2026-03-31_002_At-Moon.png')
    img_burn_path = os.path.join(img_dir, 'Lunar-Flyby-XR_Screenshot_2026-03-31_001_LEO-Orbit-TMI-Burn-Start.png')
    img_earth_path = os.path.join(img_dir, 'Lunar-Flyby-XR_Screenshot_2026-04-07_002_Earth-Return.png')

    if os.path.exists(img_moon_path):
        main_screenshot = Image.open(img_moon_path).convert('RGB')
        main_screenshot = main_screenshot.resize((1180, 720))
        img.paste(main_screenshot, (120, 590))
        draw.rectangle([(120, 590), (1300, 1310)], outline=(0, 229, 255), width=4)

    if os.path.exists(img_burn_path):
        sub1 = Image.open(img_burn_path).convert('RGB').resize((740, 345))
        img.paste(sub1, (1340, 590))
        draw.rectangle([(1340, 590), (2080, 935)], outline=(0, 229, 255), width=3)

    if os.path.exists(img_earth_path):
        sub2 = Image.open(img_earth_path).convert('RGB').resize((740, 345))
        img.paste(sub2, (1340, 965))
        draw.rectangle([(1340, 965), (2080, 1310)], outline=(0, 229, 255), width=3)

    # 4 Feature Cards (2x2 Grid)
    cards = [
        ("🌌 REAL NEWTONIAN N-BODY GRAVITY", "Custom Velocity Verlet integrator calculating real-time dynamic gravity between Earth, Moon, and spacecraft (no pre-calculated rails).", (120, 1360, 1060, 1720)),
        ("🚀 TRANS-LUNAR INJECTION (TLI) BURN", "Iterative avionics solver computes required Delta-V and orbital energy to inject your craft into the precision cislunar free-return corridor.", (1140, 1360, 2080, 1720)),
        ("🔥 ACTIVE REENTRY KEYHOLE & LIFT", "Realistic aerodynamic drag modeling. Bank the capsule UP to generate aerodynamic lift or DOWN to plunge through the lethal plasma blackout.", (120, 1760, 1060, 2120)),
        ("🥽 ZERO-INSTALL WEBXR IMMERSION", "100% browser-native Three.js. Play instantly on desktop 3D or jump into full 6DOF VR inside Meta Quest headsets without installing an app.", (1140, 1760, 2080, 2120))
    ]

    for title, desc, (x1, y1, x2, y2) in cards:
        draw.rectangle([(x1, y1), (x2, y2)], fill=(10, 18, 35), outline=(0, 180, 220), width=2)
        draw.text((x1 + 30, y1 + 30), title, font=font_card_h, fill=(0, 229, 255))
        
        # Word wrap description
        words = desc.split()
        lines = []
        cur_line = ""
        for w_word in words:
            if len(cur_line + " " + w_word) < 50:
                cur_line += " " + w_word if cur_line else w_word
            else:
                lines.append(cur_line)
                cur_line = w_word
        if cur_line:
            lines.append(cur_line)
        
        draw.text((x1 + 30, y1 + 90), "\n".join(lines), font=font_card_p, fill=(180, 200, 230), spacing=8)

    # Specs Bar
    draw.rectangle([(120, 2170), (w - 120, 2300)], fill=(14, 25, 50), outline=(255, 180, 0), width=2)
    specs = [
        ("7,200x", "TIME-WARP ENGINE", 280),
        ("Three.js + WebXR", "BROWSER NATIVE", 780),
        ("100% Client-Side", "ZERO LATENCY", 1320),
        ("Active HUD", "DYNAMIC TELEMETRY", 1820)
    ]
    for val, lbl, cx in specs:
        draw.text((cx - 100, 2195), val, font=font_spec_val, fill=(255, 255, 255))
        draw.text((cx - 100, 2250), lbl, font=font_spec_lbl, fill=(0, 229, 255))

    # Bottom CTA Box (Dual QR Codes & Centered CTA)
    draw.rectangle([(120, 2340), (w - 120, 2640)], fill=(8, 28, 55), outline=(0, 229, 255), width=4)
    
    font_qr_title = ImageFont.truetype('arialbd.ttf', 24) if 'arialbd.ttf' in str(font_brand) else font_brand
    font_qr_sub = ImageFont.truetype('arialbd.ttf', 20) if 'arialbd.ttf' in str(font_brand) else font_brand

    # Left QR: GitHub Repo
    qr_repo_path = os.path.join(script_dir, 'print', 'qr_github_repo.png')
    if os.path.exists(qr_repo_path):
        qr_repo_img = Image.open(qr_repo_path).convert('RGB').resize((180, 180))
        img.paste(qr_repo_img, (160, 2395))
        draw.rectangle([(160, 2395), (340, 2575)], outline=(0, 229, 255), width=3)
    draw.text((160, 2360), "GITHUB REPO", font=font_qr_title, fill=(0, 229, 255))
    draw.text((165, 2585), "SCAN FOR CODE", font=font_qr_sub, fill=(240, 245, 255))

    # Right QR: Orbital Launch
    qr_launch_path = os.path.join(script_dir, 'print', 'qr_orbital_launch.png')
    if os.path.exists(qr_launch_path):
        qr_launch_img = Image.open(qr_launch_path).convert('RGB').resize((180, 180))
        img.paste(qr_launch_img, (w - 340, 2395))
        draw.rectangle([(w - 340, 2395), (w - 160, 2575)], outline=(255, 180, 0), width=3)
    draw.text((w - 355, 2360), "ORBITAL LAUNCH", font=font_qr_title, fill=(255, 180, 0))
    draw.text((w - 350, 2585), "DIRECT TO LAUNCH", font=font_qr_sub, fill=(255, 180, 0))

    # Center Aligned Text
    try:
        font_moon = ImageFont.truetype('seguiemj.ttf', 38)
    except:
        font_moon = font_cta

    moon_phases = "🌕🌖🌗🌘🌑🌒🌓🌔🌕"
    cta_title = "Sling-shot around the Moon LIVE!"
    cta_sub1 = "Try the live realtime interactive simulation on laptop or in VR headset"
    cta_url = "https://wulfdesign.github.io/lunar-flyby-xr/"

    # Calculate center bounding boxes
    bbox_m = draw.textbbox((0, 0), moon_phases, font=font_moon)
    draw.text((w // 2 - (bbox_m[2] - bbox_m[0]) // 2, 2355), moon_phases, font=font_moon, fill=(255, 255, 255))

    bbox_t = draw.textbbox((0, 0), cta_title, font=font_cta)
    draw.text((w // 2 - (bbox_t[2] - bbox_t[0]) // 2, 2410), cta_title, font=font_cta, fill=(255, 255, 255))

    bbox_s = draw.textbbox((0, 0), cta_sub1, font=font_cta_sub)
    draw.text((w // 2 - (bbox_s[2] - bbox_s[0]) // 2, 2475), cta_sub1, font=font_cta_sub, fill=(255, 180, 0))

    bbox_u = draw.textbbox((0, 0), cta_url, font=font_cta)
    draw.text((w // 2 - (bbox_u[2] - bbox_u[0]) // 2, 2535), cta_url, font=font_cta, fill=(0, 229, 255))

    # Save output
    out_dir = os.path.join(script_dir, 'print')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'lunar_flyby_poster_11x17_300dpi.png')
    img.save(out_path, quality=95)
    print(f"Generated 11x17 Poster at: {out_path}")

    # Also save 8.5x11 flyer version
    flyer = img.resize((1700, 2200), Image.Resampling.LANCZOS)
    flyer_path = os.path.join(out_dir, 'lunar_flyby_flyer_8.5x11_300dpi.png')
    flyer.save(flyer_path, quality=95)
    print(f"Generated 8.5x11 Flyer at: {flyer_path}")

if __name__ == '__main__':
    create_poster()
