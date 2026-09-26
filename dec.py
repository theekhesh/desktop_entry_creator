#!/usr/bin/env python3
import os
import sys
import subprocess
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio, GLib


class DesktopEntryApp(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id="com.example.DesktopEntryCreator",
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS
        )

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()


class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("Desktop Entry Creator")
        self.set_default_size(500, 580)

        self.exec_path = ""
        self.icon_path = ""

        # Root Layout
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_content(main_box)

        # Header Bar
        header = Adw.HeaderBar()
        main_box.append(header)

        # Centered Clamp for GNOME Design Guidelines
        clamp = Adw.Clamp(maximum_size=600)
        main_box.append(clamp)

        preferences_page = Adw.PreferencesPage()
        clamp.set_child(preferences_page)

        # Section 1: Application Information
        group_info = Adw.PreferencesGroup(title="Application Metadata")
        preferences_page.add(group_info)

        self.name_row = Adw.EntryRow(title="Application Name")
        group_info.add(self.name_row)

        self.comment_row = Adw.EntryRow(title="Description / Comment")
        group_info.add(self.comment_row)

        # Executable File Picker
        self.exec_row = Adw.ActionRow(
            title="Executable Path", 
            subtitle="Binary, Shell Script, or AppImage"
        )
        exec_btn = Gtk.Button(label="Browse…")
        exec_btn.set_valign(Gtk.Align.CENTER)
        exec_btn.connect("clicked", self.on_select_exec)
        self.exec_row.add_suffix(exec_btn)
        group_info.add(self.exec_row)

        # Icon File Picker
        self.icon_row = Adw.ActionRow(
            title="Icon Image", 
            subtitle="Select PNG, SVG, or XPM file"
        )
        icon_btn = Gtk.Button(label="Browse…")
        icon_btn.set_valign(Gtk.Align.CENTER)
        icon_btn.connect("clicked", self.on_select_icon)
        self.icon_row.add_suffix(icon_btn)
        group_info.add(self.icon_row)

        # Section 2: Categories and Execution Options
        group_options = Adw.PreferencesGroup(title="Configuration Options")
        preferences_page.add(group_options)

        # Categories Dropdown
        self.categories = [
            "Utility", "Development", "Game", "Graphics", 
            "Network", "Office", "AudioVideo", "System"
        ]
        self.cat_model = Gtk.StringList.new(self.categories)
        self.cat_row = Adw.ComboRow(title="Category", model=self.cat_model)
        group_options.add(self.cat_row)

        # Terminal Switch
        self.terminal_row = Adw.SwitchRow(title="Run in Terminal")
        group_options.add(self.terminal_row)

        # Section 3: Save Action
        group_action = Adw.PreferencesGroup()
        preferences_page.add(group_action)

        create_btn = Gtk.Button(label="Create Desktop Entry")
        create_btn.add_css_class("suggested-action")
        create_btn.add_css_class("pill")
        create_btn.connect("clicked", self.on_create_entry)
        group_action.add(create_btn)

    def on_select_exec(self, widget):
        dialog = Gtk.FileChooserNative.new(
            "Select Executable File", self, Gtk.FileChooserAction.OPEN, "Select", "Cancel"
        )
        dialog.connect("response", self._on_exec_selected)
        dialog.show()

    def _on_exec_selected(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            self.exec_path = dialog.get_file().get_path()
            self.exec_row.set_subtitle(self.exec_path)
        dialog.destroy()

    def on_select_icon(self, widget):
        dialog = Gtk.FileChooserNative.new(
            "Select Icon File", self, Gtk.FileChooserAction.OPEN, "Select", "Cancel"
        )
        
        filter_img = Gtk.FileFilter()
        filter_img.set_name("Images (*.png, *.svg, *.xpm)")
        filter_img.add_mime_type("image/png")
        filter_img.add_mime_type("image/svg+xml")
        filter_img.add_mime_type("image/x-xpixmap")
        dialog.add_filter(filter_img)

        dialog.connect("response", self._on_icon_selected)
        dialog.show()

    def _on_icon_selected(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            self.icon_path = dialog.get_file().get_path()
            self.icon_row.set_subtitle(self.icon_path)
        dialog.destroy()

    def show_alert(self, title, body):
        dialog = Adw.MessageDialog.new(self, title, body)
        dialog.add_response("ok", "OK")
        dialog.show()

    def on_create_entry(self, widget):
        name = self.name_row.get_text().strip()
        comment = self.comment_row.get_text().strip()
        category = self.categories[self.cat_row.get_selected()]
        terminal = "true" if self.terminal_row.get_active() else "false"

        if not name or not self.exec_path:
            self.show_alert("Missing Information", "Please enter an Application Name and select an Executable Path.")
            return

        # Ensure executable file permissions are set (chmod +x)
        try:
            os.chmod(self.exec_path, 0o755)
        except Exception as e:
            print(f"Warning: Could not set execution permission: {e}")

        # Desktop Entry File standard template
        desktop_content = f"""[Desktop Entry]
Type=Application
Version=1.0
Name={name}
Comment={comment}
Exec="{self.exec_path}"
Icon={self.icon_path}
Terminal={terminal}
Categories={category};
"""

        # Write to user-specific desktop applications directory
        target_dir = os.path.expanduser("~/.local/share/applications")
        os.makedirs(target_dir, exist_ok=True)

        slug = "".join(c if c.isalnum() else "-" for c in name.lower()).strip("-")
        file_path = os.path.join(target_dir, f"{slug}.desktop")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(desktop_content)
            os.chmod(file_path, 0o755)

            # Update the desktop entries database cache
            subprocess.run(["update-desktop-database", target_dir], check=False)

            self.show_alert("Success", f"Desktop entry created successfully at:\n{file_path}")
        except Exception as e:
            self.show_alert("Error", f"Failed to save desktop entry: {str(e)}")


if __name__ == "__main__":
    app = DesktopEntryApp()
    app.run(sys.argv)
