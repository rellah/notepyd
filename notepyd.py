#!/usr/bin/env python3
"""
    notepyd.py
    a simple note taking script by Max Walsh

    Notepyd Usage:
        notes list          - Lists all current notes
        notes add  'title'  - Allows you to enter a note
        notes tick 'title'  - Check off a done task
        notes del  'title'  - Removes a note of your choice
        notes delall        - Removes all notes in the database.

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
            elif sys.argv[1].lower() == 'del':
                Notes.delete_note(notesShelf, sys.argv[2])
            elif sys.argv[1].lower() == 'view':
                Notes.view_note(notesShelf, sys.argv[2])
        if len(sys.argv) == 4:
            if sys.argv[1].lower()   == 'tick':
                Notes.delete_step(notesShelf, sys.argv[2], sys.arg[3])
    # Closes the database safely before termination
    finally:
        notesShelf.close()

"""
    TODO
        - System to rank notes by importance
        - Add date functionality

"""
