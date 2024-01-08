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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk, GdkPixbuf
import os
import subprocess

class RoundedBox(Gtk.Box):
    def __init__(self, background_color, border_color, border_width, corner_radius):
        super(RoundedBox, self).__init__()

        # Set background color
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(*background_color))

        # Set border color and width
        self.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(*border_color))
        self.set_border_width(border_width)

        # Set round corners
        self.get_style_context().add_class("rounded-box")
        self.get_style_context().add_class("linked")

        # Set corner radius
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b'''
            .rounded-box {
                border-radius: %dpx;
            }
        ''' % corner_radius)

        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(
            screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

####################################################################################################

class LanguageSelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome")
        self.set_default_size(600, 450)
        self.set_border_width(35)

        # Next button in the top-right corner
        next_button = Gtk.Button(label="Next")
        next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Welcome"
        header_bar.pack_end(next_button)
        self.set_titlebar(header_bar)

        svg_file_path = "opensuse-logo-green.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 200, 100)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Welcome</b></span>')

        # Read languages from file
        self.languages = self.read_languages_from_file()

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

    def read_languages_from_file(self):
        with open('languages.txt', 'r') as file:
            languages = [line.strip() for i, line in enumerate(file) if i % 2 == 0]

        return languages

    def on_language_selected(self, listbox, row):
        selected_language = self.languages[row.get_index()]
        # Update the title text based on the selected language:
        if selected_language == "Afrikaans":
            new_title = "Welkom"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 0
        elif selected_language == "Albanian":
            new_title = "Mirë se vini"
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.set_title(new_title)
            self.keyboard_layout = 1
        elif selected_language == "Arabic":
            new_title = "مرحباً"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 3
        elif selected_language == "Basque":
            new_title = "Ongi etorri"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 29
        elif selected_language == "Belarusian":
            new_title = "Сардэчна запрашаем"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 9
        elif selected_language == "Bosnian":
            new_title = "Dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 7
        elif selected_language == "Bulgarian":
            new_title = "Добре дошли"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 10
        elif selected_language == "Catalan":
            new_title = "Benvingut"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 16
        elif selected_language == "Croatian":
            new_title = "Dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 39
        elif selected_language == "Chinese (Simplified)":
            new_title = "欢迎"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 20
        elif selected_language == "Chinese (Traditional)":
            new_title = "歡迎"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 92
        elif selected_language == "Czech":
            new_title = "Vítejte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 22
        elif selected_language == "Danish":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 24
        elif selected_language == "Dutch":
            new_title = "Welkom"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 71
        elif selected_language == "English":
            new_title = "Welcome"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 95
        elif selected_language == "Estonian":
            new_title = "Tere tulemast"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 26
        elif selected_language == "Finnish":
            new_title = "Tervetuloa"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 31
        elif selected_language == "French":
            new_title = "Bienvenue"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 33
        elif selected_language == "Gaelic":
            new_title = "Fàilte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 42
        elif selected_language == "Gallego":
            new_title = "Benvido"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 29
        elif selected_language == "Georgian":
            new_title = "მოგესალმებით"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 35
        elif selected_language == "German":
            new_title = "Willkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 23
        elif selected_language == "Greek":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 38
        elif selected_language == "Hebrew":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 43
        elif selected_language == "Hungarian":
            new_title = "Üdvözöljük"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 40
        elif selected_language == "Icelandic":
            new_title = "Velkominn"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 47
        elif selected_language == "Indonesian":
            new_title = "Selamat datang"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 41
        elif selected_language == "Italian":
            new_title = "Benvenuto"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 48
        elif selected_language == "Japanese":
            new_title = "いらっしゃいませ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 49
        elif selected_language == "Korean":
            new_title = "환영"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 53
        elif selected_language == "Lithuanian":
            new_title = "Sveiki"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 58
        elif selected_language == "Malaysian":
            new_title = "Selamat datang"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 69
        elif selected_language == "Maori":
            new_title = "Nau mai haere mai"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 74
        elif selected_language == "Norwegian":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 72
        elif selected_language == "Nynorsk":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 72
        elif selected_language == "Polish":
            new_title = "Powitanie"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 77
        elif selected_language == "Portuguese":
            new_title = "Bem-vindo"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 78
        elif selected_language == "Romanian":
            new_title = "Bine ati venit"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 79
        elif selected_language == "Russian":
            new_title = "Добро пожаловать"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 81
        elif selected_language == "Samoan":
            new_title = "Afio mai"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 74
        elif selected_language == "Slovak":
            new_title = "Vitajte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 84
        elif selected_language == "Slovenian":
            new_title = "dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 83
        elif selected_language == "Somali":
            new_title = "Soo dhawoow"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 95
        elif selected_language == "Spanish":
            new_title = "Bienvenido"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 29
        elif selected_language == "Swedish":
            new_title = "Välkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 82
        elif selected_language == "Tagalog":
            new_title = "Maligayang pagdating"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 74
        elif selected_language == "Thai":
            new_title = "ยินดีต้อนรับ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 88
        elif selected_language == "Tongan":
            new_title = "ʻOku talitali lelei koe"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 74
        elif selected_language == "Turkish":
            new_title = "Hoş geldin"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 91
        elif selected_language == "Ukrainian":
            new_title = "Ласкаво просимо"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 94
        else:
            new_title = "Welcome"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.keyboard_layout = 95

        selected_keyboard_layout_cmd=f"""
            #!/bin/bash
            echo -n {self.keyboard_layout} > '/tmp/_selected_keyboard_layout.XXXXXXX'
        """
        os.system(selected_keyboard_layout_cmd)

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")

        keyboard_layout_configurator = KeyboardLayoutConfigurator()
        keyboard_layout_configurator.connect("destroy", Gtk.main_quit)
        keyboard_layout_configurator.show_all()
        self.hide()

####################################################################################################

class KeyboardLayoutConfigurator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Layout Configurator")
        self.set_default_size(600, 450)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Next button in the top-right corner
        next_button_1 = Gtk.Button(label="Next")
        next_button_1.connect("clicked", self.on_save_keyboard_layout_button)

        # Next button in the top-right corner
        back_button = Gtk.Button(label="Previous")
        back_button.connect("clicked", self.on_back_clicked)

        # Header-Bar Configuration
        header_bar_1 = Gtk.HeaderBar()
        header_bar_1.props.title = "Typing"
        header_bar_1.pack_start(back_button)
        header_bar_1.pack_end(next_button_1)
        self.set_titlebar(header_bar_1)

        # Create a vertical box (MAIN Container)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(35)
        self.add(vbox)

        # Info text container (Vertical)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        vbox.pack_start(info_box, False, False, 0)        
        svg_file_path = "keyboard.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 100, 50)
        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        info_box.pack_start(image, True, True, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            f'<span font_size="20000"><b>Typing</b></span>'
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Select your keyboard layout or an input method."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        # Create a horizontal box (MAIN INNER CONTAINER)
        container_main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_valign(Gtk.Align.CENTER)
        container_main.set_margin_top(35)
        container_main = RoundedBox(background_color=(0.92, 0.92, 0.92, 1.0),
                           border_color=(0.2, 0.2, 0.2, 1.0),
                           border_width=5,
                           corner_radius=3)
        vbox.add(container_main)
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

    def populate_layouts(self):
        # Use localectl to get available layouts
        result = subprocess.run(['localectl', 'list-x11-keymap-layouts'], capture_output=True, text=True)
        layouts = result.stdout.strip().split('\n')

        for layout in layouts:
            self.layout_combo.append_text(layout)

        # Read which keyboard layout number was selected in the LanguageSelectionWindow window:     
        file_path = '/tmp/_selected_keyboard_layout.XXXXXXX'
        with open(file_path, 'r') as file:
            content = file.read()
            # Assuming the file contains an integer, you can convert it to an integer using the int() function.
            keyboard_layout = int(content)
            self.layout_combo.set_active(keyboard_layout)        

        # Remove all TMP-Files:
        del_tmp_files_cmd="rm /tmp/_*.XXXXXXX"
        os.system(del_tmp_files_cmd)

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

    def on_save_keyboard_layout_button(self, button):
        # Additional code to save the configured keyboard layout
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()

        subprocess.run(['setxkbmap', layout, variant, '-option'])

    def on_back_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")

        language_selection_window = LanguageSelectionWindow()
        language_selection_window.connect("destroy", Gtk.main_quit)
        language_selection_window.show_all()
        self.hide()


####################################################################################################        

if __name__ == "__main__":
    language_selection_window = LanguageSelectionWindow()
    language_selection_window.connect("destroy", Gtk.main_quit)
    language_selection_window.show_all()
    Gtk.main()
