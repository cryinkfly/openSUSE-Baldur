#!/bin/env bash

# Detect connected monitors and resolutions
connected_monitors=$(xrandr | grep -w connected)
is_4k=false

# Check if any monitor is 4K
while read -r line; do
    if [[ $line == *3840x2160* ]]; then
        is_4k=true
        break
    fi
done <<< "$connected_monitors"

# If 4K monitor is detected
if $is_4k; then
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfwm4-xhdpi.xml > $HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xsettings-xhdpi.xml > $HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
    xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40-xhdpi
    sleep 3
    xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40-xhdpi
    sleep 3
    xfconf-query -c xsettings -p /Gdk/WindowScalingFactor -s 2
    sleep 3
    xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
    sleep 3
    xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
    sleep 3
    xfwm4 --replace
    xfsettingsd --replace
    flatpak override --user --filesystem=$HOME/.themes
    flatpak override --user --filesystem=$HOME/.icons
    flatpak override --user --env=GTK_THEME=Nordic-v40-xhdpi 
    flatpak override --user --env=ICON_THEME=Tela-circle-manjaro-dark 
    flatpak override --user --env=CURSOR_THEME=Bibata-Modern-Classic
else
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml > $HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml > $HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
    xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40
    sleep 3
    xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40
    sleep 3
    xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
    sleep 3
    xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
    sleep 3
    xfwm4 --replace
    xfsettingsd --replace
    flatpak override --user --filesystem=$HOME/.themes
    flatpak override --user --filesystem=$HOME/.icons
    flatpak override --user --env=GTK_THEME=Nordic-v40 
    flatpak override --user --env=ICON_THEME=Tela-circle-manjaro-dark 
    flatpak override --user --env=CURSOR_THEME=Bibata-Modern-Classic
fi

sleep 10

rm -f $HOME/.config/autostart/mod-theme_config.desktop
# After finishing execution, delete the script itself
rm "$0"
