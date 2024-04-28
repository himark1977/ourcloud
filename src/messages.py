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

    readmessage_button = Gtk.Template.Child()
    message_label = Gtk.Template.Child()
    message_from = Gtk.Template.Child()
    entry_to = Gtk.Template.Child()
    entry_message = Gtk.Template.Child()
    send_message_button = Gtk.Template.Child()

    def __init__(self, send_message, username, **kwargs):
        self.username = username
        self.send_message = send_message
        super().__init__(**kwargs)

        self.readmessage_button.connect("clicked", self.on_message_read_clicked)
        self.send_message_button.connect("clicked", self.on_send_message_clicked)
        
    
    def on_message_read_clicked(self, button):
        # Messages are arrived from the server with username, message
        self.data_message = self.send_message(f'read_messages:{self.username}')
        for i in range(0, len(self.data_message.split(','))):
            self.sender = self.data_message.split(',')[i].split(':')[0]
            self.message = self.data_message.split(',')[i].split(':')[1]
            print(f'Message from {self.sender}: {self.message}')
        
        
    def on_send_message_clicked(self, button):
        self.receiver = str(self.entry_to.get_text())
        self.message = str(self.entry_message.get_text())
        self.send_message(f'write_message:{self.username},{self.receiver},{self.message}')
