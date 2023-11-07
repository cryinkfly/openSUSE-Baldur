<div id="openSUSE-MicroOS-header" align="center">
<img align="center" src="https://microos.opensuse.org/assets/images/microos-logo.svg" width="300px" height="150px">
<h1>[GUIDE] Tips, Tricks & Tutorials for getting fully up and running openSUSE MicroOS Desktop</h1>
<a href="https://en.opensuse.org/Portal:Aeon"><img src="https://img.shields.io/badge/Aeon-089f8f?style=for-the-badge"></a>
<a href="https://en.opensuse.org/Portal:Baldur"><img src="https://img.shields.io/badge/Baldur*-37a779?style=for-the-badge"></a>
<a href="https://en.opensuse.org/Portal:Kalpa"><img src="https://img.shields.io/badge/Kalpa-088fd7?style=for-the-badge"></a>
<br>
<img align="center" src="https://img.shields.io/github/license/cryinkfly/openSUSE-MicroOS?style=flat">
<img align="center" src="https://img.shields.io/github/last-commit/cryinkfly/openSUSE-MicroOS?style=flat">
<img align="center" src="https://img.shields.io/github/issues-raw/cryinkfly/openSUSE-MicroOS?style=flat"> 
<img align="center" src="https://img.shields.io/github/stars/cryinkfly/openSUSE-MicroOS?style=flat"> 
<img align="center" src="https://img.shields.io/github/forks/cryinkfly/openSUSE-MicroOS?style=flat"> 
</div>
 
---

<div id="openSUSE-MicroOS-about" align="center">
<h2>📜 Description</h2>
<p>In my project you will first receive a brief overview of the Linux distribution openSUSE MicroOS and will also receive some helpful tips in the areas of virtualization, Flatpak apps and display settings, to name just a few. Some executable scripts will also be published here that are intended to make the implementation of certain tasks quicker and easier. Of course, this always depends on the application and intended use. And now have fun exploring, experimenting and using openSUSE MicroOS!</p>
<a href="https://en.opensuse.org/Portal:MicroOS"><img src="https://img.shields.io/badge/Documentation-d3d9df?style=for-the-badge"></a>
<a href="https://microos.opensuse.org/#hardware"><img src="https://img.shields.io/badge/System Requirements-143f7a?style=for-the-badge"></a>
<a href="https://en.opensuse.org/Portal:MicroOS/Downloads"><img src="https://img.shields.io/badge/Downloads-5f9a1f?style=for-the-badge"></a>
<a href="https://bugzilla.opensuse.org/enter_bug.cgi?product=openSUSE+Tumbleweed&component=MicroOS&format=guided"><img src="https://img.shields.io/badge/Report a Bug-bb9d43?style=for-the-badge"></a>
<br></br>

**openSUSE Baldur is still in the development phase and is not yet officially available as a system role in the openSUSE MicroOS installation image, please keep this in mind!*
</div>

---

<div id="openSUSE-MicroOS-screenshots" align="center">
<h3>📸 Screenshots</h3>
<img src="https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/bf23b91e-251a-485c-961b-360a20edb627" width="300px" height="150px">
<img src="https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/dc1f31bc-3502-44fb-963b-b0d9c99fcd2c" width="300px" height="150px">
<img src="https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/3137e6e0-94d7-4b56-894c-ba8e9c3289ac" width="300px" height="150px">
<img src="https://user-images.githubusercontent.com/79079633/222974896-36ef1f0a-6deb-4620-b75c-954e821ddd9e.jpg" width="300px" height="150px">
<img src="https://user-images.githubusercontent.com/79079633/222975021-91deec7b-fd5f-4635-87c4-f02715043fa0.png" width="300px" height="150px">
</div>

---

