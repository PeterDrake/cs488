# Iterator
* Problem: You want to go through the elements in a collection without knowing how the collection is represented
  * TPS: Why would you ever need to do this?
* Solution: Create an iterator object that can get the next item to report that there are none left
* [Structure diagram](https://refactoring.guru/design-patterns/iterator)
  * Iterable vs Iterator
* Bonus idea: Provide more than one iterator for the same collection
* Warning: Don't modify the collection while it is being iterated through
* [iter.py](../src/iter.py)

# Observer
* Also known as Listener
* Problem: Many objects want to be notified when certain events happen.
* Solution: Have Subscribers subscribe to a Publisher, who keeps track of them. When an event occurs, it goes through its list of Subscribers, notifying each one.
* [Pseudocode diagram](https://refactoring.guru/design-patterns/observer)
* [Python code](https://refactoring.guru/design-patterns/observer/python/example)

# Iteration 4
* Code
* Send build to customer
