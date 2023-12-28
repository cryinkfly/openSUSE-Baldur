#!/usr/bin/python	

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import os
import random
import string

##############################################################################################################################################################################
##############################################################################################################################################################################

# Remove all TMP-Files:
def Del_Tmp_files():
    del_tmp_files_cmd="rm /tmp/_*.XXXXXXX"
    os.system(del_tmp_files_cmd)

##############################################################################################################################################################################
##############################################################################################################################################################################

# Load the MainWindow:
def Main():
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

##############################################################################################################################################################################
##############################################################################################################################################################################

# Reload the MainWindow:
def Reload_MainWindow(self, widget):
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    self.hide()
    return True  # Returning True stops the default action (closing the window)

##############################################################################################################################################################################
##############################################################################################################################################################################

# Show the MainWindow:
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Main container (VERTICAL)
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_border_width(10)
        self.add(main_box)

        # Info text container (HORIZONTAL)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(info_box, False, False, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            "<big><b>Benutzereinstellungen</b></big>"
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label(label="In diesem Bereich können Sie die Einstellungen des Benutzerkontos ändern und Benutzer hinzufügen/löschen, die mit ihrem Konto verknüpft sind. Wählen Sie einfach aus der Liste den Benutzer aus, den Sie ändern oder löschen möchten.")
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        # Checklist container (HORIZONTAL)
        check_file_cmd="""
            #!/bin/bash
            LIST_ALL_HUMAN_USERS() {
                list_users=$(awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd)
                echo "$list_users" | tr ' ' '\n' > /tmp/_all_users_list_.XXXXXXX

                if [ "$(id -u)" != "0" ]; then
                    echo "Show only human users"
                else
                    username=$(whoami)
                    echo "$username" >> /tmp/_all_users_list_new.XXXXXXX
                fi

                cat /tmp/_all_users_list_.XXXXXXX | while read line; do echo ${line} >> /tmp/_all_users_list_new.XXXXXXX; done
                rm /tmp/_all_users_list_.XXXXXXX
                mv /tmp/_all_users_list_new.XXXXXXX /tmp/_all_users_list_.XXXXXXX
            }

            ##############################################################################################################################################################################

            LIST_ALL_GROUPS() {
                list_all_groups=$(cut -d: -f1 /etc/group | sort)
                echo "$list_all_groups" | tr ' ' '\n' > /tmp/_all_groups_list_.XXXXXXX
                #cat /tmp/_all_groups_list_.XXXXXXX | while read line; do echo "FALSE" >> /tmp/_all_groups_list_new.XXXXXXX && echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
                cat /tmp/_all_groups_list_.XXXXXXX | while read line; do echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
                mv /tmp/_all_groups_list_new.XXXXXXX /tmp/_all_groups_list_.XXXXXXX
                        }

            ##############################################################################################################################################################################

            LIST_ALL_HUMAN_USERS
            LIST_ALL_GROUPS
        """
        os.system(check_file_cmd)

        # Load options from a text file
        options = self.load_options_from_file("/tmp/_all_users_list_.XXXXXXX")

        # Radio List
        self.radio_list = Gtk.ListStore(bool, str)
        for option in options:
            self.radio_list.append([False, option])

        # TreeView
        treeview = Gtk.TreeView(model=self.radio_list)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_toggle, treeview)
        column_toggle = Gtk.TreeViewColumn("Select", renderer_toggle, active=0)
        treeview.append_column(column_toggle)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Options", renderer_text, text=1)
        treeview.append_column(column_text)

        # Buttons
        close_button = Gtk.Button(label="◀️ Zurück")
        close_button.connect("clicked", self.on_close_clicked)

        add_button = Gtk.Button(label="🎭 Erstellen")
        add_button.connect("clicked", self.on_add_clicked)

        configure_button = Gtk.Button(label="⚙️ Konfigurieren")
        configure_button.connect("clicked", self.on_configure_clicked)

        del_button = Gtk.Button(label="🗑 Löschen")
        del_button.connect("clicked", self.on_del_clicked)

        # Button Box
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_box.pack_start(close_button, True, True, 0)
        button_box.pack_start(add_button, True, True, 0)
        button_box.pack_start(configure_button, True, True, 0)
        button_box.pack_start(del_button, True, True, 0)

        main_box.pack_start(label_info, False, True, 10)
        main_box.pack_start(treeview, True, True, 0)
        main_box.pack_start(button_box, False, False, 0)

        self.add(main_box)

    def load_options_from_file(self, filename):
        with open(filename, 'r') as file:
            options = [line.strip() for line in file.readlines()]
        return options

    def on_toggle(self, widget, path, treeview):
        self.radio_list[path][0] = not self.radio_list[path][0]

    def on_close_clicked(self, button):
        # Delete tmp-files:
        del_tmp_files_cmd="rm /tmp/_*.XXXXXXX"
        os.system(del_tmp_files_cmd)
        Gtk.main_quit()

    def on_add_clicked(self, button):
            window1_1 = Window_Create_User()
            window1_1.connect("destroy", Gtk.main_quit)
            window1_1.show_all()

            self.hide()
            return True

    def on_configure_clicked(self, widget):
        selected_option = self.get_selected_option()
        if selected_option:
            selected_user_cmd=f"""
                #!/bin/bash
                echo -n {selected_option} > /tmp/_selected_user.XXXXXXX
                list_user_groups=$(id -nG {selected_option})
                echo "$list_user_groups" | tr ' ' '\n' > /tmp/_all_groups_of_user_list_.XXXXXXX
            """
            os.system(selected_user_cmd)

            window2_1 = Window_Configure_User()
            window2_1.connect("destroy", Gtk.main_quit)
            window2_1.show_all()
            
            self.hide()
            return True

        else:
            print(f"Click Configure button was triggered but no option was selected!")
            window2_2 = MainWindow_No_Configure_Selected_User_Info()
            window2_2.connect("destroy", Gtk.main_quit)
            window2_2.show_all()
            
            self.hide()
            return True        

    def on_del_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            del_selected_user_cmd=f"""
                    #!/bin/bash
                    whoami > /tmp/_active_user.XXXXXXX
                    echo -n {selected_option} > /tmp/_selected_user.XXXXXXX
                    echo -n "Möchten Sie den Benutzer {selected_option} wirklich von Ihrem System entfernen? \nWenn Ihre Antwort >>JA<< ist, werden der ausgewählte Benutzer und alle damit verbundenen Daten aus diesem System entfernt!" > /tmp/_selected_del_user_warn_text.XXXXXXX
                    echo -n "Der ausgewählte Benutzer {selected_option} kann nicht gelöscht werden, da Sie mit ihm bei diesem System angemeldet sind! \nWählen Sie bitte einen anderen Benutzer aus, falls Sie mit dem Löschen von Benutzern fortfahren möchten, die auf diesem System nicht mehr benötigt werden." > /tmp/_selected_del_user_info_text.XXXXXXX
               """
            os.system(del_selected_user_cmd)

            open_active_user_file = open(r"/tmp/_active_user.XXXXXXX",'r') 
            read_active_user_file = open_active_user_file.read()
            open_active_user_file.close()

            # Test another user with overriding the variable ...
            #read_active_user_file="user"
            print(f"Active user: {read_active_user_file}")

            # This checks whether the selected user is currently logged in or not! (if...else...)
            if selected_option in read_active_user_file:
                print(f"The user is currently logged in!")
                # Perform actions if variable1 is found
                window3_1 = Window_Del_Selection_Info()
                window3_1.connect("destroy", Gtk.main_quit)
                window3_1.show_all()
                self.hide()
                return True

            else:
                print(f"The user is not currently logged in.")
                # Perform actions if variable1 is not found
                window3_2 = Window_Del_Selection_Warn()
                window3_2.connect("destroy", Gtk.main_quit)
                window3_2.show_all()
                self.hide()
                return True

        else:
            print(f"Click Delete button was triggered but no option was selected!")
            window3_3 = MainWindow_No_Del_Selected_User_Info()
            window3_3.connect("destroy", Gtk.main_quit)
            window3_3.show_all()
            self.hide()
            return True

    def get_selected_option(self):
        selection = self.radio_list.get_iter_first()
        while selection is not None:
            if self.radio_list.get_value(selection, 0):
                return self.radio_list.get_value(selection, 1)
            selection = self.radio_list.iter_next(selection)
        return None

