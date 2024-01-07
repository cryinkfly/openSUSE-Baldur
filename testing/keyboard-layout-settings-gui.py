import gi
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class KeyboardLayoutConfigurator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Layout Configurator")
        self.set_default_size(500, 350)
        self.set_border_width(10)

        # Layout dropdown
        self.layout_label = Gtk.Label(label="Select Layout:")
        self.layout_combo = Gtk.ComboBoxText()
        self.populate_layouts()
        self.layout_combo.connect("changed", self.on_layout_changed)

        # Variant dropdown
        self.variant_label = Gtk.Label(label="Select Variant:")
        self.variant_combo = Gtk.ComboBoxText()
        self.populate_variants()
        self.variant_combo.connect("changed", self.on_variant_changed)

        # Options entry
        self.options_label = Gtk.Label(label="Options:")
        self.options_entry = Gtk.Entry()

        # Test button
        self.test_button = Gtk.Button(label="Check your keyboard settings")
        self.test_button.connect("clicked", self.test_keyboard_layout)

        # Save button
        self.save_button = Gtk.Button(label="Save")
        self.save_button.connect("clicked", self.save_keyboard_layout)
        self.save_button.set_hexpand(True)
        self.save_button.set_vexpand(True)

        # Text entry for testing keyboard layout
        self.test_entry = Gtk.Entry()
        self.test_entry.set_text("Type here to test your keyboard ...")
        self.test_entry.connect("focus-in-event", self.on_entry_clicked)
        self.test_entry.connect("focus-out-event", self.off_entry_clicked)

        # Layout
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        grid.attach(self.layout_label, 0, 0, 1, 1)
        grid.attach(self.layout_combo, 1, 0, 1, 1)
        grid.attach(self.variant_label, 0, 1, 1, 1)
        grid.attach(self.variant_combo, 1, 1, 1, 1)
        grid.attach(self.options_label, 0, 2, 1, 1)
        grid.attach(self.options_entry, 1, 2, 1, 1)
        grid.attach(self.test_button, 0, 3, 2, 1)
        grid.attach(self.test_entry, 0, 4, 2, 1)
        grid.attach(self.save_button, 0, 5, 2, 1)

        # Set horizontal and vertical expansion for the grid
        grid.set_hexpand(True)
        grid.set_vexpand(True)

        self.add(grid)

    def populate_layouts(self):
        # Use localectl to get available layouts
        result = subprocess.run(['localectl', 'list-x11-keymap-layouts'], capture_output=True, text=True)
        layouts = result.stdout.strip().split('\n')

        for layout in layouts:
            self.layout_combo.append_text(layout)

        self.layout_combo.set_active(0)

    def populate_variants(self):
        # Use localectl to get available variants for the selected layout
        current_layout = self.layout_combo.get_active_text()
        result = subprocess.run(['localectl', 'list-x11-keymap-variants', current_layout], capture_output=True, text=True)
        variants = result.stdout.strip().split('\n')

        for variant in variants:
            self.variant_combo.append_text(variant)

        self.variant_combo.set_active(0)

    def on_layout_changed(self, combo):
        self.variant_combo.remove_all()
        self.populate_variants()

    def on_variant_changed(self, combo):
        pass  # Additional actions when variant is changed, if needed

    def test_keyboard_layout(self, button):
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()
        options = self.options_entry.get_text()

        # Set the keyboard layout for testing
        subprocess.run(['setxkbmap', layout, variant, '-option', options])

        # Use the test entry to allow the user to type and test the configured layout
        self.test_entry.set_text("Type here to test your keyboard ...")
        self.test_entry.connect("focus-in-event", self.on_entry_clicked)

    def on_entry_clicked(self, entry, event):
        self.test_entry.set_text("")  # Clear the text when entry is clicked

    def off_entry_clicked(self, entry, event):
        self.test_entry.set_text("Type here to test your keyboard ...")

    def save_keyboard_layout(self, button):
        # Additional code to save the configured keyboard layout
        pass

win = KeyboardLayoutConfigurator()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
