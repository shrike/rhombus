#!/usr/bin/env python
import gtk

def quit (*args):
    gtk.main_quit ()

w = gtk.Window ()
w.connect ("delete-event", quit)

# Main vbox has a menu, a horizontally paned view and a status bar
main_vbox = gtk.VBox ()

# Menu - File, Edit
menu_bar = gtk.MenuBar ()
main_vbox.pack_start (menu_bar, False, False)

file_menu = gtk.Menu ()

new_mi = gtk.MenuItem ("_New")
open_mi = gtk.MenuItem ("_Open")
save_mi = gtk.MenuItem ("_Save")

file_menu.append (new_mi)
file_menu.append (open_mi)
file_menu.append (save_mi)

file_mi = gtk.MenuItem ("_File")
menu_bar.add (file_mi)
file_mi.set_submenu (file_menu)

edit_menu = gtk.Menu ()
undo_mi = gtk.MenuItem ("Undo")
pref_mi = gtk.MenuItem ("Preferences")

edit_menu.append (undo_mi)
edit_menu.append (pref_mi)

edit_mi = gtk.MenuItem ("_Edit")
menu_bar.add (edit_mi)
edit_mi.set_submenu (edit_menu)

# HPaned
hpane = gtk.HPaned ()
main_vbox.pack_start (hpane, True, True, 5)

# Statusbar
status = gtk.Statusbar ()
id = status.get_context_id ("status")
status.push (id, "Done.")
main_vbox.pack_start (status, False, False)

w.add (main_vbox)

# Now add stuff to both sides of the paned view
### left side
left = gtk.VBox ()
hpane.add1 (left)

name_hbox = gtk.HBox ()
left.add (name_hbox)

name_lbl = gtk.Label ("Name: ")
name_hbox.add (name_lbl)

name_entry = gtk.Entry ()
name_hbox.add (name_entry)

freshman_check  = gtk.RadioButton (None, "Freshman")
sophomore_check = gtk.RadioButton (freshman_check, "Sophomore")
junior_check    = gtk.RadioButton (freshman_check, "Junior")
senior_check    = gtk.RadioButton (freshman_check, "Senior")

left.add (freshman_check)
left.add (sophomore_check)
left.add (junior_check)
left.add (senior_check)

ok_btn = gtk.Button ("_Ok")
left.add (ok_btn)

### right side
right_pane = gtk.VBox ()
hpane.add2 (right_pane)

hbox = gtk.HBox ()
right_pane.add (hbox)
right = gtk.VBox ()
hbox.pack_start (right,1,1,5)

classes_lbl = gtk.Label ("Classes")
right.add (classes_lbl)

cs_check = gtk.CheckButton ("CS 100")
ma_check = gtk.CheckButton ("MA 200")
ee_check = gtk.CheckButton ("EE 100")
en_check = gtk.CheckButton ("EN 101")
me_check = gtk.CheckButton ("ME 105")

right.add (cs_check)
right.add (ma_check)
right.add (ee_check)
right.add (en_check)
right.add (me_check)

text_vbox = gtk.VBox ()
text_vbox.pack_start (gtk.Label ("Notes:"),0,0,5)

text_view = gtk.TextView ()
text_view.set_left_margin (5)
text_view.set_right_margin (5)
text_view.get_buffer ().set_text ("Enter some notes here. ")

text_vbox.add (text_view)

hbox.pack_start (text_vbox,1,1,5)

cancel_btn = gtk.Button ("_Cancel")
right.add (cancel_btn)

# show everything and call the mainloop
w.show_all ()
gtk.main ()

print ("Done.")
