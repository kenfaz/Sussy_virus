"AMOGUS VIRUS!!!"
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QUrl
import sys
from pygame import mixer
from random import randint, choice
from PIL import Image
import os

mixer.init()
mixer.music.load("Images/amogus.wav")
mixer.music.play(-1)

def get_num_pixels(image):
    w, h = Image.open(image).size
    return [w, h]


size = [500, 500]


class Window(QWidget):
    def __init__(self, size: list, window_title: str, window_icon: str, window_label: str, window_gif: str,
                 window_sound: str) -> object:
        super().__init__()

        # Initiating variables
        self.size = size

        self.window_title = window_title
        self.window_icon = window_icon
        self.window_label = window_label
        self.movie = QMovie(window_gif)
        self.sound = window_sound
                
        self.setGeometry(self.size[0], self.size[1],
                         self.size[2], self.size[3])
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QIcon(self.window_icon))

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel(window_label)
        label.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(label)


def main():
    # Launch window
    app = QApplication(sys.argv)
    gif = choice(os.listdir("Images/gifs"))
    gif_size = get_num_pixels("Images/gifs/" + gif)
    window = Window([randint(1, 400), randint(1, 400), gif_size[0], gif_size[1]],
                    "You got amogus!", "Images/amogussus.jpg", "Amogus", "Images/gifs/" + gif, "Images/amogus.wav")
    window.show()
    app.exec()


if __name__ == "__main__":
    while True:
        main()
