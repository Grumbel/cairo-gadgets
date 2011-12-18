#! /usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk, gobject, cairo
import random
import math

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

def gen_segments(a, b, depth, midfunc):
    def loop(a, b, r):
        if r == 0:
            return [a]
        else:
            m = midfunc(a, b, depth-r)
            return loop(a, m, r-1) + loop(m, b, r-1)

    return loop(a, b, depth) + [b]

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

        for i in range(0, 500):
            gray = random.random()
            cr.set_source_rgb(gray, gray, gray)
            cr.arc(width  * random.random() + 0.5,
                   height * random.random() + 0.5,
                   0.1, 0.0, 2 * math.pi)
            cr.stroke()

        c = [random.random(),
             random.random(),
             random.random()]

        xof = (random.random()-0.5) * 2.0
        yof = (random.random()-0.5) * 2.0

        for i in range(0, random.randint(1, 2)):
            x = random.randint(0, width)
            y = random.randint(0, height/2)
            radius = random.randint(5, 72)

            self.draw_moon(cr, x, y, radius, xof * radius, yof * radius, 
                           [c[0] * (1.0 - random.random()/10.0), 
                            c[1] * (1.0 - random.random()/10.0), 
                            c[2] * (1.0 - random.random()/10.0)])

        y = height / 2.0 * 1.5
        n = 64

        for i in range(0, n):
            cr.set_source_rgb(((i+1)/float(n) * c[0]) ** 2.2,
                              ((i+1)/float(n) * c[1]) ** 2.2,
                              ((i+1)/float(n) * c[2]) ** 2.2)
            self.draw_mountain(cr, y + 2**(7.0 * (float(i)/(n-1))), width, height)

    def draw_moon(self, cr, x, y, radius, xof, yof, c):
        cr.set_source_rgb(c[0], c[1], c[2])
        cr.arc(x, y, radius * 1.1, 0.0, 2 * math.pi)
        cr.fill()

        cr.set_source_rgb(c[0]*2.0, c[1]*2.0, c[2]*2.0)
        cr.arc(x, y, radius, 0.0, 2 * math.pi)
        cr.fill()
        
        cr.save()
        cr.arc(x, y, radius * 1.2, 0.0, 2 * math.pi)
        cr.clip()

        cr.new_path()
        cr.set_source_rgb(0, 0, 0)
        cr.arc(x + xof,
               y + yof,
               radius * 1.5, 0.0, 2 * math.pi)
        cr.fill()
        # cr.reset_clip()
        cr.restore()       

    def draw_mountain(self, cr, y, width, height):
        points = gen_segments(y + (random.random()-0.5) * 128.0,
                              y + (random.random()-0.5) * 128.0,
                              8, 
                              lambda a, b, d: (a+b)/2.0 + (random.random()-0.5) * (height/3.0) / 2**d)

        cr.move_to(0, height)
        for idx, p in enumerate(points):
            cr.line_to(width/float(len(points)-1) * idx, p)
        cr.line_to(width, height)
        cr.fill()       

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
