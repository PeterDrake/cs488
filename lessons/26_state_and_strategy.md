# State
* Problem: An object can be in any of several states, each with different behavior. This can be handled by a long if/else statement, but it's difficult to maintain and might appear redundantly in each method.
* Solution: Have the outer object contain an object encapsulating the state, which knows how to do everything when in that state. When the state changes, the outer object just points to a different state object.
* Traffic light
  * I'll produce a version where you can print the current light color or advance it, using if/elses.
  * Class: refactor this to use the State pattern.
* OO designers like to use different classes instead of ifs!

# Strategy
* Problem: You want to provide several variants of an algorithm without bloating your class.
  * Example from Refactoring Guru: route planning for car, walking, mass transit, biking...
* Solution: Make a class for each strategy. They all implement a common interface.
* [Pros and cons](https://refactoring.guru/design-patterns/strategy)
  * TPS: In Python, how could you avoid defining a class for each strategy?
  * Example: key argument to sorted (sorting strings lexicographically, by length, or by last character)

# Iteration 5
* Code
