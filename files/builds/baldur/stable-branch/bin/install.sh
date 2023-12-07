#!/bin/bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Setup Wizard                                 #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2023                                                                               #
# Time/Date:    11:55/07.12.2023                                                                   #
# Version:      1.3.4                                                                              #
####################################################################################################

##############################################################################################################################################################################
# CONFIGURATION OF THE COLOR SCHEME:                                                                                                                                         #
##############################################################################################################################################################################

function SP_LOAD_COLOR_SHEME {
    RED=$'\033[0;31m'
    YELLOW=$'\033[0;33m'
    GREEN=$'\033[0;32m'
    NOCOLOR=$'\033[0m'
}

##############################################################################################################################################################################
# CREATING & CONFIGURING A NORMAL USER:                                                                                                                                      #
##############################################################################################################################################################################

function SP_SETUP_USER {
    read -p "${YELLOW}Would you like to create a new user without root privileges? [yn]: ${NOCOLOR}" answer
                if [[ $answer = y ]] ; then
                    read -p "${YELLOW}Please enter the name of the new user? ${NOCOLOR}" USERNAME
                    useradd -m $USERNAME
                    echo -e "${GREEN}The user $USERNAME was created successfully and is available after the restart!${NOCOLOR}"
                    echo -e "${YELLOW}Please enter a secure password for your new user in the next step!${NOCOLOR}"
                    passwd $USERNAME
                    echo -e "${GREEN}The password has now been set for the new user if the entry was correct!${NOCOLOR}"
                    echo -e "${YELLOW}The user $USERNAME will be added to the correct user groups!${NOCOLOR}"
                    usermod -a -G users,video,audio,render,disk,lp $USERNAME
                    echo -e "${GREEN}The user $USERNAME has been successfully added to the correct user groups!${NOCOLOR}"
                    sleep 3
                    SP_SETUP_XFCE4_KEYBOARD_SHORTCUTS_USER
                    SP_SETUP_XFCE4_POWER_MANAGER_USER
                    SP_SETUP_FIRSTBOOT_ROOT
                    SP_SETUP_FIRSTBOOT_USER
                else
                    echo -e "${YELLOW}Setting up a new user has been skipped, but you can still manually create a new user later.${NOCOLOR}"
                    sleep 3
                    SP_SETUP_XFCE4_KEYBOARD_SHORTCUTS_ROOT
                    SP_SETUP_XFCE4_POWER_MANAGER_ROOT
                    SP_SETUP_FIRSTBOOT_ROOT
                fi
}

##############################################################################################################################################################################
# CONFIGURING THE KEYBOARD SHORTCUTS FOR OPENSUSE BALDUR:                                                                                                                    #
##############################################################################################################################################################################

function SP_SETUP_XFCE4_KEYBOARD_SHORTCUTS_ROOT {
    mkdir -p ~/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
}

function SP_SETUP_XFCE4_KEYBOARD_SHORTCUTS_USER {
    mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
}

##############################################################################################################################################################################
# CONFIGURING THE XFCE4-POWER-MANAGER FOR OPENSUSE BALDUR:                                                                                                                    #
##############################################################################################################################################################################

function SP_SETUP_XFCE4_POWER_MANAGER_ROOT {
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
}

function SP_SETUP_XFCE4_POWER_MANAGER_USER {
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
    chown -R $USERNAME:$USERNAME /home/$USERNAME/.config/xfce4/
    chmod -R g-rwx /home/$USERNAME/.config/xfce4/
    chmod -R o-rwx /home/$USERNAME/.config/xfce4/
}


##############################################################################################################################################################################
# CONFIGURING THE MICROOS DESKTOP FIRSTBOOT SETUP:                                                                                                                           #
##############################################################################################################################################################################

function SP_SETUP_FIRSTBOOT_ROOT {
    transactional-update -c run bash -c '
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/firstboot/mod-firstboot > /usr/bin/mod-firstboot
        chmod +x /usr/bin/mod-firstboot
    '

    SP_CONFIGURE_DESKTOP_LOCALE
}

function SP_SETUP_FIRSTBOOT_USER {
    mkdir -p /home/$USERNAME/.config/autostart
    cat > /home/$USERNAME/.config/autostart/mod-firstboot.desktop << EOF
[Desktop Entry]
Name=MicroOS Desktop FirstBoot Setup
Comment=Sets up MicroOS Desktop Correctly On FirstBoot
Exec=/usr/bin/mod-firstboot
Icon=org.gnome.Terminal
Type=Application
Categories=Utility;System;
Name[en_GB]=startup
Name[en_US]=startup
EOF

    chown $USERNAME:$USERNAME /home/$USERNAME/.config/autostart/
    
    SP_CONFIGURE_DESKTOP_LOCALE
}

##############################################################################################################################################################################
# CHANGE SYSTEM LANGUAGE ON OPENSUSE MICROOS (XFCE):                                                                                                                         #
##############################################################################################################################################################################

