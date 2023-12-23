#!/usr/bin/python	

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import os
import random
import string

##############################################################################################################################################################################
##############################################################################################################################################################################

del_tmp_files_cmd="rm /tmp/_*.XXXXXXX"
os.system(del_tmp_files_cmd)

##############################################################################################################################################################################
##############################################################################################################################################################################

def main():
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()

##############################################################################################################################################################################
##############################################################################################################################################################################

def Reload_MainWindow(self, widget):
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    self.hide()
    return True  # Returning True stops the default action (closing the window)

##############################################################################################################################################################################
##############################################################################################################################################################################

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
                #cat /tmp/_all_groups_list_.XXXXXXX | while read line; do echo "FALSE" >> /tmp/_all_groups_list_new.XXXXXXX && echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
                cat /tmp/_all_groups_list_.XXXXXXX | while read line; do echo ${line} >> /tmp/_all_groups_list_new.XXXXXXX; done
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
        label.set_text("In this area you can change the user account settings and add/delete users associated with their account. Simply select the user you want to modify from the list.")
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
               """
            os.system(selected_user_cmd)

            window2_1 = Window_Configure_User()
            window2_1.connect("destroy", Gtk.main_quit)
            window2_1.show_all()
            
            self.hide()
            return True

        else:
            print(f"Click Configure button was triggered but no option was selected!")
            window2_2 = Window_Configure_User_Info()
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
                    echo -n "Are you sure you want to remove the user {selected_option} from your system? \nIf your answer is >>YES<<, then the selected user and all their associated data will be removed from this system!" > /tmp/_selected_del_user_warn_text.XXXXXXX
                    echo -n "The selected user {selected_option} cannot be deleted because you are logged in to this system with it! \nPlease select a different user if you would like to continue deleting users that are no longer needed on this system." > /tmp/_selected_del_user_info_text.XXXXXXX
               """
            os.system(del_selected_user_cmd)

            open_active_user_file = open(r"/tmp/_active_user.XXXXXXX",'r') 
            read_active_user_file = open_active_user_file.read()
            open_active_user_file.close()

            # Test another user with overriding the variable ...
            #read_active_user_file="max"

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
        Gtk.Window.__init__(self, title="Users Settings Manager - Info")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

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

        label_1 = Gtk.Label(label="You have not selected a user to delete! \nPlease select a user before continuing.")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Create_User(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Create a new Account")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        # Main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)      

        # Labels and Entries
        fullname_label = Gtk.Label("Full Name:")
        self.fullname_entry = Gtk.Entry()
        self.fullname_entry.set_hexpand(True)
        self.fullname_entry.set_halign(Gtk.Align.CENTER)
        self.fullname_entry.set_width_chars(25)

        username_label = Gtk.Label("Username:")
        self.username_entry = Gtk.Entry()
        self.username_entry.set_hexpand(True)
        self.username_entry.set_halign(Gtk.Align.CENTER)
        self.username_entry.set_width_chars(25)

        password_label = Gtk.Label("Password:")
        self.password_entry = Gtk.Entry()
        self.password_entry.set_hexpand(True)
        self.password_entry.set_halign(Gtk.Align.CENTER)
        self.password_entry.set_width_chars(25)
        self.password_entry.set_visibility(False)  # Password is hidden by default

        confirm_password_label = Gtk.Label("Confirmation:")
        self.confirm_password_entry = Gtk.Entry()
        self.confirm_password_entry.set_hexpand(True)
        self.confirm_password_entry.set_halign(Gtk.Align.CENTER)
        self.confirm_password_entry.set_width_chars(25)
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
        go_back_button.connect("clicked", self.on_back_clicked)
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
            if len(password) < 8:
                print("Password must be at least 8 characters.")
                window1_2 = Window_Create_User_Error_1()
                window1_2.connect("destroy", Gtk.main_quit)
                window1_2.show_all()
            else:
                # Run the command to create the user
                add_new_user_cmd=f"""
                    #!/bin/bash
                    pass=$(perl -e 'print crypt($ARGV[0], "password")' {password})
                    pkexec sudo useradd -m -p $pass -c '{fullname}' {username}
                """
                os.system(add_new_user_cmd)
                print("User created successfully.")
                window1_3 = Window_Create_User_Info_Completed()
                window1_3.connect("destroy", Gtk.main_quit)
                window1_3.show_all()
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
        Gtk.Window.__init__(self, title="Users Settings Manager - Account created successfully!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_create_user_info_text_file = open(r"/tmp/_create_user_text.XXXXXXX",'r') 
        #read_create_user_info_text_file_file = open_create_user_info_text_file.read()
        #open_create_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Add labels with the desired text
        label = Gtk.Label()
        label.set_text("✅")
        font_desc = Pango.FontDescription()
        font_desc.set_size(20 * Pango.SCALE)
        label.override_font(font_desc)
        vbox.pack_start(label, True, True, 0)

        label_1 = Gtk.Label(label="The user account has been successfully created and you can use this new user after re-login!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Create_User_Error_1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Error short password!")
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

        label_1 = Gtk.Label(label="The new password must be at least 8 characters long!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_okay_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################

# ... Password not match ...
class Window_Create_User_Error_2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Account password incorrect!")
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

        label_1 = Gtk.Label(label="The user account passwords do not match. Please try again!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_okay_clicked(self, widget):
        self.hide()
        return True

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Configure_User(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Configure the Account")
        self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable

        open_selected_user_file = open(r"/tmp/_selected_user.XXXXXXX",'r') 
        read_open_selected_user_file = open_selected_user_file.read()
        open_selected_user_file.close() 

        # Main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)

        # Get info ... in progress ...
        username_label = Gtk.Label("Selected Username:")
        self.username_entry = Gtk.Entry()
        self.username_entry.set_text(text=str(read_open_selected_user_file))
        self.username_entry.set_editable(False)
        self.username_entry.set_can_focus(False)
        self.username_entry.set_alignment(xalign = 0.5)

        old_password_label = Gtk.Label("Current Password:")
        self.old_password_entry = Gtk.Entry()
        self.old_password_entry.set_visibility(False)  # Password is hidden by default

        new_password_label = Gtk.Label("New Password:")
        self.new_password_entry = Gtk.Entry()
        self.new_password_entry.set_visibility(False)  # Password is hidden by default

        new_confirm_password_label = Gtk.Label("Confirm New Password:")
        self.new_confirm_password_entry = Gtk.Entry()
        self.new_confirm_password_entry.set_visibility(False)  # Confirm password is hidden by default

        show_password_checkbox = Gtk.CheckButton("🔎 Show password")
        show_password_checkbox.connect("toggled", self.toggle_password_visibility)
        show_password_checkbox.set_halign(Gtk.Align.CENTER)
        show_password_checkbox.set_valign(Gtk.Align.CENTER)

        change_user_groups_button = Gtk.Button("⚙️ Configure Groups")
        change_user_groups_button.connect("clicked", self.user_groups_settings)

        main_box.pack_start(username_label, False, False, 0)
        main_box.pack_start(self.username_entry, False, False, 0)
        main_box.pack_start(old_password_label, False, False, 0)
        main_box.pack_start(self.old_password_entry, False, False, 0)
        main_box.pack_start(new_password_label, False, False, 0)
        main_box.pack_start(self.new_password_entry, False, False, 0)
        main_box.pack_start(new_confirm_password_label, False, False, 0)
        main_box.pack_start(self.new_confirm_password_entry, False, False, 0)
        main_box.pack_start(show_password_checkbox, False, False, 0)
        main_box.pack_start(change_user_groups_button, False, False, 0)

        # Buttons - Container
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        main_box.pack_start(button_box, False, False, 0)

        go_back_button = Gtk.Button("◀️ Back")
        go_back_button.connect("clicked", self.on_back_clicked)
        button_box.pack_start(go_back_button, True, True, 0)

        random_password_button = Gtk.Button("🎲 Password")
        random_password_button.connect("clicked", self.generate_random_password)
        button_box.pack_start(random_password_button, True, True, 0)

        reset_button = Gtk.Button("🔄 Reset")
        reset_button.connect("clicked", self.reset_entries)
        button_box.pack_start(reset_button, True, True, 0)  

        save_button = Gtk.Button("📝 Save")
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
                    add_new_user_cmd=f"""
                        #!/bin/bash
                        pass=$(perl -e 'print crypt($ARGV[0], "password")' {new_password})
                        pkexec sudo usermod -p $pass {username}
                    """
                    os.system(add_new_user_cmd)
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
        Gtk.Window.__init__(self, title="Users Settings Manager - Configure the Groups")
        self.set_default_size(500, 550)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        self.all_groups_list = self.load_groups("/tmp/_all_groups_list_.XXXXXXX")
        self.user_groups_list = self.load_groups("/tmp/_all_groups_of_user_list_.XXXXXXX")
        self.selected_groups = []

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.main_box)

        self.label = Gtk.Label(label="In this area you can see which groups your selected user belongs to and you can also change the group membership. \n\n"
            "But be careful! You have to realize that you should know exactly what you are doing. Playing around and trying out user and group permissions can bring your entire system to a halt! \n\n"
            "If you want to create or delete a user, you simply have to have one more or less user. "
            "However, if you give a user more rights or bend the rights of a system account or system group, you may be putting your system's security at risk!")
        self.label.set_line_wrap(True)
        self.label.set_max_width_chars(50)
        self.main_box.pack_start(self.label, False, False, 0)

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

        self.button_okay = Gtk.Button.new_with_label("◀️ Back")
        self.button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(self.button_okay, True, True, 0)

        self.button_reset_groups = Gtk.Button.new_with_label("🔄 Reset")
        self.button_reset_groups.connect("clicked", self.reset_groups)
        hbox.pack_start(self.button_reset_groups, True, True, 0)

        self.save_button = Gtk.Button(label="💾 Save")
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

    def on_save_button_clicked(self, widget):
        self.selected_groups = self.get_selected_groups()
        print(f"Selected groups are: {self.selected_groups}")
        # Save selected groups to file "_selected_groups_.XXXXXXX"
        selected_user_groups_cmd=f"""
                    #!/bin/bash
                    echo -n {self.selected_groups} > /tmp/_selected_groups_.XXXXXXX
               """
        os.system(selected_user_groups_cmd)

        # Next check the selected groups file and add user to these groups and remove the user from all other groups:
        # ... in progress! ...

    def get_selected_groups(self):
        selected_groups = []
        for row in self.liststore:
            group, status = row
            if status:
                selected_groups.append(group)
        return selected_groups

        #print("Selection saved to /tmp/selected_groups.txt")

    def reset_groups(self, widget):
        window2_1_6 = Window_Configure_User_Groups()
        window2_1_6.connect("destroy", Gtk.main_quit)
        window2_1_6.show_all()  
        self.hide()
        return True        

    def on_back_clicked(self, widget):
        self.hide()
        return True 

##############################################################################################################################################################################

class Window_Configure_User_Info_Completed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Account deleted successfully!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Configure_User_Error_1(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Error account password match!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

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

        label_1 = Gtk.Label(label="The old account password must not match the new password! \nPlease choose a different password.")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Configure_User_Error_2(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Error short password!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

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

        label_1 = Gtk.Label(label="The new password must be at least 8 characters long!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Configure_User_Error_3(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Error Password doesn't match!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        #open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        #read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        #open_selected_del_user_info_text_file.close() 

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

        label_1 = Gtk.Label(label="The new password and repeatedly entered new password do not match!")
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################
##############################################################################################################################################################################

class Window_Del_Selection_Warn(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Delete Account?")
        #self.set_default_size(500, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)

        open_selected_del_user_warn_text_file = open(r"/tmp/_selected_del_user_warn_text.XXXXXXX",'r') 
        read_selected_del_user_warn_text_file = open_selected_del_user_warn_text_file.read()
        open_selected_del_user_warn_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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
        button_no.connect("clicked", self.on_no_clicked)
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
        Gtk.Window.__init__(self, title="Users Settings Manager - Account deleted successfully!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        open_selected_del_user_info_text_file.close() 

        # Create a vertical box to hold the contents
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
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
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################

class Window_Del_Selection_Info(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Users Settings Manager - Error while deleting the account!")
        #self.set_default_size(100, 0)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)  # Make the window non-resizable
        self.set_border_width(10)

        open_selected_del_user_info_text_file = open(r"/tmp/_selected_del_user_info_text.XXXXXXX",'r') 
        read_selected_del_user_info_text_file = open_selected_del_user_info_text_file.read()
        open_selected_del_user_info_text_file.close() 

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

        label_1 = Gtk.Label(label=str(read_selected_del_user_info_text_file))
        label_1.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(label_1, True, True, 0)

        # Create a horizontal box to hold the buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        # Add a "Okay" button
        button_okay = Gtk.Button.new_with_label("◀️ Back")
        button_okay.connect("clicked", self.on_back_clicked)
        hbox.pack_start(button_okay, True, False, 0)

    def on_back_clicked(self, widget):
        Reload_MainWindow(self, widget)

##############################################################################################################################################################################
##############################################################################################################################################################################

if __name__ == "__main__":
    main()
