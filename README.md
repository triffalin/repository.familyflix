# FamilyFlix Repository

Private Kodi repository for the FamilyFlix skin.

## Installation

### Method 1: Add Repository Source (Recommended)

1. Open Kodi
2. Go to **Settings → File Manager → Add source**
3. Enter URL: `https://triffalin.github.io/repository.familyflix/`
4. Name it: `FamilyFlix`
5. Go to **Settings → Add-ons → Install from zip file**
6. Select `FamilyFlix` → `repository.familyflix` → Install
7. Go to **Install from repository → FamilyFlix Repository → Look and feel → Skin**
8. Install **FamilyFlix**

### Method 2: Direct ZIP Install

Download and install directly:
- [repository.familyflix-1.0.0.zip](repository.familyflix/repository.familyflix-1.0.0.zip)
- [skin.familyflix-1.0.0.zip](skin.familyflix/skin.familyflix-1.0.0.zip)

## Requirements

This skin requires addons from the Bingie repository:
- script.bingie.helper
- script.bingie.toolbox
- script.bingie.widgets
- script.skinshortcuts

Install the Bingie repository first: `https://matke-84.github.io/repository.bingie/`

## Development

To update the repository after making changes:

```bash
python build_repository.py
git add .
git commit -m "Update skin"
git push
```

## Credits

Based on the excellent [Bingie skin](https://github.com/matke-84/skin.bingie) by matke-84.
