import os
import logging
import traceback
import curses

from Model.item import create_tables, Item
from Services.rssservice import importFeeds
from View.Interface import Interface

def main(screen):
    """screen is a curses screen passed from the wrapper"""

    if os.path.isfile('ir.log'):
        os.remove('ir.log')

    logging.basicConfig(filename='ir.log', level=logging.DEBUG, format='(%(asctime)s) %(message)s', datefmt='%I:%M:%S')
    logging.debug("Intelligent Reader started")

    try:
        create_tables()
        importFeeds()
        query = Item.select()
        numItems = query.count()
        interface = Interface(query, screen, numItems)
        interface.display()
    except BaseException as e:
        logging.critical(traceback.format_exc())

if __name__ == '__main__':
    curses.wrapper(main)
