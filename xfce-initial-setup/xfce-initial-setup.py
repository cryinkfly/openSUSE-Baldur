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
        self.next_button_label = "Next"  # Placeholder, replace it with the actual label
        self.next_button = Gtk.Button(label=self.next_button_label)
        self.next_button.connect("clicked", self.on_next_clicked)

        # Back button definition for the next window
        self.back_button_label = "Next"  # Placeholder, replace it with the actual label
        self.back_button = Gtk.Button(label=self.back_button_label)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Welcome"
        header_bar.pack_end(self.next_button)
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

        # Default values for not selecting a language from the langauages list:
        new_title = "Welcome"
        self.set_title(new_title)
        new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
        self.title_label.set_markup(new_title_label)
        self.next_button_label = "Next"
        self.back_button_label = "Previous"
        # Update the buttons label
        self.next_button.set_label(self.next_button_label)
        self.back_button.set_label(self.back_button_label)
        self.keyboard_layout = 95
        self.keyboard_variant = 20
        self.write_keyboard_preselected_config()

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
            self.next_button_label = "Volgende"
            self.back_button_label = "Vorige"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 0
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Albanian - Shqipëria":
            new_title = "Mirë se vini"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Tjetër"
            self.back_button_label = "E mëparshme"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 1
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Arabic - عربيعربي":
            new_title = "مرحباً"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "التالي"
            self.back_button_label = "السابق"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 3
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Basque - Euskara":
            new_title = "Ongi etorri"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Hurrengoa"
            self.back_button_label = "Aurrekoa"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 29
            self.keyboard_variant = 0
        elif selected_language == "Belarusian - беларускі":
            new_title = "Сардэчна запрашаем"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Далей"
            self.back_button_label = "Папярэдняя"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 9
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Bosnian - Bosanski":
            new_title = "Dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Dalje"
            self.back_button_label = "Prethodni"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 7
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Bulgarian - български":
            new_title = "Добре дошли"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Напред"
            self.back_button_label = "Предишен"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 10
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Catalan - Catalana":
            new_title = "Benvingut"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Següent"
            self.back_button_label = "Anterior"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 16
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Croatian - Hrvatski":
            new_title = "Dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Dalje"
            self.back_button_label = "Prethodno"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 39
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Chinese (Simplified) - 简体中文":
            new_title = "欢迎"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "下一步"
            self.back_button_label = "上一页"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 20
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Chinese (Traditional) - 中國人":
            new_title = "歡迎"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "下一步"
            self.back_button_label = "上一頁"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 92
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Czech - Čeština":
            new_title = "Vítejte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Další"
            self.back_button_label = "Předchozí"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 22
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Danish - Dansk":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Næste"
            self.back_button_label = "Forrige"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 24
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Dutch - Nederlands":
            new_title = "Welkom"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Volgende"
            self.back_button_label = "Vorige"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 71
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "English (United Kingdom)":
            new_title = "Welcome"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Next"
            self.back_button_label = "Previous"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 34
            self.keyboard_variant = 6
            self.write_keyboard_preselected_config()
        elif selected_language == "English (USA - International)":
            new_title = "Welcome"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Next"
            self.back_button_label = "Previous"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 95
            self.keyboard_variant = 20
            self.write_keyboard_preselected_config()
        elif selected_language == "Estonian - Eestlane":
            new_title = "Tere tulemast"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Järgmine"
            self.back_button_label = "Eelmine"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 26
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Finnish - Suomen kieli":
            new_title = "Tervetuloa"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Seuraava"
            self.back_button_label = "Edellinen"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 31
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "French - Français":
            new_title = "Bienvenue"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Suivant"
            self.back_button_label = "Précédent"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 33
            self.keyboard_variant = 1
            self.write_keyboard_preselected_config()
        elif selected_language == "French (Swiss) - Français (Suisse)":
            new_title = "Bienvenue"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Suivant"
            self.back_button_label = "Précédent"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 18
            self.keyboard_variant = 2
            self.write_keyboard_preselected_config()
        elif selected_language == "French (Belgium) - Français (Belgique)":
            new_title = "Bienvenue"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Suivant"
            self.back_button_label = "Précédent"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 9
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "French (Canada) - Français (Canada)":
            new_title = "Bienvenue"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Suivant"
            self.back_button_label = "Précédent"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 16
            self.keyboard_variant = 1
            self.write_keyboard_preselected_config()
        elif selected_language == "Gaelic - Ghàidhlig":
            new_title = "Fàilte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Air adhart"
            self.back_button_label = "Mu dheireadh"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 42
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Gallego":
            new_title = "Benvido"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Seguinte"
            self.back_button_label = "Anterior"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 29
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Georgian - ქართული":
            new_title = "მოგესალმებით"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "შემდეგი"
            self.back_button_label = "წინა"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 35
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "German - Deutsch":
            new_title = "Willkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Weiter"
            self.back_button_label = "Vorherige"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 23
            self.keyboard_variant = 13
            self.write_keyboard_preselected_config()
        elif selected_language == "Greek - Ελληνικά":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Επόμενο"
            self.back_button_label = "Προηγούμενο"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 38
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Hebrew - עִברִית":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "הבא"
            self.back_button_label = "הקודם"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 43
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Hungarian - Magyar":
            new_title = "Üdvözöljük"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Következő"
            self.back_button_label = "Előző"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 40
            self.write_keyboard_preselected_config()
        elif selected_language == "Icelandic - Íslenska":
            new_title = "Velkominn"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Næst"
            self.back_button_label = "Fyrri"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 47
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Indonesian - Indonesia":
            new_title = "Selamat datang"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Selanjutnya"
            self.back_button_label = "Sebelumnya"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 41
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Italian - Italiano":
            new_title = "Benvenuto"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Avanti"
            self.back_button_label = "Precedente"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 48
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Japanese - 日本語":
            new_title = "いらっしゃいませ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "次へ"
            self.back_button_label = "前へ"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 49
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Korean - 한국인":
            new_title = "환영"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "다음"
            self.back_button_label = "이전"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 53
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Lithuanian - Lietuva":
            new_title = "Sveiki"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Kitas"
            self.back_button_label = "Ankstesnis"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 58
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Malaysian - Malaysia":
            new_title = "Selamat datang"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 69
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Maori":
            new_title = "Nau mai haere mai"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Seterusnya"
            self.back_button_label = "Sebelumnya"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 74
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Norwegian - Norsk":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Seterusnya"
            self.back_button_label = "Sebelumnya"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 72
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Nynorsk":
            new_title = "Velkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Seterusnya"
            self.back_button_label = "Sebelumnya"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 72
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Polish - Polski":
            new_title = "Powitanie"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Dalej"
            self.back_button_label = "Poprzedni"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 77
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Portuguese (Brazil) - Português (Brasil)":
            new_title = "Bem-vindo"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Próximo"
            self.back_button_label = "Anterior"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 78
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Romanian - Română":
            new_title = "Bine ati venit"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Următorul"
            self.back_button_label = "Anterior"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 79
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Russian - Русский":
            new_title = "Добро пожаловать"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Далее"
            self.back_button_label = "Предыдущий"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 81
            self.write_keyboard_preselected_config()
        elif selected_language == "Samoan - Samoana":
            new_title = "Afio mai"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "O le isi"
            self.back_button_label = "Muamua"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 74
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Slovak - Slovenský":
            new_title = "Vitajte"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Ďalej"
            self.back_button_label = "Predchádzajúci"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 84
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Slovenian - Slovenščina":
            new_title = "dobrodošli"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Naprej"
            self.back_button_label = "Prejšnji"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 83
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Somali - Soomaali":
            new_title = "Soo dhawoow"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "kuxiga"
            self.back_button_label = "Ka horee"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 95
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Spanish (International) - Español (Internacional)":
            new_title = "Bienvenido"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 29
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Swedish - Svenska":
            new_title = "Välkommen"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 82
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Tagalog":
            new_title = "Maligayang pagdating"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 74
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Thai - ไทย":
            new_title = "ยินดีต้อนรับ"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 88
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Tongan - Faka-Tonga":
            new_title = "ʻOku talitali lelei koe"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 74
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Turkish - Türkçe":
            new_title = "Hoş geldin"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 91
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        elif selected_language == "Ukrainian - Український":
            new_title = "Ласкаво просимо"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = ""
            self.back_button_label = ""
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 94
            self.keyboard_variant = 0
            self.write_keyboard_preselected_config()
        else:
            new_title = "Welcome"
            self.set_title(new_title)
            new_title_label = f'<span font_size="20000"><b>{new_title}</b></span>'
            self.title_label.set_markup(new_title_label)
            self.next_button_label = "Next"
            self.back_button_label = "Previous"
            # Update the buttons label
            self.next_button.set_label(self.next_button_label)
            self.back_button.set_label(self.back_button_label)
            self.keyboard_layout = 95
            self.keyboard_variant = 20
            self.write_keyboard_preselected_config()

    def write_keyboard_preselected_config(self):      
        selected_keyboard_cmd=f"""
            #!/bin/bash
            echo -n {self.keyboard_layout} > '/tmp/_selected_keyboard_layout.XXXXXXX'
            echo -n {self.keyboard_variant} > '/tmp/_selected_keyboard_variant.XXXXXXX'
            echo -n {self.next_button_label} > '/tmp/_next_button_label.XXXXXXX'
            echo -n {self.back_button_label} > '/tmp/_back_button_label.XXXXXXX'
        """
        os.system(selected_keyboard_cmd)

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
        file_path_for_next_button_label = '/tmp/_next_button_label.XXXXXXX'
        with open(file_path_for_next_button_label, 'r') as file:
            read_next_button_label = file.read()
        
        next_button_1 = Gtk.Button(label=f"{read_next_button_label}")
        next_button_1.connect("clicked", self.on_save_keyboard_layout_button)

        # Back button in the top-left corner
        file_path_for_back_button_label = '/tmp/_back_button_label.XXXXXXX'
        with open(file_path_for_back_button_label, 'r') as file:
            read_back_button_label = file.read()

        back_button = Gtk.Button(label=f"{read_back_button_label}")
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
        file_path_for_keyboard_layout = '/tmp/_selected_keyboard_layout.XXXXXXX'
        with open(file_path_for_keyboard_layout, 'r') as file:
            read_keyboard_layout = file.read()
            # Assuming the file contains an integer, you can convert it to an integer using the int() function.
            keyboard_layout = int(read_keyboard_layout)
            self.layout_combo.set_active(keyboard_layout)

    def populate_variants(self):
        # Use localectl to get available variants for the selected layout
        current_layout = self.layout_combo.get_active_text()
        result = subprocess.run(['localectl', 'list-x11-keymap-variants', current_layout], capture_output=True, text=True)
        variants = result.stdout.strip().split('\n')

        for variant in variants:
            self.variant_combo.append_text(variant)

        # Read which keyboard variant was selected in the LanguageSelectionWindow window:     
        file_path_for_keyboard_variant = '/tmp/_selected_keyboard_variant.XXXXXXX'
        with open(file_path_for_keyboard_variant, 'r') as file:
            read_keyboard_variant = file.read()
            # Assuming the file contains an integer, you can convert it to an integer using the int() function.
            keyboard_variant = int(read_keyboard_variant)
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

    def on_save_keyboard_layout_button(self, button):
        # Additional code to save the configured keyboard layout
        layout = self.layout_combo.get_active_text()
        variant = self.variant_combo.get_active_text()

        subprocess.run(['setxkbmap', layout, variant, '-option'])

        time_zone_selector = TimeZoneSelector()
        time_zone_selector.connect("destroy", Gtk.main_quit)
        time_zone_selector.show_all()
        self.hide()

    def on_back_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")

        # Remove all TMP-Files:
        del_tmp_files_cmd="rm /tmp/_*.XXXXXXX"
        os.system(del_tmp_files_cmd)

        language_selection_window = LanguageSelectionWindow()
        language_selection_window.connect("destroy", Gtk.main_quit)
        language_selection_window.show_all()
        self.hide()


