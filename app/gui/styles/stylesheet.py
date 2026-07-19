from .colors import *


APP_STYLESHEET = f"""
QMainWindow {{
    background-color: {BACKGROUND};
}}

QWidget {{
    background-color: {BACKGROUND};
    color: {TEXT};
    font-size: 11pt;
}}

QMenuBar {{
    background-color: {SURFACE};
    color: {TEXT};
}}

QMenuBar::item {{
    spacing: 6px;
    padding: 6px 12px;
}}

QMenuBar::item:selected {{
    background: {PRIMARY};
}}

QMenu {{
    background-color: {SURFACE};
    color: {TEXT};
}}

QStatusBar {{
    background-color: {SURFACE};
    color: {TEXT};
}}

QToolBar {{
    background-color: {SURFACE};
    spacing: 6px;
    border: none;
    padding: 6px;
}}

QPushButton {{
    background-color: {PRIMARY};
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
}}

QPushButton:hover {{
    background-color: {PRIMARY_HOVER};
}}

QComboBox {{
    background-color: {SURFACE};
    border: 1px solid {BORDER};
    padding: 6px;
    border-radius: 6px;
}}

QLabel {{
    color: {TEXT};
}}
"""