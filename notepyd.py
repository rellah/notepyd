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
import sys
from notes import Notes


# If no argument is specified, print help. Otherwise, continue.
if len(sys.argv) == 1:
    Notes.print_usage()
else:
    try:
        notesShelf = shelve.open('notes')
        if len(sys.argv) == 2:
            if sys.argv[1].lower()   == 'list':
                Notes.list_notes(notesShelf)
            elif sys.argv[1].lower() == 'delall':
                Notes.delete_all_notes(notesShelf)
        if len(sys.argv) == 3:
            if sys.argv[1].lower()   == 'add':
                Notes.add_note(notesShelf, sys.argv[2])
            elif sys.argv[1].lower() == 'append':
                Notes.add_step(notesShelf, sys.argv[2])
            elif sys.argv[1].lower() == 'del':
                Notes.delete_note(notesShelf, sys.argv[2])
            elif sys.argv[1].lower() == 'view':
                Notes.view_note(notesShelf, sys.argv[2])
        if len(sys.argv) == 4:
            if sys.argv[1].lower()   == 'tick':
                Notes.delete_step(notesShelf, sys.argv[2], sys.argv[3])
    # Closes the database safely before termination
    finally:
        notesShelf.close()

"""
    TODO
        - System to rank notes by importance
        - Add date functionality

"""
