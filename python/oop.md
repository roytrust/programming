### Tips
* https://realpython.com/python-classes/
* Use single main inheritance, plus Mixin for addon features 
* Multiple constructor: @classmethod, @singledispatchmethod
* MRO (Method Resolution Order): mro(), __mro__  
  children precede their parents and the order of appearance in __bases__ is respected.
* the order of your inheritance is to make the highest to lowest from left to right.
* [super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
  * returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.  
  * can take two parameters: 1st is a subclass, 2nd is an instance of that subclass.
  * the delegation chain stops here: `assert not hasattr(super(), 'draw')`
* Refer to class dynamically: `type(self).attr`
* Dynamic class and instance attributes: `instance.__dict__['attr']=v;setattr(obj, field, val)`
* Save memory, can't add new attr, no `__dict__`: `__slots__=('x', 'y')`
* Delegation: `def __getattr__(self, attr)`
* [Static duck typing](https://devpress.csdn.net/python/62f5260a7e6682346618a2a1.html): `from typing import Protocol, TypeVar; class Duck(Protocol): id: int; M = TypeVar('M', bound=Duck); def func(d: M) -> M: pass`
* [Enum, enumerations](https://realpython.com/python-enum/). Replacing Magic Numbers, Creating a State Machine
  * `from enum import Enum; class Day(Enum); Enum(value, names, *, module=None, qualname=None, type=None, start=1); auto(); @unique; aliases; .name; .value`
  * Mixing: `class Size(int, Enum); IntEnum; StrEnum; IntFlag; Flag`
* `**kwargs dictionary` to pass parameters 
  ```
  def __init__(self, name, **kwds):
        self.name = name
        super().__init__(**kwds)
  ```
### Mixin
* Mixins are tools to create classes in compositional styles.
* A mixin is meant to be “mixed in” to other pieces of code. It might run on its own, but it was not created with the intention to run on its own.
* A mixin is a class that is implementing a small and specific set of features that is needed in many different classes.
* You want to provide a lot of optional features for a class.
* You want to use one particular feature in a lot of different classes.

#### Mixin vs. decorator
* Generally, decorators are most commonly used to modify the behavior of existing code while Mixins are used to add new behaviors.
* Decorators wrap functionality around a piece of code.
* Mixins add functionality to code using Inheritance.
* Mixins only work with Object-Oriented Programming and Classes. You cannot use Mixins to modify a function or a method, only classes.
* Decorators cannot add new methods or new pieces of code.

### Concepts
* Polymorphism
  * Method Overriding
