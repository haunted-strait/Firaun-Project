# KMK Firmware Starter for Custom Productivity Keyboard
# License: MIT

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# Inisialisasi Modul Layer untuk Switch OS (Mac / Windows / Android)
layers = Layers()
keyboard.modules.append(layers)

# --- DEFINISI SHORTCUT MAKRO PRODUKTIVITAS ---
# Shortcut untuk Layer Windows
WIN_COPY = KC.LCTRL(KC.C)
WIN_PASTE = KC.LCTRL(KC.V)
WIN_CUT = KC.LCTRL(KC.X)
WIN_UNDO = KC.LCTRL(KC.Z)
WIN_ZOOM_IN = KC.LCTRL(KC.EQUAL)
WIN_ZOOM_OUT = KC.LCTRL(KC.MINUS)

# Shortcut untuk Layer Mac
MAC_COPY = KC.LCMD(KC.C)
MAC_PASTE = KC.LCMD(KC.V)
MAC_CUT = KC.LCMD(KC.X)
MAC_UNDO = KC.LCMD(KC.Z)
MAC_ZOOM_IN = KC.LCMD(KC.EQUAL)
MAC_ZOOM_OUT = KC.LCMD(KC.MINUS)

# --- DEFINISI PIN MATRIX (Disesuaikan saat PCB Selesai) ---
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7)

# --- MAPPING TATA LETAK TOMBOL (KEYMAP MATRIX) ---
keyboard.keymap = [
    # LAYER 0: Windows Mode (Default)
    [
        WIN_ZOOM_IN, WIN_ZOOM_OUT, KC.NO,        KC.ESC,
        WIN_COPY,    WIN_CUT,      WIN_PASTE,   KC.DELETE,
        WIN_UNDO,    KC.KP_9,      KC.KP_8,     KC.KP_7, # Inverted Numpad
        KC.LCTRL,    KC.LALT,      KC.LGUI,     KC.SPACE,
    ],
    # LAYER 1: Mac Mode (Diaktifkan via Switch Fisik)
    [
        MAC_ZOOM_IN, MAC_ZOOM_OUT, KC.NO,        KC.ESC,
        MAC_COPY,    MAC_CUT,      MAC_PASTE,   MAC_UNDO,
        MAC_UNDO,    KC.KP_9,      KC.KP_8,     KC.KP_7,
        KC.LCMD,     KC.LOPT,      KC.LCTRL,    KC.SPACE,
    ]
]

if __name__ == '__main__':
    keyboard.go()
