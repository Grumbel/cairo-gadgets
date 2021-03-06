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


class Context:

    def __init__(self, cr, width, height, mouse_x, mouse_y, time, dt, rnd):
        self.cr = cr
        self.width = width
        self.height = height
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.time = time
        self.dt = dt
        self.random = rnd


# EOF #
