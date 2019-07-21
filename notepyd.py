#!/usr/bin/env python3
"""
    notepyd.py
    a simple note taking script by Max Walsh

    Notepyd Usage:
        notes list          - Lists all current notes
        tes l
        notes add  'title'  - Allows you to enter a note
        notes tick 'title'  - Check off a done task
        notes del  'title'  - Removes a note of your choice
        notes delall        - Removes all notes in the database.
        --------------------------------------------------------
        notepyd list                - Lits all current notes
        notepyd delall              - Deletes all notes/lists
        notepyd add  note           - Lets you add a note.
        notepyd add  list           - Lets you add a list (think TODO)
        notepyd del  'title'        - Removes the note/list you entered.
        notepyd 'title' tick        - Lets you check off a completed task.
        note

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
