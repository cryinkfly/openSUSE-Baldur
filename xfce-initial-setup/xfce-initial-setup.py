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
    def configuring_languages_environment(current_window, selected_language):
        # Do something with the selected language
        if selected_language == "Afrikaans":
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
            elif isinstance(current_window, Keyboard_Layout_Configurator):
                current_window.set_title(locale_variables[3])
                current_window.new_title_label = f'<span font_size="20000"><b>{locale_variables[3]}</b></span>'
                current_window.title_label.set_markup(current_window.new_title_label)


####################################################################################################
####################################################################################################

class Language_Selection_Window(Gtk.Window):
    safed_language_variable = None

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

    def importing_languages_list_from_file(self):
        # Accessing lines from Languages class
        with open('localization/languages-list.txt', 'r') as file:
            read_languages = file.readlines()
            languages_list = [read_languages[i - 1].strip() for i in range(13, len(read_languages) + 1, 4)]
        return languages_list

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")
        keyboard_layout_configurator = Keyboard_Layout_Configurator()
        keyboard_layout_configurator.connect("destroy", Gtk.main_quit)
        keyboard_layout_configurator.show_all()
        self.hide()

        Languages.configuring_languages_environment(keyboard_layout_configurator, self.safed_language_variable)

    def on_language_selected(self, listbox, row):
        selected_language = self.languages[row.get_index()]
        self.safed_language_variable = selected_language
        Languages.configuring_languages_environment(self, selected_language)

####################################################################################################
####################################################################################################

class Keyboard_Layout_Configurator(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Keyboard Layout Configurator")
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

        svg_file_path = "graphics/opensuse-logo-green.svg"
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(svg_file_path, 200, 100)

        # Create an image widget and set the Pixbuf
        image = Gtk.Image.new_from_pixbuf(pixbuf)

        # Create a label widget
        self.title_label = Gtk.Label()
        self.title_label.set_markup('<span font_size="20000"><b>Typing</b></span>')





    def on_previous_clicked(self, button):
        # Perform actions when the Back button is clicked
        print("Back button clicked")

        language_selection_window = Language_Selection_Window()
        language_selection_window.connect("destroy", Gtk.main_quit)
        language_selection_window.show_all()
        self.hide()

    def on_next_clicked(self, button):
        # Perform actions when the Next button is clicked
        print("Next button clicked")
        selected_language = Language_Selection_Window.selected_language
        keyboard_layout_configurator = Keyboard_Layout_Configurator()
        Languages.configuring_languages_environment(selected_language)

####################################################################################################
####################################################################################################



####################################################################################################
# THE PROGRAM IS STARTED HERE:                                                                     #
####################################################################################################

if __name__ == "__main__":
    language_selection_window = Language_Selection_Window()
    language_selection_window.connect("destroy", Gtk.main_quit)
    language_selection_window.show_all()
    Gtk.main()
