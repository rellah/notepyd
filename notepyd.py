#!/usr/bin/env python3
"""
    notepyd.py
    a simple note taking script by Max Walsh

    Notepyd Usage:
        notes list        - Lists all current notes
        notes add (title) - Allows you to enter a note
        notes del (title) - Removes a note of your choice
        notes delall      - Removes all notes in the database.

"""
import shelve
import sys
from notes import Notes


# Function to list notes stored in database
def list_notes():
    for title, content in notesShelf.items():
        print("--+ %s +--" % (title))
        for index, line in content.items():
            print("%d. %s" % (index, line))
        print("")


# Function to add notes to database
def add_note(title):
    currentNotes = dict()
    count = 1
    while True:
        userinput = input()
        if len(userinput) >= 1:
            currentNotes[count] = userinput
            count += 1
        else:
            notesShelf[title] = dict(currentNotes)
            print("Note successfully added!")
            break


# Function to delete a note
# TODO: When a note is deleted, reorder by index
def delete_note(title):
    if title in notesShelf.keys():
        del notesShelf[title]
    else:
        print("Note not found.")


# Function to delete all notes
def delete_all_notes():
    for title in notesShelf.keys():
        del notesShelf[title]
        print("Deleting note '%s'..." % (title))


# Simply prints a help output.
def print_usage():
    print("""
        Notepyd Usage:
            notes list        - Lists all current notes
            notes add 'title' - Allows you to enter a note
            notes del 'title' - Removes a note of your choice
            notes delall      - Removes all notes in the database.
        """)


# If no argument is specified, print help. Otherwise, continue.
if len(sys.argv) == 1:
    print_usage()
else:
    try:
        notesShelf = shelve.open('notes')
        if len(sys.argv) == 2:
            if sys.argv[1].lower() == 'list':
                notesShelf.notes()
                #  list_notes()
            elif sys.argv[1].lower() == 'delall':
                delete_all_notes()
        if len(sys.argv) == 3:
            if sys.argv[1].lower() == 'add':
                add_note(sys.argv[2])
            elif sys.argv[1].lower() == 'del':
                delete_note(sys.argv[2])
    # Closes the database safely before termination
    finally:
        notesShelf.close()

"""
    TODO
        - System to rank notes by importance
        - Add date functionality

"""
