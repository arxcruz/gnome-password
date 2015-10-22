import gi

gi.require_version('Gtk', '3.0')


from gi.repository import Gtk


class PasswordWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Gnome password')
        self.set_size_request(300, 100)
        self.set_border_width(6)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect('delete-event', Gtk.main_quit)

        self.password = Gtk.Entry()
        self.password.set_visibility(False)
        self.password.set_placeholder_text('Enter your password')
        self.password.set_icon_from_stock(Gtk.EntryIconPosition.PRIMARY,
                                          Gtk.STOCK_DIALOG_AUTHENTICATION)

        self.ok_button = Gtk.Button('Ok')

        self.cancel_button = Gtk.Button('Cancel')
        self.cancel_button.connect('clicked', Gtk.main_quit)

        button_box = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL,
                                   spacing=6)
        button_box.set_layout(Gtk.ButtonBoxStyle.END)
        button_box.pack_start(self.ok_button, False, False, 0)
        button_box.pack_start(self.cancel_button, False, False, 0)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(vbox)
        vbox.pack_start(self.password, True, True, 0)
        vbox.pack_start(button_box, False, False, 0)
        self.show_all()

win = PasswordWindow()
Gtk.main()