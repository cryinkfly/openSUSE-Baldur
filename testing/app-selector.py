import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class CategorySelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Category Selection")
        self.set_default_size(400, 300)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled_window)

        vbox = Gtk.VBox(spacing=10)
        scrolled_window.add(vbox)

        self.categories = [
            {
                "name": "Productivity",
                "icons": ["productivity_logo1.png", "productivity_logo2.png", "productivity_logo3.png"],
                "titles": ["Title1", "Title2", "Title3"],
                "descriptions": ["Desc1", "Desc2", "Desc3"]
            },
            {
                "name": "Graphics & Photography",
                "icons": ["graphics_photography_logo1.png", "graphics_photography_logo2.png", "graphics_photography_logo3.png"],
                "titles": ["Title1", "Title2", "Title3"],
                "descriptions": ["Desc1", "Desc2", "Desc3"]
            },
            # ... Add entries for other categories
        ]

        for category in self.categories:
            category_box = Gtk.VBox(spacing=5)
            vbox.pack_start(category_box, True, True, 0)

            label = Gtk.Label(label=category["name"])
            category_box.pack_start(label, False, False, 0)

            treeview = self.create_treeview(category)
            category_box.pack_start(treeview, True, True, 0)

        button = Gtk.Button(label="Next")
        button.connect("clicked", self.on_next_clicked)
        vbox.pack_start(button, False, False, 0)

        # Dictionary to store selected options for each category
        self.selected_options_dict = {}

    def create_treeview(self, category):
        store = Gtk.ListStore(bool, GdkPixbuf.Pixbuf, str, str)

        for i in range(len(category["icons"])):
            icon = GdkPixbuf.Pixbuf.new_from_file_at_size(category["icons"][i], 24, 24)
            title = category["titles"][i]
            description = category["descriptions"][i]
            store.append([False, icon, title, description])

        treeview = Gtk.TreeView(model=store)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_checkbox_toggled, store, category["name"])
        column_toggle = Gtk.TreeViewColumn("Select", renderer_toggle, active=0)
        treeview.append_column(column_toggle)

        renderer_icon = Gtk.CellRendererPixbuf()
        column_icon = Gtk.TreeViewColumn("Icon", renderer_icon, pixbuf=1)
        treeview.append_column(column_icon)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Title", renderer_text, text=2)
        treeview.append_column(column_text)

        renderer_desc = Gtk.CellRendererText()
        column_desc = Gtk.TreeViewColumn("Description", renderer_desc, text=3)
        treeview.append_column(column_desc)

        return treeview

    def on_checkbox_toggled(self, widget, path, store, category_name):
        iter = store.get_iter(path)
        if iter:
            store[iter][0] = not store[iter][0]

        # Store the selected options for each category
        selected_options = [store[row][2] for row in range(len(store)) if store[row][0]]
        self.selected_options_dict[category_name] = selected_options

    def on_next_clicked(self, button):

        # username = The created user by the XFCE Initial Setup!
        username = "USERNAME" # <-- CHANGE
        command = f"runuser -l {username} -c 'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo --user && flatpak install flathub com.github.tchx84.Flatseal org.gnome.Calculator --user'"
            try:
                subprocess.run(command, shell=True, check=True)
                print("Blender installation completed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

        for category_name, selected_options in self.selected_options_dict.items():
            print(f"Selected options for {category_name}: {selected_options}")

            # Internet & E-Mail:

            if "Chromium Web Browser" in selected_options:
                print(f"Chromium Web Browser is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.chromium.Chromium --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Chromium Web Browser installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Firefox" in selected_options:
                print(f"Firefox is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.mozilla.firefox --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Firefox installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Microsoft Edge" in selected_options:
                print(f"Microsoft Edge is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.microsoft.Edge --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Microsoft Edge installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Thunderbird" in selected_options:
                print(f"Thunderbird is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.mozilla.Thunderbird --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Thunderbird installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Productivity:

            if "LibreOffice" in selected_options:
                print(f"LibreOffice is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.libreoffice.LibreOffice --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("LibreOffice installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "ONLYOFFICE" in selected_options:
                print(f"ONLYOFFICE is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.onlyoffice.desktopeditors --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("ONLYOFFICE installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "WPS Office" in selected_options:
                print(f"WPS Office is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.wps.Office --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("WPS Office installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Graphics & Photography:

            if "Blender" in selected_options:
                print(f"Blender is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.blender.Blender --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Blender installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "GIMP" in selected_options:
                print(f"GIMP is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.gimp.GIMP --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("GIMP installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Inkscape" in selected_options:
                print(f"Inkscape is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.inkscape.Inkscape --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Inkscape installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Audio & Video:

            if "Audacity" in selected_options:
                print(f"Audacity is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.audacityteam.Audacity --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Audacity installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Kdenlive" in selected_options:
                print(f"Kdenlive is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.kde.kdenlive --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Kdenlive installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "OBS Studio" in selected_options:
                print(f"OBS Studio is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.obsproject.Studio com.obsproject.Studio.Plugin.WebSocket --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("OBS Studio installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "VLC media player" in selected_options:
                print(f"VLC media player is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.videolan.VLC --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("VLC media player installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Education:

            if "GCompris" in selected_options:
                print(f"GCompris is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.kde.gcompris --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("GCompris installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Minuet" in selected_options:
                print(f"Minuet is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.kde.minuet --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Minuet installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Scratch" in selected_options:
                print(f"Scratch is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub edu.mit.Scratch --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Scratch installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Games:

            if "Discord" in selected_options:
                print(f"Discord is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.discordapp.Discord --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Discord installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Steam" in selected_options:
                print(f"Steam is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.valvesoftware.Steam --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Steam installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "SuperTuxKart" in selected_options:
                print(f"SuperTuxKart is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub net.supertuxkart.SuperTuxKart --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("SuperTuxKart installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Developer Tools:

            if "Geany" in selected_options:
                print(f"Geany is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.geany.Geany --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Geany installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Obsidian" in selected_options:
                print(f"Obsidian is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub md.obsidian.Obsidian --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Obsidian installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Visual Studio Code" in selected_options:
                print(f"Visual Studio Code is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.visualstudio.code --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Visual Studio Code installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Printing & CAD Tools:

            if "UltiMaker Cura" in selected_options:
                print(f"UltiMaker Cura is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.ultimaker.cura --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("UltiMaker Cura installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "FreeCAD" in selected_options:
                print(f"FreeCAD is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.freecadweb.FreeCAD --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("FreeCAD installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "PrusaSlicer" in selected_options:
                print(f"PrusaSlicer is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.prusa3d.PrusaSlicer --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("PrusaSlicer installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # System Tools:

            if "AnyDesk" in selected_options:
                print(f"AnyDesk is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.anydesk.Anydesk --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("AnyDesk installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Boxes" in selected_options:
                print(f"Boxes is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.gnome.Boxes --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Boxes installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Raspberry Pi Imager" in selected_options:
                print(f"Raspberry Pi Imager is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.raspberrypi.rpi-imager --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Raspberry Pi Imager installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # Security Tools:

            if "Authenticator" in selected_options:
                print(f"Authenticator is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.belmoussaoui.Authenticator --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Authenticator installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "KeePassXC" in selected_options:
                print(f"KeePassXC is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.keepassxc.KeePassXC --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("KeePassXC installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            if "Yubico Authenticator" in selected_options:
                print(f"Yubico Authenticator is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub com.yubico.yubioath --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("Yubico Authenticator installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")



win = CategorySelectionWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
