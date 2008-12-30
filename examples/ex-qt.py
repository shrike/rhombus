#!/usr/bin/env python
import sys
from PyQt4 import QtGui, QtCore

class ExQt (QtGui.QMainWindow):
    def __init__ (self):
        QtGui.QMainWindow.__init__(self)

        bar = self.statusBar ()
        bar.showMessage ("Done.")

        menubar = self.menuBar ()
        file = menubar.addMenu ('&File')
        edit = menubar.addMenu ('&Edit')
        help = menubar.addMenu ('&Help')

        about = QtGui.QAction ('About', self)
        help.addAction (about)

        new = QtGui.QAction ('New', self)
        open = QtGui.QAction ('Open', self)
        save = QtGui.QAction ('Save', self)
        save_as = QtGui.QAction ('Save as', self)
        file.addAction (new)
        file.addAction (open)
        file.addAction (save)
        file.addAction (save_as)

        exit = QtGui.QAction ('Exit', self)
        exit.setShortcut ('Ctrl+Q')
        exit.setStatusTip ('Exit application')
        self.connect (exit, QtCore.SIGNAL('triggered()'), 
                      QtCore.SLOT('close()'))
        file.addAction (exit)

        # Make the splitter (aka paned in gtk). It'll be the central widget
        splitter = QtGui.QSplitter ()
        self.setCentralWidget (splitter)

        ### Fill the left side of the splitter
        left = QtGui.QWidget (splitter)
        left_vbox = QtGui.QVBoxLayout (left)
        left.setLayout (left_vbox)

        # text entry box with a label
        name_group = QtGui.QWidget ()
        left_vbox.addWidget (name_group)

        name_hbox = QtGui.QHBoxLayout ()
        name_group.setLayout (name_hbox)

        name_lbl = QtGui.QLabel ("Name:")
        name_hbox.addWidget (name_lbl)

        name_entry = QtGui.QLineEdit ()
        name_entry.setMinimumWidth (150)
        name_hbox.addWidget (name_entry)

        # radio buttons
        yr_group = QtGui.QButtonGroup (self)
        
        freshman  = QtGui.QRadioButton ("Freshman")
        sophomore = QtGui.QRadioButton ("Sophomore")
        junior    = QtGui.QRadioButton ("Junior")
        senior    = QtGui.QRadioButton ("Senior")

        yr_group.addButton (freshman)
        yr_group.addButton (sophomore)
        yr_group.addButton (junior)
        yr_group.addButton (senior)

        freshman.toggle ()

        left_vbox.addWidget (freshman)
        left_vbox.addWidget (sophomore)
        left_vbox.addWidget (junior)
        left_vbox.addWidget (senior)

        ok_btn = QtGui.QPushButton ("&Ok")
        left_vbox.addWidget (ok_btn)

        ### Fill the right side
        right = QtGui.QWidget (splitter)
        # the right side will have an hbox with two vboxes
        #  one with the classes checkboxes and one with the text edit
        right_hbox = QtGui.QHBoxLayout (right)
        right.setLayout (right_hbox)

        classes_group = QtGui.QWidget ()
        right_hbox.addWidget (classes_group)

        right_vbox = QtGui.QVBoxLayout ()
        classes_group.setLayout (right_vbox)

        # some checkboxes with a label on top
        classes_lbl = QtGui.QLabel ("Classes")
        cs_check = QtGui.QCheckBox ("CS 100")
        ma_check = QtGui.QCheckBox ("MA 200")
        ee_check = QtGui.QCheckBox ("EE 100")
        en_check = QtGui.QCheckBox ("EN 101")
        me_check = QtGui.QCheckBox ("ME 105")

        right_vbox.addWidget (classes_lbl)
        right_vbox.addWidget (cs_check)
        right_vbox.addWidget (ma_check)
        right_vbox.addWidget (ee_check)
        right_vbox.addWidget (en_check)
        right_vbox.addWidget (me_check)

        cancel_btn = QtGui.QPushButton ("&Cancel")
        right_vbox.addWidget (cancel_btn)

        # here we make the vbox with the text edit
        notes_group = QtGui.QWidget ()
        right_hbox.addWidget (notes_group)

        notes_vbox = QtGui.QVBoxLayout ()
        notes_group.setLayout (notes_vbox)

        notes_lbl = QtGui.QLabel ("Notes:")
        notes_vbox.addWidget (notes_lbl)

        notes_edit = QtGui.QTextEdit ()
        notes_edit.setPlainText ("Enter some notes here.")
        notes_vbox.addWidget (notes_edit)


app = QtGui.QApplication (sys.argv)
window = ExQt ()
window.resize (250, 150)
window.setWindowTitle ('simple')
window.show ()

sys.exit (app.exec_ ())
