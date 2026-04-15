# Water Workshop

GTA water plane editor — part of IMG Factory 1.6, also runs standalone.

Supports GTA III / Vice City / PS2 LC / SOL (waterpro.dat binary) and GTA SA (water.dat quads).

## Running standalone

```bash
pip install PyQt6 Pillow
python3 water_workshop_main.py
python3 water_workshop_main.py /path/to/waterpro.dat
```

## Features

- **waterpro.dat** (binary) — GTA III, Vice City, PS2 LC, SOL
  - Physical grid (64×64 for III/VC, 384×384 for SOL) + Visible grid (2× size)
  - Multiple water height levels (SOL uses 4 levels at different Z values)
  - Multi-level colour rendering: sea (blue), elevated water (darker blue), land (brown)
- **water.dat** (text) — GTA III / VC / PS2
  - Axis-aligned water rectangles: level, x1, y1, x2, y2
- **SA water.dat** (text) — GTA San Andreas
  - 4-corner quads with 5 float properties + type flag

## Draw tools
- Pencil, Line, Rect outline, Filled rect, Flood fill, Colour picker, Zoom
- Left-click = draw sea (value 0), Right-click = draw land (value 128)
- Scroll wheel = zoom centred on cursor, Middle mouse = pan
- Ctrl+Z/Y = undo/redo (20 levels per grid)
- Flip display colours toggle (data unchanged)
- Grid offset / shift dialog (±8192 world units X/Y, Z adjusts all water heights)

## Export / Import
- Export physical and visible grids as BMP (90° rotation matches WaterproGen)
- Import BMP grid (auto-detects physical vs visible by image size)

## Directory layout
```
water_workshop_main.py               # standalone launcher
apps/
  components/Water_Editor/
    water_workshop.py                # main application
    depends/
      gui_workshop.py                # UI base class (standalone copy)
  methods/imgfactory_svg_icons.py    # SVG icon factory
  themes/                            # 37 colour themes (.json)
  utils/app_settings_system.py       # theme/settings system
  core/theme_utils.py                # dialog theming
```

## Author
X-Seti — Apr 2026