##############################################################################################################################################################################

class MainWindow_No_Del_Selected_User_Info(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("💡")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Sie haben keinen Benutzer zum Löschen ausgewählt! \nBitte wählen Sie einen Benutzer aus, bevor Sie fortfahren.")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class MainWindow_No_Configure_Selected_User_Info(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("💡")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Sie haben keinen Benutzer zum Konfigurieren ausgewählt! \nBitte wählen Sie einen Benutzer aus, bevor Sie fortfahren.")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Create_User(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Main container (VERTICAL)
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_border_width(10)
        self.add(main_box)

        # Info text container (HORIZONTAL)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(info_box, False, False, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            "<big><b>Benutzerkonto erstellen</b></big>"
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label(label="Bitte füllen Sie die folgenden Angaben aus, um ein neues Konto zu erstellen.")
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)      

        # Fullname container (HORIZONTAL)
        fullname_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        fullname_box.set_halign(Gtk.Align.CENTER)
        fullname_box.set_valign(Gtk.Align.CENTER)
        fullname_box.set_margin_top(20)
        main_box.pack_start(fullname_box, False, False, 0)
        fullname_label = Gtk.Label("Vollständiger Name:    ")
        fullname_box.pack_start(fullname_label, False, False, 0)
        self.fullname_entry = Gtk.Entry()
        self.fullname_entry.set_hexpand(True)
        self.fullname_entry.set_halign(Gtk.Align.CENTER)
        self.fullname_entry.set_width_chars(25)
        fullname_box.pack_start(self.fullname_entry, False, False, 0)

        # Username container (HORIZONTAL)
        username_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        username_box.set_halign(Gtk.Align.CENTER)
        username_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(username_box, False, False, 0)
        username_label = Gtk.Label("Benutzername:    ")
        username_box.pack_start(username_label, False, False, 0)
        self.username_entry = Gtk.Entry()
        self.username_entry.set_hexpand(True)
        self.username_entry.set_halign(Gtk.Align.CENTER)
        self.username_entry.set_width_chars(25)
        username_box.pack_start(self.username_entry, False, False, 0)
        
        # Password container (HORIZONTAL)
        password_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        password_box.set_halign(Gtk.Align.CENTER)
        password_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(password_box, False, False, 0)
        password_label = Gtk.Label("Passwort:      ")
        password_box.pack_start(password_label, False, False, 0)
        self.password_entry = Gtk.Entry()
        self.password_entry.set_hexpand(True)
        self.password_entry.set_halign(Gtk.Align.CENTER)
        self.password_entry.set_width_chars(25)
        self.password_entry.set_visibility(False)  # Password is hidden by default
        password_box.pack_start(self.password_entry, False, False, 0)

        # Password-Confirm container (HORIZONTAL)
        password_confirm_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        password_confirm_box.set_halign(Gtk.Align.CENTER)
        password_confirm_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(password_confirm_box, False, False, 0)
        confirm_password_label = Gtk.Label("Passwort bestätigen:")
        password_confirm_box.pack_start(confirm_password_label, False, False, 0)
        self.confirm_password_entry = Gtk.Entry()
        self.confirm_password_entry.set_hexpand(True)
        self.confirm_password_entry.set_halign(Gtk.Align.CENTER)
        self.confirm_password_entry.set_width_chars(25)
        self.confirm_password_entry.set_visibility(False)  # Confirm password is hidden by default
        password_confirm_box.pack_start(self.confirm_password_entry, False, False, 0)

        # Show password checkbox container (HORIZONTAL)
        show_password_autologin_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        show_password_autologin_box.set_margin_top(10)
        show_password_autologin_box.set_halign(Gtk.Align.CENTER)
        show_password_autologin_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(show_password_autologin_box, False, False, 0)
        show_password_checkbox = Gtk.CheckButton(" Passwort anzeigen")
        show_password_checkbox.connect("toggled", self.toggle_password_visibility)
        show_password_checkbox.set_halign(Gtk.Align.CENTER)
        show_password_checkbox.set_valign(Gtk.Align.CENTER)
        show_password_autologin_box.pack_start(show_password_checkbox, False, False, 0)
        box_autologin = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box_autologin.set_halign(Gtk.Align.CENTER)
        box_autologin.set_valign(Gtk.Align.CENTER)
        label = Gtk.Label(label="|   Automatische Anmeldung:")
        box_autologin.pack_start(label, True, True, 0)
        show_password_autologin_box.pack_start(box_autologin, False, False, 0)
        autologin_switch = Gtk.Switch()
        autologin_switch.connect("notify::active", self.autologin_check_status)
        show_password_autologin_box.pack_start(autologin_switch, True, True, 0)

        # Buttons - Container
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button_box.set_margin_top(20)
        main_box.pack_start(button_box, False, False, 0)
        go_back_button = Gtk.Button("◀️ Zurück")
        go_back_button.connect("clicked", self.on_back_clicked)
        button_box.pack_start(go_back_button, True, True, 0)
        random_password_button = Gtk.Button("🎲 Passwort")
        random_password_button.connect("clicked", self.generate_random_password)
        button_box.pack_start(random_password_button, True, True, 0)
        reset_button = Gtk.Button("🔄 Zurücksetzen")
        reset_button.connect("clicked", self.reset_entries)
        button_box.pack_start(reset_button, True, True, 0)  
        create_button = Gtk.Button("🎭 Erstellen")
        create_button.connect("clicked", self.create_user)
        button_box.pack_start(create_button, True, True, 0)

    def autologin_check_status(self, autologin_switch, gparam):
        if autologin_switch.get_active():
            print("Automatic login: Yes")
            autologin_status_cmd="echo -n 'Yes' > /tmp/_autologin_status_.XXXXXXX"
            os.system(autologin_status_cmd)
        else:
            print("Automatic login: No")

    def create_user(self, widget):
        fullname = self.fullname_entry.get_text()
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()
        confirm_password = self.confirm_password_entry.get_text()

        if password == confirm_password:
            if len(password) < 8:
                print("Password must be at least 8 characters.")
                window1_2 = Window_Create_User_Error_1()
                window1_2.connect("destroy", Gtk.main_quit)
                window1_2.show_all()
            else:
                add_user_cmd=f"""
                    #!/bin/bash
                    # Converting the password:
                    pass=$(perl -e 'print crypt($ARGV[0], "password")' {password})
                        
                    # Set the desired username for autologin:
                    autologin_user="{username}"

                    # Specify the path to the display manager configuration file:
                    display_manager_config="/etc/sysconfig/displaymanager"

                    # Check the Autologin-Status:
                    if grep -q "Yes" "/tmp/_autologin_status_.XXXXXXX"; then
                        # Check if the file exists
                        if [ -f "$display_manager_config" ]; then
                            # Create a temporary script file
                            script_1=$(mktemp)

                            # Add user and modify group membership in the temporary script
                            echo "useradd -m -p $pass -c '{fullname}' {username}" > "$script_1"
                            echo "usermod -a -G users {username}" >> "$script_1"

                            echo "$script_1"

                            # Execute the temporary script with elevated privileges using pkexec
                            pkexec su -c "bash $script_1"

                            # Remove the temporary script
                            rm "$script_1"

                            pkexec sed -i "s/DISPLAYMANAGER_AUTOLOGIN=.*/DISPLAYMANAGER_AUTOLOGIN=\"$autologin_user\"/" "$display_manager_config"
 
                            # Display a message indicating success
                            echo "Autologin user set to: $autologin_user"
                        else
                            # Display an error message if the file does not exist
                            echo "Error: Display manager configuration file not found at $display_manager_config"
                        fi
                    else
                        # Create a temporary script file
                        script_2=$(mktemp)

                        # Add user and modify group membership in the temporary script
                        echo "useradd -m -p $pass -c '{fullname}' {username}" > "$script_2"
                        echo "usermod -a -G users {username}" >> "$script_2"
                        echo "mkdir -p /home/{username}/.config/xfce4/xfconf/xfce-perchannel-xml" >> "$script_2"

                        # KEYBOARD SHORTCUTS & XFCE4-POWER-MANAGER:
                        echo "cp ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml /home/{username}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml" >> "$script_2"
                        echo "cp ~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml /home/{username}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml" >> "$script_2"
                        echo "chown -R {username}:{username} /home/{username}/.config/xfce4/" >> "$script_2"
                        echo "chmod -R g-rwx /home/{username}/.config/xfce4/" >> "$script_2"
                        echo "chmod -R o-rwx /home/{username}/.config/xfce4/" >> "$script_2"

                        # FIRSTBOOT SETUP OF FLATPAK:
                        echo "mkdir -p /home/{username}/.config/autostart" >> "$script_2"
                        echo "cat > /home/{username}/.config/autostart/mod-firstboot.desktop << EOF" >> "$script_2"
                        echo "[Desktop Entry]" >> "$script_2"
                        echo "Name=MicroOS Desktop FirstBoot Setup" >> "$script_2"
                        echo "Comment=Sets up MicroOS Desktop Correctly On FirstBoot" >> "$script_2"
                        echo "Exec=/usr/bin/mod-firstboot" >> "$script_2"
                        echo "Icon=org.xfce.terminal" >> "$script_2"
                        echo "Type=Application" >> "$script_2"
                        echo "Categories=Utility;System;" >> "$script_2"
                        echo "Name[en_US]=startup" >> "$script_2"
                        echo "EOF" >> "$script_2"
                        echo "chown {username}:{username} /home/{username}/.config/autostart/" >> "$script_2"

                        # Execute the temporary script with elevated privileges using pkexec
                        pkexec su -c "bash $script_2"

                        # Remove the temporary script
                        rm "$script_2"
                    fi
                """
                os.system(add_user_cmd)

                print("User created successfully.")
                window1_3 = Window_Create_User_Info_Completed()
                window1_3.connect("destroy", Gtk.main_quit)
                window1_3.show_all()
                self.hide()
                return True
        else:
            print("Passwords do not match. Please try again.")
            window1_4 = Window_Create_User_Error_2()
            window1_4.connect("destroy", Gtk.main_quit)
            window1_4.show_all()

    def generate_random_password(self, widget):
        chars = string.ascii_letters + string.digits + "#$%&"
        random_password = "".join(random.choice(chars) for _ in range(12))
        self.password_entry.set_text(random_password)

    def toggle_password_visibility(self, widget):
        visibility = widget.get_active()
        self.password_entry.set_visibility(visibility)
        self.confirm_password_entry.set_visibility(visibility)

    def reset_entries(self, widget):
        self.fullname_entry.set_text("")
        self.username_entry.set_text("")
        self.password_entry.set_text("")
        self.confirm_password_entry.set_text("")

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

