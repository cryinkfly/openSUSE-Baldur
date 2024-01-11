import gi
import os
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class TimeZoneSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Time Zone Selector")
        self.set_default_size(600, 450)

        # Create the main box
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.main_box)

        # Create the scrolled window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.main_box.pack_start(scrolled_window, True, True, 0)

        # Create the list store and tree view
        self.list_store = Gtk.ListStore(str)
        self.tree_view = Gtk.TreeView(model=self.list_store)
        scrolled_window.add(self.tree_view)

        # Create the columns
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Time Zone", renderer, text=0)
        self.tree_view.append_column(column)

        # Populate the list store with time zones
        time_zones = subprocess.check_output(["timedatectl", "list-timezones"]).decode("utf-8").splitlines()
        for zone in time_zones:
            self.list_store.append([zone])

        # Get the current time zone using the 'timedatectl' command
        current_time_cmd = "timedatectl | grep 'Time zone' | awk '{print $3}'"
        time_zone = os.popen(current_time_cmd).read().strip()

        # Create and set up the label
        self.time_zone_label = Gtk.Label(label=f"Current Time Zone: {time_zone}")
        self.main_box.pack_start(self.time_zone_label, False, False, 0)

        # Create a search entry
        search_entry = Gtk.SearchEntry()
        search_entry.connect("search-changed", self.on_search_changed)
        self.main_box.pack_start(search_entry, False, False, 0)

        # Create an apply button
        apply_button = Gtk.Button(label="Apply")
        apply_button.connect("clicked", self.on_apply_clicked)
        self.main_box.pack_start(apply_button, False, False, 0)

        # Connect the row-activated signal
        self.tree_view.connect("row-activated", self.on_row_activated)

    def on_row_activated(self, tree_view, path, column):
        # Get the selected time zone and update the label
        iter = self.list_store.get_iter(path)
        selected_time_zone = self.list_store.get_value(iter, 0)
        print(f"Selected Time Zone: {selected_time_zone}")
        self.new_time_zone = "Selected Time Zone: " + selected_time_zone
        self.time_zone_label.set_label(self.new_time_zone)

    def on_search_changed(self, entry):
        # Filter the list based on the search text
        search_text = entry.get_text().lower()
        self.list_store.clear()
        time_zones = subprocess.check_output(["timedatectl", "list-timezones"]).decode("utf-8").splitlines()
        for zone in time_zones:
            if search_text in zone.lower():
                self.list_store.append([zone])

    def on_apply_clicked(self, button):
        # Get the selected time zone and apply it using timedatectl
        selection = self.tree_view.get_selection()
        model, iter = selection.get_selected()
        if iter is not None:
            selected_time_zone = model.get_value(iter, 0)
            subprocess.run(["timedatectl", "set-timezone", selected_time_zone])
            print(f"Time Zone Applied: {selected_time_zone}")

if __name__ == "__main__":
    win = TimeZoneSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
