#!/usr/bin/python	

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - XFCE-Initial-Setup                           #
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
from gi.repository import Gtk

class LanguageSelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome")
        self.set_default_size(300, 250)

        # Next button in the top-right corner
        next_button = Gtk.Button(label="Next")
        next_button.connect("clicked", self.on_next_clicked)

        # Header-Bar Configuration
        header_bar = Gtk.HeaderBar()
        header_bar.props.title = "Welcome"
        header_bar.pack_end(next_button)
        self.set_titlebar(header_bar)

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
        elif selected_language == "Albanian":
            new_title = "Mirë se vini"
            self.set_title(new_title)
        elif selected_language == "Arabic":
            new_title = "مرحباً"
            self.set_title(new_title)
        elif selected_language == "Basque":
            new_title = "Ongi etorri"
            self.set_title(new_title)
        elif selected_language == "Belarusian":
            new_title = "Сардэчна запрашаем"
            self.set_title(new_title)
        elif selected_language == "Bosnian":
            new_title = "Dobrodošli"
            self.set_title(new_title)
        elif selected_language == "Bulgarian":
            new_title = "Добре дошли"
            self.set_title(new_title)
        elif selected_language == "Catalan":
            new_title = "Benvingut"
            self.set_title(new_title)
        elif selected_language == "Croatian":
            new_title = "Dobrodošli"
            self.set_title(new_title)
        elif selected_language == "Chinese (Simplified)":
            new_title = "欢迎"
            self.set_title(new_title)
        elif selected_language == "Chinese (Traditional)":
            new_title = "歡迎"
            self.set_title(new_title)
        elif selected_language == "Czech":
            new_title = "Vítejte"
            self.set_title(new_title)
        elif selected_language == "Danish":
            new_title = "Velkommen"
            self.set_title(new_title)
        elif selected_language == "Dutch":
            new_title = "Welkom"
            self.set_title(new_title)
        elif selected_language == "English":
            new_title = "Welcome"
            self.set_title(new_title)
        elif selected_language == "Estonian":
            new_title = "Tere tulemast"
            self.set_title(new_title)
        elif selected_language == "Finnish":
            new_title = "Tervetuloa"
            self.set_title(new_title)
        elif selected_language == "French":
            new_title = "Bienvenue"
            self.set_title(new_title)
        elif selected_language == "Gaelic":
            new_title = "Fàilte"
            self.set_title(new_title)
        elif selected_language == "Gallego":
            new_title = "Benvido"
            self.set_title(new_title)
        elif selected_language == "Georgian":
            new_title = "მოგესალმებით"
            self.set_title(new_title)
        elif selected_language == "German":
            new_title = "Willkommen"
            self.set_title(new_title)
        elif selected_language == "Greek":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
        elif selected_language == "Hebrew":
            new_title = "καλως ΗΡΘΑΤΕ"
            self.set_title(new_title)
        elif selected_language == "Hungarian":
            new_title = "Üdvözöljük"
            self.set_title(new_title)
        elif selected_language == "Icelandic":
            new_title = "Velkominn"
            self.set_title(new_title)
        elif selected_language == "Indonesian":
            new_title = "Selamat datang"
            self.set_title(new_title)
        elif selected_language == "Italian":
            new_title = "Benvenuto"
            self.set_title(new_title)
        elif selected_language == "Japanese":
            new_title = "いらっしゃいませ"
            self.set_title(new_title)
        elif selected_language == "Korean":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Lithuanian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Malaysian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Maori":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Norwegian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Nynorsk":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Polish":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Portuguese":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Romanian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Russian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Samoan":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Slovak":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Slovenian":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Somali":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Spanish":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Swedish":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Tagalog":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Thai":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Tongan":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Turkish":
            new_title = ""
            self.set_title(new_title)
        elif selected_language == "Ukrainian":
            new_title = ""
            self.set_title(new_title)
        else:
            new_title = "Welcome"
            self.set_title(new_title)

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")
        

if __name__ == "__main__":
    win = LanguageSelectionWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
