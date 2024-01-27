#!/usr/bin/python

####################################################################################################
# Name:         openSUSE Baldur - XFCE-Initial-Setup                                               #
# Description:  This file calls the graphical XFCE-Initial-Setup!                                  #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2024                                                                               #
# Time/Date:    xx:xx/xx.xx.xxxx                                                                   #
# Version:      1.0.0                                                                              #
####################################################################################################

# Directory structure:
# --------------------

# /usr/bin/xfce-initial-setup/xfce-initial-setup.py
# /usr/bin/xfce-initial-setup/localization
# /usr/bin/xfce-initial-setup/graphics
# /usr/bin/xfce-initial-setup/styles
# /usr/bin/xfce-initial-setup/logs

####################################################################################################
####################################################################################################

import gi
gi.require_versions({'Gtk': '3.0', 'Gdk': '3.0'})
from gi.repository import Gdk, GdkPixbuf, Gio, GObject, Gtk, Pango
import urllib.request
from urllib.error import URLError
import subprocess, os

####################################################################################################
####################################################################################################

# Reading/Importing the styles:
class UI_CSS_Style:
    @staticmethod
    def importing__css_styles():
        style_provider = Gtk.CssProvider()

        # Load the CSS file:
        css_file = Gio.File.new_for_path("styles/default.css")
        css_data = css_file.load_contents(None)[1].decode('utf-8')
        style_provider.load_from_data(css_data.encode('utf-8'))

        # Add the style provider to the default style context
        Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    importing__css_styles()

####################################################################################################
####################################################################################################

# Reading/Importing the languages:
class Languages:

    keyboard_layout = 0
    keyboard_variant = 0

    @staticmethod
    def configuring_languages_environment(current_window, selected_language):
        # Do something with the selected language
        if selected_language == "Afrikaans":

            # Configuring the correct keyboard settings
            Languages.keyboard_layout = 0
            Languages.keyboard_variant = 0

            try:
                with open('localization/af_ZA/locale.txt', 'r', encoding='utf-8') as file:
                    locale_variables = [line.strip() for line in file.readlines()]

                # Update buttons on the current window
                if hasattr(current_window, 'previous_button_label'):
                    current_window.previous_button_label = locale_variables[0]
                    current_window.previous_button.set_label(current_window.previous_button_label)
                if hasattr(current_window, 'next_button_label'):
                    current_window.next_button_label = locale_variables[1]
                    current_window.next_button.set_label(current_window.next_button_label)

                # Update other UI elements based on the current window type
                if isinstance(current_window, Language_Selection_Window):
                    current_window.set_title(locale_variables[2])
                    current_window.new_title_label = f'<span font_size="20000"><b>{locale_variables[2]}</b></span>'
                    current_window.title_label.set_markup(current_window.new_title_label)
                elif isinstance(current_window, Keyboard_Configurator_Window):
                    current_window.set_title(locale_variables[3])
                    current_window.new_title_label = f'<span font_size="20000"><b>{locale_variables[3]}</b></span>'
                    current_window.title_label.set_markup(current_window.new_title_label)

                # ...

            except FileNotFoundError:
                print(f"Error: File 'localization/af_ZA/locale.txt' not found.")
            except Exception as e:
                print(f"Error: {e}")

        elif selected_language == "Albanian - Shqipëria":

            # Configuring the correct keyboard settings
            Languages.keyboard_layout = 1
            Languages.keyboard_variant = 0

            # ...

        else:

            # Configuring the correct keyboard settings
            Languages.keyboard_layout = 95
            Languages.keyboard_variant = 20

            # Update buttons on the current window
            if hasattr(current_window, 'previous_button_label'):
                current_window.previous_button_label = "Previous"
                current_window.previous_button.set_label(current_window.previous_button_label)
            if hasattr(current_window, 'next_button_label'):
                current_window.next_button_label = "Next"
                current_window.next_button.set_label(current_window.next_button_label)

            new_title = "Welcome"
            current_window.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            current_window.title_label.set_markup(new_title_label)

            # ...

