#!/usr/bin/env python3
"""
FamilyFlix Repository Builder
Generates ZIP files and checksums for Kodi addon repository
"""

import os
import zipfile
import hashlib
import re
from pathlib import Path

# Configuration
REPO_DIR = Path(__file__).parent

# All addons in the repository
ADDONS = [
    'repository.familyflix',
    'skin.familyflix',
    'plugin.program.autocompletion',
    'plugin.video.tmdb.bingie.helper',
    'resource.images.studios.coloured',
    'screensaver.bingie',
    'script.bingie.helper',
    'script.bingie.toolbox',
    'script.bingie.widgets',
    'script.module.bingie',
    'script.skin.helper.colorpicker',
    'script.skin.helper.skinbackup'
]


def get_addon_version(addon_dir: Path) -> str:
    """Extract version from addon.xml"""
    addon_xml = addon_dir / 'addon.xml'
    if not addon_xml.exists():
        return None

    with open(addon_xml, 'r', encoding='utf-8') as f:
        content = f.read()

    version_match = re.search(r'version="([^"]+)"', content)
    if version_match:
        return version_match.group(1)
    return None


def create_zip(addon_name: str) -> str:
    """Create ZIP file for an addon"""
    addon_dir = REPO_DIR / addon_name

    if not addon_dir.exists():
        print(f"  [SKIP] {addon_name} - folder not found")
        return None

    version = get_addon_version(addon_dir)
    if not version:
        print(f"  [SKIP] {addon_name} - no version found")
        return None

    zip_name = f"{addon_name}-{version}.zip"
    zip_path = addon_dir / zip_name

    # Remove old zip if exists
    if zip_path.exists():
        zip_path.unlink()

    print(f"  Creating {zip_name}...")

    # Create ZIP
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(addon_dir):
            # Skip .git folder and existing zips
            dirs[:] = [d for d in dirs if d != '.git' and d != '__pycache__']

            for file in files:
                if file.endswith('.zip'):
                    continue

                file_path = Path(root) / file
                arc_name = addon_name + '/' + str(file_path.relative_to(addon_dir))
                zf.write(file_path, arc_name)

    return str(zip_path)


def generate_md5(file_path: str) -> str:
    """Generate MD5 checksum for a file"""
    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def update_addons_xml_md5():
    """Create/update addons.xml.md5"""
    addons_xml = REPO_DIR / 'addons.xml'
    md5_file = REPO_DIR / 'addons.xml.md5'

    if addons_xml.exists():
        md5_hash = generate_md5(addons_xml)
        with open(md5_file, 'w') as f:
            f.write(md5_hash)
        print(f"  addons.xml.md5: {md5_hash}")


def main():
    print("=" * 60)
    print("  FamilyFlix Repository Builder")
    print("=" * 60)
    print()
    print("Creating ZIP files...")

    success_count = 0
    for addon in ADDONS:
        result = create_zip(addon)
        if result:
            success_count += 1

    print()
    print(f"Created {success_count}/{len(ADDONS)} ZIP files")
    print()
    print("Generating checksums...")
    update_addons_xml_md5()

    print()
    print("=" * 60)
    print("  Build complete!")
    print()
    print("  Repository URL:")
    print("  https://triffalin.github.io/repository.familyflix/")
    print("=" * 60)


if __name__ == '__main__':
    main()
