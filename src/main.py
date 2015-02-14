from Model.item import create_tables, Item
import curses
from Services.rssservice import importFeeds
from Model.item import *
from View.Interface import Interface


def main(screen):
    """screen is a curses screen passed from the wrapper"""
    create_tables()
    importFeeds()
    query = Item.select()
    numItems = query.count()

    interface = Interface(query, screen, numItems)
    interface.display()

if __name__ == '__main__':
    curses.wrapper(main)