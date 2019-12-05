#!/usr/bin/env python3

# cairo-gadgets - A collection of gadgets for cairo
# Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
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

from setuptools import setup, find_packages


def find_cairogadget_examples():
    results = []
    for filename in os.listdir("cairogadget/examples/"):
        if filename.endswith(".py") and filename != "__init__.py":
            name, ext = os.path.splitext(filename)
            results.append('cairogadget-{} = cairogadget.examples.{}:main'.format(name, name))
    print(results)
    return results


setup(name='cairogadget',
      version='0.1.0',
      scripts=[],
      entry_points={
          'gui_scripts': find_cairogadget_examples()
      },
      install_requires=[
          'pycairo'
      ],
      packages=find_packages(),
)


# EOF #