# ... User created ...
class Window_Create_User_Info_Completed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_create_user_info_text_file = open(r"/tmp/_create_user_text.XXXXXXX",'r') 
        #read_create_user_info_text_file_file = open_create_user_info_text_file.read()
        #open_create_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("✅")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das Benutzerkonto wurde erfolgreich erstellt und Sie können diesen neuen Benutzer nach erneuter Anmeldung verwenden!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Create_User_Error_1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_create_user_info_text_file = open(r"/tmp/_create_user_error1_text.XXXXXXX",'r') 
        #read_create_user_info_text_file_file = open_create_user_info_text_file.read()
        #open_create_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das neue Passwort muss mindestens 8 Zeichen lang sein!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

# ... Password not match ...
class Window_Create_User_Error_2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_create_user_info_text_file = open(r"/tmp/_create_user_error1_text.XXXXXXX",'r') 
        #read_create_user_info_text_file_file = open_create_user_info_text_file.read()
        #open_create_user_info_text_file.close()  

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Die neuen Kennwörter des Benutzerkontos stimmen nicht überein. Bitte versuche es erneut!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Configure_User(Gtk.Window):

    # Check if the autologin user is the same as the current user
    def is_autologin_user():   
        try:
            with open("/etc/sysconfig/displaymanager", "r") as file:
                for line in file:
                    if line.startswith("DISPLAYMANAGER_AUTOLOGIN="):
                        autologin_user = line.split("=")[1].strip()
                        #current_user = os.getenv("USER")
                        current_user = os.system(cat /tmp/_selected_user.XXXXXXX)
                        print
                        return autologin_user == current_user
                    else:
                        self.autologin_switch.set_active(False)
        except FileNotFoundError:
            return False

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_border_width(10)
        self.add(main_box)

        # Info text container (HORIZONTAL)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(info_box, False, False, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            "<big><b>Konto konfigurieren</b></big>"
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label(label="In diesem Bereich können Sie die Einstellungen des Benutzerkontos ändern.")
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        open_selected_user_file = open(r"/tmp/_selected_user.XXXXXXX",'r') 
        read_open_selected_user_file = open_selected_user_file.read()
        open_selected_user_file.close()

        # Username container (HORIZONTAL)
        username_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        username_box.set_halign(Gtk.Align.CENTER)
        username_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(username_box, False, False, 0)
        username_label = Gtk.Label("Ausgewählter Benutzername:      ")
        username_box.pack_start(username_label, False, False, 0)
        self.username_entry = Gtk.Entry()
        self.username_entry.set_text(text=str(read_open_selected_user_file))
        self.username_entry.set_editable(False)
        self.username_entry.set_can_focus(False)
        self.username_entry.set_alignment(xalign = 0.5)
        username_box.pack_start(self.username_entry, False, False, 0)

        # Old password container (HORIZONTAL)
        old_password_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        old_password_box.set_halign(Gtk.Align.CENTER)
        old_password_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(old_password_box, False, False, 0)
        old_password_label = Gtk.Label("Aktuelles Passwort:         ")
        old_password_box.pack_start(old_password_label, False, False, 0)
        self.old_password_entry = Gtk.Entry()
        self.old_password_entry.set_visibility(False)  # Password is hidden by default
        old_password_box.pack_start(self.old_password_entry, False, False, 0)

        # New password container (HORIZONTAL)
        new_password_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        new_password_box.set_halign(Gtk.Align.CENTER)
        new_password_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(new_password_box, False, False, 0)
        new_password_label = Gtk.Label("Neues Passwort:              ")
        new_password_box.pack_start(new_password_label, False, False, 0)
        self.new_password_entry = Gtk.Entry()
        self.new_password_entry.set_visibility(False)  # Password is hidden by default
        new_password_box.pack_start(self.new_password_entry, False, False, 0)

        # New confirmed password container (HORIZONTAL)
        new_confirmed_password_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        new_confirmed_password_box.set_halign(Gtk.Align.CENTER)
        new_confirmed_password_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(new_confirmed_password_box, False, False, 0)
        new_confirm_password_label = Gtk.Label("Neues Passwort bestätigen:")
        new_confirmed_password_box.pack_start(new_confirm_password_label, False, False, 0)
        self.new_confirm_password_entry = Gtk.Entry()
        self.new_confirm_password_entry.set_visibility(False)  # Confirm password is hidden by default
        new_confirmed_password_box.pack_start(self.new_confirm_password_entry, False, False, 0)

        # Show password checkbox container (HORIZONTAL)
        show_password_autologin_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        show_password_autologin_box.set_margin_top(10)
        show_password_autologin_box.set_halign(Gtk.Align.CENTER)
        show_password_autologin_box.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(show_password_autologin_box, False, False, 0)
        show_password_checkbox = Gtk.CheckButton(" Passwort anzeigen")
        show_password_checkbox.connect("toggled", self.toggle_password_visibility)
        show_password_checkbox.set_halign(Gtk.Align.CENTER)
        show_password_checkbox.set_valign(Gtk.Align.CENTER)
        show_password_autologin_box.pack_start(show_password_checkbox, False, False, 0)
        show_password_autologin_box.pack_start(show_password_checkbox, False, False, 0)
        box_autologin = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box_autologin.set_halign(Gtk.Align.CENTER)
        box_autologin.set_valign(Gtk.Align.CENTER)
        label = Gtk.Label(label="|   Automatic Login:")
        box_autologin.pack_start(label, True, True, 0)
        show_password_autologin_box.pack_start(box_autologin, False, False, 0)

        # Read autologin user from "/etc/sysconfig/displaymanager"
        autologin_user = self.get_autologin_user()

        # Read current user from "/tmp/_selected_user.XXXXXXX"
        current_user = self.get_current_user()

        # Create a Gtk.Switch
        autologin_switch = Gtk.Switch()
        autologin_switch.set_active(current_user == autologin_user)

        # Connect the "state-set" signal to a callback
        autologin_switch.connect("state-set", self.on_switch_activated)
  
        # Show the Gtk.Switch
        show_password_autologin_box.pack_start(autologin_switch, True, True, 0)

        # Show change user groups button container (HORIZONTAL)
        change_user_groups_button = Gtk.Button("⚙️ Gruppeneinstellungen")
        change_user_groups_button.connect("clicked", self.user_groups_settings)
        change_user_groups_button.set_halign(Gtk.Align.CENTER)
        change_user_groups_button.set_valign(Gtk.Align.CENTER)
        main_box.pack_start(change_user_groups_button, False, False, 0)

        # Buttons - Container
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button_box.set_margin_top(20)
        main_box.pack_start(button_box, False, False, 0)

        go_back_button = Gtk.Button("◀️ Zurück")
        go_back_button.connect("clicked", self.on_back_clicked)
        button_box.pack_start(go_back_button, True, True, 0)

        random_password_button = Gtk.Button("🎲 Passwort")
        random_password_button.connect("clicked", self.generate_random_password)
        button_box.pack_start(random_password_button, True, True, 0)

        reset_button = Gtk.Button("🔄 Zurücksetzen")
        reset_button.connect("clicked", self.reset_entries)
        button_box.pack_start(reset_button, True, True, 0)  

        save_button = Gtk.Button("💾 Speichern")
        save_button.connect("clicked", self.save_user_settings)
        button_box.pack_start(save_button, True, True, 0)

    def save_user_settings(self, widget):
        username = self.username_entry.get_text()
        old_password = self.old_password_entry.get_text()
        new_password = self.new_password_entry.get_text()
        new_confirm_password = self.new_confirm_password_entry.get_text()

        if old_password == new_password:
            print("The new and old passwords are the same. Please choose a different password to continue setting a new password!")
            window2_1_1 = Window_Configure_User_Error_1()
            window2_1_1.connect("destroy", Gtk.main_quit)
            window2_1_1.show_all()
        
        else:
            if new_password == new_confirm_password:
                if len(new_password) < 8:
                    print("Password must be at least 8 characters.")
                    # Muss noch erstellt werden ...
                    window2_1_2 = Window_Configure_User_Error_2()
                    window2_1_2.connect("destroy", Gtk.main_quit)
                    window2_1_2.show_all()
                else:
                    # Run the command to create the user
                    safe_user_settings_cmd=f"""
                        #!/bin/bash
                        pass=$(perl -e 'print crypt($ARGV[0], "password")' {new_password})
                        pkexec sudo usermod -p $pass {username}
                    """
                    os.system(safe_user_settings_cmd)
                    print("User settings successfully saved!")
                    window2_1_3 = Window_Configure_User_Info_Completed()
                    window2_1_3.connect("destroy", Gtk.main_quit)
                    window2_1_3.show_all()
                    self.hide()
                    return True
            else:
                print("Passwords do not match. Please try again.")
                # Muss noch erstellt werden ...
                window2_1_4 = Window_Configure_User_Error_3()
                window2_1_4.connect("destroy", Gtk.main_quit)
                window2_1_4.show_all()
                self.hide()
                return True

    def generate_random_password(self, widget):
        chars = string.ascii_letters + string.digits + "#$%&"
        random_password = "".join(random.choice(chars) for _ in range(12))
        self.new_password_entry.set_text(random_password)

    def toggle_password_visibility(self, widget):
        visibility = widget.get_active()
        self.old_password_entry.set_visibility(visibility)
        self.new_password_entry.set_visibility(visibility)
        self.new_confirm_password_entry.set_visibility(visibility)

    def get_autologin_user(self):
        config_path = "/etc/sysconfig/displaymanager"
        autologin_user = None

        try:
            with open(config_path, 'r') as config_file:
                for line in config_file:
                    if line.startswith("DISPLAYMANAGER_AUTOLOGIN="):
                        autologin_user = line.split('=')[1].strip()
                        break
        except FileNotFoundError:
            print(f"Error: {config_path} not found.")

        return autologin_user

    def get_current_user(self):
        user_file_path = "/tmp/_selected_user.XXXXXXX"
        current_user = None

        try:
            with open(user_file_path, 'r') as user_file:
                current_user = user_file.read().strip()
        except FileNotFoundError:
            print(f"Error: {user_file_path} not found.")

        return current_user

    def on_switch_activated(self, switch, gparam):
        # Handle the switch activation manually
        if switch.get_active():
            print("Switch manually activated. Do something here.")
            autologin_activate_cmd=f"""
                # Set the desired username for autologin:
                autologin_user=$(cat /tmp/_selected_user.XXXXXXX)

                # Specify the path to the display manager configuration file:
                display_manager_config="/etc/sysconfig/displaymanager"
                                 
                pkexec sed -i "s/DISPLAYMANAGER_AUTOLOGIN=.*/DISPLAYMANAGER_AUTOLOGIN=\"$autologin_user\"/" "$display_manager_config"
            """
            os.system(autologin_activate_cmd)
        else:
            print("Switch manually deactivated. Do something else here.")
            autologin_deactivate_cmd=f"""
                # Set the desired username for autologin:
                autologin_user=""

                # Specify the path to the display manager configuration file:
                display_manager_config="/etc/sysconfig/displaymanager"
                                 
                pkexec sed -i "s/DISPLAYMANAGER_AUTOLOGIN=.*/DISPLAYMANAGER_AUTOLOGIN=\"$autologin_user\"/" "$display_manager_config"
            """
            os.system(autologin_deactivate_cmd)    

    def user_groups_settings(self, widget):
        window2_1_5 = Window_Configure_User_Groups()
        window2_1_5.connect("destroy", Gtk.main_quit)
        window2_1_5.show_all()

    def reset_entries(self, widget):
        self.old_password_entry.set_text("")
        self.new_password_entry.set_text("")
        self.new_confirm_password_entry.set_text("")

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Configure_User_Groups(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(500, 550)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        self.all_groups_list = self.load_groups("/tmp/_all_groups_list_.XXXXXXX")
        self.user_groups_list = self.load_groups("/tmp/_all_groups_of_user_list_.XXXXXXX")
        self.selected_groups = []

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(self.main_box)

        # Info text container (HORIZONTAL)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        info_box.set_halign(Gtk.Align.CENTER)
        info_box.set_valign(Gtk.Align.CENTER)
        self.main_box.pack_start(info_box, False, False, 0)
        label_title = Gtk.Label()
        label_title.set_markup(
            "<big><b>Gruppen konfigurieren</b></big>"
        )
        label_title.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_title, True, True, 0)
        label_info = Gtk.Label(label="In diesem Bereich können Sie sehen, zu welchen Gruppen Ihr ausgewählter Benutzer gehört und Sie können auch die Gruppenzugehörigkeit ändern. \n\n"
             "Aber seien Sie vorsichtig! Sie müssen sich darüber im Klaren sein, dass Sie genau wissen sollten, was Sie tun. Herumspielen und Ausprobieren von Benutzer- und Gruppenberechtigungen kann Ihr gesamtes System zum Stillstand bringen! \n\n"
             "Wenn Sie einen Benutzer erstellen oder löschen möchten, müssen Sie einfach einen mehr oder weniger Benutzer haben. "
             "Wenn Sie einem Benutzer jedoch mehr Rechte gewähren oder die Rechte eines Systemkontos oder einer Systemgruppe einschränken, gefährden Sie möglicherweise die Sicherheit Ihres Systems!")
        label_info.set_line_wrap(True)
        label_info.set_max_width_chars(55)
        label_info.set_justify(Gtk.Justification.CENTER)
        info_box.pack_start(label_info, True, True, 0)

        self.liststore = Gtk.ListStore(str, bool)  # Store data for the list

        # Populate the liststore with initial data
        for group in self.all_groups_list:
            self.liststore.append([group, group in self.user_groups_list])

        self.treeview = Gtk.TreeView(model=self.liststore)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_toggle_toggled)
        column_toggle = Gtk.TreeViewColumn("Status", renderer_toggle, active=1)
        self.treeview.append_column(column_toggle)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Group", renderer_text, text=0)
        self.treeview.append_column(column_text)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self.treeview)
        self.main_box.pack_start(self.scrollable_treelist, True, True, 20)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.main_box.pack_start(hbox, False, True, 0)

        self.button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        self.button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(self.button_okay, True, True, 0)

        self.button_reset_groups = Gtk.Button.new_with_label("🔄 Zurücksetzen")
        self.button_reset_groups.connect("clicked", self.reset_groups)
        hbox.pack_start(self.button_reset_groups, True, True, 0)

        self.save_button = Gtk.Button(label="💾 Speichern")
        self.save_button.connect("clicked", self.on_save_button_clicked)
        hbox.pack_start(self.save_button, True, True, 0)

    def load_groups(self, filename):
        try:
            with open(filename, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    def on_toggle_toggled(self, widget, path):
        self.liststore[path][1] = not self.liststore[path][1]

    def reset_groups(self, widget):
        window2_1_6 = Window_Configure_User_Groups()
        window2_1_6.connect("destroy", Gtk.main_quit)
        window2_1_6.show_all()  
        self.hide()
        return True

    def on_save_button_clicked(self, widget):

        open_selected_user_file = open(r"/tmp/_selected_user.XXXXXXX",'r') 
        read_open_selected_user_file = open_selected_user_file.read()
        open_selected_user_file.close()

        self.selected_groups = self.get_selected_groups()
        print(f"Selected groups are: {self.selected_groups}")
        # Save selected groups to file "_selected_groups_.XXXXXXX"
        selected_user_groups_cmd=f"""
            #!/bin/bash
            echo -n {self.selected_groups} > /tmp/_selected_groups_.XXXXXXX
            
            # Read one line from the file
            line=$(head -n 1 "/tmp/_selected_groups_.XXXXXXX")

            SELECTED_USER=$(cat /tmp/_selected_user.XXXXXXX)
            SELECTED_USER_GROUPS=$(echo "$line" | tr -d '[] ')
            echo "$SELECTED_USER_GROUPS"

            # Create a temporary script file
            script_1=$(mktemp)

           # Add user and modify group membership in the temporary script
           echo "sudo usermod -G '' $SELECTED_USER" > "$script_1"
           echo "sudo usermod -aG $SELECTED_USER_GROUPS $SELECTED_USER" >> "$script_1"

           echo "$script_1"

           # Execute the temporary script with elevated privileges using pkexec
           pkexec su -c "bash $script_1"

           # Remove the temporary script
           rm "$script_1"

            list_user_groups=$(id -nG $SELECTED_USER)
            echo "$list_user_groups" | tr ' ' '\n' > /tmp/_all_groups_of_user_list_.XXXXXXX
        """
        os.system(selected_user_groups_cmd)

        reset_groups()
        self.hide()
        return True

    def get_selected_groups(self):
        selected_groups = []
        for row in self.liststore:
            group, status = row
            if status:
                selected_groups.append(group)
        return selected_groups

        #print("Selection saved to /tmp/selected_groups.txt")        

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

class Window_Configure_User_Info_Completed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("✅")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das Benutzerkonto wurde mit allen zugehörigen Daten erfolgreich gelöscht!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

class Window_Configure_User_Error_1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das alte Passwort des Kontos darf nicht mit dem neuen Passwort übereinstimmen! \nBitte wählen Sie ein anderes Passwort.")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

class Window_Configure_User_Error_2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das neue Passwort muss mindestens 8 Zeichen lang sein!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

class Window_Configure_User_Error_3(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="Das neue Passwort und das wiederholt eingegebene neue Passwort stimmen nicht überein!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Del_Selection_Warn(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        open_selected_del_user_warn_text_file = open(r"/tmp/_selected_del_user_warn_text.XXXXXXX",'r') 
        read_selected_del_user_warn_text_file = open_selected_del_user_warn_text_file.read()
        open_selected_del_user_warn_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add a label with the desired text
        label = Gtk.Label(label=str(read_selected_del_user_warn_text_file))
        vbox.pack_start(label, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, False, False, 0)

        # Add a "Yes" button
        button_yes = Gtk.Button.new_with_label("Yes")
        button_yes.connect("clicked", self.on_yes_clicked)
        hbox.pack_start(button_yes, True, True, 0)

        # Add a "No" button
        button_no = Gtk.Button.new_with_label("No")
        button_no.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_no, True, True, 0)

    def on_yes_clicked(self, widget):
        # Remove the USER ...
        print("The selected user will be deleted!")

        del_user_cmd="""
            #!/bin/bash
            username=$(cat /tmp/_selected_user.XXXXXXX)
            command="sudo userdel -r -f $username"
            pkexec $command
        """
        os.system(del_user_cmd)
        
        window3_2_1 = Window_Del_User_Info_Completed()
        window3_2_1.connect("destroy", Gtk.main_quit)
        window3_2_1.show_all()

        self.hide()
        return True

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Del_User_Info_Completed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("✅")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="The user account has been successfully deleted with all associated data!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Del_Selection_Info(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_border_width(10)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("⚠️")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label=str(read_selected_del_user_info_text_file))
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Zurück")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################
##############################################################################################################################################################################

if __name__ == "__main__":
    Del_Tmp_files()
    Main()
