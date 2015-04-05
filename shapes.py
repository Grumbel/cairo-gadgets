#!/usr/bin/env python

# cairo-gadgets - A collection of gadgets for cairo
# Copyright (C) 2015 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
import gobject
import math
import time


class ShapedGUI:

    def __init__(self):
        self.window = gtk.Window()
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.drawing_area = gtk.DrawingArea()

        self.drawing_area.set_size_request(854, 480)
        self.window.add(self.drawing_area)

        self.drawing_area.show()
        self.window.show()  # We show here so the window gets a border on it by the WM

        self.drawing_area.connect('expose-event', self.do_expose_event)

        x, y, w, h = self.window.get_allocation()
        self.window.set_size_request(w, h)
        # self.window.connect('size-allocate', self.reshapecircle)
        self.window.show()

        def foo():
            self.window.queue_draw()
            return True
        gobject.timeout_add(20, foo)

        self.count = 0

    def do_expose_event(self, drawing_area, event):
        # Create the cairo context
        cr = drawing_area.window.cairo_create()

        # Restrict Cairo to the exposed area; avoid extra work
        cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        cr.clip()

        self.draw(cr, *self.drawing_area.window.get_size())

    def draw(self, cr, width, height):
        # Fill the background with gray
        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        cr.set_source_rgb(1.0, 1.0, 1.0)

        start = 0
        end = math.pi * self.count / 1000.0

        cx, cy = width / 2, height / 2

        for r in range(40, 180, 20):
            cr.save()
            cr.translate(cx, cy)
            cr.rotate(0.02 * time.time() * r)
            # cr.rotate(0.02 + r)
            cr.translate(-cx, -cy)

            cr.arc(width / 2, height / 2, r + 15, start, end)
            cr.arc_negative(width / 2, height / 2, r, end, start)
            cr.close_path()
            cr.fill()
            cr.restore()

        cr.move_to(20, height - 20)
        cr.select_font_face("Deja Vu")
        cr.set_font_size(32.0)

        if self.count / 10 % 4 == 0:
            cr.show_text("Loading")
        elif self.count / 10 % 4 == 1:
            cr.show_text("Loading.")
        elif self.count / 10 % 4 == 2:
            cr.show_text("Loading..")
        else:
            cr.show_text("Loading...")

        self.count += 1

shapedWin = ShapedGUI()
shapedWin.window.connect("destroy", lambda w: gtk.main_quit())
gtk.main()

# EOF #
