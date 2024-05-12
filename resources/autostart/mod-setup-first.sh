#!/bin/env bash

echo "[Desktop Entry]" > $HOME/.config/autostart/mod-theme_config.desktop
echo "Encoding=UTF-8" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Version=1.0.0" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Type=Application" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Name=MicroOS Desktop Theme Setup" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Comment=Sets up MicroOS Desktop Theme" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Exec=sleep5 && $HOME/.config/autostart/mod-theme_config.sh" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "OnlyShowIn=XFCE;" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "RunHook=0" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "StartupNotify=false" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Terminal=false" >> $HOME/.config/autostart/mod-theme_config.desktop
echo "Hidden=false" >> $HOME/.config/autostart/mod-theme_config.desktop
curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/autostart/mod-theme_config.sh > $HOME/.config/autostart/mod-theme_config.sh
chmod +x $HOME/.config/autostart/mod-theme_config.sh

rm -f $HOME/.config/autostart/mod-setup-first.desktop
xfce4-session-logout --reboot --fast
