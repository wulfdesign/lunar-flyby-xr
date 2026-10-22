# Test normalization edge cases
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'private'))
from promote_to_production import normalize_asset_paths

cases = [
    ('case1', '<script src="../../vendor/three.min.js"></script>', '<script src="vendor/three.min.js"></script>'),
    ('case2', "<link rel='stylesheet' href='../../vendor/styles.css'>", "<link rel='stylesheet' href='vendor/styles.css'>"),
    ('case3', '<img src="../../textures/earth.jpg">', '<img src="textures/earth.jpg">'),
    ('case4', "<img src='../../images/hero.webp'>", "<img src='images/hero.webp'>"),
    ('case5', "background: url('../../textures/bar.jpg')", "background: url('textures/bar.jpg')"),
    ('case6', 'background: url("../../textures/bar.jpg")', 'background: url("textures/bar.jpg")'),
    ('case7', 'background: url(../../textures/bar.jpg)', 'background: url(textures/bar.jpg)'),
    ('case8', "background: url(  '../../textures/bar.jpg'  )", "background: url(  'textures/bar.jpg'  )"),
    ('case9', '<div style="background-image: url(\'../../textures/stars.jpg\');"></div>', '<div style="background-image: url(\'textures/stars.jpg\');"></div>'),
    ('case10', "textureLoader.load('../../textures/moon.jpg', cb);", "textureLoader.load('textures/moon.jpg', cb);"),
    ('case11', 'textureLoader.load("../../textures/moon.jpg", cb);', 'textureLoader.load("textures/moon.jpg", cb);'),
    ('case12', '<img src="../textures/foo.jpg">', '<img src="textures/foo.jpg">'),
    ('case13', '<script src="../../vendor/three.js?v=2"></script>', '<script src="vendor/three.js?v=2"></script>'),
    ('case14_cdn', '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>'),
    ('case15_backtick', 'loader.load(`../../textures/moon.jpg`);', 'loader.load(`textures/moon.jpg`);'),
    ('case16_screenshots', '<img src="../../screenshots/hud.png">', '<img src="screenshots/hud.png">')
]

results = []
for name, inp, expected in cases:
    res, count = normalize_asset_paths(inp)
    matched = (res == expected)
    results.append((name, matched, count, inp, expected, res))
    print(f"[{'PASS' if matched else 'FAIL'}] {name} (count={count})")
    if not matched:
        print(f"   Expected: {expected}")
        print(f"   Actual:   {res}")

print(f"\nSummary: {sum(1 for r in results if r[1])}/{len(cases)} matched")
