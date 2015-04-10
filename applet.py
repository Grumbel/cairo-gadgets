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


from gi.repository import Gtk
from canvas import Canvas


class Applet:

    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_size_request(640, 480)
        self.window.connect("delete-event", Gtk.main_quit)

        self.vbox = Gtk.VBox()

        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.show()

        self.drawing_area.connect("draw", self.__on_draw)

        self.button = Gtk.Button("Regenerate")
        self.button.connect("clicked", lambda ev: self.drawing_area.queue_draw())
        self.button.show()

        self.vbox.pack_start(self.drawing_area, True, True, 0)
        self.vbox.pack_start(self.button, False, True, 0)
        self.vbox.show()

        self.window.add(self.vbox)

        self.setup()

        self.window.present()
        Gtk.main()

    def setup(self):
        pass

    def draw(self, canvas):
        print("error: Applet.draw() function not implemnted")

    def set_size(self, width, height):
        self.window.set_size_request(width, height)

    def set_title(self, title):
        self.window.set_title(title)

    def __on_draw(self, widget, cr):
        self.draw(Canvas(cr,
                         widget.get_allocated_width(),
                         widget.get_allocated_height()))


# EOF #
