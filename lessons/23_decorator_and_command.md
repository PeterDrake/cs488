# Decorator
* Note: Python uses the word "decorator" for a different thing! (Example: @classmethod)
* Problem: You want to be able to attach several behaviors, chosen at runtime, to an object.
  * Example: Logging to a file, sending an email, writing to the console
* Solution: Make each one a class that delegates to the object that it's wrapped around, then does its own thing.
* [Pseudocode diagram](https://refactoring.guru/design-patterns/decorator)
* [`decorator.py`](../src/decorator.py)
* Similar pattern: Adapter.

# Command
* Problem: You want to be able to invoke the same command in several ways (button, menu, hotkey) without redundant code
* Solution: Make the command its own object
* [Diagrams in Solutions section](https://refactoring.guru/design-patterns/command)
* TPS: How does this relate to being able to undo multiple commands?

# Iteration 4
* Code
