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

@Gtk.Template(resource_path='/com/evokzh/ourcloud/gtk/window.ui')
class OurcloudWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'OurcloudWindow'


    main_hello_label = Gtk.Template.Child()
    entry_username = Gtk.Template.Child()
    entry_password = Gtk.Template.Child()
    login_button = Gtk.Template.Child()
    reg_button = Gtk.Template.Child()

    def __init__(self, send_message, **kwargs):
        self.send_message = send_message
        super().__init__(**kwargs)
        self.login_button.connect("clicked", self.on_login_button_clicked)
        self.reg_button.connect("clicked", self.on_reg_button_clicked)
    
    # get username buffer and print on the console
    def on_login_button_clicked(self, button):
        self.username = str(self.entry_username.get_text())
        self.password = str(self.entry_password.get_text())
        self.main_hello_label.set_text(self.send_message(f'login:{self.username},{self.password}'))
        if(self.main_hello_label.get_text() != 'Invalid username or password.'):
            self.entry_password.hide()
            self.entry_username.hide()
            self.login_button.hide()
            self.reg_button.hide()

    def on_reg_button_clicked(self, button):
        self.username = str(self.entry_username.get_text())
        self.password = str(self.entry_password.get_text())
        self.main_hello_label.set_text(self.send_message(f'register:{self.username},{self.password}'))
