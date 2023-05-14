# openSUSE-MicroOS with libvirt (KVM), Elgato Stream Deck, ...

![Bildschirmfoto vom 2023-05-13 08-15-29](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/b6c455ac-5d51-4b6d-a1df-73fb303949a7)

---

<div id="fusion360-project-screenshots" align="center">
<h2>🖼 Screenshots from this project:</h2>
<img src="https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/dc1f31bc-3502-44fb-963b-b0d9c99fcd2c" width="300px" height="150px">
<img src="https://user-images.githubusercontent.com/79079633/222974795-834d0827-a9e4-4a38-9cb9-fa9cf2f01bfc.png" width="300px" height="150px">
<img src="https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/3137e6e0-94d7-4b56-894c-ba8e9c3289ac" width="300px" height="150px">
<img src="https://user-images.githubusercontent.com/79079633/222974896-36ef1f0a-6deb-4620-b75c-954e821ddd9e.jpg" width="300px" height="150px">
<img src="https://user-images.githubusercontent.com/79079633/222975021-91deec7b-fd5f-4635-87c4-f02715043fa0.png" width="300px" height="150px">
</div>

---

### 1.)  Installation of some Flatpak apps:

- Flatseal (com.github.tchx84.Flatseal) --> Is a graphical utility to review and modify permissions (Flatpak apps)!
- Firefox (org.mozilla.firefox)
- Evolution (org.gnome.Evolution)
- Kontakte (org.gnome.Contacts)
- Kalender (org.gnome.Calendar)
- LibreOffice (org.libreoffice.LibreOffice)
- KeePassXC (org.keepassxc.KeePassXC)
- Yubico Authenticator (com.yubico.yubioath)
- GIMP (org.gimp.GIMP)
- Inkscape (org.inkscape.Inkscape)
- Blender (org.blender.Blender)
- FreeCAD (org.freecadweb.FreeCAD)
- PrusaSlicer (com.prusa3d.PrusaSlicer) --> PrusaSlicer & Prusa GCode viewer
- OBS Studio (com.obsproject.Studio)
- WebSocket Server 4.x Compat Plugin (com.obsproject.Studio.Plugin.WebSocket)  --> Required for Boatswain!
- Kdenlive (org.kde.kdenlive)
- VLC (org.videolan.VLC)
- Steam (com.valvesoftware.Steam)
- Discord (com.discordapp.Discord)
- Boatswain (com.feaneron.Boatswain) --> Alternative Elgato Stream Deck Controller app!
  
You can find more Flatpak apps here: https://flathub.org/home

Flatpak applications are installed either via the Gnome Software Center/Discover or via the terminal. The user can search for and install any application in the Software Center himself or install* them all at once via the terminal with the following command:

    flatpak install flathub com.github.tchx84.Flatseal org.mozilla.firefox org.gnome.Evolution org.gnome.Contacts org.gnome.Calendar org.libreoffice.LibreOffice org.keepassxc.KeePassXC com.yubico.yubioath  org.gimp.GIMP org.inkscape.Inkscape org.blender.Blender org.freecadweb.FreeCAD com.prusa3d.PrusaSlicer com.obsproject.Studio com.obsproject.Studio.Plugin.WebSocket org.kde.kdenlive org.videolan.VLC com.valvesoftware.Steam com.discordapp.Discord com.feaneron.Boatswain

*Flatpak apps are automatically installed via the terminal in Flatpak USER mode!

---

### 2.) Installation of other important system packages via the terminal:

- nano --> Is a simple terminal-based text editor.
- pciutils --> Required to view device IDs for KVM Passthrough!
- usbutils --> Required to view device IDs for KVM Passthrough!
- pcsc-ccid --> Required for the Yubico Authenticator!
- pcsc-tools --> Required for the Yubico Authenticator!
- ~~gparted --> Works better because the "gnome-disk-utility" still has a few bugs under openSUSE MicroOS at the moment!~~ <-- FIXED!
- v4l2loopback-kmp-default --> Required for OBS Studio (Virtual Camera)!
- libvirt --> Required for KVM!
- libvirt-daemon-qemu --> Required for KVM!
- qemu-tools --> Required for KVM!
- virt-install --> Required for KVM!
- virt-manager --> Required for for KVM-GUI!
- ~~hplip --> Hewlett-Packard's Linux imaging and printing software.~~ <-- The printer & scanner can be configured via the web interface after installing openSUSE MicroOS!
- menulibre --> Required for configuring your own icons if no icon theme is used! (Optional)
- gnome-shell-extension-pop-shell --> Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and sensible navigation and management of windows. (Optional)

