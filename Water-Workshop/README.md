# Radar Workshop

GTA water editor — part of IMG Factory 1.6, also runs standalone.

Supports GTA III / VC / SA / LCS / VCS (PC, PS2, Xbox) and GTA SOL.

## Features

## Running standalone

```bash
pip install PyQt6 Pillow
python3 water_workshop.py
python3 water_workshop.py /path/to/gta3.img
```

## Directory layout
```
apps/
  components/Water_Editor/water_workshop.py   # main application
  methods/imgfactory_svg_icons.py             # SVG icon factory
  themes/                                     # colour themes (.json)
  utils/app_settings_system.py               # theme/settings system
  core/theme_utils.py                        # dialog theming
water_workshop_main.py                        # standalone launcher
```

## Author
X-Seti — Apr 2026