####################################################################################################
####################################################################################################

class Language_Selection_Window(Gtk.Window):
    #safed_language_variable = None

    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome")
        self.set_default_size(600, 450)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Next button in the top-right corner
        self.next_button_label = "Next"
        self.next_button = Gtk.Button(label=self.next_button_label)
        self.next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Welcome"
        header_bar.pack_end(self.next_button)
        self.set_titlebar(header_bar)

        svg_file_path = "graphics/opensuse-logo-green.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 200, 100)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget for title
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Welcome</b></span>')

        # Read languages from file
        self.languages = self.importing_languages_list_from_file()

        # Create a ListBox to display the languages
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)

        for i, language in enumerate(self.languages):
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            label = Gtk.Label(label=language)
            hbox.pack_start(label, True, True, 0)
            row.add(hbox)
            listbox.add(row)

        # Add the ListBox to a ScrolledWindow
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(listbox)

        # Create a VBox to organize widgets vertically
        vbox = Gtk.VBox(spacing=10)
        vbox.set_margin_top(35)
        vbox.pack_start(image, False, False, 0)
        vbox.pack_start(self.title_label, False, False, 0)
        vbox.pack_start(scrolled_window, True, True, 0)

        # Add the VBox to the window
        self.add(vbox)

        # Connect the "row-activated" signal to the callback function
        listbox.connect("row-activated", self.on_language_selected)

    def importing_languages_list_from_file(self):
        # Accessing lines from Languages class
        with open('localization/languages-list.txt', 'r') as file:
            read_languages = file.readlines()
            languages_list = [read_languages[i - 1].strip() for i in range(13, len(read_languages) + 1, 4)]
        return languages_list

    def on_language_selected(self, listbox, row):
        selected_language = self.languages[row.get_index()]
        self.safed_language_variable = selected_language
        var = self.safed_language_variable
        Languages.configuring_languages_environment(self, selected_language)

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")
        keyboard_configurator_window = Keyboard_Configurator_Window()
        keyboard_configurator_window.connect("destroy", Gtk.main_quit)
        keyboard_configurator_window.show_all()
        self.hide()

        Languages.configuring_languages_environment(keyboard_configurator_window, self.safed_language_variable)

####################################################################################################
####################################################################################################

