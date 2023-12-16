#!/usr/bin/python	

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Configure User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Add widgets to Window1
        self.label = Gtk.Label("This is Window 1 where you can add a new user.")
        self.add(self.label)

class Window2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Add User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.set_border_width(10)

        # Vertical box to hold all widgets
        vbox = Gtk.VBox(spacing=10)
        self.add(vbox)

        # Username entry
        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Username")
        vbox.pack_start(self.username_entry, True, True, 0)

        # Password entry
        self.password_entry = Gtk.Entry()
        self.password_entry.set_visibility(False)
        self.password_entry.set_placeholder_text("Password")
        vbox.pack_start(self.password_entry, True, True, 0)

        # Password confirmation entry
        self.confirm_password_entry = Gtk.Entry()
        self.confirm_password_entry.set_visibility(False)
        self.confirm_password_entry.set_placeholder_text("Confirm Password")
        vbox.pack_start(self.confirm_password_entry, True, True, 0)

        # Checkbox
        self.checkbox = Gtk.CheckButton("I agree to the terms and conditions")
        vbox.pack_start(self.checkbox, True, True, 0)

        # Submit button
        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.on_submit_clicked)
        vbox.pack_start(submit_button, True, True, 0)

    def on_submit_clicked(self, widget):
        username = self.username_entry.get_text()
        password = self.password_entry.get_text()
        confirm_password = self.confirm_password_entry.get_text()
        agreement = self.checkbox.get_active()

        if password == confirm_password and agreement:
            print(f"Username: {username}")
            print(f"Password: {password}")
            print("Registration successful!")
        else:
            print("Registration failed. Please check your inputs.")

class Window3(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Delete User")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Add widgets to Window3
        self.label = Gtk.Label("This is Window 3 where you can delete a user.")
        self.add(self.label)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)

        check_file="""
            #!/bin/bash
            LIST_ALL_HUMAN_USERS() {
                tmpfile0=$(mktemp -t /tmp/_all_users_list_.XXXXXXX)
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
                tmpfile1=$(mktemp -t /tmp/_all_groups_of_user_list_.XXXXXXX)
                list_user_groups=$(id -nG $username)
                echo "$list_user_groups" | tr ' ' '\n' > /tmp/_all_groups_of_user_list_.XXXXXXX
            }

            ##############################################################################################################################################################################
            # LIST OF ALL GROUPS ON THIS SYSTEM (/etc/group):                                                                                                                            #
            ##############################################################################################################################################################################

            LIST_ALL_GROUPS() {
                tmpfile2=$(mktemp -t /tmp/_all_groups_list_.XXXXXXX)
                list_all_groups=$(cut -d: -f1 /etc/group | sort)
                echo "$list_all_groups" | tr ' ' '\n' > /tmp/_all_groups_list_.XXXXXXX
                cat /tmp/_all_users_list_.XXXXXXX | while read line; do echo "FALSE" >> /tmp/_all_groups_list_new.XXXXXXX && echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
                rm /tmp/_all_groups_list.XXXXXXX
                mv /tmp/_all_groups_list_new.XXXXXXX /tmp/_all_groups_list_.XXXXXXX
                        }

            ##############################################################################################################################################################################

            LIST_ALL_HUMAN_USERS
            LIST_ALL_GROUPS_OF_USER
            LIST_ALL_GROUPS
        """
        os.system(check_file)

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
        close_button = Gtk.Button(label="✖️ Close")
        close_button.connect("clicked", self.on_close_clicked)

        add_button = Gtk.Button(label="⚙️ Configure")
        add_button.connect("clicked", self.on_configure_clicked)

        extra_button_0 = Gtk.Button(label="➕ Add")
        extra_button_0.connect("clicked", self.on_add_clicked)

        extra_button_1 = Gtk.Button(label="❌ Delete")
        extra_button_1.connect("clicked", self.on_del_clicked)

        # Button Box
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_box.pack_start(close_button, True, True, 0)
        button_box.pack_start(add_button, True, True, 0)
        button_box.pack_start(extra_button_0, True, True, 0)
        button_box.pack_start(extra_button_1, True, True, 0)

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
        # Run your Bash command here
        delete_file="rm /tmp/_all_users_list_.XXXXXXX"
        os.system(delete_file)

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
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Add button clicked. Selected option: {selected_option}")

            window2 = Window2()
            window2.connect("destroy", Gtk.main_quit)
            window2.show_all()
        else:
            print(f"Click Add button was triggered but no option was selected!")

    def on_del_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Delete button clicked. Selected option: {selected_option}")

            window3 = Window3()
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
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
