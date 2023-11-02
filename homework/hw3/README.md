> COMP 525 Data Structures Fundamentals - Fall 2023

## Homework 3 Guidelines
### Purpose of the homework
In this homework assignment you will:
- Test, design, and implement methods of the linked list implementation of an UnsortedList ADT
- Practice test-driven, incremental develment
- Develop code that meets code analysis and styling requirements
- Apply version control that supports incremental development.

### Starter project content
#### Class Node
```
class Node:
    """
    Element in a linked list data structure
    Insatnce variables
        data: integer
        next: Node
    """
```
The `Node` class implements the data type of an element in a linked list
implementation of the Unsorted List ADT. The class has two attributes:
* `self._data`holds an integer
* `self._next`holds a reference to a Node object

The API of this class has:
* getters for both attributes `self._data` and `self._next`
* setters for both both attributes
* `__str__()` special method to produce a string representation of a Node 
  object. 

Note that we use Python's **@property** and **@<attr_name>.setter** 
decorators, where **<attr_name>** is the name of the attribute, e.g., 
`data` or `next`
Read https://docs.python.org/3/library/functions.html#property to learn about
the these Python decorators.

The basis of this implementation is Brad Miller and Dave Ranum's
Runestone Academy textbook, *Problem Solving with Algorithms and Data
Structures in Python*.

#### Unsorted List
```
class UnsortedList:
    """
    UnorderedList ADT implemented with a linked list of Node  objects
    Instance variables
        _head: object reference (or address or id) of a Node
            or None, if this unordered list doesn't have any Node
        Note: In Python, the value of  object reference is a positive integer
            obtained from calling id() and passing the object as argument.
    """
```
The `UnsortedList` class implements the linked list data structure of a
**UnsortedList ADT**. The class has one instance variable:
* `self._head` points to the first node in the list or None if the list is
empty

The API of this class has:
* getter and setter for `self._head` instance variable: `head(self)` and 
  `head(self, other_node)`
* `__str__()` special method to produce a string representation of an 
  unsorted list object
* methods that implement UnsortedList ADT operations:
    * `is_empty()`
    * `prepend(item)`
    * `size()`
    * `search(item)`
    * `remove(item)`
    * `append(item)`
    * `pop(pos)`

### Test-driven incremental development

#### I. Understand and document the problem

- The docstrings for the modules in the `src` subdirectory must have your name 
  and completion date. 
- The last three methods in the `UnsortedList` class must have 
  well-formed docstrings. Replace the `#` comments with docstrings that 
  include, if appropriate, `:param <name>` and `:return:` docstring items. 
- **Version control** these changes to reflect the 
  **documentation step**. Note that this is the very first commit of the 
  program development for this assignment. 

#### II. Testing the methods
To understand the problem, we need to know **what** the **output** should 
be for different **input** cases. That's why we write test 
cases as testing functions in `main.py` module. These testing functions are 
called one at a time in `main()` function. 

Each `UnsortedList` method has its own testing function. 
- `test_prepen()` has been implemneted and discussed in class. Just run 
  `main.py` program to see the resutls. 
- `test_size()` and `test_search()` are testing functions for methods that 
  have also been implemented. 
  - Implement these two testing functions. 
  - Call one at a time in `main()` to verify them. 
  - Debug, fix errors, if any.
  - Check code analysis and style (PyCharm Problems, pyling, and pycodestyle)
  - **Version control** this step of testing. 

The remaining 4 testing functions are for methods that don't have a design 
and implementation:
- `test_print()`
- `test_append()`
- `test_pop()`
- `test_remove()`

For each of these testing functions:
- FIRST, write the code for the testing function, and then you will continue 
  with steps III and IV to design and implement the method that's being tested.
- Check code analysis and style for the testing function
- **Version control** the development of the testing function.

#### III.. Devise a plan: Write your design ONE method at at time.

- Design the solution the source functions, ONE function at a time.
- Write the design in the **DESIGN.md** file.
- **Version control** these changes to reflect the **design development 
  step** for each source function.

After designing a source function, move on to implement it

#### IV. Carry out the plan: Implement the methods, ONE at a time

- Implement the method guided by your design.
- Test, debug, fix, and test again its implementation.
- Check code analysis and style of the implementation. 
  - Fix all **PyCharm Problems**.
  - Run **pycodestyle** and **pylint** and fix all styling errors.
- **Version control** these changes to reflect the **implementation step**.

Repeat steps I, II, and III for each of these methods:
- `__str__()`
- `append(item)`
- `pop()`
- `remove()`

Note that development is ONE method at a time. This means that the testing, 
design, and implementation steps require at minimim 3 commits for each 
method. Counting the very first commit for documentaiton and the commit for 
writing testing function for the methods that were already implemented, 
the minimum total of commits is 14.  

### Individual work
This assignment is exclusively individual work. If you have any questions, 
please ask me. I'll share my answers with the entire class. This work will 
give you more practice with a "white-board" technical interview. 

- Do not copy the implementation from the internet or have the implementation 
  generated by online services.
- Do not ask somebody else to write the implementation for you.
- Do not give your implementation to someone else.

### Make your submission

When you are done, synchronize your remote repo with the development in 
your local repo using the following `git` commands in PyCharm `git-bash` or 
`bash` terminal:

- `git remote -v` \<--- shows the remote URL, to ensure that you push to the right remote repo
- `git log`\<--- to see the all your commits
- `git push origin main` \<-- to publish your local repo to GitHub

In the GitHub organization **2023-spring-comp-525** , check out that your 
**h3-xxx** repo has been updated.

### Evaluation

- **Documentation** : 10%
- **Testing**: 24%
- **Implementation**: 16%
- **Design** : 20%
- **Incremental development** : 14%
- **Style** : 16%:
  - Eliminate all **PyCharm Problems** signaled by PyCharm.
  - Run **pycodestyle** and **pylint** to eliminate any styling errors.