<div id="openSUSE-MicroOS-screenshots">
<h3>🔖 Table of contents</h3>
<ul>
  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#1-brief-overview-of-opensuse-microos">1. Brief overview of openSUSE MicroOS</a></li>
    <ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#11-what-is-opensuse-microos">1.1 What is openSUSE MicroOS?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#12-what-features-does-opensuse-microos-offer">1.2 What features does openSUSE MicroOS offer?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#13-which-download-variants-are-available">1.3 Which download variants are available?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#14-which-desktops-can-i-choose-with-opensuse-microos">1.4 Which desktops can I choose with OpenSUSE MicroOS?</a></li> 
    </ul><br> 
  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#2-tips--tricks-for-opensuse-microos">2. Tips & tricks for openSUSE MicroOS</a></li>
    <ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#21-qemukvm-with-gpu-pci-usb--passthrough">2.1 QEMU/KVM with GPU, PCI-USB, ... Passthrough</a></li>
	<ul>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#211-which-packages-need-to-be-installed">2.1.1 Which packages need to be installed?</a></li>
          <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#212-how-can-i-turn-off-the-password-prompt-when-starting-the-virt-manager-application">2.1.2 How can I turn off the password prompt when starting the “Virt Manager” application?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#213-which-parameters-need-to-be-set-in-the-grub-file">2.1.3 Which parameters need to be set in the grub file?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#214-can-i-change-the-default-directorydrive-for-the-virtual-machines-guests">2.1.4 Can I change the default directory/drive for the virtual machines (guests)?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#215-what-settings-need-to-be-made-in-virt-manager-for-example-to-be-able-to-pass-on-the-graphics-card">2.1.5 What settings need to be made in Virt Manager, for example to be able to pass on the graphics card?</a></li>
        </ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#22-flatpak-runtime---apps">2.2 Flatpak-Runtime & -Apps</a></li>
        <ul>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#221-how-do-i-install-update-or-remove-flatpak-apps">2.2.1 How do I install, update or remove Flatpak apps?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#222-can-i-change-the-appearance-of-flatpak-apps">2.2.2 Can I change the appearance of Flatpak apps?</a></li>
        </ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#23-obs-studio--elgato-stream-decks">2.3 OBS-Studio & Elgato Stream Deck's</a></li>
        <ul>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#231-how-can-i-activate-the-virtual-camera-function-for-obs-studio-under-opensuse-microos">2.3.1 How can I activate the "Virtual Camera" function for OBS-Studio under openSUSE MicroOS?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#232-can-i-use-the-elgato-stream-deck-on-opensuse-microos">2.3.2 Can I use the Elgato Stream Deck on openSUSE MicroOS?</a></li>
        </ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#24-connect-to-your-mobile-phone-with-kde-connect-or-the-gsconnects-gnome-extension">2.4 Connect to your mobile phone with KDE-Connect or the GSConnect's Gnome extension</a></li>
        <ul>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#241-which-packages-need-to-be-installed">2.4.1 Which packages or Apps need to be installed?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#242-which-firewall-settings-need-to-be-set">2.4.2 Which firewall settings need to be set?</a></li>
        </ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#25-linux-security-with-yubikey--keepassxc">2.5 Linux Security with YubiKey</a></li>
	<ul>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#251-which-packages-need-to-be-installed">2.5.1 Which packages need to be installed?</a></li>
	  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#252-installing-the-yubico-authenticator--keepassxc">2.5.2 Installing the Yubico Authenticator</a></li>
        </ul> 
    </ul><br> 
  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#3-opensuse-baldur">3. openSUSE Baldur</a></li>
    <ul>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#31-what-is-opensuse-baldur">3.1 What is openSUSE Baldur?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#32-who-is-opensuse-baldur-for">3.2 Who is openSUSE Baldur for?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#33-what-are-the-design-goals-of-this-version-of-opensuse-microos-desktop">3.3 What are the design goals of this version of openSUSE MicroOS Desktop?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#34-how-can-i-download-and-install-this">3.4 How can I download and Install this?</a></li>
      <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#35-what-special-features-are-there">3.5 What special features are there?</a></li>
    </ul><br>
  <li><a href="https://github.com/cryinkfly/openSUSE-MicroOS#4-additional-information--links">4. Additional information & links</a></li>
</ul>
</div>

---

<h3>1. Brief overview of openSUSE MicroOS</h3>
<h4>1.1 What is openSUSE MicroOS?</h4>
<p>Designed to host container workloads with automated management and patching. Installing openSUSE MicroOS gives you a fast, small environment for deploying containers or other workloads that benefit from transactional updates. As a rolling release distribution, the software is always up to date.</p>

