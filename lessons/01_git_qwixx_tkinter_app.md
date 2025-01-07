**Bring to class: dice, pencils, score sheets**

# Git

Walk through steps on [Pythonorama git](NEED URL), with everyone following in lock step using `student` account:
* Installation verification
  * Install nano or another text editor first
* Configuration
* Creating a repo and initial commit
* Committing
* Working with past commits (log, checkout)
* Branches
* Don't talk about remote repos yet

Mistakes
* Forgetting to add a file
  * If you changed nothing else, trying to commit does nothing
  * If you did change something else, committing does not save the file in question in the repo
    * It can’t be reverted to past versions that were never committed
    * Other people won’t be able to get to it
* Changing branches when you haven’t committed yet
  * If you’ve changed a file that would be affected, git tells you to commit your changes first
* Committing again after a failed merge (without resolving the conflict)
  * Git will complain that there is an unresolved conflict
* Committing in detached HEAD state
  * Works, but branch has no name until you give it one

# Qwixx

Play.

# Tkinter

Python package for building GUIs. The name stands for "Tk interface", where "Tk" ("toolkit") is a multi-language GUI-building library.

[Tk Documentation](https://tkdocs.com/tutorial/)
* Be sure to choose Show > Python on the right side
* You don't have to worry about installation, but run the first program at the bottom of the installation page
    * TTk ("themed Tk") makes interfaces not look like they're from 1995
    * `root` is an instance of `Tk` -- the top-level window
    * The next line creates a button and installs it within the root window
    * The last line starts the event loop
* A First (Real) Example
* Tk Concepts
  * Offensive terminology
* Quick header skim of Basic Widgets
* Even quicker skim of other section titles

Challenge for everyone simultaneously: build a running-sum adding machine. If you get done early, build a four-function calculator.

# Standalone Python Application

* Install the pyinstaller package
* In terminal (within PyCharm) do `pyinstaller -F src/tk_hello.py`
* The application should be in `dist`

# For Next Time

* Do first day survey
* Reading: Ko chapters 1-2
