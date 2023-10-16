#!/bin/bash

####################################################################################################
# Name:         openSUSE Baldur (MicroOS with XFCE) - Setup Wizard                                 #
# Description:  With this file you get openSUSE MicroOS with the XFCE desktop enviroment.          #
# Author:       Steve Zabka                                                                        #
# Author URI:   https://cryinkfly.com                                                              #
# License:      MIT                                                                                #
# Copyright (c) 2023                                                                               #
# Time/Date:    13:50/15.10.2023                                                                   #
# Version:      1.1.1                                                                              #
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
# INSTALLATION OF THE REQUIRED PACKAGES FOR OPENSUSE MICROOS (XFCE):                                                                                                         #
##############################################################################################################################################################################

function SP_INSTALL_REQUIRED_PACKAGES {
    echo -e "${YELLOW}All required packages for openSUSE Baldur will be installed!${NOCOLOR}"
    sudo transactional-update -c pkg install \
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
        cups \
        cups-filters \
        cups-pk-helper \
        curl \
        dejavu-fonts \
        dejavu-fonts \
        desktop-file-utils \
        dosfstools \
        ethtool \
        e2fsprogs \
        exfat-utils \
        fcoe-utils \
        file-roller \
        firewalld \
        filesystem \
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
        hwinfo \
        iproute2 \
        iputils \
        irqbalance \
        issue-generator \
        kdeconnect-kde \
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
        usbutils \
        OpenPrintingPPDs \
        openssh \
        openssh-askpass-gnome \
        openSUSE-build-key \
        openSUSE-build-key \
        pam \
        pam-config \
        pavucontrol \
        pcsc-ccid \
        pcsc-tools \
        pipewire-alsa \
        pipewire-pulseaudio \
        policycoreutils \
        policycoreutils-python-utils \
        procps4 \
        pciutils \
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
        ffmpegthumbnailer \
        udev-configure-printer \
        udisks2 \
        unzip \
        upower \
        util-linux \
        vim-small \
        v4l2loopback-kmp-default \
        v4l-utils \
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
        xfce4-session \
        xfce4-session-branding-openSUSE \
        xfce4-settings \
        xfce4-settings-branding-openSUSE \
        xfce4-terminal \
        xfce4-xkb-plugin \
        xfconf \
        xfdesktop \
        xfdesktop-branding-openSUSE \
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
}

##############################################################################################################################################################################
# INSTALLATION OF THE GRAPHICS CARD DRIVER:                                                                                                                                  #
##############################################################################################################################################################################

function SP_CHECK_GPU_DRIVER {
    if [[ $(lspci | grep VGA) == *"AMD"* ]]; then
        GPU_DRIVER="amd"
        sudo transactional-update -c pkg install kernel-firmware-amdgpu libdrm_amdgpu1 libdrm_amdgpu1-32bit libdrm_radeon1 libdrm_radeon1-32bit libvulkan_radeon libvulkan_radeon-32bit libvulkan1 libvulkan1-32bit
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
    elif [[ $(lspci | grep VGA) == *"Intel"* ]]; then
        GPU_DRIVER="intel"
        sudo transactional-update -c pkg install kernel-firmware-intel libdrm_intel1 libdrm_intel1-32bit libvulkan1 libvulkan1-32bit libvulkan_intel libvulkan_intel-32bit
        echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
    elif [[ $(lspci | grep VGA) == *"NVIDIA"* ]]; then
        GPU_DRIVER="nvidia"
        if [[ $(zypper search --installed-only) == *"x11-video-nvidiaG05"*"libvulkan1"*"libvulkan1-32bit"* ]]; then
            echo -e "${GREEN}The latest graphics card driver is already installed.${NOCOLOR}"
        else
            if [[ $(zypper lr -u) == *"https://download.nvidia.com/opensuse/tumbleweed"* ]] || [[ $(zypper lr -u) == *"https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo"* ]]; then
                sudo transactional-update -c pkg install nvidia-video-G06 nvidia-gl-G06 libvulkan1 libvulkan1-32bit
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
            else
                read -p "${YELLOW}Do you want to install the NVIDIA drivers with full CUDA support? [yn] ${NOCOLOR}" answer
                if [[ $answer = y ]] ; then
                    sudo transactional-update -c run bash -c '
                    sudo zypper addrepo --refresh https://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/cuda-opensuse15.repo NVIDIA
                    sudo zypper install -y cuda libvulkan1 libvulkan1-32bit
                    '
                else
                    sudo transactional-update -c run bash -c '
                    sudo zypper addrepo --refresh https://download.nvidia.com/opensuse/tumbleweed NVIDIA
                    sudo zypper install -y x11-video-nvidiaG05 libvulkan1 libvulkan1-32bit
                    '
                fi
                echo -e "${GREEN}After a restart, the latest graphics card driver is installed and activated!${NOCOLOR}"
            fi
        fi
    else
        echo -e "${YELLOW}The graphics card analysis failed because your graphics card was not detected!${NOCOLOR}"
        echo -e "${RED}The installer has been terminated!${NOCOLOR}"
    fi
}

##############################################################################################################################################################################
# SWITCH BOOT TARGET TO GUI (GRAPHICAL UI):                                                                                                                                  #
##############################################################################################################################################################################

function SP_ACTIVATE_GUI {
    echo -e "${YELLOW}Boot target is switched to GUI (graphical user interface)!${NOCOLOR}"
    sudo transactional-update -c run bash -c '
        sudo systemctl set-default graphical.target
    '
    echo -e "${GREEN}The graphical user interface will be show after reboot!${NOCOLOR}"
}

