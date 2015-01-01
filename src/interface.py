import curses
import sys
import logging
import webbrowser

from src.item import Item
from src.database import Database
from src.model import Model
from src.rss import RSS

class Interface:
    
    TOP_MENU_HEIGHT = 3
    TOP_MENU_MARGIN_BOTTOM = 1

    LIST_ITEM_HEIGHT = 3
    LIST_ITEM_MARGIN_BOTTOM = 1
    
    def run():

        Interface.init()

        Interface.init_data()
        Interface.init_objects()

        while True:
            Interface.screen.clear()
            Interface.screen.refresh()
            Interface.init_objects()

            c = Interface.screen.getch()

            #logging.debug("Pressed key %s", c)

            if c == ord("q"):
                logging.debug("Pressed q: Quit")
                break

            if c == ord("j"):
                logging.debug("Pressed j: Move one item down")
                Interface.current_item_index += 1
                total = len(Interface.db.get_items())-1
                if Interface.current_item_index > total:
                    Interface.current_item_index = total

            if c == ord("k"):
                logging.debug("Pressed k: Move one item up")
                Interface.current_item_index -= 1
                if Interface.current_item_index < 0:
                    Interface.current_item_index = 0

            if c == ord("l"):
                entry = Interface.items[Interface.current_item_index][0]
                logging.debug("Pressed l: Class = 1 for '%s'", entry)
                entry.set_class(1)
                Database.write(Interface.db)

            if c == ord("h"):
                entry = Interface.items[Interface.current_item_index][0]
                logging.debug("Pressed h: Class = 0 for '%s'", entry)
                entry.set_class(0)
                Database.write(Interface.db)

            if c == ord("r"):
                logging.debug("Pressed r: Reload database, regenerate model")
                Interface.init_data()

            # Not portable
            # Enter key
            if c == 10:
                entry = Interface.items[Interface.current_item_index][0]
                logging.debug("Pressed Enter: Class = 1 for '%s'", entry)
                entry.set_class(1)
                Database.write(Interface.db)

                link = entry.get_link()

                if link:
                    webbrowser.open(link, new=2)
                    logging.debug("Open URL in Browser: %s", link)
                else:
                    logging.debug("No URL available")

        Interface.close()

    def init():

        Interface.screen = curses.initscr()

        curses.noecho()
        curses.cbreak()
        curses.start_color()

        Interface.screen.keypad(1)

        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        Interface.screen.bkgd(curses.color_pair(1))
        Interface.screen.refresh()

        Interface.db = None
        Interface.model = None

        Interface.current_item_index = 0

    def init_data():
       
        logging.debug("Load database")

        if Interface.db == None:
            Interface.db = Database.read()
        
        for url in open('config/src', 'r'):
            items = RSS.get_items_by_url(url)
            for i in items:
                Interface.db.add(i)
        
        Database.write(Interface.db)

        logging.debug("Database loaded (%i entries)", len(Interface.db.get_items()))

        logging.debug("Create model")

        Interface.model = Model(Interface.db)
        Interface.model.generate()

        logging.debug("Model created")

        logging.debug("Apply model")

        items = list(map((lambda x: (x, Interface.model.apply(x))), Interface.db.get_items()))
        items = sorted(items, reverse=True, key=(lambda x: x[1]))
        Interface.items = items

    def init_objects():

        maxy, maxx = Interface.screen.getmaxyx()

        Interface.top_menu = curses.newwin(Interface.TOP_MENU_HEIGHT, maxx, 0, 0)
        Interface.top_menu.bkgd(curses.color_pair(2))
        Interface.top_menu.box()
        Interface.top_menu.addstr(1, 2, "=== Intelligent Reader ===")
        Interface.top_menu.refresh()

        Interface.item_wins = {}

        y = Interface.TOP_MENU_HEIGHT + Interface.TOP_MENU_MARGIN_BOTTOM

        for idx, item in enumerate(Interface.items):

            if idx < Interface.current_item_index:
                continue

            win = curses.newwin(Interface.LIST_ITEM_HEIGHT, maxx, y, 0)

            if item[0].get_class() == 0:
                win.bkgd(curses.color_pair(2))
            else:
                win.bkgd(curses.color_pair(3))

            win.box()

            content = "{} ({:.3})".format(item[0], float(item[1]))

            if idx == Interface.current_item_index:
                win.addstr(1, 2, content, curses.A_UNDERLINE)
            else:
                win.addstr(1, 2, content)

            win.refresh()

            Interface.item_wins[idx] = win

            if y > maxy:
                break
            
            y += Interface.LIST_ITEM_HEIGHT + Interface.LIST_ITEM_MARGIN_BOTTOM

    def close():

        curses.nocbreak()
        Interface.screen.keypad(0)
        curses.echo()
        curses.endwin()
