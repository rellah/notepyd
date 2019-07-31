#!/usr/bin/env python3
"""
    notepyd.py
    a simple note taking script by Max Walsh

        Notepyd Usage:
    +-------------------------------------------------------------------------+
    | notepyd  list               - Lits all current notes                    |
    | notepyd  delall             - Deletes all notes/lists                   |
    | notepyd  add    'title'     - Current way of adding a note/title        |
    | !notepyd add    note        - ^^ (NOT WORKING YET) Lets you add a note  |
    | !notepyd add    list        -    (NOT WORKING YET) Lets you add a list  |
    | notepyd  del    'title'     - Removes the note/list you entered.        |
    | notepyd  tick   'title'     - Lets you check off a completed task       |
    | notepyd  append 'title'     - Appends a task/text to a list/note        |
    +-------------------------------------------------------------------------+

"""
import shelve
from notes import Notes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', help='List all current notes', action='store_true')
parser.add_argument('-a','--add', help='Current way of adding a note/title', type=str)
parser.add_argument('-ap','--append', help='Append to note', type=str)
parser.add_argument('-d','--delete', help='Delete note', type=str)
parser.add_argument('-da','--delall', help='Delete all notes', action='store_true')
parser.add_argument('-v','--view', help='View a note', type=str)
parser.add_argument('-t','--tick', help='Check off completed note', type=str)
parser.add_argument('--step', help='unknown, required for tick', type=int)

args = parser.parse_args()

try:
    notesShelf = shelve.open('notes')
    if args.add:
        Notes.add_note(notesShelf, args.add)
    elif args.append:
        Notes.add_step(notesShelf, args.append)
    elif args.delete:
        Notes.delete_note(notesShelf, args.delete)
    elif args.delall:
        Notes.delete_all_notes(notesShelf)
    elif args.view:
         Notes.view_note(notesShelf, args.view)
    elif args.tick:
        Notes.delete_step(notesShelf, args.tick, args.step)
    elif args.list:
        Notes.list_notes(notesShelf)

except ImportError:
    print('There was an error')
    
finally:
    notesShelf.close()
"""
    TODO
        - System to rank notes by importance
        - Add date functionality

"""
