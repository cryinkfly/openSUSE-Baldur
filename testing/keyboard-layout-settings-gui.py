import gi
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class KeyboardLayoutSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Layout Selector")
        self.set_border_width(10)

        # Fetch available layouts
        self.layouts = self.get_keyboard_layouts()

        # Layout ComboBox
        self.layout_label = Gtk.Label(label="Select Keyboard Layout:")
        self.layout_combo = Gtk.ComboBoxText()
        for layout in self.layouts:
            self.layout_combo.append_text(layout)
        self.layout_combo.connect("changed", self.on_layout_selected)

        # Variant ComboBox
        self.variant_label = Gtk.Label(label="Select Keyboard Variant:")
        self.variant_combo = Gtk.ComboBoxText()
        self.variant_combo.connect("changed", self.on_variant_selected)

        # Apply Button
        self.apply_button = Gtk.Button(label="Apply")
        self.apply_button.connect("clicked", self.apply_layout)

        # Grid layout
        grid = Gtk.Grid()
        grid.attach(self.layout_label, 0, 0, 1, 1)
        grid.attach(self.layout_combo, 1, 0, 1, 1)
        grid.attach(self.variant_label, 0, 1, 1, 1)
        grid.attach(self.variant_combo, 1, 1, 1, 1)
        grid.attach(self.apply_button, 0, 2, 2, 1)

        self.add(grid)

    def get_keyboard_layouts(self):
        # Get list of keyboard layouts using localectl
        try:
            result = subprocess.run(["localectl", "list-x11-keymap-layouts"], capture_output=True, text=True)
            layouts = result.stdout.strip().split('\n')
            return layouts
        except Exception as e:
            print(f"Error fetching keyboard layouts: {e}")
            return []

    def get_keyboard_variants(self, layout):
        # Get list of keyboard variants for a given layout using localectl
        try:
            result = subprocess.run(["localectl", "list-x11-keymap-variants", layout], capture_output=True, text=True)
            variants = result.stdout.strip().split('\n')
            return variants
        except Exception as e:
            print(f"Error fetching keyboard variants: {e}")
            return []

    def on_layout_selected(self, combo):
        # Update variant combo based on selected layout
        active_layout = combo.get_active_text()
        self.variant_combo.remove_all()
        variants = self.get_keyboard_variants(active_layout)
        for variant in variants:
            self.variant_combo.append_text(variant)

    def on_variant_selected(self, combo):
        pass

    def apply_layout(self, button):
        # Apply selected layout and variant using setxkbmap
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()

        try:
            subprocess.run(["setxkbmap", layout, variant])
            print(f"Keyboard layout set to {layout} {variant}")
        except Exception as e:
            print(f"Error applying keyboard layout: {e}")

if __name__ == "__main__":
    win = KeyboardLayoutSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
