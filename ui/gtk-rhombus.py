#!/usr/bin/env python
import gtk

class RhombusLayout (gtk.VBox):
    def __init__ (self):
        gtk.VBox.__init__ (self) # init the parent class
        
        self.menu = RhombusLayout.make_menu ()
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
    def make_menu ():
        menu_bar = gtk.MenuBar ()

        file_menu = gtk.Menu ()
        file_mi = gtk.MenuItem ("_File")
        menu_bar.add (file_mi)
        exit_mi = gtk.MenuItem ("_Exit")
        file_menu.append (exit_mi)
        file_mi.set_submenu (file_menu)

        configuration_menu = gtk.Menu ()
        configuration_mi = gtk.MenuItem ("_Configuration")
        menu_bar.add (configuration_mi)
        configuration_mi.set_submenu (configuration_menu)

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
        self.layout = RhombusLayout ()
        self.main_window.add (self.layout)

        self.main_window.show_all ()

    @staticmethod
    def make_window ():
        w = gtk.Window ()
        w.connect ("delete-event", GuiDriver.quit)
        return w

    @staticmethod
    def quit (*args):
        gtk.main_quit ()


def main ():
    gui = GuiDriver ()
    gtk.main ()

if (__name__ == '__main__'):
    main ()
