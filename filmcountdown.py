#!/usr/bin/env python3

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


import cairo
import math
from gi.repository import Gtk, GObject


from canvas import Canvas


def film_countdown(canvas, second, frame, frames):
    cr = canvas.cr

    # background fill
    cr.set_source_rgb(0.5, 0.5, 0.5)
    cr.paint()

    # progress
    progress = (frame + 1) / frames
    radius = canvas.width
    cr.move_to(canvas.width / 2, canvas.height / 2)
    cr.arc(canvas.width / 2, canvas.height / 2, radius,
           0 - math.pi / 2, 2 * math.pi * progress - math.pi / 2)
    cr.close_path()

    cr.set_source_rgb(0.4, 0.4, 0.4)
    cr.fill_preserve()

    cr.set_source_rgb(0.25, 0.25, 0.25)
    cr.stroke()

    # background cross
    cr.move_to(canvas.width / 2, 0)
    cr.line_to(canvas.width / 2, canvas.height)
    cr.move_to(0, canvas.height / 2)
    cr.line_to(canvas.width, canvas.height / 2)

    cr.set_source_rgb(0.25, 0.25, 0.25)
    cr.set_line_width(6.0)
    cr.stroke()

    # two white circles
    radius = canvas.height / 2 * 0.9
    cr.arc(canvas.width / 2, canvas.height / 2, radius,
           0, 2 * math.pi)
    cr.new_sub_path()
    cr.arc(canvas.width / 2, canvas.height / 2, radius * 0.8,
           0, 2 * math.pi)

    cr.set_source_rgb(1, 1, 1)
    cr.set_line_width(6.0)
    cr.stroke()

    # progress
    cr.set_source_rgb(0, 0, 0)

    cr.select_font_face("Ubuntu",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(canvas.height * 0.8)
    center_text = "%d" % second
    fascent, fdescent, fheight, fxadvance, fyadvance = cr.font_extents()
    x_bearing, y_bearing, text_width, text_height, x_advance, y_advance = cr.text_extents(center_text)
    cr.move_to(canvas.width / 2 - x_advance / 2,
               canvas.height / 2 - fdescent + fheight / 2 - 12)
    cr.show_text(center_text)

    cr.set_font_size(canvas.height * 0.1)
    frameno_text = "%02d/%02d" % (frame + 1, frames)
    x_bearing, y_bearing, text_width, text_height, x_advance, y_advance = cr.text_extents(frameno_text)
    cr.move_to(canvas.width - x_advance - 8,
               canvas.height - 8)
    cr.show_text(frameno_text)


g_total_redraws = 0


def on_draw(canvas):
    global g_total_redraws

    second = g_total_redraws / 24
    frame = g_total_redraws % 24

    film_countdown(canvas, second, frame, 24)

    g_total_redraws += 1


def on_update(widget):
    widget.queue_draw()
    return True


def on_restart():
    global g_total_redraws
    g_total_redraws = 0


def main():
    window = Gtk.Window()
    window.set_size_request(854, 480)
    window.connect("delete-event", Gtk.main_quit)

    vbox = Gtk.VBox()

    widget = Gtk.DrawingArea()
    widget.show()

    widget.connect("draw", lambda widget, cr: on_draw(Canvas(cr,
                                                             widget.get_allocated_width(),
                                                             widget.get_allocated_height())))

    button = Gtk.Button("Restart")
    button.connect("clicked", lambda ev: on_restart())
    button.show()

    vbox.pack_start(widget, True, True, 0)
    vbox.pack_start(button, False, True, 0)
    vbox.show()

    window.add(vbox)

    window.present()

    GObject.timeout_add(1000 / 24.0, lambda: on_update(widget))

    Gtk.main()


if __name__ == "__main__":
    main()


# EOF #
