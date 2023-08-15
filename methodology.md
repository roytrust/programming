# Agile
* Explain **whay & why**
* Coaching


## Coaching
* Cooching is not about fixing people problems; it is about believing in people and helping them grow.
* team build: conversational turn-taking, ostentatious listening -> psychological safety
* Facilitative skills: emotional intelligence, connecting the dots, active listening, powerful questions, engaging conflict, flexibility
* Elements of EQ
  * Self-awareness: knowing how you feel
  * Self-regulation: managing your emotions
  * Motivation: desire to work toward something
  * Empathy: understanding and sharing the feelings of another
  * Social skills: communicating effectively
* Active listening
  * listen and understand, inquire, summarize what you heard, acknowledge their perspective
  * yes, and

### Ask more open, powerful questions
* open, stimulating, flowing, clear, rooted, non-judgmental
* how, what, why, who/when/where, which/yes-no questions

## Team, soft skills 
* Dysfunctions: lack of trust, fear of conflict (purpue truth), avoidance of accountability, 
* [Eisenhower Matrix](https://todoist.com/productivity-methods/eisenhower-matrix) 
* Managers lead by example when it comes to working hours.
* However, managers need to ensure even allocation of work.
* Effective managers maintain large internal networks across their company.
* One-on-ones remain vital
* Lastly, managers are engaged at work, too.

### Delegation framework
* What: what are you delegating?
* Why: to big picture and why them?
* How: any specific requirements? mode of communication?
* What if: any anticipated issues or obstacles?
* What next: how will you follow up and monitor progress?

### Habits 
[7 habits of highly effective people](https://franklincovey.ca/the-7-habits/)
* Be proactive: taking responsibility, responsible, we have the freedom to choose our response. One of the most important things we choose is what we say. On circle of influence.
  * Reactive: blame external sources, reactive language, in the circle of concern. 
* Begin with the end in mind. Mental, physical
* Prioritize, first things first, important things
* Think win-win. Mutual benefit.
* Seek first to understand, then to be understood. Empathetic communication.
* Creative cooperation
* Daily selfhrenewal

# [Design Patterns](https://refactoring.guru/design-patterns)
## Design Principle
* __Encapsulate what varies__. Identify the aspects of your application that vary and separate them from what stays the same.  
  Take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that don't.
* __Promgram to an interface__, not an implementation. Program to a supertype.  
  Exploit polymorphism by programming to a supertype so that the actual runtime object isn't locked into the code. 
  "program to a supertype" as "the declared type of the variables should be a supertype, usually an abstract class or interface, so that the objects
  assigned to those variables can be any concrete implementation of the supertype,
  which means the class declaring them doesn't have to know about the actual boject types.
* __Favor composition over inheritance__. HAS-A can be better than IS-A.
  Flexibility: encapsulate a family of algorithms. change behavior at runtime.
* Strive for __loosely coupled designs__ between objects that interact.
* __Open-Closed__: classes should be open for extension, but closed for modification.
* __Dependency Inversion__: Depend upon abstractions. Do not depend upon concrete classes.
  * No variable should hold a reference to a concrete class.
  * No class should derive from a concrete class.
  * No method should override an implemented method of any of its base classes.
* Principle of **Least Knowledge**: talk only to your immediate friends.
  * The object itself
  * Objects passed in as a parameter to the method
  * Any object the method creates or instantiates
  * Any components of the object
* **Don't call us, we'll call you**
  * Prevent "dependency rot". Allow low-level components to hook themselves into a system, but the high-level components determine when are needed, and how.
  * DI avoid the use of concrete classes and instead work as much as possible with abstractions.
* **Single Responsibility**: A class should have only one reason to change. Cohesion.
* 

## Concepts
* __algorithm__ always defines a clear set of actions that can achieve some goal, a __pattern__ is a more high-level description of a solution. algorithm is a cooking recipe, a pattern is more like a blueprint.
* Patterns aren't invented, they are discovered.
* OO Basics: abstraction, encapsulation, polymorphism, inheritance.
* __Null Objects__: don't have a meaningful object to return, and yet want to remove the responsibility for handling null from the client.

## Creational Patterns
### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
* Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

### [Factory Method](https://refactoring.guru/design-patterns/factory-method)
* Defines an interface for creating an objects but let subclasses to decide which class to instantiate. Factory Method lets a class defer instantiation to subclass.

### Singleton

## Behavioral Patterns
### [Strategy](https://refactoring.guru/design-patterns/strategy)
* Define a family of algorithms, encapsulates each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
* __context__ must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object instead of executing it on its own.
* __client__ passes the desired strategy to the context. In fact, the context doesn’t know much about strategies. It works with all strategies through the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the selected strategy.
* This way the context becomes independent of concrete strategies, so you can add new algorithms or modify existing ones without changing the code of the context or other strategies.

### [Observer](https://refactoring.guru/design-patterns/observer)
* Defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically. Subject, observer.

### [Command: encapsulate invocation](https://refactoring.guru/design-patterns/command)
* Encapsulates a request as an object, thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.
* Decouples an object making a request from the one that knows how to perform it.
* A Command object is at the center of this decoupling and encapsulates a receiver with an action (or set of actions).
* An invoker makes a request of a Command object by calling its execute() method, which invokes those actions on the receiver.
* Invokers can be parameterized with Commands, even dynamically at runtime.
* Commands may support undo by implementing an undo() method that restores the object to its previous state before the execute() method was last called.
* MacroCommands are a simple extension of the Command Pattern that allow multiple commands to be invoked. Likewise, MacroCommands can easily support undo().
* In practice, it's not uncommon for "smart" Command objects to implement the request themselves rather than delegating to a receiver.
* Commands may also be used to implement logging and transactional systems.
* Turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

### [Template Method](https://refactoring.guru/design-patterns/template-method)
* Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
* Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
* Methods: concrete, abstract, hook
* Hooks are methods that do nothing or default behavior in the abstract class, but may be override in the subclass.
* High-level modules decide how and when to call low-level modules.
* The strategy and template method patterns both encapsulate algorithms, the first by composition and the other by inheritance.
* Factory method is a specialization of template method.
* For creating frameworks.

### [Iterator](https://refactoring.guru/design-patterns/iterator)
* Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
* An Iterator takes the job of iterating over an aggregate and encapsulates it in another object.
* Iterable return an Iterator.

### [State](https://refactoring.guru/design-patterns/state)
* Lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.
* Unlike a procedural state machine, the State pattern represents each state as a full-blown class.
* The Context gets its behavior by delegating to the current state object it is composed with.
* By encapsulating each state into a class, we localize any changes that will need to be made.
* The State and Strategy patterns have the same class diagram, but they differ in intent.
* The Strategy Pattern typically configures Context classes with a behavior or algorithm.
* The State Pattern allows a Context to change its behavior as the state of the Context changes.
* State transitions can be controlled by the State classes or by the Context classes.
* State classes may be shared among Context instances.

## Structural Patterns
### [Decorator](https://refactoring.guru/design-patterns/decorator)
* Attaches additional responsibilities to an object dynamically, by placing these objects inside special wrapper objects that contain the behaviors. Decorators provide a flexible alternative to subclassing for extending fucntionality.

### [Adapter](https://refactoring.guru/design-patterns/adapter)
* Converts the interface of a class into another interface clients expect. Lets classes work together that couldn't otherwise because of incompatible interfaces.
### [Facade](https://refactoring.guru/design-patterns/facade)
* Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

### [Composite](https://refactoring.guru/design-patterns/composite)
* Compose objects into tree structure to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
* A component is any object in a Composite structure. Components may be other composites or leaves.
* Balance transparency and safety.

## References
* https://refactoring.guru/design-patterns


