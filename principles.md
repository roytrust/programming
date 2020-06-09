## Top motto
* DRY: Don't repeat yourself
* Testable
* MVP
* Business outcome
* User story & backlog, acceptance

## Principles
### SRP: single responsibility principle
A class should have only one reason to change. 
This principle is about people (actor).
Gather together the things that change for the same reason. Separate those things that change for different reasons. (cohesion & coupling)

### OCP: open/close ptinciple
 "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification"
* Abstraction is the Key
* Strategic Closure
* Using Abstraction to Gain Explicit Closure
* Using a “Data Driven” Approach to Achieve Closure
* No Global Variables -- Ever

### LSP: liskov substitution principle
* Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
* Design by Contract

### ISP: interface segregation principle
* Many client-specific interfaces are better than one general-purpose interface.
* no client should be forced to depend on methods it does not use.
* Separation through Delegation

### DIP: dependency inversion principle
* One should "depend upon abstractions, [not] concretions."
* High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces).
* Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

### SoC: Separation of Concerns
Modular, layer

### Principle of least knowledge
* Writing shy code
* Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
* Each unit should only talk to its friends; don't talk to strangers.
* Only talk to your immediate friends.

### Proverb
* The art of programming is, and has always been, the art of language design. Think of systems as stories to be told rather than programs to be written.
* code=detailed spec. Such a spec is code.
* Leave the campground cleaner than you found it. Continuous improvement.
* Easy to read/understand, clarity


## Terms
* **Paradigm**: a style or approach to programming
* **Design Pattern**: tried and tested solution to common cases.
* **Higher-order function**: takes a function as an argument, or return a function.
* **Principles** are ways of thinking, **patterns** are common ways to solve problems. Coding patterns may be seen as missing programming language features.

## Dependency injection, IoC
Dependency injection involves four roles:
* the **service** object(s) to be used
* the **client** object that is depending on the service(s) it uses
* the **interfaces** that define how the client may use the services
* the **injector**, which is responsible for constructing the services and injecting them into the client

As an analogy,
* **service** - an electric, gas, hybrid, or diesel car
* **client** - a driver who uses the car the same way regardless of the engine
* **interface** - automatic, ensures driver doesn't have to understand engine details like gears
* **injector** - the parent who bought the kid the car and decided which kind

## Library vs Framework 
* The key difference is "Inversion of Comtrol". When you call a method from a **library**, you are in control. But with a **framework**, the control is inverted: the framework calls you.
* Both of them defined API, which is used for programmers to use. To put those together, we can think of a library as a certain function of an application, a framework as the skeleton of the application, and an API is connector to put those together. A typical development process normally starts with a framework, and fill out functions defined in libraries through API.
* **Toolkit** is a collocation of libraries.

## References
* Style guide: http://google.github.io/styleguide/
* http://manifesto.softwarecraftsmanship.org/