In order for certain programs such as the "Yubico Authenticator" to function properly on the computer, these applications require other important system packages such as "pcsc-ccid" and "pcsc-tools". 

Furthermore, every time the system substructure of openSUSE MicroOS is changed, a new snapshot is created that only becomes effective after a restart!

#### 2a.) The following commands must be executed:

    sudo transactional-update pkg install nano pciutils usbutils pcsc-ccid pcsc-tools v4l2loopback-kmp-default libvirt libvirt-client libvirt-daemon virt-manager virt-install virt-viewer qemu qemu-kvm qemu-ovmf-x86_64 qemu-tools
    
    sudo reboot
    
    sudo systemctl enable --now libvirtd
    
    sudo usermod -aG audio,video,render,libvirt,lp $USER

    sudo reboot
    
With the addition of the "libvirt" user group, for example, the "normal" user is no longer asked for the "root" password when starting the "Virt Manager" application!

---

### 3.)  Set up KVM - GPU, USB, ... passthrough via the terminal:

Enable the IOMMU feature and the [vfio-pci] kernel module on the KVM host (line 6). 

- for AMD CPU, set [amd_iommu=on iommu=pt video=efifb:off]
- for INTEL CPU, set [intel_iommu=on iommu=pt video=efifb:off]

Note: The "video=efifb:off" option should only be added if your system is configured to automatically load the graphical environment! If you want to switch to the graphical environment via the terminal after booting, you may no longer see the terminal. In addition, the option causes problems with some NVIDIA graphics cards!

![Bildschirmfoto vom 2023-05-09 19-19-33](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/a91e4c93-92e3-4397-88df-6e68d10eee01)

#### 3a.) The following commands must be executed:

    su -c 'nano /etc/default/grub'
    
Save changes with "Ctrl+X -> "Y". 

#### 3b.) Show PCI identification number and [Vendor-ID:Device-ID] of the graphics card and USB controller:

    lspci -nn | grep -i amd #All AMD graphics cards are displayed!
    
    lspci -nn | grep -i nvidia #All NVIDIA graphics cards are displayed!
    
    lspci -nn | grep -i usb #All USB devices (controllers) are displayed!
	
- 12:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 24 [Radeon PRO W6400] [1002:7422]
- 12:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 21/23 HDMI/DP Audio Controller [1002:ab28] 
- 06:00.0 USB controller [0c03]: ASMedia Technology Inc. ASM2142/ASM3142 USB 3.1 Host Controller [1b21:2142]
	
The audio controller from the graphics card must also be passed through to the VM!

#### 3c.) Two files (/etc/modprobe.d/vfio.conf &/etc/modules-load.d/vfio-pci.conf) must be created and your device-specific numbers must be entered there:

    su -c 'echo "options vfio-pci ids=1002:7422,1002:ab28,1b21:2142" > /etc/modprobe.d/vfio.conf && echo "vfio-pci" > /etc/modules-load.d/vfio-pci.conf'

#### 3d.) You need to rebuild the initial ram disk to include all the needed modules. Create a file named /etc/dracut.conf.d/gpu-passthrough.conf:

    su -c 'nano /etc/dracut.conf.d/gpu-passthrough.conf'
    
    # Insert the respective line that matches your CPU!
    
    # INTEL CPU:
    add_drivers+="pci_stub vfio vfio_iommu_type1 vfio_pci vfio_virqfd kvm kvm_intel"
    
    #OR FOR AMD CPU:
    add_drivers+="pci_stub vfio vfio_iommu_type1 vfio_pci vfio_virqfd kvm kvm_amd"
    
Save changes with "Ctrl+X -> "Y" and now we regenerate grub and rebuild the initrd by executing:

    sudo transactional-update grub.cfg

    # With the -c option, the latest or given snapshot as base continues to be used after the regenerate grub.
    sudo transactional-update -c initrd
    
    sudo reboot