function SP_CONFIGURE_DESKTOP_LOCALE {
    transactional-update -c run bash -c '
        curl https://github.com/cryinkfly/openSUSE-MicroOS/raw/main/files/builds/baldur/stable-branch/resources/locale-xfce-settings/icons/hicolor/hicolor.zip -O -J -L
        unzip hicolor.zip
        mv hicolor/scalable/apps/preferences-desktop-locale.svg /usr/share/icons/hicolor/scalable/apps
        mv hicolor/128x128/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/128x128/apps
        mv hicolor/64x64/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/64x64/apps
        rm -rf hicolor
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/locale-xfce-settings/mod-locale-conf.desktop > /usr/share/applications/mod-locale-conf.desktop
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/locale-xfce-settings/mod-locale-conf > /usr/bin/mod-locale-conf
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/resources/locale-xfce-settings/locale.txt > /usr/etc/locale.txt
        chmod +x /usr/bin/mod-locale-conf
    '

    SP_INSTALL_REQUIRED_PACKAGES
    SP_CHECK_GPU_DRIVER
    SP_ACTIVATE_GUI
    SP_ACTIVATE_VC
}

##############################################################################################################################################################################
# INSTALLATION OF THE REQUIRED PACKAGES FOR OPENSUSE MICROOS (XFCE):                                                                                                         #
##############################################################################################################################################################################

function SP_INSTALL_REQUIRED_PACKAGES {
    echo -e "${YELLOW}All required packages for openSUSE Baldur will be installed!${NOCOLOR}"
    sleep 3
    transactional-update -c pkg install --non-interactive pciutils usbutils
    transactional-update apply
    transactional-update -c pkg install --non-interactive \
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

function SP_CHECK_GPU_DRIVER {
    if [[ $(lspci | grep VGA) == *"AMD"* ]]; then
        GPU_DRIVER="amd"
        echo -e "${YELLOW}An AMD graphics card has been analyzed on your system and the required packages will now be installed.${NOCOLOR}"
        transactional-update -c pkg install --non-interactive kernel-firmware-amdgpu libdrm_amdgpu1 libdrm_amdgpu1-32bit libdrm_radeon1 libdrm_radeon1-32bit libvulkan_radeon libvulkan_radeon-32bit libvulkan1 libvulkan1-32bit
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
        sleep 3
    elif [[ $(lspci | grep VGA) == *"Intel"* ]]; then
        GPU_DRIVER="intel"
        echo -e "${YELLOW}An INTEL graphics card has been analyzed on your system and the required packages will now be installed.${NOCOLOR}"
        transactional-update -c pkg install --non-interactive kernel-firmware-intel libdrm_intel1 libdrm_intel1-32bit libvulkan1 libvulkan1-32bit libvulkan_intel libvulkan_intel-32bit
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
                transactional-update -c pkg install --non-interactive nvidia-video-G06 nvidia-gl-G06 libvulkan1 libvulkan1-32bit
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
                sleep 3
            else
                read -p "${YELLOW}Do you want to install the NVIDIA drivers with full CUDA support? [yn] ${NOCOLOR}" answer
                if [[ $answer = y ]] ; then
                    transactional-update -c run bash -c '
                    zypper ar -f https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo NVIDIA
                    zypper install --non-interactive cuda libvulkan1 libvulkan1-32bit
                    '
                else
                    transactional-update -c run bash -c '
                    zypper ar -f https://download.nvidia.com/opensuse/tumbleweed NVIDIA
                    zypper install --non-interactive x11-video-nvidiaG05 libvulkan1 libvulkan1-32bit
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

function SP_ACTIVATE_GUI {
    echo -e "${YELLOW}Boot target is switched to GUI (graphical user interface)!${NOCOLOR}"
    sleep 3
    transactional-update -c run bash -c '
        systemctl set-default graphical.target
    '
    echo -e "${GREEN}The graphical user interface will be show after reboot!${NOCOLOR}"
    sleep 3
}

##############################################################################################################################################################################
# ENABLE THE "VIRTUAL CAMERA" FOR OBS STUDIO:                                                                                                                                #
##############################################################################################################################################################################

function SP_ACTIVATE_VC {
    echo -e "${YELLOW}Enable the Virtual Camera function for OBS Studio!${NOCOLOR}"
    sleep 3
    transactional-update -c run bash -c '
        echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf
    '
    echo -e "${YELLOW}The Virtual Camera function for OBS Studio will be work after reboot!${NOCOLOR}"
    echo -e "${GREEN}The installation of openSUSE MicoOS with the XFCE desktop enviroment is finished!${NOCOLOR}"
    echo -e "${YELLOW}Please restart the system for all changes to take effect!${NOCOLOR}"
    sleep 3
}

#####################################################################################################################################################################################################################
# THE INSTALLATION PROGRAM IS STARTED HERE:                                                                                                                                                                         #
#####################################################################################################################################################################################################################

SP_LOAD_COLOR_SHEME
SP_SETUP_USER
