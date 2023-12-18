#!/usr/bin/python	

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import os
import random
import string


class Window1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Configure User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Add widgets to Window1
        self.label = Gtk.Label("This is Window 1 where you can add a new user.")
        self.add(self.label)

class Window2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Create New User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)

        # Labels and Entries
        fullname_label = Gtk.Label("Full Name:")
        self.fullname_entry = Gtk.Entry()

        username_label = Gtk.Label("Username:")
        self.username_entry = Gtk.Entry()

        password_label = Gtk.Label("Password:")
        self.password_entry = Gtk.Entry()
        self.password_entry.set_visibility(False)  # Password is hidden by default

        confirm_password_label = Gtk.Label("Confirmation:")
        self.confirm_password_entry = Gtk.Entry()
        self.confirm_password_entry.set_visibility(False)  # Confirm password is hidden by default

        show_password_checkbox = Gtk.CheckButton("🔎 Show password")
        show_password_checkbox.connect("toggled", self.toggle_password_visibility)
        show_password_checkbox.set_halign(Gtk.Align.CENTER)
        show_password_checkbox.set_valign(Gtk.Align.CENTER)

        main_box.pack_start(fullname_label, False, False, 0)
        main_box.pack_start(self.fullname_entry, False, False, 0)
        main_box.pack_start(username_label, False, False, 0)
        main_box.pack_start(self.username_entry, False, False, 0)
        main_box.pack_start(password_label, False, False, 0)
        main_box.pack_start(self.password_entry, False, False, 0)
        main_box.pack_start(confirm_password_label, False, False, 0)
        main_box.pack_start(self.confirm_password_entry, False, False, 0)
        main_box.pack_start(show_password_checkbox, False, False, 0)

        # Buttons - Container
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        main_box.pack_start(button_box, False, False, 0)

        go_back_button = Gtk.Button("◀️ Back")
        go_back_button.connect("clicked", self.go_back)
        button_box.pack_start(go_back_button, True, True, 0)

        random_password_button = Gtk.Button("🎲 Password")
        random_password_button.connect("clicked", self.generate_random_password)
        button_box.pack_start(random_password_button, True, True, 0)

        reset_button = Gtk.Button("🔄 Reset")
        reset_button.connect("clicked", self.reset_entries)
        button_box.pack_start(reset_button, True, True, 0)  

        create_button = Gtk.Button("🎭 Create")
        create_button.connect("clicked", self.create_user)
        button_box.pack_start(create_button, True, True, 0)      

    def create_user(self, widget):
        fullname = self.fullname_entry.get_text()
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()
        confirm_password = self.confirm_password_entry.get_text()

        if password == confirm_password:
            if len(password) < 12:
                self.show_error_dialog("Password must be at least 10 characters.")
                return
            else:
                # Run the command to create the user
                add_new_user_cmd=f"""
                    #!/bin/bash
                    pkexec sudo useradd -m -p {password} -c '{fullname}' {username}
                """
                os.system(add_new_user_cmd)
                print("User created successfully.")
        else:
            print("Passwords do not match. Please try again.")

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

    def go_back(self, widget):
        self.hide()
        return True  # Returning True stops the default action (closing the window)


