#!/usr/bin/env python

# Copyright (C) 2006, Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk

from sugar.graphics2.window import Window

class ActivityToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

class EditToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

class TextToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

        button = gtk.ToolButton()
        button.set_icon_name('text-format-bold')
        self.insert(button, -1)
        button.show()

class ImageToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

class TableToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

class FormatToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

class ViewToolbar(gtk.Toolbar):
    def __init__(self):
        gtk.Toolbar.__init__(self)

window = Window()
window.connect("destroy", lambda w: gtk.main_quit())

activity_toolbar = ActivityToolbar()
window.toolbox.add_toolbar('Activity', activity_toolbar)
activity_toolbar.show()

edit_toolbar = EditToolbar()
window.toolbox.add_toolbar('Edit', edit_toolbar)
edit_toolbar.show()

text_toolbar = TextToolbar()
window.toolbox.add_toolbar('Text', text_toolbar)
text_toolbar.show()

image_toolbar = ImageToolbar()
window.toolbox.add_toolbar('Image', image_toolbar)
image_toolbar.show()

table_toolbar = TableToolbar()
window.toolbox.add_toolbar('Table', table_toolbar)
table_toolbar.show()

format_toolbar = FormatToolbar()
window.toolbox.add_toolbar('Format', format_toolbar)
format_toolbar.show()

view_toolbar = ViewToolbar()
window.toolbox.add_toolbar('View', view_toolbar)
view_toolbar.show()

scrolled_window = gtk.ScrolledWindow()
scrolled_window.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
window.set_canvas(scrolled_window)
scrolled_window.show()

text_view = gtk.TextView()
scrolled_window.add(text_view)
text_view.show()

window.show()

gtk.main()