import sys
import cv2
#import time # if you need to slow down playback
import curses
from math import floor

def normalize(value, max, new_max):
    return clamp((value * new_max) / max, 0, new_max)

def clamp(input, min, max):
    if input < min:
        return min
    elif input > max:
        return max
    else:
        return input

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    rows, cols = screen.getmaxyx()
    charset = "Ñ@#W$9876543210?!abc;:+=-,._ "
    charset_length = len(charset)-1
    
    path = sys.argv[1]
    video = cv2.VideoCapture(path)
    success, image = video.read()

    try:
        while success:
            screen.clear()
            image = cv2.resize(image, (cols-1, rows-1))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for row in gray:
                for pixel in row:
                    screen.addstr(charset[floor(normalize(pixel, 255, charset_length))])
                screen.addstr("\n")

            screen.refresh()
            success, image = video.read()
    except KeyboardInterrupt:
        curses.endwin()

if __name__ == "__main__":
    main()