class Window_Del_Selection_Warn(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Delete User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        open_selected_del_user_file = open(r"/tmp/_selected_user.XXXXXXX",'r') 
        read_selected_del_user_file = open_selected_del_user_file.read()
        open_selected_del_user_file.close() 
        selected_del_user_warn_text="Are you sure you want to remove user >" + str(read_selected_del_user_file) + "< from your system? (Keep in mind that all saved data from that user will be lost as the home directory will also be deleted!)"

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Add a label with the desired text
        label = Gtk.Label()
        label.set_text(label=str(selected_del_user_warn_text))
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
        button_no.connect("clicked", self.on_no_clicked)
        hbox.pack_start(button_no, True, True, 0)

    def on_yes_clicked(self, widget):
        print("Yes button clicked")
        # Remove USER ...

    def on_no_clicked(self, widget):
        self.hide()
        return True  # Returning True stops the default action (closing the window)

class Window_Del_No_Selection_Info(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Info about current using user")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        open_selected_del_user_file = open(r"/tmp/_selected_user.XXXXXXX",'r') 
        read_selected_del_user_file = open_selected_del_user_file.read()
        open_selected_del_user_file.close() 
        selected_del_user_info_text="The selected user " + str(read_selected_del_user_file) + " cannot be deleted because you are logged in to this system with it! \nPlease select a different user if you would like to continue deleting users that are no longer needed on this system." 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("💡")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label=str(selected_del_user_info_text))
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Yes" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_okay_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_okay_clicked(self, widget):
        self.hide()
        return True  # Returning True stops the default action (closing the window)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        check_file_cmd="""
            #!/bin/bash
            LIST_ALL_HUMAN_USERS() {
                list_users=$(awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd)
                echo "$list_users" | tr ' ' '\n' > /tmp/_all_users_list_.XXXXXXX

                if [ "$(id -u)" != "0" ]; then
                    echo "Show only human users"
                else
                    username=$(whoami)
                    echo "FALSE" > /tmp/_all_users_list_new.XXXXXXX
                    echo "$username" >> /tmp/_all_users_list_new.XXXXXXX
                fi

                cat /tmp/_all_users_list_.XXXXXXX | while read line; do echo ${line} >> /tmp/_all_users_list_new.XXXXXXX; done
                rm /tmp/_all_users_list_.XXXXXXX
                mv /tmp/_all_users_list_new.XXXXXXX /tmp/_all_users_list_.XXXXXXX
            }

            ##############################################################################################################################################################################
            # LIST OF ALL GROUPS OF A SPECIAL HUMAN USER ON THIS SYSTEM (/etc/group):                                                                                                    #
            ##############################################################################################################################################################################

            LIST_ALL_GROUPS_OF_USER() {
                list_user_groups=$(id -nG $username)
                echo "$list_user_groups" | tr ' ' '\n' > /tmp/_all_groups_of_user_list_.XXXXXXX
            }

            ##############################################################################################################################################################################
            # LIST OF ALL GROUPS ON THIS SYSTEM (/etc/group):                                                                                                                            #
            ##############################################################################################################################################################################

            LIST_ALL_GROUPS() {
                list_all_groups=$(cut -d: -f1 /etc/group | sort)
                echo "$list_all_groups" | tr ' ' '\n' > /tmp/_all_groups_list_.XXXXXXX
                cat /tmp/_all_groups_list_.XXXXXXX | while read line; do echo "FALSE" >> /tmp/_all_groups_list_new.XXXXXXX && echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
                mv /tmp/_all_groups_list_new.XXXXXXX /tmp/_all_groups_list_.XXXXXXX
                        }

            ##############################################################################################################################################################################

            LIST_ALL_HUMAN_USERS
            LIST_ALL_GROUPS_OF_USER
            LIST_ALL_GROUPS
        """
        os.system(check_file_cmd)

        # Add a Description
        label = Gtk.Label()
        label.set_markup(
            "Text can be <small>small</small>, <big>big</big>, "
            "<b>bold</b>, <i>italic</i> and even point to "
            'somewhere in the <a href="https://www.gtk.org" '
            'title="Click to find out more">internets</a>.'
        )
        label.set_line_wrap(True)
        label.set_max_width_chars(48)

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
        close_button = Gtk.Button(label="⛔️ Close")
        close_button.connect("clicked", self.on_close_clicked)

        add_button = Gtk.Button(label="🎭 Create")
        add_button.connect("clicked", self.on_add_clicked)

        configure_button = Gtk.Button(label="⚙️ Configure")
        configure_button.connect("clicked", self.on_configure_clicked)

        del_button = Gtk.Button(label="🗑 Delete")
        del_button.connect("clicked", self.on_del_clicked)

        # Button Box
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_box.pack_start(close_button, True, True, 0)
        button_box.pack_start(add_button, True, True, 0)
        button_box.pack_start(configure_button, True, True, 0)
        button_box.pack_start(del_button, True, True, 0)

        # Main Box
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        # Add widgets to Window1

        main_box.pack_start(label, False, True, 10)
        main_box.pack_start(treeview, True, True, 0)
        main_box.pack_start(button_box, False, False, 0)
        main_box.set_border_width(10)

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

    def on_configure_clicked(self, widget):
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Configure button clicked. Selected option: {selected_option}")
            
            window1 = Window1()
            window1.connect("destroy", Gtk.main_quit)
            window1.show_all()
        else:
            print(f"Click Configure button was triggered but no option was selected!")
    
    def on_add_clicked(self, button):
            window2 = Window2()
            window2.connect("destroy", Gtk.main_quit)
            window2.show_all()

    def on_del_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            del_selected_user_cmd=f"""
                    #!/bin/bash
                    echo {selected_option} > /tmp/_selected_user.XXXXXXX
                """
            os.system(del_selected_user_cmd)

            check_active_user_cmd=f"""
                    #!/bin/bash
                    peter > /tmp/_active_user.XXXXXXX
                """

            active_user = os.system(check_active_user_cmd)
            open_active_user_file = open(r"/tmp/_active_user.XXXXXXX",'r') 
            read_active_user_file = open_active_user_file.read()
            open_active_user_file.close()

            print(f"Active user: {read_active_user_file}")

            # This checks whether the selected user is currently logged in or not! (if...else...)
            if selected_option in read_active_user_file:
                print(f"The user is currently logged in!")
                # Perform actions if variable1 is found
            else:
                print(f"The user is not currently logged in.")
                # Perform actions if variable1 is not found

                window3 = Window_Del_Selection_Warn()
                window3.connect("destroy", Gtk.main_quit)
                window3.show_all()
        else:
            print(f"Click Delete button was triggered but no option was selected!")

    def get_selected_option(self):
        selection = self.radio_list.get_iter_first()
        while selection is not None:
            if self.radio_list.get_value(selection, 0):
                return self.radio_list.get_value(selection, 1)
            selection = self.radio_list.iter_next(selection)
        return None

def main():
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
