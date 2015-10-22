from gi.repository import Gtk


class Inspector(Gtk.Revealer):
    """
    Inspector widget.
    This is a simple implementation of a panel that
    will show information regarding the selected password
    """
    def __init__(self):
        super(Gtk.Revealer, self).__init__()
        self.builder = Gtk.Builder()
        self.builder.add_from_file('widgets.ui')
        box = self.builder.get_object('inspector')
        self.builder.connect_signals(self)
        self._connect_glade_objects()
        self._create_popover(self.expire_button)

        self.set_transition_type(Gtk.RevealerTransitionType.SLIDE_RIGHT)
        self.add(box)
        self.show_all()

    def _connect_glade_objects(self):
        self.show_password = self.builder.get_object('show_password_button')
        self.expires = self.builder.get_object('expires_check_button')
        self.expire_button = self.builder.get_object('expiration_date_button')

    def _create_popover(self, widget):
        self.popover = Gtk.Popover()
        self.popover.set_relative_to(widget)
        self.popover.set_position(Gtk.PositionType.BOTTOM)
        calendar = Gtk.Calendar()
        calendar.connect('day-selected', self.on_calendar_day_selected)
        self.popover.connect('closed', self.on_popover_closed)
        self.popover.add(calendar)
        calendar.show()

    def on_expiration_button_toggled(self, toggle_button):
        self.popover.set_visible(True)

    def on_calendar_day_selected(self, calendar):
        if self.expires.get_active():
            # Set the date
            pass
        self.popover.set_visible(False)

    def on_popover_closed(self, popover):
        self.expire_button.set_active(False)
