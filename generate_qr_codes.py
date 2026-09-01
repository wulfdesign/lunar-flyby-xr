import os
import qrcode

repo_url = 'https://github.com/wulfdesign/lunar-flyby-xr'
launch_url = 'https://wulfdesign.github.io/lunar-flyby-xr/'

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'print')
os.makedirs(out_dir, exist_ok=True)

# Generate PNGs
qr_repo = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
qr_repo.add_data(repo_url)
qr_repo.make(fit=True)
img_repo = qr_repo.make_image(fill_color='black', back_color='white')
img_repo.save(os.path.join(out_dir, 'qr_github_repo.png'))

qr_launch = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
qr_launch.add_data(launch_url)
qr_launch.make(fit=True)
img_launch = qr_launch.make_image(fill_color='black', back_color='white')
img_launch.save(os.path.join(out_dir, 'qr_orbital_launch.png'))

# Generate SVGs
def get_svg(qr_obj):
    matrix = qr_obj.get_matrix()
    dim = len(matrix)
    rects = []
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val:
                rects.append(f'<rect x="{c}" y="{r}" width="1.02" height="1.02" fill="#000000"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {dim} {dim}" width="100%" height="100%" style="background:#ffffff; border-radius:4px;">
  <rect width="{dim}" height="{dim}" fill="#ffffff"/>
  {"".join(rects)}
</svg>'''

with open(os.path.join(out_dir, 'qr_github_repo.svg'), 'w', encoding='utf-8') as f:
    f.write(get_svg(qr_repo))

with open(os.path.join(out_dir, 'qr_orbital_launch.svg'), 'w', encoding='utf-8') as f:
    f.write(get_svg(qr_launch))

print('Generated QR codes for GitHub Repo and Orbital Launch successfully!')
