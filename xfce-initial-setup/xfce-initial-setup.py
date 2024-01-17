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
from urllib.request import urlopen
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

    @staticmethod
    def configuring_languages_environment(selected_language):
        # Do something with the selected language
        # For example, you can store it in a variable or use it in some way
        # For demonstration, I'll just print it here
        print(f"Received selected language: {selected_language}")
        if selected_language == "Afrikaans":
            with open('localization/de_DE/locale.txt', 'r', encoding='utf-8') as file:
                locale_variables = [line.strip() for line in file.readlines()]

            language_selection_window.set_title(locale_variables[0])
            language_selection_window.new_title_label = f'<span font_size="20000"><b>{locale_variables[0]}</b></span>'
            language_selection_window.title_label.set_markup(language_selection_window.new_title_label)

            # Assuming window2 is a class defined somewhere in your code
            if hasattr(language_selection_window, 'previous_button_label'):

                language_selection_window.previous_button_label = locale_variables[1]
                language_selection_window.previous_button.set_label(language_selection_window.previous_button_label)

            language_selection_window.next_button_label = locale_variables[2]
            language_selection_window.next_button.set_label(language_selection_window.next_button_label)


####################################################################################################
####################################################################################################

class Language_Selection_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome")
        self.set_default_size(600, 450)
        self.set_border_width(35)

        # Next button in the top-right corner
        self.next_button_label = "Next"  # Placeholder, replace it with the actual label
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

        # Create a label widget
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

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")

    def importing_languages_list_from_file(self):
        # Accessing lines from Languages class
        with open('localization/languages-list.txt', 'r') as file:
            read_languages = file.readlines()
            languages_list = [read_languages[i - 1].strip() for i in range(13, len(read_languages) + 1, 4)]
        return languages_list

    def on_language_selected(self, listbox, row):
        selected_language = self.languages[row.get_index()]
        Languages.configuring_languages_environment(selected_language)


####################################################################################################
# THE PROGRAM IS STARTED HERE:                                                                     #
####################################################################################################

if __name__ == "__main__":
    language_selection_window = Language_Selection_Window()
    language_selection_window.connect("destroy", Gtk.main_quit)
    language_selection_window.show_all()
    Gtk.main()
