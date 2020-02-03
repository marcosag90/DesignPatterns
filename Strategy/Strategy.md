# Strategy Design Pattern

The strategy design pattern is meant to be used when we have several methods to do the same thing, and we have to be flexible to choose them at runtime. Each strategy is a class by itself. In other words, we can create a family of algorithms, and select one from the pool at runtime. All this algorithms should be interchangeable.


![](https://cdn.journaldev.com/wp-content/uploads/2013/07/Strategy-Pattern.png)

All these strategies do the same (single) job. For example, think of SortingAlgorithm as the interface, and BobbleSort, MergeSort, DivideAndConquerSort, HeapSort, etc, as the different strategies one could choose from.

A real world example of this are the plug-ins of a computer. You plug some device to the computer, and it does a different thing depending on what it is.
