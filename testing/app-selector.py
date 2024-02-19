import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class CategorySelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Category Selection")
        self.set_default_size(600, 300)
        self.set_border_width(35)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled_window)

        vbox = Gtk.VBox(spacing=10)
        scrolled_window.add(vbox)

        self.categories = [
            {
                "name": "Internet & E-Mail",
                "icons": ["graphics/chromium.png", "graphics/firefox.png", "graphics/microsoft-edge.png", "graphics/thunderbird.png"],
                "titles": ["Chromium", "Firefox", "Microsoft Edge", "Thunderbird"],
                "descriptions": ["Open-source Web Browser from Google", "Fast, Private & Safe Web Browser from Mozilla", "Smarter & Faster Web Browser with AI Support", "E-Mail, Newsfeed, Chat & Calendaring Client"]
            },
            {
                "name": "Productivity",
                "icons": ["productivity_logo1.png", "productivity_logo2.png", "productivity_logo3.png"],
                "titles": ["LibreOffice", "ONLYOFFICE", "WPS Office"],
                "descriptions": ["Powerful Free & Open Source Office Suite", "Secure compatible MS Online Office Suite", "Office Suite for PDF, Docs, Sheets & Slides"]
            },
            {
                "name": "Graphics & Photography",
                "icons": ["graphics_photography_logo1.png", "graphics_photography_logo2.png", "graphics_photography_logo3.png"],
                "titles": ["Blender", "GIMP", "Inkscape"],
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
            treeview.set_headers_visible(False)
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

            # Set active=True for Firefox, LibreOffice, ... entries:
            active = title in [
                "Firefox",
                "LibreOffice",
                "GIMP",
                "VLC media player",
                "Mousepad"
                ]

            store.append([active, icon, title, description])

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
        username = "steve" # <-- CHANGE
        command = f"runuser -l {username} -c 'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo --user'"
        try:
            subprocess.run(command, shell=True, check=True)
            print("The Flatpak Runtime has been configured!")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

        for category_name, selected_options in self.selected_options_dict.items():
            print(f"Selected options for {category_name}: {selected_options}")

            # Initialize a list to store Flatpak app names
            flatpak_apps = [""] * 36

            # Internet & E-Mail:

            if "Chromium Web Browser" in selected_options:
                print(f"Chromium Web Browser is selected for {category_name}. Performing action...")
                flatpak_apps[0] = "org.chromium.Chromium"

            if "Firefox" in selected_options:
                print(f"Firefox is selected for {category_name}. Performing action...")
                flatpak_apps[1] = "org.mozilla.firefox"

            if "Microsoft Edge" in selected_options:
                print(f"Microsoft Edge is selected for {category_name}. Performing action...")
                flatpak_apps[2] = "com.microsoft.Edge"

            if "Thunderbird" in selected_options:
                print(f"Thunderbird is selected for {category_name}. Performing action...")
                flatpak_apps[3] = "org.mozilla.Thunderbird"

            # Productivity:

            if "LibreOffice" in selected_options:
                print(f"LibreOffice is selected for {category_name}. Performing action...")
                flatpak_apps[4] = "org.libreoffice.LibreOffice"

            if "ONLYOFFICE" in selected_options:
                print(f"ONLYOFFICE is selected for {category_name}. Performing action...")
                flatpak_apps[5] = "org.onlyoffice.desktopeditors"

            if "WPS Office" in selected_options:
                print(f"WPS Office is selected for {category_name}. Performing action...")
                flatpak_apps[6] = "com.wps.Office"

            # Graphics & Photography:

            if "Blender" in selected_options:
                print(f"Blender is selected for {category_name}. Performing action...")
                flatpak_apps[7] = "org.blender.Blender"

            if "GIMP" in selected_options:
                print(f"GIMP is selected for {category_name}. Performing action...")
                flatpak_apps[8] = "org.gimp.GIMP"

            if "Inkscape" in selected_options:
                print(f"Inkscape is selected for {category_name}. Performing action...")
                flatpak_apps[9] = "org.inkscape.Inkscape"

            # Audio & Video:

            if "Audacity" in selected_options:
                print(f"Audacity is selected for {category_name}. Performing action...")
                flatpak_apps[10] = "org.audacityteam.Audacity"

            if "Boatswain" in selected_options:
                print(f"Boatswain is selected for {category_name}. Performing action...")
                flatpak_apps[11] = "com.feaneron.Boatswain"

            if "Kdenlive" in selected_options:
                print(f"Kdenlive is selected for {category_name}. Performing action...")
                flatpak_apps[12] = "org.kde.kdenlive"

            if "OBS Studio" in selected_options:
                print(f"OBS Studio is selected for {category_name}. Performing action...")
                flatpak_apps[13] = "com.obsproject.Studio com.obsproject.Studio.Plugin.WebSocket"

            if "VLC media player" in selected_options:
                print(f"VLC media player is selected for {category_name}. Performing action...")
                flatpak_apps[14] = "org.videolan.VLC"

            # Education:

            if "GCompris" in selected_options:
                print(f"GCompris is selected for {category_name}. Performing action...")
                flatpak_apps[15] = "org.kde.gcompris"

            if "Minuet" in selected_options:
                print(f"Minuet is selected for {category_name}. Performing action...")
                flatpak_apps[16] = "org.kde.minuet"

            if "Scratch" in selected_options:
                print(f"Scratch is selected for {category_name}. Performing action...")
                flatpak_apps[17] = "edu.mit.Scratch"

            # Games:

            if "Discord" in selected_options:
                print(f"Discord is selected for {category_name}. Performing action...")
                flatpak_apps[18] = "com.discordapp.Discord"

            if "Steam" in selected_options:
                print(f"Steam is selected for {category_name}. Performing action...")
                flatpak_apps[19] = "com.valvesoftware.Steam"

            if "SuperTuxKart" in selected_options:
                print(f"SuperTuxKart is selected for {category_name}. Performing action...")
                flatpak_apps[20] = "net.supertuxkart.SuperTuxKart"

            # Developer Tools:

            if "Geany" in selected_options:
                print(f"Geany is selected for {category_name}. Performing action...")
                flatpak_apps[21] = "org.geany.Geany"

            if "Obsidian" in selected_options:
                print(f"Obsidian is selected for {category_name}. Performing action...")
                flatpak_apps[22] = "md.obsidian.Obsidian"

            if "Visual Studio Code" in selected_options:
                print(f"Visual Studio Code is selected for {category_name}. Performing action...")
                flatpak_apps[23] = "com.visualstudio.code"

            # Printing & CAD Tools:

            if "UltiMaker Cura" in selected_options:
                print(f"UltiMaker Cura is selected for {category_name}. Performing action...")
                flatpak_apps[24] = "com.ultimaker.cura"

            if "FreeCAD" in selected_options:
                print(f"FreeCAD is selected for {category_name}. Performing action...")
                flatpak_apps[25] = "org.freecadweb.FreeCAD"

            if "PrusaSlicer" in selected_options:
                print(f"PrusaSlicer is selected for {category_name}. Performing action...")
                flatpak_apps[26] = "com.prusa3d.PrusaSlicer"

            # System Tools:

            if "AnyDesk" in selected_options:
                print(f"AnyDesk is selected for {category_name}. Performing action...")
                flatpak_apps[27] = "com.anydesk.Anydesk"

            if "Boxes" in selected_options:
                print(f"Boxes is selected for {category_name}. Performing action...")
                flatpak_apps[28] = "org.gnome.Boxes"

            if "Déjà Dup Backups" in selected_options:
                print(f"Déjà Dup Backups is selected for {category_name}. Performing action...")
                flatpak_apps[29] = "org.gnome.DejaDup"

            if "gedit" in selected_options:
                print(f"gedit is selected for {category_name}. Performing action...")
                flatpak_apps[30] = "org.gnome.gedit"

            if "KWrite" in selected_options:
                print(f"KWrite is selected for {category_name}. Performing action...")
                flatpak_apps[31] = "org.kde.kwrite"

            if "Mousepad" in selected_options:
                print(f"Mousepad is selected for {category_name}. Performing action...")
                flatpak_apps[32] = "org.xfce.mousepad"

            # Security Tools:

            if "Authenticator" in selected_options:
                print(f"Authenticator is selected for {category_name}. Performing action...")
                flatpak_apps[33] = "com.belmoussaoui.Authenticator"

            if "KeePassXC" in selected_options:
                print(f"KeePassXC is selected for {category_name}. Performing action...")
                flatpak_apps[34] = "org.keepassxc.KeePassXC"

            if "Yubico Authenticator" in selected_options:
                print(f"Yubico Authenticator is selected for {category_name}. Performing action...")
                flatpak_apps[35] = "com.yubico.yubioath"

            # Join non-empty app names
            flatpak_apps_str = " ".join(app for app in flatpak_apps if app)

            flatpak_command = f"runuser -l {username} -c 'flatpak install -y flathub com.github.tchx84.Flatseal org.gnome.Calculator {flatpak_apps_str} --user'"
            try:
                subprocess.run(flatpak_command, shell=True, check=True)
                print("The application installation completed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

win = CategorySelectionWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
