# Observer Pattern

The observer pattern allows us to let our classes choose which other classes are their source of information at runtime, and itt works as a suscription service; several objects are suscrived to the information that another provides. When there is an update of some sort, the source would notify the suscribers.

It defines a one-to-many dependency between objects so that when one object changes state, all the others are notified, usually by calling one of its methods. The standalone object is called the Subject, and the others are the observers.

Because of this behavior, this is useful to implement event driven software. In those systems, the subject is called "Stream of Events", and the observers "Sink of Events". This pattern is suitable when the necessary data is not availabe at startup, and it comes from any random I/O source (http, GPIO, serial, databases...). It is typical to use a background thread listening for events while the main thread is bussy doing other things.

Examples of this would be any e-mail suscription service.

## Problems that it solves.
* One to many dependency between objects should be defined without making the objects tightly coupled.
* When one object changes its state, an open ended number of objects are updated automatically.
* In should be possible that on object can notify an open-ended number of other objects.
However, one must always take into account that this flexibility comes at a price. When the objects are tightly coupled, the compiler is usually able to optimize the code to the processor instruction level. The most optimal way to implement it is to notify the observers, and let them use the getters of the subject to fetch the relevant information to them. However, it may be the subject the one pushing information to the observers.

## Trade-offs
Subscribers are notified at random objects