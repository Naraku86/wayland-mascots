"""Render the existing poses as looping GIFs; requires ImageMagick."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SEQUENCE = (
    ('both-up', 60), ('left-down', 12), ('both-up', 12),
    ('right-down', 12), ('both-down', 12), ('both-up', 60),
    ('sleeping', 100),
)

if __name__ == '__main__':
    if not shutil.which('magick'):
        sys.exit('Install ImageMagick to render previews.')
    try:
        for directory in sorted((ROOT / 'assets/mascots').iterdir()):
            command = ['magick', '-background', '#18202b']
            for pose, delay in SEQUENCE:
                command += ['-delay', str(delay), str(directory / f'bongo-{pose}.svg')]
            command += ['-alpha', 'remove', '-alpha', 'off', '-filter', 'point',
                        '-resize', '232x128', '-loop', '0', str(directory / 'preview.gif')]
            subprocess.run(command, check=True)
    except (OSError, subprocess.CalledProcessError) as error:
        sys.exit(f'Cannot render previews: {error}')
