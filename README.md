# FamilyFlix Repository

Repository privat Kodi pentru skinul FamilyFlix - complet independent, conține toate dependențele necesare.

## Instalare în Kodi

### Pasul 1: Adaugă sursa repository-ului

1. Deschide Kodi
2. Mergi la **Settings → File Manager → Add source**
3. Introdu URL-ul: `https://triffalin.github.io/repository.familyflix/`
4. Denumește-l: `FamilyFlix`
5. Click **OK**

### Pasul 2: Instalează repository-ul

1. Mergi la **Settings → Add-ons → Install from zip file**
2. Selectează **FamilyFlix**
3. Selectează **repository.familyflix** → Instalează `repository.familyflix-1.0.0.zip`

### Pasul 3: Instalează skinul FamilyFlix

1. Mergi la **Settings → Add-ons → Install from repository**
2. Selectează **FamilyFlix Repository**
3. Mergi la **Look and feel → Skin**
4. Instalează **FamilyFlix**
5. Când întreabă dacă vrei să schimbi skinul, alege **Yes**

## Conținut Repository

Acest repository conține toate addon-urile necesare:

| Addon | Descriere |
|-------|-----------|
| **skin.familyflix** | Skinul principal Netflix-style |
| script.bingie.helper | Helper pentru funcționalitățile skinului |
| script.bingie.toolbox | Toolbox pentru skin |
| script.bingie.widgets | Widgeturi pentru skin |
| plugin.video.tmdb.bingie.helper | Integrare TMDb pentru informații filme/seriale |
| plugin.program.autocompletion | Autocomplete pentru tastatură |
| script.module.bingie | Modul comun |
| script.skin.helper.colorpicker | Color picker pentru personalizare |
| script.skin.helper.skinbackup | Backup setări skin |
| screensaver.bingie | Screensaver Netflix-style |
| resource.images.studios.coloured | Iconuri studiourilor |

## Dezvoltare

### Workflow pentru modificări:

1. Modifică fișierele în `skin.familyflix/`
2. Rulează scriptul de build:
   ```bash
   python build_repository.py
   ```
3. Commit și push:
   ```bash
   git add .
   git commit -m "Descriere modificări"
   git push
   ```
4. Așteaptă 1-2 minute pentru GitHub Pages să se actualizeze
5. În Kodi: **Settings → Add-ons → Check for updates**

### Structura skinului:

```
skin.familyflix/
├── addon.xml           ← Identitate și dependențe
├── colors/defaults.xml ← Schema de culori
├── 1080i/              ← Toate layout-urile XML
│   ├── Home.xml        ← Ecranul principal
│   ├── Includes*.xml   ← Componente reutilizabile
│   └── Dialog*.xml     ← Dialoguri și popupuri
├── shortcuts/          ← Configurație meniu
│   └── mainmenu.DATA.xml ← Meniul principal
├── fonts/              ← Fișiere font
└── media/Textures.xbt  ← Imagini comprimate
```

## Credite

Bazat pe excelentul [Bingie skin](https://github.com/matke-84/skin.bingie) de matke-84.

## Licență

GPL v2.0
