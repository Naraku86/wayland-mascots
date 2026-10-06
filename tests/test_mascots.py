"""Check poses, pixel geometry and deterministic embedding."""
from pathlib import Path
import importlib.util
import subprocess
import tempfile
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('embed', root/'scripts/embed_assets.py')
embed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(embed)
for directory in sorted((root/'assets/mascots').iterdir()):
    drawings = []
    for pose in embed.POSES:
        node = ET.parse(directory/f'bongo-{pose}.svg').getroot()
        assert node.attrib['viewBox'] == '0 0 116 64', directory
        assert len(node) > 100, directory
        for pixel in node:
            assert 26 <= int(pixel.attrib['x']) < 90
            assert 0 <= int(pixel.attrib['y']) < 64
        drawings.append(ET.tostring(node))
    assert len(set(drawings)) == 5, directory
    result = embed.generate(directory)
    assert result == embed.generate(directory)
    assert result.count('const size_t ') == 5
with tempfile.TemporaryDirectory() as temporary:
    try:
        embed.generate(Path(temporary))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('Missing poses must fail')
with tempfile.TemporaryDirectory() as temporary:
    marker = Path(temporary) / 'must-not-exist'
    result = subprocess.run(
        ['make', 'mascot', f'MASCOT=invalid"; touch {marker}; #'],
        cwd=root, capture_output=True, text=True,
    )
    assert result.returncode != 0
    assert 'Unknown mascot:' in result.stderr
    assert not marker.exists(), 'Mascot names must never execute shell commands'
print('Four packs verified: distinct poses, geometry, embedding and safe selection.')
