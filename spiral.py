#! /usr/bin/env python

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

import pygtk
pygtk.require('2.0')
import gtk
import random
import math

# TODO: reuse seed, allow changing of slope

# Create a GTK+ widget on which we will draw using Cairo


class Screen(gtk.DrawingArea):

    # Draw in response to an expose-event
    __gsignals__ = {"expose-event": "override"}

    # Handle the expose-event by drawing
    def do_expose_event(self, event):

        # Create the cairo context
        cr = self.window.cairo_create()

        # Restrict Cairo to the exposed area; avoid extra work
        cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        cr.clip()

        self.draw(cr, *self.window.get_size())

    def draw(self, cr, width, height):
        # Fill the background with gray
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.rectangle(0, 0, width, height)
        cr.fill()

        self.draw_spiral(cr,
                         width / 2.0, height / 5.0 * 4.0,
                         0,
                         width / 2.0,
                         random.random() * 0.1 + 0.1)

    def draw_spiral(self, cr, x, y, angle, length, angle_delta):
        if length > 20.0:
            nangle = angle + angle_delta
            seg = length / 30.0

            dx = seg * math.sin(nangle)
            dy = -seg * math.cos(nangle)

            # cr.set_source_rgb(random.random(),
            #                  random.random(),
            #                  random.random())
            # cr.set_line_width(2.0)
            cr.set_source_rgb(1, 1, 1)
            cr.move_to(x,
                       y)
            cr.line_to(x + dx,
                       y + dy)
            cr.stroke()

            if random.randint(0, 15) == 0:
                self.draw_spiral(cr,
                                 x + dx,
                                 y + dy,
                                 nangle,
                                 length - seg,
                                 -angle_delta)

            self.draw_spiral(cr,
                             x + dx,
                             y + dy,
                             nangle,
                             length - seg,
                             angle_delta)

# GTK mumbo-jumbo to show the widget in a window and quit when it's closed


def run(Widget):
    window = gtk.Window()
    window.set_size_request(640, 480)
    window.connect("delete-event", gtk.main_quit)

    vbox = gtk.VBox()

    widget = Widget()
    widget.show()

    button = gtk.Button("Regenerate")
    button.connect("clicked", lambda ev: widget.queue_draw())
    button.show()

    vbox.pack_start(widget, True, True)
    vbox.pack_start(button, False, True)
    vbox.show()

    window.add(vbox)

    window.present()
    gtk.main()

if __name__ == "__main__":
    run(Screen)

# EOF #
