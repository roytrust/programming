## Clean Code
### Meaningful Names
* use intention-revealing name
* avoid disinformation
* make meaningful distinction
* use pronounceable names
* use searchable names
* avoid encoding
* no member prefix
* avoid mental mapping
* class names - noun
* method names - verb
* don'T be cute
* pick one word per concept
* don'T pun
* use solution domain names
* use problem domain names
* add meaningful context
* don't add gratuitous context

### Functions
* small
* indent level 1/2, no nested structure
* do one thing. Sections within fuctions signal multi things.
* one level of abstraction per function
* the stepdown rule
* switch statement, SOLID
* use descriptive names
* fuction arguments, less. Argument object, list
* have no side effects
* avoid output argument
* command query separation
* prefer exceptions to returning error codes. Extract try/catch blocks. Error handling is one thing.

### Comments
Don't comment bad code-rewrite it

### Formatting
* Your style and discipline survives, even though your code doesn't.

### Object and Data Structure
Objects expose behavior and hide data. Data structures expose data and have no significant behavior.
* Data abstraction. Hiding implemention is about abstraction.
* Data/object anti-symmetry
* principle of least knowledge. Train wrecks.
* ~~hybrid~~ - protection from functions or types. Feature Envy.
* Hiding structure- intent
* Data transfer objects. Active record.

### Error handling
* special case pattern. Dont return null. Dont pass null

### Boundaries
Code at the boundaries needs clear separation and tests that define expectations.

### Unit test
* Test code is just as important as production code.
* Test enable the -ilities. Remove fear of changes.
* Build Operate Check
* Given when then
* Single concept per test
* FIRST: Fast, Independent, Repeatable, Self-validating, Timely

### Classes
* Organization, encapsulation
* Should be small. The name of a class should describe what responsibilities it fulfills.
* Maintaining cohesion results in many small classes.
* Organizing for change
* Isolating from change

### Systems
* Separation of concerns
* separate constructing a system from using it. Separation of main
* factories
* DI: Dependence injection. IoC
* Scaling up
* cross-cutting concerns. AOP
* test drive the system arch. 
* optimize decision making
* use standards wisely, when they add demonstrable value.
* DSL: domain-specific language. Code idioms

### Getting clean via emergent design
4 rules of simple design
* Runs all the tests. A system that is comprehensively tested and passes all of its tests all of the time is a testable system.
* Refactoring
* No duplication
* Expressive. The intent
* Minimal classes and methods. Count

### Concurrency
Object are abstractions of processing. Threads are abstractions of schedule.
* Concurrency is a decoupling strategy. What and when.
* Myths and misconception
* Concurrency defense principled
  * srp, keep the concurrency-related code separate from other code.
  * corollary: limit the scope of data. Take data encapsulation to heart; severely limit the access of any data that maybe shared.
  * corollary: use copies of data. 
  * corollary: threads should be as independent as possible. Attempt to partition data into independent subsets than can be operated on by independent threads, possibly in different processors.
* Execution models. Producer-consumer, readers-writers, dining philosophers
* Writing correct shutdown code is hard.
* Make threaded code pluggable
* Make threaded code tunable
* Run with more threads than processors
* Instrument code to try and force failures. Use jiggling strategy to ferret out errors.

### Smells and Heuristics
#### Comments
* C1: Inappropriate Information
* C2: Obsolete Comment
* C3: Redundant Comment
* C4: Poorly Written Comment
* C5: Commented-out Code
#### Environment
* E1: Build requires more than 1 step
* E2: Tests require more than 1 step
#### Functions
* F1: Too many arguments
* F2: Output arguments
* F3: Flag arguments
* F4: Dead function
#### General
* G1: Multiple languages in 1 source file
* G2: Obvious behavior is unimplemented. The principle of Least surprise
* G3: Incorrect behavior at the boundaries
* G4: Overridden safeties
* G5: Duplication
* G6: Code at wrong level of abstraction
* G7: Base classes depending on their derivative
* G8: Too much information
* G9: Dead code
* G10: Vertical separation
* G11: Inconsistency
* G12: Clutter
* G13: Artificial coupling
* G14: Feature envy
* G15: Selector arguments
* G16: Obscured intent
* G17: Misplaced responsibility
* G18: Inappropriate static
* G19: Use explanatory variables
* G20: Fuction names should say what they do
* G21: Understand the algorithm
* G22: Make logical dependencies physical
* G23: Prefer polymorphism to if/else or switch/case
* G24: Follow standard convention
* G25: Replace magic numbers with named constants
* G26: Be precise
* G27: Structure over convention
* G28: Encapsulate conditionals
* G29: Avoid negative conditionals
* G30: Functions should do one thing
* G31: Hidden temporal coupling
* G32: Don'T be arbitrary
* G33: Encapsulate boundary conditions
* G34: Functions should descend only one level of abstraction
* G35: Keep configurable data at high levels
* G36: Avoid transitive navigation. Writing shy code
#### Names
* N1: Choose descriptive names
* N2: Choose names at the appropriate level of abstraction
* N3: Use standard nomenclature where possible
* N4: Unambiguous names
* N5: Use long names for long scope
* N6: Avoid encodings
* N7: Name should describe side-effects
#### Tests
* T1: Insufficient tests
* T2: Use a coverage tool
* T3: Don'T skip trivial tests
* T4: An ignored test is a question about an ambiguity
* T5: Test boundary conditions
* T6: Exhaustively test near bugs
* T7: Patterns of failure are revealing
* T8: Test coverage patterns can be revealing
* T9: Test should be fast



