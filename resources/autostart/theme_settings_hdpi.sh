#!/bin/env bash

xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40
xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40
xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
flatpak override --filesystem=$HOME/.themes
flatpak override --filesystem=$HOME/.icons
flatpak override --env=GTK_THEME=Nordic-v40 
flatpak override --env=ICON_THEME=Tela-circle-manjaro-dark 
flatpak override --env=CURSOR_THEME=Bibata-Modern-Classic

rm -f $HOME/.config/autostart/theme_settings_hdpi.desktop
# After finishing execution, delete the script itself
rm "$0"
