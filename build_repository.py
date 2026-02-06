#!/usr/bin/env python3
"""
FamilyFlix Repository Builder
Generates ZIP files and checksums for Kodi addon repository
"""

import os
import zipfile
import hashlib
import shutil
from pathlib import Path

# Configuration
REPO_DIR = Path(__file__).parent
ADDONS = ['repository.familyflix', 'skin.familyflix']

def create_zip(addon_name: str) -> str:
    """Create ZIP file for an addon"""
    addon_dir = REPO_DIR / addon_name

    if not addon_dir.exists():
        print(f"Warning: {addon_name} folder not found")
        return None

    # Read version from addon.xml
    addon_xml = addon_dir / 'addon.xml'
    if not addon_xml.exists():
        print(f"Warning: addon.xml not found in {addon_name}")
        return None

    with open(addon_xml, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract version
    import re
    version_match = re.search(r'version="([^"]+)"', content)
    if not version_match:
        print(f"Warning: Could not find version in {addon_name}/addon.xml")
        return None

    version = version_match.group(1)
    zip_name = f"{addon_name}-{version}.zip"
    zip_path = addon_dir / zip_name

    print(f"Creating {zip_name}...")

    # Create ZIP
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(addon_dir):
            # Skip .git folder and existing zips
            dirs[:] = [d for d in dirs if d != '.git']

            for file in files:
                if file.endswith('.zip'):
                    continue

                file_path = Path(root) / file
                arc_name = addon_name + '/' + str(file_path.relative_to(addon_dir))
                zf.write(file_path, arc_name)

    print(f"  Created: {zip_path}")
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
        print(f"Created addons.xml.md5: {md5_hash}")


def main():
    print("=" * 50)
    print("FamilyFlix Repository Builder")
    print("=" * 50)
    print()

    # Create ZIP files for each addon
    for addon in ADDONS:
        create_zip(addon)

    print()

    # Generate MD5 for addons.xml
    update_addons_xml_md5()

    print()
    print("=" * 50)
    print("Build complete!")
    print()
    print("Next steps:")
    print("1. Commit and push to GitHub")
    print("2. Enable GitHub Pages (Settings -> Pages -> main branch)")
    print("3. Your repository URL will be:")
    print("   https://triffalin.github.io/repository.familyflix/")
    print("=" * 50)


if __name__ == '__main__':
    main()
