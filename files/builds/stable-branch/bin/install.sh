#!/bin/bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Setup Wizard                                 #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2023-2024                                                                          #
# Time/Date:    17:30/11.04.2024                                                                   #
# Version:      1.4.6                                                                              #
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
                    usermod -a -G users $USERNAME
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
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
}

function SP_SETUP_XFCE4_KEYBOARD_SHORTCUTS_USER {
    mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml > /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
}

##############################################################################################################################################################################
# CONFIGURING THE XFCE4-POWER-MANAGER FOR OPENSUSE BALDUR:                                                                                                                    #
##############################################################################################################################################################################

function SP_SETUP_XFCE4_POWER_MANAGER_ROOT {
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
}

function SP_SETUP_XFCE4_POWER_MANAGER_USER {
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/user-config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml > /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml
    chown -R $USERNAME:$USERNAME /home/$USERNAME/.config/xfce4/
    chmod -R g-rwx /home/$USERNAME/.config/xfce4/
    chmod -R o-rwx /home/$USERNAME/.config/xfce4/
}


##############################################################################################################################################################################
# CONFIGURING THE MICROOS DESKTOP FIRSTBOOT SETUP:                                                                                                                           #
##############################################################################################################################################################################

function SP_SETUP_FIRSTBOOT_ROOT {
    transactional-update -c run bash -c '
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/files/builds/stable-branch/resources/xfce-initial-setup/mod-firstboot > /usr/bin/mod-firstboot
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
        curl https://github.com/cryinkfly/openSUSE-MicroOS/raw/main/files/builds/stable-branch/resources/icons/preferences-desktop-locale.zip -O -J -L
        unzip preferences-desktop-locale.zip
        mv preferences-desktop-locale/scalable/apps/preferences-desktop-locale.svg /usr/share/icons/hicolor/scalable/apps
        mv preferences-desktop-locale/128x128/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/128x128/apps
        mv preferences-desktop-locale/64x64/apps/preferences-desktop-locale.png /usr/share/icons/hicolor/64x64/apps
        rm -rf preferences-desktop-locale.zip
        curl https://raw.githubusercontent.com/cryinkfly/openSUSE-Baldur/main/xfce4-locale-settings/xfce4-locale-settings.desktop > ~/usr/share/applications/xfc4-locale-settings.desktop
        curl https://github.com/cryinkfly/openSUSE-Baldur/raw/main/xfce-initial-setup/resources/localization/locale-list.txt > ~/usr/etc/locale-conf/locale-setup-list.txt
        curl https://github.com/cryinkfly/openSUSE-Baldur/raw/main/files/builds/stable-branch/resources/xfce4-locale-settings/xfce4-locale-settings > ~/usr/bin/xfc4-locale-settings
        chmod +x /usr/bin/xfc4-locale-settings
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
    transactional-update -c pkg in -y pciutils usbutils
    transactional-update apply
    transactional-update -c pkg in -y \
        7zip \
        aaa_base \
        accountsservice \
        adobe-sourcecodepro-fonts \
        adobe-sourcesanspro-fonts \
        adobe-sourceserifpro-fonts \
        adwaita-icon-theme \
        adwaita-xfce-icon-theme \
        alsa-firmware \
        alsa-plugins \
        alsa-utils \
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
        lightdm-slick-greeter \
        lightdm-gtk-greeter-settings \
        microos-tools \
        mlocate \
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
        sof-firmware \
        sudo \
        sg3_utils \
        sof-firmware \
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
        xterm \
        xtermset \
        xz \
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

SP_LOAD_COLOR_SHEME
SP_SETUP_USER
