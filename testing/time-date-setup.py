import gi
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class TimeZoneSelector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Time Zone Selector")
        self.set_default_size(600, 450)

        # Create a scrolled window
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        # Create a ListBox to hold the time zones
        time_zone_list = Gtk.ListBox()
        scrolled_window.add(time_zone_list)

        # Fetch the time zones using 'timedatectl list-timezones'
        time_zones = subprocess.check_output(["timedatectl", "list-timezones"], text=True).splitlines()

        # Add time zones to the ListBox
        for zone in time_zones:
            row = Gtk.ListBoxRow()
            label = Gtk.Label(label=zone)
            row.add(label)
            time_zone_list.add(row)

        # Connect the toggle-event signal to handle selection
        time_zone_list.connect("row-activated", self.on_time_zone_selected)

        # Create a Label to display the selected time zone
        self.selected_time_zone_label = Gtk.Label()

        # Create an Apply button
        apply_button = Gtk.Button(label="Apply")
        apply_button.connect("clicked", self.on_apply_button_clicked)

        # Create a VBox to hold the elements
        vbox = Gtk.VBox(spacing=10)
        vbox.pack_start(scrolled_window, True, True, 0)
        vbox.pack_start(self.selected_time_zone_label, False, False, 0)
        vbox.pack_start(apply_button, False, False, 0)

        self.add(vbox)

    def on_time_zone_selected(self, list_box, row):
        # Get the selected time zone and update the label
        selected_zone = row.get_child().get_label()
        self.selected_time_zone_label.set_label(f"Selected Time Zone: {selected_zone}")

    def on_apply_button_clicked(self, button):
        # Get the selected time zone and apply it using 'timedatectl set-timezone'
        selected_zone = self.selected_time_zone_label.get_label().replace("Selected Time Zone: ", "")
        subprocess.run(["timedatectl", "set-timezone", selected_zone])
        print(f"Time zone set to {selected_zone}")

if __name__ == "__main__":
    win = TimeZoneSelector()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
