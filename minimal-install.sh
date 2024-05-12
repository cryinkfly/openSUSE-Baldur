#!/bin/env bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Simple Setup Wizard                          #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2024                                                                               #
# Time/Date:    20:00/12.05.2024                                                                   #
# Version:      1.2.1                                                                              #
####################################################################################################

# CONFIGURATION OF THE COLOR SCHEME:
RED=$'\033[0;31m'
YELLOW=$'\033[0;33m'
GREEN=$'\033[0;32m'
NOCOLOR=$'\033[0m'

# CHECKING IF THE SCRIPT IS RUNNING WITH ROOT PERMISSIONS:
if [ "$EUID" -ne 0 ]
    then echo -e "${RED}Please run this script with sudo!${NOCOLOR}"
    exit
else
    transactional-update -c run bash -c 'zypper install -y \
    7zip \
    aaa_base \
    accountsservice \
    adobe-sourcecodepro-fonts \
    adobe-sourcesanspro-fonts \
    adobe-sourceserifpro-fonts \
    adwaita-icon-theme \
    adwaita-xfce-icon-theme \
    at-spi2-core \
    audit \
    avahi \
    bash \
    bash-completion \
    biosdevname \
    blueman \
    bluez \
    bluez-auto-enable-devices \
    bluez-cups \
    bluez-firmware \
    bluez-test \
    bolt \
    branding-openSUSE \
    btrfsmaintenance \
    btrfsprogs \
    busybox \
    busybox-gzip \
    busybox-hostname \
    ca-certificates \
    ca-certificates-mozilla \
    canberra-gtk-play \
    chrony \
    container-selinux \
    coreutils \
    coreutils-systemd \
    cups \
    cups-filters \
    cups-pdf \
    cups-pk-helper \
    curl \
    davfs2 \
    dejavu-fonts \
    desktop-file-utils \
    distrobox \
    dosfstools \
    e2fsprogs \
    efitools \
    elfutils \
    ethtool \
    exfat-utils \
    fcoe-utils \
    ffmpegthumbnailer \
    file-roller \
    filesystem \
    firewalld \
    flatpak \
    gcr-ssh-askpass \
    gcr3-ssh-askpass \
    gdb \
    ghostscript \
    ghostscript-fonts-other \
    ghostscript-fonts-std \
    glibc \
    glibc-locale \
    glibc-locale-base \
    gnome-disk-utility \
    gnome-keyring \
    gnome-keyring-pam \
    gnome-software \
    gnome-system-monitor \
    google-carlito-fonts \
    google-droid-fonts \
    google-noto-coloremoji-fonts \
    google-noto-sans-fonts \
    google-opensans-fonts \
    google-roboto-fonts \
    gpg2 \
    grep \
    grub2 \
    grub2-branding-openSUSE \
    grub2-snapper-plugin \
    grub2-x86_64-efi \
    gstreamer-plugin-pipewire \
    gstreamer-plugins-bad \
    gstreamer-plugins-good \
    gvfs \
    gvfs-backend-afc \
    gvfs-backend-goa \
    gvfs-backend-samba \
    gvfs-backends \
    gvfs-fuse \
    health-checker \
    health-checker-plugins-MicroOS \
    hicolor-icon-theme-branding-openSUSE \
    hplip \
    hplip-hpijs \
    hplip-sane \
    hwdata \
    hwinfo \
    iproute2 \
    iputils \
    irqbalance \
    issue-generator \
    kdump \
    kernel-firmware-all \
    lastlog2 \
    less \
    libopenraw9 \
    libgsf-1-114 \
    libnss_usrfiles2 \
    libxfce4ui-tools \
    lightdm \
    lightdm-gtk-greeter \
    lightdm-gtk-greeter-settings \
    microos-tools \
    mokutil \
    mugshot \
    nano \
    NetworkManager \
    NetworkManager-applet \
    NetworkManager-bluetooth \
    NetworkManager-connection-editor \
    NetworkManager-openconnect \
    NetworkManager-openvpn \
    NetworkManager-pptp \
    ntfs-3g \
    ntfsprogs \
    OpenPrintingPPDs \
    openssh \
    openssh-askpass-gnome \
    openSUSE-build-key \
    pam \
    pam-config \
    pavucontrol \
    pciutils \
    pcsc-ccid \
    pcsc-tools \
    pipewire-alsa \
    pipewire-jack \
    pipewire-pulseaudio \
    podman \
    policycoreutils \
    policycoreutils-python-utils \
    power-profiles-daemon \
    procps4 \
    rebootmgr \
    rpm \
    samba \
    selinux-policy-targeted \
    selinux-tools \
    shadow \
    shared-mime-info \
    shim \
    snapper \
    sg3_utils \
    sof-firmware \
    sudo \
    steam-devices \
    system-config-printer \
    system-config-printer-applet \
    system-config-printer-common \
    system-config-printer-dbus-service \
    system-user-nobody \
    system-group-wheel \
    systemd \
    systemd-coredump \
    systemd-presets-branding-MicroOS \
    terminfo-base \
    tar \
    thunar \
    thunar-font-manager \
    thunar-plugin-dropbox \
    thunar-plugin-archive \
    thunar-plugin-media-tags \
    thunar-plugin-shares \
    thunar-sendto-blueman \
    thunar-volman \
    thunar-volman-branding-openSUSE \
    tigervnc \
    timezone \
    transactional-update \
    transactional-update-notifier \
    transactional-update-zypp-config \
    tumbler \
    tumbler-folder-thumbnailer \
    tumbler-webp-thumbnailer \
    udev-configure-printer \
    udisks2 \
    unrar \
    unzip \
    upower \
    usbutils \
    usb_modeswitch \
    util-linux \
    v4l-utils \
    v4l2loopback-kmp-default \
    vim-small \
    wallpaper-branding-openSUSE \
    wget \
    wpa_supplicant \
    wtmpdb \
    x11-tools \
    xdg-desktop-portal-gtk \
    xdg-user-dirs-gtk \
    xf86-input-libinput \
    xf86-input-vmmouse \
    xf86-input-wacom \
    xfce4-appfinder \
    xfce4-clipman-plugin \
    xfce4-notes-plugin \
    xfce4-notifyd \
    xfce4-notifyd-branding-openSUSE \
    xfce4-mount-plugin \
    xfce4-panel \
    xfce4-panel-branding-openSUSE \
    xfce4-panel-profiles \
    xfce4-power-manager \
    xfce4-pulseaudio-plugin \
    xfce4-screensaver \
    xfce4-screenshooter \
    xfce4-sensors-plugin \
    xfce4-session \
    xfce4-session-branding-openSUSE \
    xfce4-settings \
    xfce4-settings-branding-openSUSE \
    xfce4-terminal \
    xfce4-weather-plugin \
    xfce4-xkb-plugin \
    xfconf \
    xfdesktop \
    xfdesktop-branding-openSUSE \
    xfsprogs \
    xfwm4 \
    xfwm4-branding-openSUSE \
    xorg-x11-Xvnc \
    xorg-x11-driver-video \
    xorg-x11-essentials \
    xorg-x11-fonts \
    xorg-x11-fonts-core \
    xorg-x11-server \
    xorg-x11-server-extra \
    xrandr \
    xterm \
    xtermset \
    yast2-logs \
    zenity \
    zypper \
    zypper-needs-restarting'
    transactional-update apply
    echo -e "${GREEN}The required packages without the graphics card driver have been successfully installed!${NOCOLOR}"
    echo -e "${YELLOW}The graphics card driver is being analyzed on your system!${NOCOLOR}"
    sleep 5
    if [[ $(lspci | grep VGA) == *"AMD"* ]]; then
        echo -e "${YELLOW}An AMD graphics card has been analyzed on your system and the required packages will now be installed if available.${NOCOLOR}"
        transactional-update -c pkg in -y kernel-firmware-amdgpu libdrm_amdgpu1 libdrm_amdgpu1-32bit libdrm_radeon1 libdrm_radeon1-32bit libvulkan_radeon libvulkan_radeon-32bit libvulkan1 libvulkan1-32bit
        transactional-update apply
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
    elif [[ $(lspci | grep VGA) == *"Intel"* ]]; then
        echo -e "${YELLOW}An INTEL graphics card has been analyzed on your system and the required packages will now be installed if available.${NOCOLOR}"
        transactional-update -c pkg in -y kernel-firmware-intel libdrm_intel1 libdrm_intel1-32bit libvulkan1 libvulkan1-32bit libvulkan_intel libvulkan_intel-32bit
        transactional-update apply
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
    elif [[ $(lspci | grep VGA) == *"NVIDIA"* ]]; then
        echo -e "${YELLOW}An NVIDIA graphics card has been analyzed on your system and the required packages will now be installed if available.${NOCOLOR}"
        if [[ $(zypper search --installed-only) == *"x11-video-nvidiaG06"*"nvidia-gl-G06"*"libvulkan1"*"libvulkan1-32bit"* ]]; then
            echo -e "${GREEN}The latest graphics card driver is already installed.${NOCOLOR}"
        else
            if [[ $(zypper lr -u) == *"https://download.nvidia.com/opensuse/tumbleweed"* ]] || [[ $(zypper lr -u) == *"https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo"* ]]; then
                transactional-update -c pkg in -y x11-video-nvidiaG06 nvidia-gl-G06 libvulkan1 libvulkan1-32bit
                transactional-update apply
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
            else
                transactional-update -c run bash -c '
                zypper ar -f https://download.nvidia.com/opensuse/tumbleweed NVIDIA
                zypper in -y x11-video-nvidiaG06 nvidia-gl-G06 libvulkan1 libvulkan1-32bit
                '
                transactional-update apply
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
            fi
        fi
    else
        echo -e "${YELLOW}The graphics card analysis has no AMD, Intel or NVIDIA graphics card detected and for this reason this step is skipped!${NOCOLOR}"
    fi
    echo -e "${YELLOW}The configuration of the keyboard shortcuts for openSUSE Baldur is being set up!${NOCOLOR}"
    sleep 5
    mkdir -p ~/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
    echo -e "${GREEN}The keyboard shortcuts have been successfully configured!${NOCOLOR}"
    echo -e "${YELLOW}The configuration of the XFCE4 power manager for openSUSE Baldur is being set up!${NOCOLOR}"
    sleep 5
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
    echo -e "${GREEN}The XFCE4 power manager has been successfully configured!${NOCOLOR}"
    echo -e "${YELLOW}The configuration of the XFCE4 desktop for openSUSE Baldur is being set up!${NOCOLOR}"
    sleep 5
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
    echo -e "${GREEN}The XFCE4 desktop has been successfully configured!${NOCOLOR}"
    echo -e "${YELLOW}The theme, icons, wallpapers, ... for openSUSE Baldur are being installed!${NOCOLOR}"
    sleep 5
    transactional-update -c run bash -c '
        mkdir -p /usr/share/wallpapers/openSUSE-Baldur
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/wallpapers/openSUSE-Baldur_wallpapers.zip -O -J -L
        unzip -o openSUSE-Baldur_wallpapers.zip -d /usr/share/wallpapers/openSUSE-Baldur/
        rm -rf openSUSE-Baldur_wallpapers.zip
        curl https://github.com/cryinkfly/Xfce-Xfwm4-Themes/raw/main/themes/Nordic/Nordic-xhdpi.tar.gz -O -J -L
        tar -xzf Nordic-xhdpi.tar.gz -C /usr/share/themes
        mkdir -p $HOME/.themes && mkdir -p $HOME/.icons
        tar -xzf Nordic-xhdpi.tar.gz -C $HOME/.themes
        rm -rf Nordic-xhdpi.tar.gz    
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Tela-circle-manjaro.tar.xz -O -J -L
        tar -xJf Tela-circle-manjaro.tar.xz -C /usr/share/icons/
        tar -xJf Tela-circle-manjaro.tar.xz -C $HOME/.icons/
        rm -rf Tela-circle-manjaro.tar.xz
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Bibata-Modern-Classic.tar.xz -O -J -L
        tar -xJf Bibata-Modern-Classic.tar.xz -C /usr/share/icons
        tar -xJf Bibata-Modern-Classic.tar.xz -C $HOME/.icons
        rm -rf Bibata-Modern-Classic.tar.xz
        xfconf-query -c xfce4-desktop -p  /backdrop/screen0/monitorVirtual1/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
        xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
        rm /etc/lightdm/lightdm-gtk-greeter.conf
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/lightdm/lightdm-gtk-greeter.conf > /etc/lightdm/lightdm-gtk-greeter.conf
    '
    transactional-update apply
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
        xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40-xhdpi
        xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40-xhdpi
        sed -i 's/Gdk\/WindowScalingFactor\>/Gdk\/WindowScalingFactor>2/g' ~/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
        xfconf-query -c xsettings -p /Gdk/WindowScalingFactor -n -t int -s 2
        xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
        xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
        xfconf-query -c xsettings -p /Gtk/CursorThemeSize -s 38
        xfce4-panel -r
    else
        xfconf-query -c xsettings -p /Net/ThemeName -s Nordic-v40
        xfconf-query -c xfwm4 -p /general/theme -s Nordic-v40
        xfconf-query -c xsettings -p /Net/IconThemeName -s Tela-circle-manjaro-dark
        xfconf-query -c xsettings -p /Gtk/CursorThemeName -s Bibata-Modern-Classic
        xfce4-panel -r
    fi
    echo -e "${GREEN}Theme, icons, wallpapers, ... has been successfully installed!${NOCOLOR}"
    echo -e "${YELLOW}The boot target is being switched to the graphical user interface!${NOCOLOR}"
    transactional-update -c run bash -c '
        systemctl set-default graphical.target
    '
    echo -e "${GREEN}The boot target has been successfully switched to the graphical user interface!${NOCOLOR}"
    sleep 3
    echo -e "${YELLOW}The virtual camera for OBS Studio is being enabled!${NOCOLOR}"
    transactional-update -c run bash -c '
        echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf
    '
    echo -e "${GREEN}The virtual camera for OBS Studio has been successfully enabled!${NOCOLOR}"
    echo -e "${YELLOW}The system will now automatically restart in ...${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}10${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}9${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}8${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}7${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}6${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}5${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}4${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}3${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}2${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}1${NOCOLOR}"
    sleep 1
    echo -e "${YELLOW}0${NOCOLOR}"
    reboot
fi
