#! /usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo
import random

def midpoint(lst):
    x = 0.0
    y = 0.0
    for el in lst:
        x += el[0]
        y += el[1]
    return (x / len(lst), y / len(lst))

def jitter(p, r):
    return (p[0] + (random.random() * 2.0 - 1.0) * r, 
            p[1] + (random.random() * 2.0 - 1.0) * r)

# Create a GTK+ widget on which we will draw using Cairo
class Screen(gtk.DrawingArea):

    # Draw in response to an expose-event
    __gsignals__ = { "expose-event": "override" }

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

        cr.set_source_rgba(1.0, 1.0, 1.0, 0.5)

        line = [[(10, height/2), (width-10, height/2)]]

        for i in range(1, 7):
            for l in line:
                a, b = l

                ab = midpoint([a, b])
                bc = midpoint([b, c])
                cd = midpoint([c, d])
                da = midpoint([d, a])
                n = jitter(midpoint(q), width/10.0/(2**i))

                line.append([a, ab, n, da])
                line.append([ab, b, bc, n])
                quads.append([bc, c, cd, n])
                quads.append([cd, d, da, n])
            nquads = quads

        cr.set_line_width(1.0)
        for q in quads:
            cr.move_to(q[0][0], q[0][1])
            cr.line_to(q[1][0], q[1][1])
            cr.stroke()

# GTK mumbo-jumbo to show the widget in a window and quit when it's closed
def run(Widget):
    window = gtk.Window()
    window.connect("delete-event", gtk.main_quit)
    widget = Widget()
    widget.show()
    window.add(widget)
    window.present()
    gtk.main()

if __name__ == "__main__":
    run(Screen)

# EOF #
