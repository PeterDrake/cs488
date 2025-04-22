# Observer
* Also known as Listener
* Problem: Many objects want to be notified when certain events happen.
* Solution: Have Subscribers subscribe to a Publisher, who keeps track of them. When an event occurs, it goes through its list of Subscribers, notifying each one.
* [Pseudocode diagram](https://refactoring.guru/design-patterns/observer)
* [Python code](https://refactoring.guru/design-patterns/observer/python/example)

# State
* Problem: An object can be in any of several states, each with different behavior. This can be handled by a long if/else statement, but it's difficult to maintain and might appear redundantly in each method.
* Solution: Have the outer object contain an object encapsulating the state, which knows how to do everything when in that state. When the state changes, the outer object just points to a different state object.
* Traffic light
  * I'll produce a version where you can print the current light color or advance it, using if/elses.
  * Class: refactor this to use the State pattern.
* OO designers like to use different classes instead of ifs!

# Iteration 5
* Code
