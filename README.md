# desktop_entry_creator
Easy to use desktop entry creator linux.
When downloading standalone binaries, shell scripts, or AppImages on Linux, manual installation often leaves you launching programs from the terminal or hunting through file directories. Desktop Entry Creator solves this by providing a clean, graphical interface to register custom software directly into your system's application grid and launcher.

Built specifically for modern GNOME desktop environments using GTK 4 and Libadwaita, it adheres to FreeDesktop standards to make non-standard software feel like native system apps in just a few clicks.

Key Features
Native Modern UI: Built with Libadwaita for a polished, adaptive layout that seamlessly follows your desktop's light and dark appearance settings.

Executable & Icon Management: Graphical file pickers simplify assigning executables (.AppImage, .sh, binary) and custom application icons (.png, .svg).

Automatic Permission Handling: Automatically applies execution permissions (chmod +x) to selected target files and generated shortcuts, eliminating manual terminal commands.

Categorization & Launch Modes: Organize entries under standard system categories (Development, Games, Utilities, Audio/Video) and toggle dedicated terminal execution for CLI tools.

Instant Launcher Sync: Instantly refreshes the local desktop database (~/.local/share/applications) so newly created shortcuts appear immediately in app drawers and application launchers like GNOME Shell, KRunner, or Rofi.
