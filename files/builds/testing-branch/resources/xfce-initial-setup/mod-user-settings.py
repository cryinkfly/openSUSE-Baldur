#!/usr/bin/python	

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RadioListApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager")
        self.set_default_size(500, 0)
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
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        button_box.pack_start(close_button, True, True, 0)
        button_box.pack_start(add_button, True, True, 0)
        button_box.pack_start(extra_button_0, True, True, 0)
        button_box.pack_start(extra_button_1, True, True, 0)

        # Main Box
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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

    def on_configure_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Configure button clicked. Selected option: {selected_option}")
    
    def on_add_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Add button clicked. Selected option: {selected_option}")

    def on_del_clicked(self, button):
        selected_option = self.get_selected_option()
        if selected_option:
            print(f"Delete button clicked. Selected option: {selected_option}")   

    def get_selected_option(self):
        selection = self.radio_list.get_iter_first()
        while selection is not None:
            if self.radio_list.get_value(selection, 0):
                return self.radio_list.get_value(selection, 1)
            selection = self.radio_list.iter_next(selection)
        return None

win = RadioListApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
