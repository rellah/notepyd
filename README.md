# notepyd.py

A simple note taking script by Rellah

## Getting Started
 
### Dependencies

  Notepyd right now only requires tabulate.
  You can install tabulate via pip:
  
  ```
  pip install tabulate
  ```
  
### Installation

  Clone or download the repository
  
  ```
  git clone https://github.com/rellah/notepyd.git
  ```

  Alias the script in your .bashrc, .zshrc by adding the following to it:

```
alias notepyd="python3 ~/path/to/notepyd.py"
```

Then simply restart your terminal, or source the .rc, example for .zshrc:
```
source ~/.zshrc
```


### Usage

  Notepyd runs via terminal arguments, the usage is as follows:

```
    | notepyd  list               - Lits all current notes                    |
    | notepyd  delall             - Deletes all notes/lists                   |
    | notepyd  add    'title'     - Current way of adding a note/title        |
    | !notepyd add    note        - ^^ (NOT WORKING YET) Lets you add a note  |
    | !notepyd add    list        -    (NOT WORKING YET) Lets you add a list  |
    | notepyd  del    'title'     - Removes the note/list you entered.        |
    | notepyd  tick   'title'     - Lets you check off a completed task       |
    | notepyd  append 'title'     - Appends a task/text to a list/note        |
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/rellah/b24679402957c63ec426) for details on my code of conduct, and the process for submitting pull requests to me.


## Authors

* **Maximilian Walsh** - [Rellah](https://github.com/rellah)

See also the list of [contributors](https://github.com/rellah/notepyd/contributors) who participated in this project.


## License

This project is licensed under the GNU GPL v3 license - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* A special thanks to Al Sweigart, Brett Slatkin and Luciano Ramalho. Without your excellent sources of knowledge I might have never stayed committed enough. (Automate the Boring Stuff, Effective Python, and Fluent Python respectively)
* Sebastian, Cody and Joe. Three of my oldest and best friends
* Jesus, for always taking the wheel you crazy bastard
