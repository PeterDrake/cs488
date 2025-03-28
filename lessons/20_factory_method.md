# Factory Method
* Problem: Implementations of the same method in different subclasses want to return different types of objects.
  * [Example diagram](https://refactoring.guru/design-patterns/factory-method): `createTransport` in `RoadLogistics` vs `SeaLogistics`
* Solution: Create an interface implemented by the various types being returned. Have the creator method in the original class return this type. Subclasses of the original class can now override this method.
* Structure diagram
* Pseudocode diagram
* [Python code](https://refactoring.guru/design-patterns/factory-method/python/example)

# Iteration 3
* Code
* Send build to customer
