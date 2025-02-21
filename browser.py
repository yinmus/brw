import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2

HOMEPAGE = "https://www.google.com"


class Browser(Gtk.Window):
    def __init__(self):
        super().__init__(title="GTK + WebKit Браузер", default_width=1024, default_height=768)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        toolbar = Gtk.Box(spacing=5)
        buttons = {
            "back": "res/arrowL.ico",
            "forward": "res/arrowR.ico",
            "reload": "res/rest.ico",
            "home": "res/home.ico"
        }

        for action, icon_path in buttons.items():
            button = Gtk.Button()
            button.set_image(Gtk.Image.new_from_file(icon_path))
            button.connect("clicked", getattr(self, f"on_{action}_clicked"))
            toolbar.pack_start(button, False, False, 5)

        self.url_entry = Gtk.Entry(text=HOMEPAGE, placeholder_text="Введите адрес или поисковый запрос")
        self.url_entry.connect("activate", self.on_url_entry_activate)
        toolbar.pack_start(self.url_entry, True, True, 5)

        vbox.pack_start(toolbar, False, False, 0)

        self.webview = WebKit2.WebView()
        self.webview.load_uri(HOMEPAGE)
        self.webview.connect("load-changed", self.on_load_changed)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        vbox.pack_start(scrolled_window, True, True, 0)

        self.show_all()

    def on_back_clicked(self, button):
        self.webview.go_back()

    def on_forward_clicked(self, button):
        self.webview.go_forward()

    def on_reload_clicked(self, button):
        self.webview.reload()

    def on_home_clicked(self, button):
        self.webview.load_uri(HOMEPAGE)

    def on_url_entry_activate(self, entry):
        url = entry.get_text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        self.webview.load_uri(url)

    def on_load_changed(self, webview, event):
        self.url_entry.set_text(webview.get_uri())


if __name__ == "__main__":
    app = Browser()
    Gtk.main()