class Keyboard_Configurator_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Configurator")
        self.set_default_size(600, 450)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Previous button in the top-left corner
        self.previous_button_label = "Previous"
        self.previous_button = Gtk.Button(label=self.previous_button_label)
        self.previous_button.connect("clicked", self.on_previous_clicked)

        # Next button in the top-right corner
        self.next_button_label = "Next"  # Placeholder, replace it with the actual label
        self.next_button = Gtk.Button(label=self.next_button_label)
        self.next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Typing"
        header_bar.pack_start(self.previous_button)
        header_bar.pack_end(self.next_button)
        self.set_titlebar(header_bar)

        svg_file_path = "graphics/keyboard.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 125, 75)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget for title
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Typing</b></span>')

        # Create a label widget for information
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Select your keyboard layout or an input method."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)

        # Create a horizontal box (MAIN INNER CONTAINER)
        container_main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_valign(Gtk.Align.CENTER)
        container_main.set_margin_top(10)

        # Add a style class to the container
        UI_CSS_Style.importing__css_styles()
        container_main.get_style_context().add_class("rounded-box")

        container_main_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main.add(container_main_1)
        container_main.add(container_main_2)

        # Create a horizontal box (INNER CONTAINER)
        container_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_1.set_border_width(20)
        container_main_1.add(container_1)

        # Create a combo box for layouts
        layout_label = Gtk.Label("Select Layout:")
        container_1.pack_start(layout_label, False, False, 0)
        self.layout_combo = Gtk.ComboBoxText()
        self.populate_layouts()
        self.layout_combo.connect("changed", self.on_layout_changed)
        container_1.pack_start(self.layout_combo, False, False, 0)

        # Create a combo box for variants
        variant_label = Gtk.Label("Select Variant:")
        container_1.pack_start(variant_label, False, False, 0)
        self.variant_combo = Gtk.ComboBoxText()
        self.populate_variants()
        self.variant_combo.connect("changed", self.on_variant_changed)
        container_1.pack_start(self.variant_combo, False, False, 0)

        show_configured_keyboard_layout_label = Gtk.Label("Show layout:")
        container_1.pack_start(show_configured_keyboard_layout_label, False, False, 0)
        show_configured_keyboard_layout_button = Gtk.Button("⌨️")
        show_configured_keyboard_layout_button.connect("clicked", self.show_keyboard_layout)
        container_1.pack_start(show_configured_keyboard_layout_button, False, False, 0)

        # Create a horizontal box (INNER CONTAINER)
        container_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_2.set_border_width(20)
        container_main_2.add(container_2)

        # Create an TextView for testing the keyboard settings:
        textview_label = Gtk.Label("Test your layout configuration below:")
        container_2.pack_start(textview_label, False, False, 0)
        self.textview = Gtk.TextView()
        self.textview.set_size_request(340,180) # W x H
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textview.set_border_width(10)
        self.textview.connect("focus-in-event", self.on_textview_focus_in)
        self.textview.connect("focus-out-event", self.on_textview_focus_out)
        container_2.pack_start(self.textview, False, False, 0)

        # Create a VBox to organize widgets vertically
        vbox = Gtk.VBox(spacing=10)
        vbox.set_margin_top(35)
        vbox.pack_start(image, False, False, 0)
        vbox.pack_start(self.title_label, False, False, 0)
        vbox.pack_start(label_info, False, False, 0)
        vbox.pack_start(container_main, False, False, 0)

        # Add the VBox to the window
        self.add(vbox)

    def populate_layouts(self):
        # Use localectl to get available layouts
        result = subprocess.run(['localectl', 'list-x11-keymap-layouts'], capture_output=True, text=True)
        layouts = result.stdout.strip().split('\n')

        for layout in layouts:
            self.layout_combo.append_text(layout)

        keyboard_layout = Languages.keyboard_layout
        self.layout_combo.set_active(keyboard_layout)


    def populate_variants(self):
        # Use localectl to get available variants for the selected layout
        current_layout = self.layout_combo.get_active_text()
        result = subprocess.run(['localectl', 'list-x11-keymap-variants', current_layout], capture_output=True, text=True)
        variants = result.stdout.strip().split('\n')

        for variant in variants:
            self.variant_combo.append_text(variant)

        keyboard_variant = Languages.keyboard_variant
        self.variant_combo.set_active(keyboard_variant)

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

        subprocess.run(['setxkbmap', layout, variant, '-option'])

        self.textbuffer.set_text("")  # Clear the text when entry is clicked

    def on_textview_focus_out(self, widget, event):
        # Callback for focus-out-event
        text = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), True)
        if not text.strip():
            self.textbuffer.set_text("Type here to test your keyboard ...")

        layout = "us"
        variant = "intl"
        subprocess.run(['setxkbmap', layout, variant, '-option'])

    def show_keyboard_layout(self, button):
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()

        show_keyboard_layout_cmd=f"gkbd-keyboard-display -l {layout}$'\t'{variant}"
        os.system(show_keyboard_layout_cmd)

    def check_internet(self):
        if self.is_internet_available():
            time_zone_configurator_window = Time_Zone_Configurator_Window()
            time_zone_configurator_window.connect("destroy", Gtk.main_quit)
            time_zone_configurator_window.show_all()
            self.hide()

            Languages.configuring_languages_environment(time_zone_configurator_window, language_selection_window.safed_language_variable)

            GObject.timeout_add(0, self.skip_internet_window)
        else:
            # Check if any WiFi modules exist on the system
            try:
                # Run the 'lsmod' command to list loaded kernel modules
                result = subprocess.run(['lsmod'], capture_output=True, text=True)

                # Check if any of the lines in the output contain the string 'wifi'
                wifi_modules_exist = any('wifi' in line.lower() for line in result.stdout.splitlines())

                if wifi_modules_exist:
                    print("WiFi modules exist on this system.")
                    wifi_internet_configurator_window = WiFi_Internet_Configurator_Window()
                    wifi_internet_configurator_window.connect("destroy", Gtk.main_quit)
                    wifi_internet_configurator_window.show_all()
                    self.hide()

                    Languages.configuring_languages_environment(wifi_internet_configurator_window, language_selection_window.safed_language_variable)
                else:
                    print("No WiFi modules found.")

            except Exception as e:
                print(f"Error checking WiFi modules: {e}")

        # Returning True means the timeout will continue to be called
        return True

    def is_internet_available(self):
        try:
            urllib.request.urlopen("http://www.google.com", timeout=1)
            return True
        except URLError as err:
            return False

    def skip_internet_window(self):
        self.hide()

    def on_previous_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")

        layout = "us"
        variant = "intl"
        subprocess.run(['setxkbmap', layout, variant, '-option'])

        language_selection_window = Language_Selection_Window()
        language_selection_window.connect("destroy", Gtk.main_quit)
        language_selection_window.show_all()
        self.hide()

    def on_next_clicked(self, button):
        # Additional code to save the configured keyboard layout
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()

        subprocess.run(['setxkbmap', layout, variant, '-option'])

        # Check internet status initially
        self.check_internet()

        # Use GObject.timeout_add to periodically check internet status
        # GObject.timeout_add_seconds(60, self.check_internet)