<h4>1.2 What features does openSUSE MicroOS offer?</h4>
<p>As a modern Linux operating system, openSUSE MicroOS is characterized as follows:</p>
<ul><li><b>Small:</b> Lightweight images designed to be deployed for a specific use case</li>
<li><b>Scalable:</b> Optimized for large deployments while capable as a single machine OS</li>
<li><b>Always up-to-date:</b> Updates are automatically applied without impacting the running system</li>
<li><b>Resilient:</b> In case of trouble the system automatically rolls back to last working state</li>
<li><b>Fast:</b> Doesn't ship with baggage that slows it down</li></ul>
<p>In other words, openSUSE MicroOS is an operating system you don't have to worry about. It is designed for, but not limited to, container hosts and edge devices. The focus on unattended operation makes it particularly suitable for large deployment environments. openSUSE MicroOS inherits the knowledge of openSUSE Tumbleweed and SUSE Linux Enterprise and redefines the operating system into a small, efficient and reliable distribution.</p>

<h4>1.3 Which download variants are available?</h4>
<p>In order to be able to install openSUSE MicroOS on the respective system, a variety of different images are available, such as:</p>
<ul><li><b>Intel or AMD 64-bit desktops, laptops, and servers (x86_64) image</b></li>
<li><b>UEFI Arm 64-bit servers, desktops, laptops and boards (aarch64) image</b></li>
<li><b>KVM and XEN image</b></li>
<li><b>VirtualBox image</b></li>
<li><b>VMware image</b></li>
<li><b>MS HyperV image</b></li>
<li><b>...</b></li></ul>
<p>If you are interested in installing it on your system yourself, then go to the <a href="https://en.opensuse.org/Portal:MicroOS/Downloads">download area of openSUSE images</a>!</p>

<h4>1.4 Which desktops can I choose with OpenSUSE MicroOS?</h4>

<table>
	<thead>
		<tr>
			<th></th>
			<th>Desktop environment?</th>
			<th>Packages installed?</th>
			<th>Memory (RAM) usage?</th>
			<th>Yubikeys are supported?[^5]</th>
			<th>Official supported?</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>openSUSE Base</td>
			<td>Terminal</td>
			<td>320 (rpm), 0 (flatpak)</td>
			<td>> 200 MB</td>
			<td><g-emoji class="g-emoji" alias="heavy_multiplication_x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png"><img class="emoji" alt="heavy_multiplication_x" src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png" width="20" height="20"></g-emoji></td>
			<td><g-emoji class="g-emoji" alias="heavy_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png"><img class="emoji" alt="heavy_check_mark" src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png" width="20" height="20"></g-emoji></td>
		</tr>
		<tr>
			<td><a href="https://en.opensuse.org/Portal:Aeon">openSUSE Aeon</a></td>
			<td>GNOME</td>
			<td>~ 1200 (rpm), 10 (flatpak)</td>
			<td>> 850 MB</td>
			<td><g-emoji class="g-emoji" alias="heavy_multiplication_x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png"><img class="emoji" alt="heavy_multiplication_x" src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png" width="20" height="20"></g-emoji></td>
			<td><g-emoji class="g-emoji" alias="heavy_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png"><img class="emoji" alt="heavy_check_mark" src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png" width="20" height="20"></g-emoji></td>
		</tr>
		<tr>
			<td><a href="https://en.opensuse.org/Portal:Baldur">openSUSE Baldur</a></td>
			<td>Xfce</td>
			<td>~ 1200 (rpm), 10 (flatpak)</td>
			<td>> 620 MB</td>
			<td><g-emoji class="g-emoji" alias="heavy_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png"><img class="emoji" alt="heavy_check_mark" src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png" width="20" height="20"></g-emoji></td>
			<td><g-emoji class="g-emoji" alias="heavy_multiplication_x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png"><img class="emoji" alt="heavy_multiplication_x" src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png" width="20" height="20"></g-emoji></td>
		</tr>
		<tr>
			<td><a href="https://en.opensuse.org/Portal:Kalpa">openSUSE Kalpa</a></td>
			<td>KDE Plasma</td>
			<td>~ 1300 (rpm), 10 (flatpak)</td>
			<td>> 780 MB</td>
			<td><g-emoji class="g-emoji" alias="heavy_multiplication_x" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png"><img class="emoji" alt="heavy_multiplication_x" src="https://github.githubassets.com/images/icons/emoji/unicode/2716.png" width="20" height="20"></g-emoji></td>
			<td><g-emoji class="g-emoji" alias="heavy_check_mark" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png"><img class="emoji" alt="heavy_check_mark" src="https://github.githubassets.com/images/icons/emoji/unicode/2714.png" width="20" height="20"></g-emoji></td>
		</tr>
	</tbody>