#### 3e.) In order to be able to change the default storage location of KVM Libvirt, you should also change this file (/etc/libvirt/qemu.conf):

![Bildschirmfoto vom 2023-03-05 13-33-40](https://user-images.githubusercontent.com/79079633/222960741-8770a034-e1e1-40b9-bd70-6e052f67b053.png)

    su -c 'nano /etc/libvirt/qemu.conf'
    
Note: The username "steve" should be replaced with your username!

Save changes with "Ctrl+X -> "Y" and reboot the system with:

    sudo reboot
    
---

Further information can be found here:

- https://ostechnix.com/how-to-change-kvm-libvirt-default-storage-pool-location/
- https://ostechnix.com/solved-cannot-access-storage-file-permission-denied-error-in-kvm-libvirt/

---

### 4.) Enable the "Virtual Camera" for OBS Studio on openSUSE MicroOS:

So that the "Virtual Camera" function can be used under OBS-Studio under openSUSE MicroOS, a file (/etc/modules-load.d/v4l2loopback.conf) must be created with the following command via the terminal:

    su -c 'echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf'
    
    sudo reboot

... and the "v4l2loopback-kmp-default" package must also be installed on the system!

---
	
### 5.) Using GSConnect's Gnome extension on openSUSE MicroOS:

If you have GSConnect's Gnome extension installed and want to use it to connect to your mobile phone, you need to make the following changes to your firewall setting:

    sudo firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=1714-1764/udp --permanent
    #OR
    su -c 'firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent && firewall-cmd --zone=public --add-port=1714-1764/udp --permanent

Further information can be found here: 

- https://extensions.gnome.org/extension/1319/gsconnect/
- https://en.opensuse.org/SDB:KDE_Connect
- https://www.cyberciti.biz/faq/set-up-a-firewall-using-firewalld-on-opensuse-linux/

---

### 6.) Use Stream Deck using Boatswain:

In order for the Elgato Stream Deck to be used, a "udev rule" must be created.

#### 6a.) List all USB Devices Details using lsusb command:

    lsusb
    
![205458785-6e1c092c-cd12-48fb-8637-0e3dfe0f6f87](https://user-images.githubusercontent.com/79079633/222963013-9a9e4526-dbee-44cb-89c3-158c8a165341.jpg)

Then you need to replace the ATTRS{idVendor} and ATTRS{idProduct} in the following command:

    su

- Elgato Stream Deck Mini:

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0063", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck Original:

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0060", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck Original (v2):

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006d", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck XL:

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="006c", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck XL (v2):

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="008f", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck MK.2:

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0080", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

- Elgato Stream Deck Pedal:

      echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="0fd9", ATTRS{idProduct}=="0086", TAG+="uaccess"' >> /etc/udev/rules.d/70-streamdeck.rules

After that, it is best to restart the system:

    exit
    
    sudo reboot
    
Then all you have to do is pair Boatswain with OBS Studio: https://www.youtube.com/watch?v=zrgQyrtQrCo 

Further information can be found here:

  - https://flathub.org/apps/details/com.feaneron.Boatswain
  - https://gitlab.gnome.org/World/boatswain
  
---

### 7.) Changing the Theme, Icons & Wallpaper:

- https://www.gnome-look.org/p/1359276 <- Tela circle icon theme
- https://www.gnome-look.org/p/1831077 <- Colloid cursors theme
- https://www.gnome-look.org/p/1357889 <- Orchis gtk theme (Orchis-Teal version)
- https://itsfoss.com/flatpak-app-apply-theme/ <- How to Apply GTK Themes on Flatpak Applications?

![Bildschirmfoto vom 2023-05-14 16-46-29](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/f93e040f-52e6-4f4b-90dd-56853db4febf)

![Bildschirmfoto vom 2023-05-14 16-45-21](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/18efc45d-7a78-47dd-a5c0-04a45b3e2d1c)

---

### 8.) You can find further important information here:

- https://microos.opensuse.org/
- https://www.facebook.com/cryinkfly/
- https://www.instagram.com/cryinkfly/
- https://www.youtube.com/@cryinkfly
