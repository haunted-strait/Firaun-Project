# Open-Source Low-Profile Productivity Keyboard ⌨️🚀

A custom, low-profile mechanical keyboard designed specifically for creators, video editors, designers, and heavy document workers. Built on top of open-source firmware (KMK / QMK / ZMK) with native multi-OS support.

## 🌟 Key Features
- **Low-Profile Form Factor:** Inspired by sleek designs like the Keychron K5, using Kailh Choc / Gateron Low Profile switches.
- **Dedicated Productivity Keys:** Hardware-level macro buttons for `Copy`, `Cut`, `Paste`, `Undo`, `Redo`, `Zoom In`, and `Zoom Out`.
- **Inverted Numpad Layout:** Ergonomically adjusted 9-8-7 top-row numpad layout for faster numerical data entry.
- **Hardware OS Switch:** Physical switch on the front edge to toggle between macOS, Windows, and Android layout layers natively.
- **Fully Customizable:** Open-source firmware compatible with VIAL / VIA for GUI-based key remapping without coding knowledge.

## 🛠️ Hardware & Specs Target
- **MCU:** Raspberry Pi RP2040 or nRF52840 (for Bluetooth)
- **Firmware Framework:** KMK (CircuitPython) / QMK / ZMK
- **Hot-swappable:** Low-profile hot-swap sockets
- **Layout:** Full-size custom productivity layout

## 📁 Repository Structure

├── hardware/          # KiCad schematics and PCB designs (WIP)
├── case/              # 3D printable STL/STEP files for casing (WIP)
└── firmware/          # KMK / QMK source code and keymaps

## 🤝 How to Contribute
This project is in its early conceptual stage! We are actively looking for collaborators:
- **PCB Designers:** Help design the KiCad PCB schematic & matrix routing.
- **Firmware Developers:** Help refine the matrix configuration and OS layer switching logic.
- **3D / Industrial Designers:** Help design low-profile case files.

Feel free to open an **Issue** or submit a **Pull Request** if you want to contribute!
