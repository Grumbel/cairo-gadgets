;; dirtools - Python Scripts for directory stuff
;; Copyright (C) 2019 Ingo Ruhnke <grumbel@gmail.com>
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

(set! %load-path
      (cons* "/ipfs/QmZdLjyRm29uL4Eh4HqkZHvwMMus6zjwQ8EdBtp5JUPT99/guix-cocfree_0.0.0-52-ga8e1798"
             %load-path))

(use-modules (guix packages)
             (guix build-system python)
             ((guix licenses) #:prefix license:)
             (gnu packages glib)
             (gnu packages gtk)
             (guix-cocfree utils))

(define %source-dir (dirname (current-filename)))

(define-public cairogadget
  (package
   (name "cairogadget")
   (version (version-from-source %source-dir))
   (source (source-from-source %source-dir))
   (inputs
    `(("gtk+" ,gtk+)
      ("python-pygobject" ,python-pygobject)
      ("python-pycairo" ,python-pycairo)))
   (build-system python-build-system)
   (synopsis (synopsis-from-source %source-dir))
   (description (description-from-source %source-dir))
   (home-page (homepage-from-source %source-dir))
   (license license:gpl3+)))

cairogadget

;; EOF ;;
