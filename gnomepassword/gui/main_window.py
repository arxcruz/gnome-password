import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from widgets import Inspector


class MainWindow(object):
    """Main window of Gnome password manager"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gnome_password_manager.ui")

        self._connect_glade_objects()
        self._connect_signal_handlers()
        self._configure_main_window()

    def _connect_signal_handlers(self):
        handlers = {
            'on_inspector_toggled': self.on_inspector_toggled
        }

        self.builder.connect_signals(handlers)

    def _connect_glade_objects(self):
        self.inspector = self.builder.get_object('inspector')
        self.headerbar = self.builder.get_object('main_window_headerbar')

    def _configure_main_window(self):
        main_window = self.builder.get_object("main_window")
        main_window.set_titlebar(self.headerbar)
        main_window.connect('delete-event', Gtk.main_quit)
        main_window.show_all()

        main_hbox = self.builder.get_object('main_hbox')
        self.inspector = Inspector()
        main_hbox.pack_start(self.inspector, False, True, 0)

    # Signal events

    def on_inspector_toggled(self, toggle_button):
        self.inspector.set_reveal_child(toggle_button.get_active())

if __name__ == '__main__':
    main = MainWindow()
    Gtk.main()
