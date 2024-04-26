# window.py
#
# Copyright 2024 evokzh
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
import socket

@Gtk.Template(resource_path='/com/evokzh/ourcloud/gtk/messages.ui')
class OurcloudMessages(Adw.ApplicationWindow):
    __gtype_name__ = 'OurcloudMessages'

    def __init__(self, send_message, **kwargs):
        self.send_message = send_message
        super().__init__(**kwargs)