</table>

---

<h3>2. Tips & tricks for openSUSE MicroOS</h3>
<h4>2.1 QEMU/KVM with GPU, PCI-USB, ... Passthrough</h4>
<h5>2.1.1 Which packages need to be installed?</h5>
<p>Related software packages from openSUSE Leap and Tumbleweed software repositories are organized into installation patterns. openSUSE MicroOS uses openSUSE Tumbleweed repositories as a basis and therefore you can use these patterns to install specific virtualization components on an already running openSUSE MicroOS.<br><br>Use transactional-update to install them:</p>

    sudo transactional-update pkg install -t pattern PATTERN_NAME

To install the KVM environment, consider the following patterns:

    sudo transactional-update pkg install -t pattern kvm_server kvm_tools

- kvm_server = Installs basic VM Host Server with the KVM and QEMU environments.
- kvm_tools = Installs libvirt tools for managing and monitoring VM Guests in KVM environment.

And if you prefer to install the Xen environment, consider the following patterns:

    sudo transactional-update pkg install -t pattern xen_server xen_tools

- xen_server = Installs a basic Xen VM Host Server.
- xen_tools = Installs libvirt tools for managing and monitoring VM Guests in Xen environment.

The following packages are also required to find out the device IDs and for changing some config files:

    sudo transactional-update -c pkg install pciutils usbutils nano

And after successful installation of all packages and reboot, the libvirt service should be activated:

    sudo systemctl enable --now libvirtd

<h5>2.1.2 How can I turn off the password prompt when starting the “Virt Manager” application?</h5>
<p>With the addition of the "libvirt" user group, for example, the "normal" user is no longer asked for the "root" password when starting the "Virt Manager" application!<br><br>And for that you have to execute the following command:</p>

    sudo usermod -aG libvirt $USER

<h5>2.1.3 Which parameters need to be set in the grub file?</h5>

Enable the IOMMU feature and the [vfio-pci] kernel module on the KVM host (line 6). 

- for AMD CPU, set [amd_iommu=on iommu=pt video=efifb:off]
- for INTEL CPU, set [intel_iommu=on iommu=pt video=efifb:off]

*Note 1: The "video=efifb:off" option should only be added if your system is configured to automatically load the graphical environment! If you want to switch to the graphical environment via the terminal after booting, you may no longer see the terminal.*

*Note 2: In addition, the option causes problems with some NVIDIA graphics cards!*

*Note 3: Basically, the "amd_iommu=on" or "intel_iommu=on" option would also suffice, but you get better performance in the guest VM with the "iommu=pt" option and with the "video=efifb:off" option will prevent the driver from stealing the GPU.*

![Bildschirmfoto vom 2023-05-09 19-19-33](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/a91e4c93-92e3-4397-88df-6e68d10eee01)

1. The following commands must be executed[^1]:

       su -c 'nano /etc/default/grub'
    
2. Save changes with "Ctrl+X -> "Y". 

3. Show PCI identification number and [Vendor-ID:Device-ID] of the graphics card[^2] and USB controller:

       lspci -nn | grep -i amd #All AMD graphics cards are displayed!
    
       lspci -nn | grep -i nvidia #All NVIDIA graphics cards are displayed!
    
       lspci -nn | grep -i usb #All USB devices (controllers) are displayed!
	
