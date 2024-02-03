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
        command = f"runuser -l {username} -c 'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo --user'"
            try:
                subprocess.run(command, shell=True, check=True)
                print("Blender installation completed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

        for category_name, selected_options in self.selected_options_dict.items():
            print(f"Selected options for {category_name}: {selected_options}")

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

            if "VLC media player" in selected_options:
                print(f"VLC media player is selected for {category_name}. Performing action...")
                command = f"runuser -l {username} -c 'flatpak install flathub org.videolan.VLC --user'"
                try:
                    subprocess.run(command, shell=True, check=True)
                    print("VLC media player installation completed successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")

            # ...



win = CategorySelectionWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

