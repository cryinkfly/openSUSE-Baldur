#!/bin/env bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Setup Wizard                                 #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2024                                                                               #
# Time/Date:    19:45/05.05.2024                                                                   #
# Version:      1.0.0                                                                              #
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
    # Checking if the user will create a new user account without root permissions: (yY = yes, nN = no) answer
    echo -e "${YELLOW}Do you want to create a new user account without root permissions? (y/n)${NOCOLOR}" && read answer
    if [[ $answer == [yY] ]]; then
        echo -e "${YELLOW}Please enter the username of the new user account!${NOCOLOR}" && read username
        useradd users $username
        echo -e "${YELLOW}Please enter the password of the new user account!${NOCOLOR}" && passwd $username
        echo -e "${GREEN}The new user account has been successfully created!${NOCOLOR}"
        sleep 3
    else
        echo -e "${YELLOW}The user account has not been created and for this reason this step is skipped!${NOCOLOR}"
    fi
    echo -e "${YELLOW}The required packages without the graphics card driver are being installed!${NOCOLOR}"
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
    if [ -n "$username" ]; then
        echo -e "${YELLOW}Configuring settings for user $username...${NOCOLOR}"
        sleep 5
        su - $username -c '
            mkdir -p ~/.config/xfce4/xfconf/xfce-perchannel-xml
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
            mkdir -p $HOME/.themes && mkdir -p $HOME/.icons
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Tela-circle-manjaro.tar.xz -O -J -L
            tar -xJf Tela-circle-manjaro.tar.xz -C $HOME/.icons/
            rm -rf Tela-circle-manjaro.tar.xz
            curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Bibata-Modern-Classic.tar.xz -O -J -L
            tar -xJf Bibata-Modern-Classic.tar.xz -C $HOME/.icons
            rm -rf Bibata-Modern-Classic.tar.xz
            xfconf-query -c xfce4-desktop -p  /backdrop/screen0/monitorVirtual1/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
            xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
        '
        echo -e "${GREEN}Settings have been successfully configured for user $username!${NOCOLOR}"
    fi

    echo -e "${YELLOW}Configuring settings for root user...${NOCOLOR}"
    sleep 5
    su -c '
        mkdir -p /root/.config/xfce4/xfconf/xfce-perchannel-xml
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > /root/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > /root/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml > /root/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml > /root/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
        mkdir -p /root/.themes && mkdir -p /root/.icons
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Tela-circle-manjaro.tar.xz -O -J -L
        tar -xJf Tela-circle-manjaro.tar.xz -C /root/.icons/
        rm -rf Tela-circle-manjaro.tar.xz
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/resources/icons/Bibata-Modern-Classic.tar.xz -O -J -L
        tar -xJf Bibata-Modern-Classic.tar.xz -C /root/.icons
        rm -rf Bibata-Modern-Classic.tar.xz
        xfconf-query -c xfce4-desktop -p  /backdrop/screen0/monitorVirtual1/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
        xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s /usr/share/wallpapers/openSUSE-Baldur/openSUSE/origami-green-chameleon-with-dark-bg-1-4864x3328.jpg
    '
    echo -e "${GREEN}Settings have been successfully configured for root user!${NOCOLOR}"
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