####################################################################################################
####################################################################################################

class WiFi_Internet_Configurator_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Internet")
        self.set_default_size(600, 450)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Previous button in the top-left corner
        self.previous_button_label = "Previous"
        self.previous_button = Gtk.Button(label=self.previous_button_label)
        self.previous_button.connect("clicked", self.on_previous_clicked)

        # Next button in the top-right corner
        self.next_button_label = "Next"  # Placeholder, replace it with the actual label
        self.next_button = Gtk.Button(label=self.next_button_label)
        self.next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Internet"
        header_bar.pack_start(self.previous_button)
        header_bar.pack_end(self.next_button)
        self.set_titlebar(header_bar)

        svg_file_path = "graphics/wifi.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 125, 75)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget for title
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Internet</b></span>')

        # Create a label widget for information
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Connecting this computer to a wi-fi network allows you to install third-party-software, download updates, automatically detect your timezone, and install full support for your language."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)

        # Check if nmcli is available
        if not self.is_nmcli_available():
            print("Error: nmcli is not installed.")
            Gtk.main_quit()

        # Get available WiFi networks
        wifi_list = self.get_wifi_list()

        # UI Elements
        self.network_liststore = Gtk.ListStore(str)
        for wifi in wifi_list:
            self.network_liststore.append([wifi['SSID']])
        self.network_listview = Gtk.TreeView(self.network_liststore)

        # Scrolled Window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        scrolled_window.add(self.network_listview)

        # Network List View
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Available Networks", renderer, text=0)
        self.network_listview.append_column(column)

        scrolled_window.set_margin_top(10)
        scrolled_window.set_hexpand(True)
        scrolled_window.set_size_request(600,180) # W x H

        # Create a horizontal box (INNER CONTAINER)
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container.set_halign(Gtk.Align.CENTER)
        container.set_border_width(5)

        passphrase_label = Gtk.Label(f"Password:")
        container.pack_start(passphrase_label, False, False, 0)
        self.passphrase_entry = Gtk.Entry(placeholder_text="Enter Passphrase ...")
        self.passphrase_entry.set_property("hexpand", True)
        self.passphrase_entry.set_width_chars(25)
        self.passphrase_entry.set_visibility(False)  # Password is hidden by default
        container.pack_start(self.passphrase_entry, True, True, 0)
        show_passphrase_checkbox = Gtk.CheckButton()
        show_passphrase_checkbox.set_direction(Pango.Direction.RTL)
        show_passphrase_checkbox.connect("toggled", self.toggle_password_visibility)
        container.pack_start(show_passphrase_checkbox, False, False, 0)
        show_passphrase_label = Gtk.Label()
        show_passphrase_label.set_text(f"Display password")
        show_passphrase_label.set_direction(Pango.Direction.RTL)
        container.pack_start(show_passphrase_label, False, False, 0)

        # Create a horizontal box (INNER CONTAINER)
        container_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_1.set_halign(Gtk.Align.CENTER)
        container_1.set_border_width(5)

        refresh_button = Gtk.Button(label="Refresh")
        refresh_button.connect("clicked", self.update_network_list)
        container_1.pack_start(refresh_button, True, True, 0)

        connect_button = Gtk.Button(label="Connect")
        connect_button.connect("clicked", self.on_connect_button_clicked)
        container_1.pack_start(connect_button, True, True, 0)

        # Create a VBox to organize widgets vertically
        vbox = Gtk.VBox(spacing=10)
        vbox.set_margin_top(35)
        vbox.pack_start(image, False, False, 0)
        vbox.pack_start(self.title_label, False, False, 0)
        vbox.pack_start(label_info, False, False, 0)
        vbox.pack_start(scrolled_window, False, False, 0)
        vbox.pack_start(container, False, False, 0)
        vbox.pack_start(container_1, False, False, 0)

        # Add the VBox to the window
        self.add(vbox)

    def is_nmcli_available(self):
        try:
            subprocess.run(["nmcli", "--version"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_wifi_list(self):
        try:
            result = subprocess.run(["nmcli", "-f", "SSID", "d", "wifi", "list"], check=True, capture_output=True, text=True)
            wifi_list = []
            for line in result.stdout.strip().split('\n')[1:]:
                ssid = line.strip()
                wifi_list.append({'SSID': ssid})
            return wifi_list
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving WiFi list: {e}")
            return []

    def update_network_list(self, widget):
        # Clear existing network list
        self.network_liststore.clear()

        try:
            result = subprocess.run(["nmcli", "-f", "SSID", "d", "wifi", "list"], check=True, capture_output=True, text=True)
            wifi_list = []
            for line in result.stdout.strip().split('\n')[1:]:
                ssid = line.strip()
                self.network_liststore.append([ssid])
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving WiFi list: {e}")
            return []

        return True  # Continue updating

    def toggle_password_visibility(self, widget):
        visibility = widget.get_active()
        self.passphrase_entry.set_visibility(visibility)

    def on_connect_button_clicked(self, widget):
        # Get selected network and passphrase
        selection = self.network_listview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            ssid = model[treeiter][0]
            passphrase = self.passphrase_entry.get_text()

            # Connect to the selected network using "nmcli"
            try:
                subprocess.check_output(["nmcli", "d", "wifi", "connect", ssid, "password", passphrase],
                                        universal_newlines=True)
                print(f"Connected to {ssid}")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

    def on_previous_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")
        keyboard_configurator_window = Keyboard_Configurator_Window()
        keyboard_configurator_window.connect("destroy", Gtk.main_quit)
        keyboard_configurator_window.show_all()
        self.hide()

        Languages.configuring_languages_environment(keyboard_configurator_window, language_selection_window.safed_language_variable)

    def on_next_clicked(self, button):
        # Additional code to save the configured keyboard layout
        print("Next button clicked")
        time_zone_configurator_window = Time_Zone_Configurator_Window()
        time_zone_configurator_window.connect("destroy", Gtk.main_quit)
        time_zone_configurator_window.show_all()
        self.hide()

        Languages.configuring_languages_environment(time_zone_configurator_window, language_selection_window.safed_language_variable)

####################################################################################################
####################################################################################################

class Time_Zone_Configurator_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Time Zone")
        self.set_default_size(600, 450)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Previous button in the top-left corner
        self.previous_button_label = "Previous"
        self.previous_button = Gtk.Button(label=self.previous_button_label)
        self.previous_button.connect("clicked", self.on_previous_clicked)

        # Next button in the top-right corner
        self.next_button_label = "Next"  # Placeholder, replace it with the actual label
        self.next_button = Gtk.Button(label=self.next_button_label)
        self.next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Time Zone"
        header_bar.pack_start(self.previous_button)
        header_bar.pack_end(self.next_button)
        self.set_titlebar(header_bar)

        svg_file_path = "graphics/clock-calendar.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 125, 75)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget for title
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Time Zone</b></span>')

        # Create a label widget for information
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Please search for a nearby city or use automatic time tracking using a geolocation API."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)

        # Create a horizontal box (MAIN INNER CONTAINER)
        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_valign(Gtk.Align.CENTER)
        container_main_1_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main_1_1.set_size_request(400, 150)
        container_main.add(container_main_1_1)
        container_main_1_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main_1_2.set_halign(Gtk.Align.CENTER)
        container_main.add(container_main_1_2)
        container_main_1_3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main.add(container_main_1_3)

        # Create the scrolled window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        container_main_1_1.pack_start(scrolled_window, True, True, 0)

        # Create the list store and tree view
        self.list_store = Gtk.ListStore(str)
        self.tree_view = Gtk.TreeView(model=self.list_store)
        scrolled_window.add(self.tree_view)

        # Create the columns
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Time Zone", renderer, text=0)
        self.tree_view.append_column(column)

        # Populate the list store with time zones
        time_zones = subprocess.check_output(["timedatectl", "list-timezones"]).decode("utf-8").splitlines()
        for zone in time_zones:
            self.list_store.append([zone])

        # Create a search entry
        search_entry = Gtk.SearchEntry()
        search_entry.connect("search-changed", self.on_search_changed)
        container_main_1_2.pack_start(search_entry, False, False, 0)

        autoconfig_time_zone_checkbox = Gtk.CheckButton(f"Automatic time adjustment")
        autoconfig_time_zone_checkbox.connect("toggled", self.toggle_autoconfig_time_zone)
        container_main_1_2.pack_start(autoconfig_time_zone_checkbox, False, False, 0)

        # Define automatic_time_zone as a class attribute
        self.automatic_time_zone = 0

        # Get the current time zone using the 'timedatectl' command
        current_time_zone_cmd = "timedatectl | grep 'Time zone' | awk '{print $3}'"
        current_time_zone = os.popen(current_time_zone_cmd).read().strip()
        current_time_cmd = f"TZ={current_time_zone} date"
        current_time = os.popen(current_time_cmd).read().strip()
        print(f"Current Time: {current_time}")

        # Create and set up the label (Current time zone)
        self._current_time_zone_label = Gtk.Label()
        self._current_time_zone_label.set_markup(f'<span foreground="#2B2D42" background="#19b1a2"> Current Time Zone: </span> <span foreground="#19b1a2">{current_time_zone} [{current_time}]</span>')
        self._current_time_zone_label.set_line_wrap(True)
        container_main_1_3.pack_start(self._current_time_zone_label, False, False, 0)

        # Create and set up the label (Selected time zone)
        self.selected_time_zone_label = Gtk.Label()
        self.selected_time_zone_label.set_markup('<span foreground="#2B2D42" background="#F7E733"> Selected Time Zone: </span> <span foreground="#F7E733">Please select a timezone first!</span>')
        self.selected_time_zone_label.set_line_wrap(True)
        container_main_1_3.pack_start(self.selected_time_zone_label, False, False, 0)

        # Connect the row-activated signal
        self.tree_view.connect("row-activated", self.on_row_activated)

        # Create a VBox to organize widgets vertically
        vbox = Gtk.VBox(spacing=10)
        vbox.set_margin_top(35)
        vbox.pack_start(image, False, False, 0)
        vbox.pack_start(self.title_label, False, False, 0)
        vbox.pack_start(label_info, False, False, 0)
        vbox.pack_start(container_main, False, False, 0)

        # Add the VBox to the window
        self.add(vbox)

    def on_row_activated(self, tree_view, path, column):
        # Get the selected time zone and update the label
        iter = self.list_store.get_iter(path)
        selected_time_zone = self.list_store.get_value(iter, 0)
        print(f"Selected Time Zone: {selected_time_zone}")
        selected_time_cmd = f"TZ={selected_time_zone} date"
        selected_time = os.popen(selected_time_cmd).read().strip()
        print(f"Selected Time: {selected_time_zone} | {selected_time}")
        # Using f-string to format the string correctly
        self.new_time_zone = f'<span foreground="#2B2D42" background="#F7E733"> Selected Time Zone: </span> <span foreground="#F7E733">{selected_time_zone} | {selected_time}</span>'
        self.selected_time_zone_label.set_markup(self.new_time_zone)

    def on_search_changed(self, entry):
        # Filter the list based on the search text
        search_text = entry.get_text().lower()
        self.list_store.clear()
        time_zones = subprocess.check_output(["timedatectl", "list-timezones"]).decode("utf-8").splitlines()
        for zone in time_zones:
            if search_text in zone.lower():
                self.list_store.append([zone])

    def toggle_autoconfig_time_zone(self, widget):
        if widget.get_active():
            print("CheckButton is active")
            self.new_time_zone = f'<span foreground="#2B2D42" background="#F7E733"> Selected Time Zone: </span> <span foreground="#F7E733">The time zone will be determined automatically!</span>'
            self.selected_time_zone_label.set_markup(self.new_time_zone)
            self.automatic_time_zone = 1
        else:
            print("CheckButton is not active")
            self.new_time_zone = f'<span foreground="#2B2D42" background="#F7E733"> Selected Time Zone: </span> <span foreground="#F7E733">Please select a timezone first!</span>'
            self.selected_time_zone_label.set_markup(self.new_time_zone)
            self.automatic_time_zone = 0

    def on_previous_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")
        keyboard_configurator_window = Keyboard_Configurator_Window()
        keyboard_configurator_window.connect("destroy", Gtk.main_quit)
        keyboard_configurator_window.show_all()
        self.hide()

        Languages.configuring_languages_environment(keyboard_configurator_window, language_selection_window.safed_language_variable)

    def on_next_clicked(self, button):
        # Additional code to save the configured keyboard layout
        print("Next button clicked")
        if self.automatic_time_zone == 1:
            # Perform actions when the checkbox is checked
            print("Automatic time zone adjustment is enabled")

            # Run the command to set the timezone
            timezone_cmd = 'timedatectl set-timezone "$(curl --fail https://ipapi.co/timezone)"'
            subprocess.run(timezone_cmd, shell=True)

            # Get the selected timezone
            auto_timezone = subprocess.check_output(['timedatectl', 'status', '--no-pager']).decode('utf-8')

            # Display the selected timezone
            print(f"Automatic configured Time Zone: {auto_timezone}")
        else:
            # Perform actions when the checkbox is not checked
            print("Automatic time zone adjustment is disabled")

            # Get the selected time zone and apply it using timedatectl
            selection = self.tree_view.get_selection()
            model, iter = selection.get_selected()
            if iter is not None:
                selected_time_zone = model.get_value(iter, 0)
                subprocess.run(["timedatectl", "set-timezone", selected_time_zone])
                print(f"Time Zone Applied: {selected_time_zone}")

####################################################################################################
# THE PROGRAM IS STARTED HERE:                                                                     #
####################################################################################################

if __name__ == "__main__":
    language_selection_window = Language_Selection_Window()
    language_selection_window.connect("destroy", Gtk.main_quit)
    language_selection_window.show_all()
    Gtk.main()
