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
            userinput = input("%d. " % (count))
            if len(userinput) >= 1:
                currentNotes[count] = userinput
                count += 1
            else:
                if len(currentNotes) > 1:
                    shelf[title] = dict(currentNotes)
                    print("Note successfully added!")
                    break
                else:
                    print("Nothing has been added.")
                    break

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
        else:
            print("Invalid number.")
        Notes.sort_list(shelf, title)

    def add_step(shelf, title):
        content = shelf[title]
        stepCount = len(content) + 1
        while True:
            userinput = input("%d. " % (stepCount))
            if len(userinput) >= 1:
                content[stepCount] = userinput
                stepCount += 1
            else:
                break
        shelf[title] = dict(content)

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

    def sort_list(shelf, title):
        count = 1
        _list = shelf[title]
        newList = dict()
        for index, text in _list.items():
            newList[count] = text
            count += 1
        shelf[title] = newList

