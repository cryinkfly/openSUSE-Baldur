import gi
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class WifiScanner(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Wi-Fi Scanner")
        self.set_default_size(400, 300)

        # Check if nmcli is available
        if not self.is_nmcli_available():
            print("Error: nmcli is not installed.")
            Gtk.main_quit()

        # Get available WiFi networks
        wifi_list = self.get_wifi_list()

        # UI Elements
        self.network_liststore = Gtk.ListStore(str)
        for wifi in wifi_list:
            self.network_liststore.append([wifi['SSID']])
        self.network_listview = Gtk.TreeView(self.network_liststore)
        self.passphrase_entry = Gtk.Entry()
        self.refresh_button = Gtk.Button("Refresh")
        self.connect_button = Gtk.Button("Connect")
        self.scrolled_window = Gtk.ScrolledWindow()

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Scrolled Window
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        self.scrolled_window.add(self.network_listview)

        # Network List View
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Available Networks", renderer, text=0)
        self.network_listview.append_column(column)

        # Passphrase Entry
        passphrase_label = Gtk.Label("Enter Passphrase:")
        passphrase_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        passphrase_box.pack_start(passphrase_label, False, False, 0)
        passphrase_box.pack_start(self.passphrase_entry, True, True, 0)

        # Refresh Button
        self.refresh_button.connect("clicked", self.update_network_list)

        # Connect Button
        self.connect_button.connect("clicked", self.on_connect_button_clicked)

        # Main Box
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        main_box.pack_start(self.scrolled_window, True, True, 0)
        main_box.pack_start(passphrase_box, False, False, 0)
        main_box.pack_start(self.refresh_button, False, False, 0)
        main_box.pack_start(self.connect_button, False, False, 0)

        self.add(main_box)

    def is_nmcli_available(self):
        try:
            subprocess.run(["nmcli", "--version"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def get_wifi_list(self):
        try:
            result = subprocess.run(["nmcli", "-f", "SSID", "d", "wifi", "list"], check=True, capture_output=True, text=True)
            wifi_list = []
            for line in result.stdout.strip().split('\n')[1:]:
                ssid = line.strip()
                wifi_list.append({'SSID': ssid})
            return wifi_list
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving WiFi list: {e}")
            return []

    def update_network_list(self, widget):
        # Clear existing network list
        self.network_liststore.clear()

        try:
            result = subprocess.run(["nmcli", "-f", "SSID", "d", "wifi", "list"], check=True, capture_output=True, text=True)
            wifi_list = []
            for line in result.stdout.strip().split('\n')[1:]:
                ssid = line.strip()
                self.network_liststore.append([ssid])
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving WiFi list: {e}")
            return []

        return True  # Continue updating

    def on_connect_button_clicked(self, widget):
        # Get selected network and passphrase
        selection = self.network_listview.get_selection()
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            ssid = model[treeiter][0]
            passphrase = self.passphrase_entry.get_text()

            # Connect to the selected network using "nmcli"
            try:
                subprocess.check_output(["nmcli", "d", "wifi", "connect", ssid, "password", passphrase],
                                        universal_newlines=True)
                print(f"Connected to {ssid}")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    win = WifiScanner()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
