#!/bin/bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Setup Wizard                                 #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2023                                                                               #
# Time/Date:    15:00/31.12.2023                                                                   #
# Version:      1.4.1                                                                              #
####################################################################################################

##############################################################################################################################################################################
# CONFIGURATION OF THE COLOR SCHEME:                                                                                                                                         #
##############################################################################################################################################################################

function LOAD_COLOR_SHEME {
    RED=$'\033[0;31m'
    YELLOW=$'\033[0;33m'
    GREEN=$'\033[0;32m'
    NOCOLOR=$'\033[0m'
}

##############################################################################################################################################################################
# GET THE MICROOS DESKTOP XFCE-INITIAL-SETUP-FILE:                                                                                                                           #
##############################################################################################################################################################################

function GET_XFCE_INITIAL_SETUP_FILE {
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce-initial-setup/xfce-initial-setup > /usr/bin/xfce-initial-setup
    chmod +x /usr/bin/xfce-initial-setup
    mkdir -p /root/.config/autostart
    cat > /root/.config/autostart/xfce-initial-setup.desktop << EOF
[Desktop Entry]
Name=MicroOS Desktop XFCE-INITIAL-SETUP
Comment=Start the XFCE-INITIAL-SETUP On FirstBoot
Exec=/usr/bin/mod-xfce-initial-setup
Icon=org.xfce.terminal
Type=Application
Categories=Utility;System;
Name[en_GB]=startup
Name[en_US]=startup
EOF
}

##############################################################################################################################################################################
# GET THE MICROOS DESKTOP FLATPAK-SETUP-FILE:                                                                                                                                #
##############################################################################################################################################################################

function GET_FLATPAK_SETUP_FILE {
    mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/flatpak-setup/mod-flatpak-first-setup > ~/usr/bin/mod-flatpak-setup
    chmod +x /usr/bin/mod-flatpak-setup
}

##############################################################################################################################################################################
# ACTIVATE THE AUTOMATIC LOGIN FOR THE FIRSTBOOT-SETUP:                                                                                                                      #
##############################################################################################################################################################################

function ACTIVATE_AUTO_LOGIN_FIRSTBOOT {
    sed -i 's/DISPLAYMANAGER_AUTOLOGIN=""/DISPLAYMANAGER_AUTOLOGIN="root"/' /etc/sysconfig/displaymanager
}

##############################################################################################################################################################################
# GET THE XFCE4-LANGUAGE-SETTINGS-FILE:                                                                                                                                      #
##############################################################################################################################################################################

function GET_XFCE4_LOCALE_SETTINGS_FILE {
    curl https://github.com/cryinkfly/openSUSE-MicroOS/raw/main/files/builds/stable-branch/resources/icons/preferences-desktop-locale.zip -O -J -L
    unzip preferences-desktop-locale.zip
    mv preferences-desktop-locale/scalable/apps/preferences-desktop-locale.svg /usr/share/icons/hicolor/scalable/apps
    mv preferences-desktop-locale/128x128/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/128x128/apps
    mv preferences-desktop-locale/64x64/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/64x64/apps
    rm -rf preferences-desktop-locale.zip
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce4-locale-settings/locale-settings.desktop > ~/usr/share/applications/xfc4-locale-settings.desktop
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce4-locale-settings/locale-setup-list.txt > ~/usr/etc/locale-conf/locale-setup-list.txt
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce4-locale-settings/xfc4-locale-settings > ~/usr/bin/xfc4-locale-settings
    chmod +x /usr/bin/xfc4-locale-settings
}

##############################################################################################################################################################################
# GET THE XFCE4-USER-MANAGEMENT-FILE:                                                                                                                                      #
##############################################################################################################################################################################

function GET_XFCE4_USER_MANAGEMENT_FILE {
    curl https://github.com/cryinkfly/openSUSE-MicroOS/raw/main/files/builds/stable-branch/resources/icons/preferences-desktop-user-management.zip -O -J -L
    unzip preferences-desktop-user-management.zip
    mv preferences-desktop-user-management/scalable/apps/preferences-system-users.svg /usr/share/icons/hicolor/scalable/apps
    mv preferences-desktop-user-management/128x128/apps/preferences-system-users.png /usr/share/icons/hicolor/128x128/apps
    mv preferences-desktop-user-management/64x64/apps/preferences-system-users.png /usr/share/icons/hicolor/64x64/apps
    rm -rf preferences-desktop-user-management.zip
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce4-user-management/xfce4-user-management.desktop > ~/usr/share/applications/xfce4-user-management.desktop
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce4-user-management/xfce4-user-management > ~/usr/bin/xfce4-user-management
    chmod +x /usr/bin/xfce4-user-management
}

