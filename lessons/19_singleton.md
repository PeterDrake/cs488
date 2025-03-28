# Singleton
* Problem: You need to ensure that only one instance of a class exists
  * Examples: Sound or score manager in a game, database connection
* Solution: Make the constructor private, then provide a static way of getting the instance (or creating one if there is none).
* [Python implementation](https://refactoring.guru/design-patterns/singleton/python/example)
* A more Pythonic approach: [Just use a global variable](https://python-patterns.guide/python/module-globals/)
  * Be very careful if the object is mutable

# Iteration 3
Code