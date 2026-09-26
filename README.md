# Desktop Entry Creator

![Target Distribution](https://img.shields.io/badge/distro-CachyOS%20%7C%20Arch%20Linux-blue?logo=archlinux)
![UI Toolkit](https://img.shields.io/badge/GTK4-Libadwaita-3584e4?logo=gnome)
![Language](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A modern, lightweight GTK 4 and Libadwaita utility designed for Arch-based Linux distributions like **CachyOS**. **Desktop Entry Creator** allows you to easily generate application shortcuts (`.desktop` files) for manually downloaded binaries, AppImages, and custom scripts without using the terminal or editing configuration files.

---

## ✨ Features

- 🎨 **Modern Libadwaita Interface**: Designed according to GNOME Human Interface Guidelines with automatic dark and light theme switching.
- ⚡ **Auto Executable Permission**: Automatically executes `chmod +x` on selected target binaries/AppImages and created shortcut files.
- 🖼️ **Native File Selection**: Simple file picking for application executables and custom image icons (`.png`, `.svg`, `.xpm`).
- 📂 **Standard Categorization**: Organize your apps under official FreeDesktop categories (*Utility, Development, Game, Graphics, AudioVideo*, etc.).
- 💻 **Terminal Execution Toggle**: Dedicated switch to configure command-line utilities to launch inside a terminal window.
- 🔄 **Instant Database Refresh**: Automatically triggers `update-desktop-database` on creation so new apps show up instantly in launchers like GNOME Shell, Rofi, or KRunner.

---

## 🛠️ Project Structure

```text
auto-desktop/
├── desktop_creator.py                      # Main Application Logic
├── com.example.DesktopEntryCreator.desktop # System Desktop Entry
├── PKGBUILD                                # Arch/CachyOS Package Build Script
├── README.md                               # Project Documentation
└── LICENSE                                 # License File
```

---

## 📦 Installation

### Option 1: Install Pre-built Arch Package (`.pkg.tar.zst`)

If you downloaded or built the `.pkg.tar.zst` package file, install it using `pacman`:

```fish
sudo pacman -U desktop-entry-creator-1.0-1-any.pkg.tar.zst
```

### Option 2: Build from Source (`PKGBUILD`)

1. Clone the repository:
   ```fish
   git clone https://github.com/your-username/auto-desktop.git
   cd auto-desktop
   ```

2. Compile and install using `makepkg`:
   ```fish
   makepkg -si
   ```

---

## 📋 System Dependencies

The package requires the following standard system libraries (handled automatically when installing via `pacman`):

- `python-gobject` (PyGObject bindings)
- `gtk4` (GTK4 UI toolkit)
- `libadwaita` (Libadwaita building blocks)
- `desktop-file-utils` (For refreshing local desktop entries)

---

## 🚀 Usage

Launch the app from your desktop launcher/app drawer, or directly from your terminal:

```fish
desktop-creator
```

### Creating a Shortcut
1. Enter the **Application Name** and optional **Description**.
2. Click **Browse** under *Executable Path* and select your executable, script, or `.AppImage`.
3. Click **Browse** under *Icon Image* and pick a `.png` or `.svg` icon.
4. Choose the application **Category** and toggle **Run in Terminal** if needed.
5. Click **Create Desktop Entry**. Your app will immediately appear in your launcher!

