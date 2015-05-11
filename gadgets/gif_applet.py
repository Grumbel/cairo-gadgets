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


import os
import random
import tempfile
import cairo
from context import Context


class GifApplet:

    def __init__(self):
        self.width = 640
        self.height = 480
        self.random = random.Random()
        self.output_directory = None

    def run(self, draw_callback):
        if self.output_directory is None:
            self.output_directory = tempfile.mkdtemp()

        pointer = (self.width / 2, self.height / 2)

        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)
        cr = cairo.Context(surface)
        draw_callback(Context(cr,
                              self.width,
                              self.height,
                              pointer[0],
                              pointer[1],
                              0,
                              0,
                              self.random))

        surface.write_to_png(os.path.join(self.output_directory, "frame0000.png"))
        print("Images written to: {}".format(self.output_directory))

    def run_animation(self, draw_callback, msec=1000 / 30):
        if self.output_directory is None:
            self.output_directory = tempfile.mkdtemp()

        pointer = (self.width / 2, self.height / 2)

        time = 0
        for frame in range(1000):
            surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)
            cr = cairo.Context(surface)
            draw_callback(Context(cr,
                                  self.width,
                                  self.height,
                                  pointer[0],
                                  pointer[1],
                                  time,
                                  msec,
                                  self.random))
            outfile = os.path.join(self.output_directory, "frame{0:04d}.png".format(frame))
            print("Writing to: {}".format(outfile))
            surface.write_to_png(outfile)
            time += msec

        print("Images written to: {}".format(self.output_directory))

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def set_title(self, title):
        pass

    def set_output_directory(self, path):
        self.output_directory = path


# EOF #
