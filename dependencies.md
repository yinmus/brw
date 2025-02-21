## Зависимости

### Основные:
- [Python](https://www.python.org/) >= 3.6  
- [GTK+3](https://www.gtk.org/) (libgtk-3-dev, python3-gi)  
- [WebKit2GTK](https://webkitgtk.org/) (libwebkit2gtk-4.0-dev, gir1.2-webkit2-4.0)  
- [PyGObject](https://pygobject.readthedocs.io/en/latest/) (python3-gi, gir1.2-gtk-3.0)  

### Установка зависимостей
[есть инсталлер](install)

#### Debian/Ubuntu:
```sh
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 \
                 gir1.2-webkit2-4.0 libwebkit2gtk-4.0-dev \
                 libgtk-3-dev
```
#### Arch/Manjaro
```sh
sudo pacman -S python-gobject gtk3 webkit2gtk
```
(честно, хз, заработает ли у вас на Debian/Ubuntu, только на Arch смотел )
