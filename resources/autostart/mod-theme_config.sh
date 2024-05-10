#!/bin/env bash

# Detect connected monitors and resolutions
connected_monitors=$(xrandr | grep -w connected)
is_4k=false

# Check if any monitor is 4K
while read -r line; do
    if [[ $line == *4K* ]]; then
        is_4k=true
        break
    fi
done <<< "$connected_monitors"

# If 4K monitor is detected
if $is_4k; then
    xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40-xhdpi
    xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40-xhdpi
    xfconf-query -c xsettings -p /Gdk/WindowScalingFactor -s 2
    flatpak override --filesystem=$HOME/.themes
    flatpak override --filesystem=$HOME/.icons
    flatpak override --env=GTK_THEME=Nordic-v40-xhdpi 
    flatpak override --env=ICON_THEME=Tela-circle-manjaro-dark 
    flatpak override --env=CURSOR_THEME=Bibata-Modern-Classic
else
    xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40
    xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40
    xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
    xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
    flatpak override --filesystem=$HOME/.themes
    flatpak override --filesystem=$HOME/.icons
    flatpak override --env=GTK_THEME=Nordic-v40 
    flatpak override --env=ICON_THEME=Tela-circle-manjaro-dark 
    flatpak override --env=CURSOR_THEME=Bibata-Modern-Classic
fi

rm -f $HOME/.config/autostart/mod-theme_config.desktop
# After finishing execution, delete the script itself
rm "$0"
