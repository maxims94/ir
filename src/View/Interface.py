import curses
from curses import panel

import logging

class Interface(object):

    def __init__(self, items, stdscreen, numItems):
        self.screen = stdscreen
        curses.curs_set(0)

        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.numItems = numItems
        # self.items.append(('exit','exit'))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= self.numItems:
            self.position = self.numItems-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index, item.title)
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                # insert rules here
                pass

            elif key in [curses.KEY_UP, ord("k")]:
                self.navigate(-1)

            elif key in [curses.KEY_DOWN, ord("j")]:
                self.navigate(1)

            elif key == ord("h"):
                # Set Class to 0
                entry = self.items[self.position]
                logging.debug("Pressed h: Class = 0 for '%s'", entry.title)

            elif key == ord("l"):
                # Set Class to 1
                entry = self.items[self.position]
                logging.debug("Pressed h: Class = 0 for '%s'", entry.title)

            elif key == ord("r"):
                logging.debug("Pressed r: Reload database, regenerate model")
                # call controller

            elif key == ord("q"):
                logging.debug("Pressed q: Quit")
                break

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()