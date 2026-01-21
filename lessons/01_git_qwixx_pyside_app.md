**Bring to class: dice, pencils, score sheets**

# Git

Walk through steps on [Pythonorama](https://github.com/alainkaegi/pythonorama/blob/main/software_development/git.md), with everyone following in lock step using `student` account:
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
* Committing again after a failed merge (without resolving the conflict)
  * Assuming you use -a, git commits the file with the conflicts included!
* Committing in detached HEAD state
  * Works, but branch has no name until you give it one

# Qwixx
(1:00)  
* [Rules](https://www.ultraboardgames.com/qwixx/deluxe.php)
  * Note typo: a penalty is worth -5, not 75
* Play

# PySide6
(1:30)  
Python package for building GUIs.

[PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/)
* Install package
* Work through first tutorial (creating your first app together)
* Everyone work through signals, widgets, and layouts

Challenge for everyone simultaneously: build a running-sum adding machine. If you get done early, build a four-function calculator.

# Standalone Python Application
(2:30)  
* Install the pyinstaller package
* In terminal (within PyCharm) do `pyinstaller -F src/adder.py`
* The application should be in `dist`
  * Copy it to the desktop and try to run it
    * Linux: right click, run as program
    * Windows: double click?
    * MacOS: double click?
  * Pyinstaller produces a build for the OS you're on


