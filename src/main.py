# main.py
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

import sys
import gi
import socket

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import OurcloudWindow
from .preferences import OurcloudPreferences
from .messages import OurcloudMessages


class OurcloudApplication(Adw.Application):
    is_connected_to_server = False
    """The main application singleton class."""

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the server IP and port
    server_ip = 'localhost'
    server_port = 12345

    try:
        client_socket.connect((server_ip, server_port))
        print("Connection established.")
        is_connected_to_server = True
    except ConnectionRefusedError:
        print("Failed to connect to the server. Connection refused.")
        # Handle the connection error gracefully, e.g., display an error message to the user
        client_socket.close()


    def __init__(self):
        super().__init__(application_id='com.evokzh.ourcloud',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)
        self.create_action('quit', lambda *_: self.quit(), ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)
        

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = OurcloudWindow(application=self, send_message=self.send_message, is_connected_to_server=self.is_connected_to_server)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(transient_for=self.props.active_window,
                                application_name='ourcloud',
                                application_icon='com.evokzh.ourcloud',
                                developer_name='evokzh',
                                version='0.1.0',
                                developers=['evokzh'],
                                copyright='© 2024 evokzh')
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        # TODO: Fix this!
        print('app.preferences action activated')
        preferences = OurcloudPreferences(application=self)
        preferences.present()

    def send_message(self, message):
        """Send a message to the server."""
        self.client_socket.sendall(message.encode())
        response = self.client_socket.recv(1024)
        return response.decode()

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)



def main(version):
    """The application's entry point."""
    app = OurcloudApplication()
    return app.run(sys.argv)
