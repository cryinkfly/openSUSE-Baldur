import gi
gi.require_versions({'Gtk': '3.0', 'GdkPixbuf': '2.0'})
from gi.repository import GdkPixbuf, Gtk

class CategorySelectionWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Category Selection")
        self.set_default_size(400, 300)

        # Create a scrolled window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        self.add(scrolled_window)

        # Create a vertical box container
        vbox = Gtk.VBox(spacing=10)
        scrolled_window.add(vbox)

        categories = [
            {
                "name": "Productivity",
                "icons": ["productivity_logo1.png", "productivity_logo2.png", "productivity_logo3.png"],
                "titles": ["Fire", "Water", "Dust"],
                "descriptions": ["Hello World", "Lalelu", "Ohaha"]
            },
            {
                "name": "Graphics & Photography",
                "icons": ["graphics_photography_logo1.png", "graphics_photography_logo2.png", "graphics_photography_logo3.png"],
                "titles": ["Title1", "Title2", "Title3"],
                "descriptions": ["Desc1", "Desc2", "Desc3"]
            },
            # ... Add entries for other categories
        ]

        for category_info in categories:
            category_name = category_info["name"]
            icons = category_info["icons"]
            titles = category_info["titles"]
            descriptions = category_info["descriptions"]

            # Add category label
            label = Gtk.Label(label=category_name)
            vbox.pack_start(label, False, False, 0)

            # Create a TreeView for each category
            treeview = Gtk.TreeView()
            treeview.get_selection().set_mode(Gtk.SelectionMode.MULTIPLE)  # Allow multiple selection
            vbox.pack_start(treeview, True, True, 0)

            # Create a TreeStore for the data
            treestore = Gtk.TreeStore(GdkPixbuf.Pixbuf, str, str)

            # Function to load and insert icons
            def load_and_insert_icon(filename):
                try:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(filename, 24, 24)
                    return pixbuf
                except Exception as e:
                    print(f"Error loading icon: {e}")
                    return None

            # Insert data into the TreeStore (Icon, Title, Description)
            for i in range(len(icons)):
                icon_path = icons[i]
                pixbuf = load_and_insert_icon(icon_path)

                if pixbuf:
                    iter = treestore.append(None)
                    treestore.set(iter, 0, pixbuf, 1, titles[i], 2, descriptions[i])

            # Create a TreeViewColumn for the Icon
            renderer_pixbuf = Gtk.CellRendererPixbuf()
            column_pixbuf = Gtk.TreeViewColumn("Icon", renderer_pixbuf, pixbuf=0)
            treeview.append_column(column_pixbuf)

            # Create a TreeViewColumn for the Title
            renderer_text = Gtk.CellRendererText()
            column_text = Gtk.TreeViewColumn("Title", renderer_text, text=1)
            treeview.append_column(column_text)

            # Create a TreeViewColumn for the Description
            renderer_desc = Gtk.CellRendererText()
            column_desc = Gtk.TreeViewColumn("Description", renderer_desc, text=2)
            treeview.append_column(column_desc)

            # Link the TreeStore with the TreeView
            treeview.set_model(treestore)

if __name__ == "__main__":
    win = CategorySelectionWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

