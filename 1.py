from pystray import Icon, Menu, MenuItem
import PIL.Image
import webbrowser
import os


icon = PIL.Image.open('icon.png')


def close_prog():
    tray.stop()


def open_browser():
    url = 'https://www.google.com'
    webbrowser.open(url)


def open_spotify():
    url = 'https://open.spotify.com/'
    webbrowser.open(url)


def open_explorer():
    os.system("explorer")


tray = Icon('Huynya', icon, menu=Menu(
    MenuItem('Браузер', Menu(
        MenuItem('Открыть', open_browser),
        MenuItem('Спотик', open_spotify)
    )),
    MenuItem('Проводник', open_explorer),
    MenuItem('Закрыть', close_prog)
), title='Huynya')


if __name__=='__main__':
    tray.run()
