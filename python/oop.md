### Tips
* Use single main inheritance, plus Mixin for addon features 
* MRO (Method Resolution Order): mro(), __mro__  
  children precede their parents and the order of appearance in __bases__ is respected.
* [super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
  * returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.  
  * can take two parameters: 1st is a subclass, 2nd is an instance of that subclass.
  * the delegation chain stops here: `
        assert not hasattr(super(), 'draw')`

* `**kwargs dictionary` to pass parameters 
  ```
  def __init__(self, name, **kwds):
        self.name = name
        super().__init__(**kwds)
  ```


### Concepts
* Polymorphism
  * Method Overriding
