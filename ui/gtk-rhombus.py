#!/usr/bin/env python
import gtk

class RhombusLayout (gtk.VBox):
    def __init__ (self, quit_cb, conf_conn_cb):
        gtk.VBox.__init__ (self) # init the parent class
        
        self.menu = RhombusLayout.make_menu (quit_cb, conf_conn_cb)
        self.pack_start (self.menu, False, False)

        self.main_hpaned = RhombusLayout.make_mainview ()
        self.add (self.main_hpaned)

        left = RhombusLayout.make_folder_view ()
        self.main_hpaned.add1 (left)
        self.add_folder ('Inbox')

        right = RhombusLayout.make_email_view ()
        self.main_hpaned.add2 (right)
        self.add_email ('', 'Viktor', 'cornell', 'wassup', 
                        'here is a part of my email', 'pdf', 'Today')

        self.statusbar = RhombusLayout.make_statusbar ()
        self.pack_start (self.statusbar, False, False)

    @staticmethod
    def make_menu (quit_cb, conf_conn_cb):
        menu_bar = gtk.MenuBar ()

        file_menu = gtk.Menu ()
        file_mi = gtk.MenuItem ("_File")
        menu_bar.add (file_mi)
        file_mi.set_submenu (file_menu)

        exit_mi = gtk.MenuItem ("_Exit")
        exit_mi.connect ('activate', quit_cb)
        file_menu.append (exit_mi)


        configure_menu = gtk.Menu ()
        configure_mi = gtk.MenuItem ("_Configure")
        menu_bar.add (configure_mi)
        configure_mi.set_submenu (configure_menu)

        conn_mi = gtk.MenuItem ("Connection")
        conn_mi.connect ('activate', conf_conn_cb)
        configure_menu.append (conn_mi)

        return menu_bar

    @staticmethod
    def make_mainview ():
        hpaned = gtk.HPaned ()
        return hpaned

    @staticmethod
    def make_statusbar ():
        status = gtk.Statusbar ()
        return status

    @classmethod
    def make_folder_view (cls):
        liststore = gtk.ListStore (str)

        def add_folder (cls, folder):
            liststore.append ([folder])

        cls.add_folder = add_folder
        view = gtk.TreeView (liststore)
        cell = gtk.CellRendererText ()
        tvcolumn = gtk.TreeViewColumn ('Folder', cell, text=0)
        view.append_column (tvcolumn)

        return view

    @classmethod
    def make_email_view (cls):
        titles = ['star', 'from', 'labels', 'subject', 'blurp', 
                  'attachment', 'datetime']
        liststore = gtk.ListStore (str, str, str, str, str, str, str)

        def add_email (cls, *args):
            liststore.append (args)

        cls.add_email = add_email
        view = gtk.TreeView (liststore)
        cell = gtk.CellRendererText ()
        i = 0
        for title in titles:
            tvcolumn = gtk.TreeViewColumn (title, cell, text=i)
            i += 1
            view.append_column (tvcolumn)

        return view

class GuiDriver:
    def __init__ (self):
        self.main_window = GuiDriver.make_window ()
        self.layout = RhombusLayout (GuiDriver.quit, self.conf_conn_dialog)
        self.main_window.add (self.layout)

        self.main_window.show_all ()

    def conf_conn_dialog (self, menu_item):
        """Make and run the connection configuration dialog."""
        conf_dialog = ConnDialog (self.conf_connection)
        response = conf_dialog.run ()
        conf_dialog.destroy ()

    def conf_connection (self, dialog, response_id, 
                         server_entry, user_entry, pass_entry):
        if (response_id == gtk.RESPONSE_OK):
            print server_entry.get_text ()
            print user_entry.get_text ()
            print pass_entry.get_text ()


    @staticmethod
    def make_window ():
        w = gtk.Window ()
        w.connect ("delete-event", GuiDriver.quit)
        return w

    @staticmethod
    def quit (*args):
        gtk.main_quit ()

# This is a class for the connection settings dialog
class ConnDialog (gtk.Dialog):
    def __init__ (self, response_cb):
        """The parameter response_cb is supposed to be a function that will be
        called when the dialog is closed. It will be passed the gtk.Entry
        objects from the form."""

        gtk.Dialog.__init__ (self) # init the parent class
        
        conf_tbl = gtk.Table (3, 2)
        conf_tbl.set_row_spacings (5)
        conf_tbl.set_col_spacings (5)

        server_lbl = gtk.Label ("IMAP4 Server: ")
        server_entry = gtk.Entry ()

        conf_tbl.attach (server_lbl,   0,1, 0,1, xoptions=0, yoptions=0)
        conf_tbl.attach (server_entry, 1,2, 0,1)

        user_lbl = gtk.Label ("User name: ")
        user_entry = gtk.Entry ()

        conf_tbl.attach (user_lbl,   0,1, 1,2, xoptions=0, yoptions=0)
        conf_tbl.attach (user_entry, 1,2, 1,2)

        pass_lbl = gtk.Label ("Password: ")
        pass_entry = gtk.Entry ()
        pass_entry.set_visibility (False)

        conf_tbl.attach (pass_lbl,   0,1, 2,3, xoptions=0, yoptions=0)
        conf_tbl.attach (pass_entry, 1,2, 2,3)

        self.vbox.add (conf_tbl)

        self.add_button ("_Cancel", gtk.RESPONSE_CANCEL)
        self.add_button ("_OK", gtk.RESPONSE_OK)
        self.show_all ()

        self.connect ("response", response_cb, 
                      server_entry, user_entry, pass_entry)


def main ():
    gui = GuiDriver ()
    gtk.main ()

if (__name__ == '__main__'):
    main ()
