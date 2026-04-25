#!/usr/bin/env python3
# water_workshop_main.py - Standalone launcher for Water Workshop
# X-Seti - Apr 2026
#
# Usage:
#   python3 water_workshop_main.py
#   python3 water_workshop_main.py /path/to/waterpro.dat
#
# Requires: PyQt6, Pillow

import sys
import os
from pathlib import Path

# Add repo root to path so 'apps' package resolves
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Water Workshop")
    app.setOrganizationName("X-Seti")

    from apps.components.Water_Editor.water_workshop import WaterWorkshop

    win = WaterWorkshop(parent=None, main_window=None)
    win.setWindowTitle("Water Workshop — Standalone")
    win.resize(1300, 800)
    win.show()

    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            win._load_file(path)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
