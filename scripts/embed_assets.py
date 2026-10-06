"""Embed five SVG poses deterministically, from the project root."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

POSES = ('both-up', 'left-down', 'right-down', 'both-down', 'sleeping')


def generate(directory: Path) -> str:
    arrays = ['#include "graphics/embedded_assets.h"\n']
    for pose in POSES:
        svg = (directory / f'bongo-{pose}.svg').read_text(encoding='utf-8')
        ET.fromstring(svg)
        if directory == Path('assets/new'):
            # Preserve upstream's original artwork crop and editor cleanup.
            svg = svg.replace('viewBox="0 0 500 500"', 'viewBox="0 101 500 277"')
            svg = '\n'.join(line for line in svg.splitlines() if '<rect ' not in line)
        data = svg.encode()
        symbol = 'bongo_' + pose.replace('-', '_') + '_svg'
        rows = [', '.join(f'0x{v:02x}' for v in data[i:i+12])
                for i in range(0, len(data), 12)]
        arrays.append(f'const unsigned char {symbol}[] = {{\n  ' + ',\n  '.join(rows)
                      + f'\n}};\nconst size_t {symbol}_size = {len(data)};\n')
    return '\n'.join(arrays)


if __name__ == '__main__':
    try:
        generated = generate(Path(sys.argv[1] if len(sys.argv) > 1 else 'assets/new'))
        Path('src/graphics/embedded_assets.c').write_text(generated, encoding='utf-8')
    except (OSError, UnicodeError, ET.ParseError) as error:
        sys.exit(f'Cannot embed mascot: {error}')
