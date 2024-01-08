import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
import subprocess

class KeyboardLayoutConfigurator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Layout Configurator")
        self.set_default_size(700, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        # Create a vertical box (MAIN Container)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Info text container (Vertical)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        vbox.pack_start(info_box, False, False, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            f"KEYBOARD LAYOUT"
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Which keyboard layout would you like to use on this system?\n"
            f"The keyboard layout can be changed later and additional keyboard layouts can also be added if you want to use more than just one keyboard layout on this system."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        # Create a horizontal box (MAIN INNER CONTAINER)
        container_main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_valign(Gtk.Align.CENTER)
        container_main.set_margin_top(20)
        vbox.add(container_main)
        container_main_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main.add(container_main_1)
        container_main.add(container_main_2)


        # Create a horizontal box (INNER CONTAINER)
        container_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main_1.add(container_1)

        # Create a combo box for layouts
        layout_label = Gtk.Label("Select Layout:")
        container_1.pack_start(layout_label, False, False, 0)
        self.layout_combo = Gtk.ComboBoxText()
        self.populate_layouts()
        self.layout_combo.connect("changed", self.on_layout_changed)
        container_1.pack_start(self.layout_combo, False, False, 0)

        # Create a horizontal box (INNER CONTAINER)
        container_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main_1.add(container_2)

        # Create a combo box for variants
        variant_label = Gtk.Label("Select Variant:")
        container_1.pack_start(variant_label, False, False, 0)
        self.variant_combo = Gtk.ComboBoxText()
        self.populate_variants()
        self.variant_combo.connect("changed", self.on_variant_changed)
        container_1.pack_start(self.variant_combo, False, False, 0)

        # Options entry
        options_label = Gtk.Label(label="Options:")
        container_1.pack_start(options_label, False, False, 0)
        self.option_combo = Gtk.ComboBoxText()
        self.populate_options()
        self.option_combo.connect("changed", self.on_option_changed)
        container_1.pack_start(self.option_combo, False, False, 0)

        # Create a horizontal box (INNER CONTAINER)
        container_3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main_2.add(container_3)

        # Create an entry for testing
        self.textview = Gtk.TextView()
        self.textview.set_size_request(300,200) # W x H
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textview.set_border_width(10)
        self.textview.connect("focus-in-event", self.on_textview_focus_in)
        self.textview.connect("focus-out-event", self.on_textview_focus_out)
        container_3.pack_start(self.textview, False, False, 0)

        # Create a horizontal box (INNER CONTAINER)
        container_4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_4.set_margin_top(20)
        container_4.set_halign(Gtk.Align.CENTER)
        container_4.set_valign(Gtk.Align.CENTER)
        vbox.add(container_4)

        reset_button = Gtk.Button("Reset")
        reset_button.connect("clicked", self.reset_keyboard_layout)
        container_4.pack_start(reset_button, False, False, 0)

        # Create a button for saving
        save_button = Gtk.Button("Save")
        save_button.connect("clicked", self.save_keyboard_layout)
        container_4.pack_start(save_button, False, False, 0)

    def populate_layouts(self):
        # Use localectl to get available layouts
        result = subprocess.run(['localectl', 'list-x11-keymap-layouts'], capture_output=True, text=True)
        layouts = result.stdout.strip().split('\n')

        for layout in layouts:
            self.layout_combo.append_text(layout)

        # This option will configured with the language selection tool in the welcome window:
        selected_language_option = 0

        self.layout_combo.set_active(selected_language_option)

    def populate_variants(self):
        # Use localectl to get available variants for the selected layout
        current_layout = self.layout_combo.get_active_text()
        result = subprocess.run(['localectl', 'list-x11-keymap-variants', current_layout], capture_output=True, text=True)
        variants = result.stdout.strip().split('\n')

        for variant in variants:
            self.variant_combo.append_text(variant)

        self.variant_combo.set_active(0)

    def populate_options(self):
        result = subprocess.run(['localectl', 'list-x11-keymap-options'], capture_output=True, text=True)
        options = result.stdout.strip().split('\n')

        for option in options:
            self.option_combo.append_text(option)

        self.option_combo.set_active(-1)

    def on_layout_changed(self, combo):
        self.variant_combo.remove_all()
        self.populate_variants()

    def on_variant_changed(self, combo):
        pass  # Additional actions when variant is changed, if needed

    def on_option_changed(self, combo):
        pass  # Additional actions when variant is changed, if needed

    def on_textview_focus_in(self, widget, event):
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()
        option = self.option_combo.get_active_text()

        subprocess.run(['setxkbmap', layout, variant, '-option', option])      

        self.textbuffer.set_text("")  # Clear the text when entry is clicked      

    def on_textview_focus_out(self, widget, event):
        # Callback for focus-out-event
        text = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)
        if not text.strip():
            self.textbuffer.set_text("Type here to test your keyboard ...")

    def reset_keyboard_layout(self, button):
        layout = "us"
        variant = "intl"
        subprocess.run(['setxkbmap', layout, variant, '-option']) 

    def save_keyboard_layout(self, button):
        # Additional code to save the configured keyboard layout
        pass

if __name__ == "__main__":
    win = KeyboardLayoutConfigurator()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