##############################################################################################################################################################################
# GET THE XFCE4-XCONF-FILES:                                                                                                                                                 #
##############################################################################################################################################################################

function GET_XFCE4_XCONF_FILES {
    mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
}

##############################################################################################################################################################################
# INSTALLATION OF THE REQUIRED PACKAGES FOR OPENSUSE MICROOS (XFCE):                                                                                                         #
##############################################################################################################################################################################

function INSTALL_REQUIRED_PACKAGES {
    echo -e "${YELLOW}All required packages for openSUSE Baldur will be installed!${NOCOLOR}"
    sleep 3
    transactional-update -c pkg in -y pciutils usbutils
    transactional-update apply
    transactional-update -c pkg in -y \
        7zip \
        aaa_base \
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
        bluez-cups \
        bluez-firmware \
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
        cups-pk-helper \
        curl \
        dejavu-fonts \
        desktop-file-utils \
        distrobox \
        dosfstools \
        e2fsprogs \
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
        google-carlito-fonts \
        google-droid-fonts \
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
        gvfs-backend-afc \
        gvfs-backend-goa \
        gvfs-backend-samba \
        gvfs-backends \
        gvfs-fuse \
        health-checker \
        health-checker-plugins-MicroOS \
        hicolor-icon-theme-branding-openSUSE \
        hplip-hpijs \
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
        NetworkManager-openconnect-gnome \
        NetworkManager-openvpn \
        NetworkManager-openvpn-gnome \
        NetworkManager-pptp \
        NetworkManager-pptp-gnome \
        NetworkManager-wifi \
        noto-coloremoji-fonts \
        noto-emoji-fonts \
        noto-sans-fonts \
        noto-sans-fonts \
        ntfs-3g \
        ntfsprogs \
        OpenPrintingPPDs \
        openssh \
        openssh-askpass-gnome \
        openSUSE-build-key \
        openSUSE-build-key \
        pam \
        pam-config \
        pavucontrol \
        pciutils \
        pcsc-ccid \
        pcsc-tools \
        pipewire-alsa \
        pipewire-pulseaudio \
        podman \
        policycoreutils \
        policycoreutils-python-utils \
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
        sof-firmware \
        sudo \
        system-config-printer \
        system-config-printer-applet \
        system-config-printer-common \
        system-config-printer-dbus-service \
        system-user-nobody \
        systemd \
        systemd-coredump \
        systemd-icon-branding-openSUSE \
        systemd-presets-branding-MicroOS \
        terminfo-base \
        thunar \
        thunar-plugin-archive \
        thunar-plugin-media-tags \
        thunar-sendto-blueman \
        thunar-volman \
        thunar-volman-branding-openSUSE \
        timezone \
        transactional-update \
        transactional-update-notifier \
        transactional-update-zypp-config \
        tumbler \
        tumbler-folder-thumbnailer \
        tumbler-webp-thumbnailer \
        udev-configure-printer \
        udisks2 \
        unzip \
        upower \
        usbutils \
        util-linux \
        v4l-utils \
        v4l2loopback-kmp-default \
        vim-small \
        wallpaper-branding-openSUSE \
        wget \
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
        xfce4-notifyd \
        xfce4-notifyd-branding-openSUSE \
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
        xorg-x11-driver-video \
        xorg-x11-essentials \
        xorg-x11-fonts \
        xorg-x11-fonts-core \
        xorg-x11-server \
        xorg-x11-server-extra \
        xterm \
        xtermset \
        yast2-logs \
        zenity \
        zypper \
        zypper-needs-restarting

    echo -e "${GREEN}After a restart, openSUSE MicoOS is installed with the XFCE desktop enviroment!${NOCOLOR}"
    sleep 3
}

##############################################################################################################################################################################
# INSTALLATION OF THE GRAPHICS CARD DRIVER:                                                                                                                                  #
##############################################################################################################################################################################