##############################################################################################################################################################################
# ENABLE THE "VIRTUAL CAMERA" FOR OBS STUDIO:                                                                                                                                #
##############################################################################################################################################################################

function SP_ACTIVATE_VC {
    echo -e "${YELLOW}Enable the Virtual Camera function for OBS Studio!${NOCOLOR}"
    sudo transactional-update -c run bash -c '
        sudo echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf
    '
    echo -e "${GREEN}The Virtual Camera function for OBS Studio will be work after reboot!${NOCOLOR}"
}

##############################################################################################################################################################################
# CONFIGURING THE FIREWALL SETTINGS FOR KDE-CONNECT:                                                                                                                         #
##############################################################################################################################################################################

function SP_ACTIVATE_KDE-CONNECT-PORTS {
    echo -e "${YELLOW}Opens the ports so that KDE-Connect works properly!${NOCOLOR}"
    sudo transactional-update -c run bash -c '
        sudo firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent
        sudo firewall-cmd --zone=public --add-port=1714-1764/udp --permanent
    '
    echo -e "${GREEN}The ports for KDE-Connect are open after a restart!${NOCOLOR}"
}

##############################################################################################################################################################################
# CREATING & CONFIGURING A NORMAL USER:                                                                                                                                      #
##############################################################################################################################################################################

function SP_SETUP_USER {
    read -p "${YELLOW}Would you like to create a new user without root privileges? [yn]: ${NOCOLOR}" answer
                if [[ $answer = y ]] ; then
                    sudo transactional-update -c run bash -c '
                    read -p "${YELLOW}Please enter the name of the new user? ${NOCOLOR}" USERNAME
                    sudo useradd -m $USERNAME
                    echo -e "${GREEN}The user $USERNAME was created successfully and is available after the restart!${NOCOLOR}"
                    echo -c "${YELLOW}Please enter a secure password for your new user in the next step! ${NOCOLOR}" USERNAME
                    sudo passwd $USERNAME
                    echo -e "${GREEN}The password has now been set for the new user if the entry was correct!${NOCOLOR}"
                    sudo mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
                    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/stable-branch/bin/xfce4-keyboard-shortcuts.xml > xfce4-keyboard-shortcuts.xml
                    sudo mv xfce4-keyboard-shortcuts.xml /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/
                    sudo mkdir -p /home/$USERNAME/.config/autostart
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/stable-branch/bin/mod-firstboot.sh > mod-firstboot.sh
    chmod +rwx mod-firstboot.sh
    sudo mv mod-firstboot.sh /home/$USERNAME/.config/autostart/
    cat > mod-firstboot.desktop << EOF
[Desktop Entry]
Name=MicroOS Desktop FirstBoot Setup
Comment=Sets up MicroOS Desktop Correctly On FirstBoot
Exec=/home/$USERNAME/.config/autostart/mod-firstboot.sh
Icon=org.gnome.Terminal
Type=Application
Categories=Utility;System;
Name[en_GB]=startup
Name[en_US]=startup
EOF

    chmod +rwx mod-firstboot.desktop
    sudo mv mod-firstboot.desktop /home/$USERNAME/.config/autostart/
                    '
                else
                    echo "Nothing to do ..."
                fi
}

##############################################################################################################################################################################
# CONFIGURING THE MICROOS DESKTOP FIRSTBOOT SETUP:                                                                                                                           #
##############################################################################################################################################################################

function SP_SETUP_FIRSTBOOT {
  sudo transactional-update -c run bash -c '
    sudo mkdir -p /home/$USERNAME/.config/autostart
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/stable-branch/bin/mod-firstboot.sh > mod-firstboot.sh
    chmod +rwx mod-firstboot.sh
    sudo mv mod-firstboot.sh /home/$USERNAME/.config/autostart/
    cat > mod-firstboot.desktop << EOF
[Desktop Entry]
Name=MicroOS Desktop FirstBoot Setup
Comment=Sets up MicroOS Desktop Correctly On FirstBoot
Exec=/home/$USERNAME/.config/autostart/mod-firstboot.sh
Icon=org.gnome.Terminal
Type=Application
Categories=Utility;System;
Name[en_GB]=startup
Name[en_US]=startup
EOF

    chmod +rwx mod-firstboot.desktop
    sudo mv mod-firstboot.desktop /home/$USERNAME/.config/autostart/
  '
}

##############################################################################################################################################################################
# CONFIGURING THE KEYBOARD SHORTCUTS FOR OPENSUSE BALDUR:                                                                                                                    #
##############################################################################################################################################################################

function SP_SETUP_XFCE4-KEYBOARD-SHORTCUTS {
  sudo transactional-update -c run bash -c '
    sudo mkdir -p /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml
    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/stable-branch/bin/xfce4-keyboard-shortcuts.xml > xfce4-keyboard-shortcuts.xml
    sudo mv xfce4-keyboard-shortcuts.xml /home/$USERNAME/.config/xfce4/xfconf/xfce-perchannel-xml/
    '
}

#####################################################################################################################################################################################################################
# THE INSTALLATION PROGRAM IS STARTED HERE:                                                                                                                                                                         #
#####################################################################################################################################################################################################################

SP_LOAD_COLOR_SHEME
SP_INSTALL_REQUIRED_PACKAGES
SP_CHECK_GPU_DRIVER
SP_ACTIVATE_GUI
SP_ACTIVATE_VC
SP_ACTIVATE_KDE-CONNECT-PORTS
SP_SETUP_USER
