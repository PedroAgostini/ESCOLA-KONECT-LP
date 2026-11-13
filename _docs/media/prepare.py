from pathlib import Path
from PIL import Image
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
# Pasta local com os PNGs originais gerados (defina KONECT_IMG_SOURCE antes de rodar).
SOURCE = Path(os.environ.get('KONECT_IMG_SOURCE', ROOT / '_docs' / 'media' / 'originais'))
images = {
    'ingles-hero': 'exec-8bff6d23-fa37-4304-8b8a-404e34966620.png',
    'ingles-trabalho': 'exec-edfe61d9-ba53-4b14-ab4c-b8c94bfcbb46.png',
    'ingles-viagem': 'exec-544b41de-3972-4626-b0d3-b1e5b1f1baf0.png',
    'ingles-estudo': 'exec-556f533d-3c08-4dfb-96f0-4b56c41fdba7.png',
    'ingles-conexoes': 'exec-0d41abe6-41ac-400a-bc33-5ed584fec0af.png',
    'ingles-aula': 'exec-57ec5d4d-31c1-4bee-b42b-a472e75bdf8d.png',
    'impressao-pecas': 'exec-42df26ab-bc83-411d-ae4c-bd8bc966d82e.png',
}
for name, file in images.items():
    im = Image.open(SOURCE / file).convert('RGB')
    widths = [640, 1024, 1536] if name in ('ingles-hero', 'ingles-aula') else [400, 800]
    if name == 'impressao-pecas': widths = [480, 960]
    for width in widths:
        size = (width, round(im.height * width / im.width))
        im.resize(size, Image.Resampling.LANCZOS).save(ROOT / f'assets/img/generated/{name}-{width}.webp', quality=82, method=6)

def ffmpeg(*args):
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *map(str,args)], cwd=ROOT, check=True)

stills = {'fachada': 5.5, 'recepcao': 40, 'sala-tecnica': 114, 'sala-aula': 203, 'impressoras': 171}
for name, time in stills.items():
    ffmpeg('-ss', time, '-i', 'assets/escola.mp4', '-frames:v', 1, '-c:v', 'libwebp', '-quality', 85, f'assets/img/escola/{name}-1024.webp')
    im = Image.open(ROOT / f'assets/img/escola/{name}-1024.webp')
    im.resize((512, 288), Image.Resampling.LANCZOS).save(ROOT / f'assets/img/escola/{name}-512.webp', quality=82, method=6)

# Six four-second shots: facade, reception, computer lab, technical room, printers, classroom.
starts = [3, 38, 64, 112, 170, 203]
filters = []
for i, start in enumerate(starts):
    filters.append(f'[0:v]trim=start={start}:duration=4,setpts=PTS-STARTPTS,fps=24,setsar=1[v{i}]')
filters.append(''.join(f'[v{i}]' for i in range(len(starts))) + f'concat=n={len(starts)}:v=1:a=0,fade=t=in:st=0:d=0.35,fade=t=out:st=23.65:d=0.35[out]')
ffmpeg('-i', 'assets/escola.mp4', '-filter_complex', ';'.join(filters), '-map', '[out]', '-an', '-c:v', 'libx264', '-preset', 'medium', '-crf', '25', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', 'assets/video/escola-tour-24s.mp4')
ffmpeg('-ss', 170, '-i', 'assets/escola.mp4', '-t', 10, '-an', '-vf', 'fps=24,fade=t=in:st=0:d=0.25,fade=t=out:st=9.75:d=0.25', '-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', 'assets/video/impressoras-10s.mp4')
for path in sorted((ROOT / 'assets').rglob('*')):
    if path.is_file() and path.suffix in ('.webp', '.mp4'): print(path.relative_to(ROOT), round(path.stat().st_size / 1024), 'KB')