function INSTALL_GPU_DRIVER {
    if [[ $(lspci | grep VGA) == *"AMD"* ]]; then
        GPU_DRIVER="amd"
        echo -e "${YELLOW}An AMD graphics card has been analyzed on your system and the required packages will now be installed.${NOCOLOR}"
        transactional-update -c pkg in -y kernel-firmware-amdgpu libdrm_amdgpu1 libdrm_amdgpu1-32bit libdrm_radeon1 libdrm_radeon1-32bit libvulkan_radeon libvulkan_radeon-32bit libvulkan1 libvulkan1-32bit
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
        sleep 3
    elif [[ $(lspci | grep VGA) == *"Intel"* ]]; then
        GPU_DRIVER="intel"
        echo -e "${YELLOW}An INTEL graphics card has been analyzed on your system and the required packages will now be installed.${NOCOLOR}"
        transactional-update -c pkg in -y kernel-firmware-intel libdrm_intel1 libdrm_intel1-32bit libvulkan1 libvulkan1-32bit libvulkan_intel libvulkan_intel-32bit
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
        sleep 3
    elif [[ $(lspci | grep VGA) == *"NVIDIA"* ]]; then
        GPU_DRIVER="nvidia"
        echo -e "${YELLOW}An NVIDIA graphics card has been analyzed on your system and the required packages will now be installed.${NOCOLOR}"
        if [[ $(zypper search --installed-only) == *"x11-video-nvidiaG05"*"libvulkan1"*"libvulkan1-32bit"* ]]; then
            echo -e "${GREEN}The latest graphics card driver is already installed.${NOCOLOR}"
            sleep 3
        else
            if [[ $(zypper lr -u) == *"https://download.nvidia.com/opensuse/tumbleweed"* ]] || [[ $(zypper lr -u) == *"https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo"* ]]; then
                transactional-update -c pkg in -y nvidia-video-G06 nvidia-gl-G06 libvulkan1 libvulkan1-32bit
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
                sleep 3
            else
                read -p "${YELLOW}Do you want to install the NVIDIA drivers with full CUDA support? [yn] ${NOCOLOR}" answer
                if [[ $answer = y ]] ; then
                    transactional-update -c run bash -c '
                    zypper ar -f https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo NVIDIA
                    zypper in -y cuda libvulkan1 libvulkan1-32bit
                    '
                else
                    transactional-update -c run bash -c '
                    zypper ar -f https://download.nvidia.com/opensuse/tumbleweed NVIDIA
                    zypper in -y x11-video-nvidiaG05 libvulkan1 libvulkan1-32bit
                    '
                fi
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
                sleep 3
            fi
        fi
    else
        echo -e "${YELLOW}The graphics card analysis failed because your graphics card was not detected!${NOCOLOR}"
        sleep 3
    fi
}

##############################################################################################################################################################################
# SWITCH BOOT TARGET TO GUI (GRAPHICAL UI):                                                                                                                                  #
##############################################################################################################################################################################

function ACTIVATE_GUI {
    echo -e "${YELLOW}Boot target is switched to GUI (graphical user interface)!${NOCOLOR}"
    sleep 3
    transactional-update -c run bash -c '
        systemctl set-default graphical.target
    '
    echo -e "${GREEN}The graphical user interface will be show after reboot!${NOCOLOR}"
    sleep 3
}

##############################################################################################################################################################################
# ACTIVATE THE PORTS FOR KDE-CONNECT:                                                                                                                                        #
##############################################################################################################################################################################

function OPEN_FIREWALL_PORTS {
    echo -e "${YELLOW}Opens the ports so that KDE-Connect can works properly later if you install it!${NOCOLOR}"
    sleep 3
    transactional-update -c run bash -c '
        firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent && firewall-cmd --zone=public --add-port=1714-1764/udp --permanent
    '
    echo -e "${GREEN}The ports for KDE-Connect are open after a restart!${NOCOLOR}"
    sleep 3
}

##############################################################################################################################################################################
# ENABLE THE "VIRTUAL CAMERA" FOR OBS STUDIO:                                                                                                                                #
##############################################################################################################################################################################

function ACTIVATE_VCAM {
    echo -e "${YELLOW}Enable the Virtual Camera function for OBS Studio!${NOCOLOR}"
    sleep 3
    transactional-update -c run bash -c '
        echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf
    '
    echo -e "${YELLOW}The Virtual Camera function for OBS Studio will be work after reboot!${NOCOLOR}"
}

##############################################################################################################################################################################
# REBOOT THE SYSTEM:                                                                                                                                                         #
##############################################################################################################################################################################

function EXIT_REBOOT {
    echo -e "${GREEN}The installation of openSUSE MicoOS with the XFCE desktop enviroment is finished!${NOCOLOR}"
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
}

#####################################################################################################################################################################################################################
# THE INSTALLATION PROGRAM IS STARTED HERE:                                                                                                                                                                         #
#####################################################################################################################################################################################################################

LOAD_COLOR_SHEME
GET_XFCE_INITIAL_SETUP_FILE
GET_FLATPAK_SETUP_FILE
ACTIVATE_AUTO_LOGIN_FIRSTBOOT
GET_XFCE4_LOCALE_SETTINGS_FILE
GET_XFCE4_USER_MANAGEMENT_FILE
GET_XFCE4_XCONF_FILES
INSTALL_REQUIRED_PACKAGES
INSTALL_GPU_DRIVER
ACTIVATE_GUI
OPEN_FIREWALL_PORTS
ACTIVATE_VCAM
EXIT_REBOOT
