import gi
import subprocess
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class ProcessWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="XFCE4 & Flatpak Configuration")
        self.set_border_width(10)
        self.set_default_size(400, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        
        # Label for displaying progress
        self.label = Gtk.Label(label="Processing ...")
        vbox.pack_start(self.label, True, True, 0)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
        self.count = 0

        self.run_bash_commands()

    def run_bash_commands(self):
        bash_script = """#!/bin/bash
        connected_monitors=$(xrandr | grep -w connected)
        is_4k=false

        while read -r line; do
            if [[ $line == *3840x2160* ]]; then
                is_4k=true
                break
            fi
        done <<< "$connected_monitors"

        if $is_4k; then
            xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40-xhdpi
            xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40-xhdpi
            sed -i 's/Gdk\/WindowScalingFactor\>/Gdk\/WindowScalingFactor>2/g' ~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
            xfconf-query -c xsettings -p /Gdk/WindowScalingFactor -n -t int -s 2
            xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
            xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
            xfconf-query -c xsettings -p /Gtk/CursorThemeSize -s 38
            xfce4-panel -r
            flatpak override --user --filesystem=$HOME/.themes
            flatpak override --user --filesystem=$HOME/.icons
            flatpak override --user --env=GTK_THEME=Nordic-v40-xhdpi 
            flatpak override --user --env=ICON_THEME=Tela-circle-manjaro-dark 
            flatpak override --user --env=CURSOR_THEME=Bibata-Modern-Classic
            flatpak override --user --env=GDK_SCALE=2
            flatpak override --user --env=QT_SCALE_FACTOR=2
        else
            xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40
            xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40
            xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
            xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
            xfce4-panel -r
            flatpak override --user --filesystem=$HOME/.themes
            flatpak override --user --filesystem=$HOME/.icons
            flatpak override --user --env=GTK_THEME=Nordic-v40 
            flatpak override --user --env=ICON_THEME=Tela-circle-manjaro-dark 
            flatpak override --user --env=CURSOR_THEME=Bibata-Modern-Classic
        fi

        rm -f $HOME/.config/autostart/mod-theme-setup.desktop
        rm "$0"
        """
        os.system(bash_script)

    def on_timeout(self, user_data):
        self.count += 0.01
        if self.count >= 1:
            self.destroy()
            return False  # Stop the timeout
        self.progressbar.set_fraction(self.count)
        return True  # Continue the timeout

win = ProcessWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
