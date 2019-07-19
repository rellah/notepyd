"""
Notes class
     Dedicated to encapsulating the listing, adding, removing etc.
     and removing clutter from the main class.
"""


class Notes:
    def __init__(self):
        pass

    def print_usage():
        print("""
            Notepyd Usage:
                notes list         - Lists all current notes
                notes add  'title' - Allowes you to enter a note
                notes tick 'title' - Check off a done task
                notes del  'title' - Removes a note of your choice
                notes delall       - Removes all notes in the database
            """)

    def list_notes(shelf):
        for title, content in shelf.items():
            print("+----- %s -----+" % (title))
            for index, line in content.items():
                print("%d. %s" % (index, line))
            print("")

    def add_note(shelf, title):
        currentNotes = dict()
        count = 1
        while True:
            userinput = input()
            if len(userinput) >= 1:
                currentNotes[count] = userinput
                count += 1
            else:
                shelf[title] = dict(currentNotes)
                print("Note successfully added!")
                break

    # TODO Add in sorting by index once a step has been deleted
    def delete_step(shelf, title, step):
        step = int(step)
        content = shelf[title]
        if step in content.keys():
            del content[step]
            if len(content.keys()) >= 1:
                shelf[title] = content
                print("Task complete!")
            else:
                del shelf[title]
                print("You completed all your tasks!")

    # TODO
    def add_step(shelf, title, append_step):
        pass

    def delete_note(shelf, title):
        if title in shelf.keys():
            del shelf[title]
        else:
            print("Note could not be found.")

    def delete_all_notes(shelf):
        for title in shelf.keys():
            del shelf[title]
            print("Deleting note '%s'..." % (title))

    def view_note(shelf, title):
        if title in shelf.keys():
            print("+----%s----+" % (title))
            for index, line in shelf[title].items():
                print("%d. %s" % (index, line))