- 12:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 24 [Radeon PRO W6400] [1002:7422]
- 12:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Navi 21/23 HDMI/DP Audio Controller [1002:ab28] 
- 06:00.0 USB controller [0c03]: ASMedia Technology Inc. ASM2142/ASM3142 USB 3.1 Host Controller [1b21:2142]
	
4. Two files (/etc/modprobe.d/vfio.conf &/etc/modules-load.d/vfio-pci.conf) must be created and your device-specific numbers must be entered there:

       su -c 'echo "options vfio-pci ids=1002:7422,1002:ab28,1b21:2142" > /etc/modprobe.d/vfio.conf && echo "vfio-pci" > /etc/modules-load.d/vfio-pci.conf'

5. You need to rebuild the initial ram disk to include all the needed modules. Create a file named /etc/dracut.conf.d/gpu-passthrough.conf:

       su -c 'nano /etc/dracut.conf.d/gpu-passthrough.conf'
    
       # Insert the respective line that matches your CPU!
    
       # INTEL CPU:
       add_drivers+="pci_stub vfio vfio_iommu_type1 vfio_pci vfio_virqfd kvm kvm_intel"
    
       #OR FOR AMD CPU:
       add_drivers+="pci_stub vfio vfio_iommu_type1 vfio_pci vfio_virqfd kvm kvm_amd"
    
6. Save changes with "Ctrl+X -> "Y" and now we regenerate grub and rebuild the initrd by executing:

       sudo transactional-update grub.cfg

       # With the -c option, the latest or given snapshot as base continues to be used after the regenerate grub.
       sudo transactional-update -c initrd
    
       sudo reboot

<h5>2.1.4 Can I change the default directory/drive for the virtual machines (guests)?</h5>
<p>In order to be able to change the default storage location of KVM Libvirt, you should also change this file (/etc/libvirt/qemu.conf):</p>

