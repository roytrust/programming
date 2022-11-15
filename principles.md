## Top motto
* DRY: Don't repeat yourself
* Testable
* MVP
* Separate concerns
* Business outcome
* User story & backlog, acceptance
* [Defensive programming](https://en.m.wikipedia.org/wiki/Defensive_programming)

## [12factor](https://12factor.net/)
* A **codebase** is any single repo, or any set of repos who share a root commit.
* A **deploy** is a running instance of the app.
* A **backing service** is any service the app consumes over the network as part of its normal operation. The code for a twelve-factor app makes no distinction between local and third party services. To the app, both are attached resources, accessed via a URL or other locator/credentials stored in the config. 
* Twelve-factor processes are stateless and share-nothing. Any data that needs to persist must be stored in a stateful backing service, typically a database.
* Export services via port binding
* Concurrency: Scale out via the process model. The process model truly shines when it comes time to scale out. The share-nothing, horizontally partitionable nature of twelve-factor app processes means that adding more concurrency is a simple and reliable operation.
* The twelve-factor app’s processes are disposable, meaning they can be started or stopped at a moment’s notice. This facilitates fast elastic scaling, rapid deployment of code or config changes, and robustness of production deploys.
* 
## [Six Myths of Product Development](https://hbr.org/2012/05/six-myths-of-product-development)
1. Fallacy 1: High utilization of resources will improve performance. 
   * They don’t take into full account the intrinsic variability of development work.
   * They don’t understand how queues affect economic performance.
   * In product development, work-in-process inventory is predominantly invisible.
   * Change the management-control systems.
   * Selectively increase capacity.
   * Limit the number of active projects.
   * Make the work-in-process inventory easier to see.
1. Fallacy 2: Processing work in large batches improves the economics of the development process.  
   * Small batches have even greater utility in product development
   * In a well-managed process, the batch size will balance transaction and holding costs
   * By shrinking batch sizes, one company improved the efficiency of its product testing by 220% and decreased defects by 33%.
3. Fallacy 3: Our development plan is great; we just need to stick to it.
   * Testing and experimentation reveal what does and doesn’t work, and initial assumptions about costs and value may be disproved.
   * Defining customers’ needs can also be hard to do at the outset of a product-development project.
   * the plan should be treated as an initial hypothesis that is constantly revised as the evidence unfolds, economic assumptions change, and the opportunity is reassessed.
1. Fallacy 4: The sooner the project is started, the sooner it will be finished.
   * That’s problematic because product-development work is highly perishable: Assumptions about technologies and the market can quickly become obsolete.
   * The importance of reducing the amount of work in process is evident when we look at one of the classic formulas of queuing theory: Little’s Law.
   * carefully manage the number of projects in process
1. Fallacy 5: The more features we put into a product, the more customers will like it.
   * less can be more is hard because it requires extra effort in two areas of product development:
   * Defining the problem. The result is deep insights into customers that are tested, improved, or abandoned throughout the iterative development process.
   * Determining what to hide or omit.  The really great person will keep on going, and find…the key underlying principle of the problem and come up with a beautiful, elegant solution that works.
   * Determining which features to omit is just as important as—and perhaps more important than—figuring out which ones to include.
   * Products get closer to perfection when no more features can be eliminated. As Leonardo da Vinci once said, “Simplicity is the ultimate sophistication.”
1. Fallacy 6: We will be more successful if we get it right the first time.
   * Experimenting with many diverse ideas is crucial to innovation projects.
   * What we hope is becoming clear by now is that experiments resulting in failures are not necessarily failed experiments. They generate new information that an innovator was unable to foresee. The faster the experimentation cycle, the more feedback can be gathered and incorporated into new rounds of experiments with novel and potentially risky ideas. In such an environment employees tend to persevere when times get tough, engage in more-challenging work, and outperform their risk-averse peers.
   * 

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

## Object Oriented
### Advantages of OOP
1. Modularity for easier troubleshooting. encapsulation, self-contained.
2. Resue of code through inheritance.
3. Flexibility through polymorphism.
4. Effective problem solving. Divide-and-conquer.


## Agile
* [Agile Manifesto](https://agilemanifesto.org/)

### Scrum Master
* Ceremonies: Sprint planning, backlog review, daily standup, sprint review, retrospective
* Framework: Briefing from clients and other stakeholders, proudct owner
* Backlog review is effective:
  * Stories are refined in order or priority
  * Business value drives prioritization
  * Focus is on getting stories ready
  * Acceptance criteria are defined
  * Product owner sends agenda in advance
  * Backlog is clear
* Sprint Review is effective:
* Retrospective is effective: retromat.org
  * Squad has open and honest discussion
  * Issues are being resolved
  * Each issue has an owner
  * The session is fund!
  * Squad members express gratitude
  * Achievements are celebrated
* Squad: small 8-12 members. cross functional. dedicated. persistent 12-18 months.

  
  

## References
* Style guide: http://google.github.io/styleguide/
* http://manifesto.softwarecraftsmanship.org/
* [Embracing Agile](https://hbr.org/2016/05/embracing-agile)
* 