####################################################################################################        

class TimeZoneSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Time Zone")
        self.set_default_size(600, 550)
        self.set_border_width(35)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Next button in the top-right corner
        file_path_for_next_button_label = '/tmp/_next_button_label.XXXXXXX'
        with open(file_path_for_next_button_label, 'r') as file:
            read_next_button_label = file.read()
        
        next_button_1 = Gtk.Button(label=f"{read_next_button_label}")
        next_button_1.connect("clicked", self.on_save_time_zone)

        # Back button in the top-left corner
        file_path_for_back_button_label = '/tmp/_back_button_label.XXXXXXX'
        with open(file_path_for_back_button_label, 'r') as file:
            read_back_button_label = file.read()

        back_button = Gtk.Button(label=f"{read_back_button_label}")
        back_button.connect("clicked", self.on_back_clicked)

        # Header-Bar Configuration
        header_bar_1 = Gtk.HeaderBar()
        header_bar_1.props.title = "Time Zone"
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
        svg_file_path = "bg.png"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 250, 100)
        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        info_box.pack_start(image, True, True, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            f'<span font_size="20000"><b>Time Zone</b></span>'
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label()
        label_info.set_markup(
            f"Please search for a nearby city or use automatic time tracking using a geolocation API."
        )
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        # Create a horizontal box (MAIN INNER CONTAINER)
        container_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main.set_halign(Gtk.Align.CENTER)
        container_main.set_valign(Gtk.Align.CENTER)
        vbox.add(container_main)
        container_main_1_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        container_main_1_1.set_size_request(400, 350)
        container_main.add(container_main_1_1)
        container_main_1_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
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
            self.autoconfig_time_zone_status()
        else:
            print("CheckButton is not active")
            self.new_time_zone = f'<span foreground="#2B2D42" background="#F7E733"> Selected Time Zone: </span> <span foreground="#F7E733">Please select a timezone first!</span>'
            self.selected_time_zone_label.set_markup(self.new_time_zone)

    def autoconfig_time_zone_status(self):
        automatic_time_zone = 1
        return automatic_time_zone

    def on_save_time_zone(self, button):
        # Additional code to save the configured keyboard layout
        print("Next button clicked")
        automatic_time_zone = self.autoconfig_time_zone_status()
        if automatic_time_zone == 1:
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

    def on_back_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")

        keyboard_layout_configurator = KeyboardLayoutConfigurator()
        keyboard_layout_configurator.connect("destroy", Gtk.main_quit)
        keyboard_layout_configurator.show_all()
        self.hide()

####################################################################################################        

if __name__ == "__main__":
    language_selection_window = LanguageSelectionWindow()
    language_selection_window.connect("destroy", Gtk.main_quit)
    language_selection_window.show_all()
    Gtk.main()
