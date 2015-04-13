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


from gi.repository import Gtk, Gdk, GObject
from context import Context


class Applet:

    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_size_request(640, 480)
        self.window.connect("delete-event", Gtk.main_quit)

        self.vbox = Gtk.VBox()

        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.show()

        self.button = Gtk.Button("Reset")
        self.button.show()

        self.vbox.pack_start(self.drawing_area, True, True, 0)
        self.vbox.pack_start(self.button, False, True, 0)
        self.vbox.show()

        self.window.add(self.vbox)

    def run(self, draw_callback):
        def on_draw(widget, cr):
            pointer = self.drawing_area.get_pointer()
            draw_callback(Context(cr,
                                  widget.get_allocated_width(),
                                  widget.get_allocated_height(),
                                  pointer[0],
                                  pointer[1]))
        self.drawing_area.connect("draw", on_draw)

        self.button.connect("clicked", lambda ev: self.drawing_area.queue_draw())

        def on_key_press(window, event):
            if event.keyval == Gdk.KEY_F11 or event.keyval == Gdk.KEY_f:
                fullscreen = Gdk.WindowState.FULLSCREEN & window.get_window().get_state()
                if fullscreen:
                    window.unfullscreen()
                else:
                    window.fullscreen()
        self.window.connect("key-press-event", on_key_press)

        self.window.present()
        Gtk.main()

    def run_animation(self, draw_callback, msec=1000 / 30):
        time = 0

        def on_draw(widget, cr):
            nonlocal time

            pointer = self.drawing_area.get_pointer()

            draw_callback(Context(cr,
                                  widget.get_allocated_width(),
                                  widget.get_allocated_height(),
                                  pointer[0],
                                  pointer[1]),
                          time)
        self.drawing_area.connect("draw", on_draw)

        def on_reset():
            nonlocal time
            time = 0
            self.window.queue_draw()
        self.button.connect("clicked", lambda ev: on_reset())

        def on_timeout():
            nonlocal time
            time += msec
            self.window.queue_draw()
            return True
        GObject.timeout_add(msec, on_timeout)

        self.window.present()
        Gtk.main()

    def set_size(self, width, height):
        self.window.set_size_request(width, height)

    def set_title(self, title):
        self.window.set_title(title)


# EOF #