![Bildschirmfoto vom 2023-03-05 13-33-40](https://user-images.githubusercontent.com/79079633/222960741-8770a034-e1e1-40b9-bd70-6e052f67b053.png)

    su -c 'nano /etc/libvirt/qemu.conf'
    
*Note: The username "steve" should be replaced with your username!*

Save changes with "Ctrl+X -> "Y" and reboot the system with:

    sudo reboot

Further information can be found here:

- https://ostechnix.com/how-to-change-kvm-libvirt-default-storage-pool-location/
- https://ostechnix.com/solved-cannot-access-storage-file-permission-denied-error-in-kvm-libvirt/

<h5>2.1.5 What settings need to be made in Virt Manager, for example to be able to pass on the graphics card?</h5>
<p>I have already published a <a href="https://www.youtube.com/live/6u-ZKKVg9-A?feature=shared&t=10884">video</a> on my YouTube channel where I showed how, for example, you can pass a graphics card and a PCI USB card to the guest.</p>

<h5>2.1.6 The latest update in MicroOS (version: 20231101) means that KVM cannot start the "default" network!</h5>
<p>I have already written a workaround for this problem and you can read it here: https://github.com/cryinkfly/openSUSE-MicroOS/issues/2</p>

---

<h4>2.2 Flatpak-Runtime & -Apps</h4>
<h5>2.2.1 How do I install, update or remove Flatpak apps?</h5>
<p>Flatpak applications are installed either via the Gnome Software Center/Discover or via the terminal. The user can search for and install any application in the Software Center himself or install[^3] them all at once via the terminal.</p>

Please look this videos here: 

- https://youtu.be/SavmR9ZtHg0?feature=shared
- https://youtu.be/5w-Rt3QCV84?feature=shared

And install the Flatpak-App "Flatseal" on your system with this command:

    flatpak install --user com.github.tchx84.Flatseal

<h5>2.2.2 Can I change the appearance of Flatpak apps?</h5>

- https://www.gnome-look.org/p/1359276 <- Tela circle icon theme
- https://www.gnome-look.org/p/1831077 <- Colloid cursors theme
- https://www.gnome-look.org/p/1357889 <- Orchis gtk theme (Orchis-Teal version)
- https://itsfoss.com/flatpak-app-apply-theme/ <- How to Apply GTK Themes on Flatpak Applications?

Please look this video here: https://youtu.be/V-0yngWXbU4?feature=shared&t=1625

![Bildschirmfoto vom 2023-05-14 16-46-29](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/f93e040f-52e6-4f4b-90dd-56853db4febf)

![Bildschirmfoto vom 2023-05-14 16-45-21](https://github.com/cryinkfly/openSUSE-MicroOS/assets/79079633/18efc45d-7a78-47dd-a5c0-04a45b3e2d1c)

---

<h4>2.3 OBS-Studio & Elgato Stream Deck's</h4>
<h5>2.3.1 How can I activate the "Virtual Camera" function for OBS-Studio under openSUSE MicroOS?</h5>

First, the package ... must be installed with the following command:

    sudo transactional-update -c pkg install v4l2loopback-kmp-default

So that the “Virtual Camera” function can actually be used in OBS Studio under openSUSE MicroOS, a file (/etc/modules-load.d/v4l2loopback.conf) must be created using the following command via the terminal:

    su -c 'echo "v4l2loopback" > /etc/modules-load.d/v4l2loopback.conf'
    
    sudo reboot

After a restart, the “Virtual Camera” function can now be used in OBS Studio!

<h5>2.3.2 Can I use the Elgato Stream Deck on openSUSE MicroOS?</h5>
<p>Yes, the Elgato Stream Deck can be used on Linux by implementing or installing a few things.</p>

The best way to do this is with the Flatpak app Boatswain, for example!

Boatswain[^4] can then be installed via the app store (Gnome Software Center/Discover) or via the terminal with the following command:

    flatpak install --user com.feaneron.Boatswain com.obsproject.Studio.Plugin.WebSocket

After that you have to do the following things:

1. List all USB Devices Details using lsusb command:

       lsusb
    
![205458785-6e1c092c-cd12-48fb-8637-0e3dfe0f6f87](https://user-images.githubusercontent.com/79079633/222963013-9a9e4526-dbee-44cb-89c3-158c8a165341.jpg)

2. Then you need to replace the ATTRS{idVendor} and ATTRS{idProduct} in the following command:

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

3. After that, it is best to restart the system:

       exit
    
       sudo reboot
    
4. Then all you have to do is pair Boatswain with OBS Studio: https://www.youtube.com/watch?v=zrgQyrtQrCo 

Further information can be found here:

  - https://flathub.org/apps/details/com.feaneron.Boatswain
  - https://gitlab.gnome.org/World/boatswain

---

<h4>2.4 Connect to your mobile phone with KDE-Connect or the GSConnect's Gnome extension</h4>
<h5>2.4.1 Which packages need to be installed?</h5>
<p>So if you don't use a Gnome desktop environment, then you need to install the KDE-Connect app.<br><br>And you can do this with the following command:</p>

    sudo transactional-update -c pkg install kdeconnect-kde

Otherwise, simply install the <a href="https://extensions.gnome.org/extension/1319/gsconnect/">GSConnect's Gnome extension</a> via your web browser of your choice and activate it.

<h5>2.4.2 Which firewall settings need to be set?</h5>
<p>You need to make the following changes to your firewall settings:</p>

    sudo firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=1714-1764/udp --permanent
    #OR
    su -c 'firewall-cmd --zone=public --add-port=1714-1764/tcp --permanent && firewall-cmd --zone=public --add-port=1714-1764/udp --permanent'

    sudo reboot

Further information can be found here: 

- https://extensions.gnome.org/extension/1319/gsconnect/
- https://en.opensuse.org/SDB:KDE_Connect
- https://www.cyberciti.biz/faq/set-up-a-firewall-using-firewalld-on-opensuse-linux

---


<h4>2.5 Linux Security with YubiKey & KeePassXC</h4>
<h5>2.5.1 Which packages need to be installed?</h5>
<p>For example, so that the USB sticks from Yubico can be used under openSUSE MicroOS, a few packages must be installed on your system.<br><br>And that can be done with the following command:</p>

    sudo transactional-update -c pkg install pcsc-ccid pcsc-tools

<h5>2.5.2 Installing the Yubico Authenticator & KeePassXC</h5>
<p>The Yubico Authenticator and KeePassXC can then be installed via the app store (Gnome Software Center/Discover) or via the terminal with the following command:</p>

    flatpak install --user com.yubico.yubioath org.keepassxc.KeePassXC

---

<h3>3. openSUSE Baldur</h3>
<h4>3.1 What is openSUSE Baldur?</h4>

openSUSE Baldur provides only a minimal base system with a XFCE Desktop Environment and Basic Configuration Tools ONLY. All Applications, Browsers, Codecs, etc are provided by FlatPaks from FlatHub.

<h4>3.2 Who is openSUSE Baldur for?</h4>

It is NOT for everyone. Your highly customisable Tumbleweed & Leap Desktops are safe and will remain the best choice for those who want to tinker with their Desktop.

It should be perfect for lazy developers, who no longer want to mess around with their desktop and just ”get stuff done”, especially if they develop around containers.

It should also appeal to the same audience now more used to an iOS, Chromebook or Android-like experience where the OS is static, automated & reliable and the Apps are the main thing the user cares about.

To deep dive on the origins and the case why some users should use openSUSE Baldur check out the following workshop:

- https://youtu.be/V-0yngWXbU4?feature=shared
- https://www.youtube.com/live/PPYOM3z_DIc?feature=shared 

<h4>3.3 What are the design goals of this version of openSUSE MicroOS Desktop?</h4>

Baldur should be reliable, predictable & immutable, just like openSUSE MicroOS.

Baldur should be less customisable than regular openSUSE Tumbleweed/Leap.

Baldur should be small, but not at the expense of functionality. Printing, Gaming, Media Production and much more should all work.

Baldur should just work “out of the box” without the need for additional configuration to get key functionality like software installation and web browsing working. All features offered by default should work - features that don't work shouldn't be offered/visible/available to users. 

<h4>3.4 How can I download and Install this?</h4>

Since openSUSE Baldur is still in development and is not in the official installation medium of openSUSE MicroOS, the installation is still a bit complicated!

Because some Linux knowledge is required in terms of using the command line in order to be able to run the installation script after the basic installation of openSUSE MicroOS.

For this reason, please watch the above two videos!

And this would be the command after the basic installation of openSUSE MicroOS to get the XFCE desktop: 

    curl https://raw.githubusercontent.com/cryinkfly/openSUSE-MicroOS/main/files/builds/baldur/stable-branch/bin/install.sh > install-openSUSE-Baldur.sh && chmod +x install-openSUSE-Baldur.sh && ./install-openSUSE-Baldur.sh

<h4>3.5 What special features are there?</h4>
<p>Since openSUSE Baldur is basically structured in the same way as openSUSE Aeon and Kalpa, it also offers the same functions!<br><br>However, openSUSE Baldur has a few special features:</p>
<ul><li><b>Graphics card driver:</b> The installation script install the graphics card drivers (e.g.: NVIDIA CUDA, ...) automaticly!</li>
<li><b>Keyboard shortcuts:</b> The keyboard shortcuts have been adapted directly for the XFCE and Flatpak environment!</li>
<li><b>2FA authentication:</b> The 2FA authentication using external devices such as a Yubikey works out-of-the-box after installing openSUSE Baldur!</li>
<li>...</li></ul>
<p>In other words, openSUSE Baldur is a new flavor of openSUSE MicroOS Desktop that gives users a light, fast and stable working environment.</p>

---

<h3>4. Additional information & links</h3>

You can find further important information here:

- https://microos.opensuse.org/
- https://en.opensuse.org/Portal:Aeon
- https://en.opensuse.org/Portal:Baldur
- https://en.opensuse.org/Portal:Kalpa
- https://www.cryinkfly.com
- https://www.facebook.com/cryinkfly/
- https://www.instagram.com/cryinkfly/
- https://www.youtube.com/@cryinkfly

[^1]: Nano is used as the editor in this example!
[^2]: The audio controller from the graphics card must also be passed through to the VM!
[^3]: Flatpak apps are automatically installed in USER mode!
[^4]: Boatswain requires the WebSocket plugin to connect to OBS Studio!
[^5]: Under openSUSE Baldur the Yubikeys are supported by default after installation!
