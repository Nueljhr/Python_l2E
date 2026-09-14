
think of tuples as list written in permanent marker and list as written with pencil
tuples ..secret to multiple returns 
tuples cant be changed 
list is a mutable collection
a tuple is a collection that can hold lots of values together
Indents (spaces) at the start of a line that tell Python which instructions belong inside a specific decision gate.
Python uses spaces (exactly 4 spaces) to define what code belongs inside a conditional branch. The colon (:) at the end of an if, elif, or else line tells Python: "The instructions that follow this colon are inside the gate."
loops are structures for iterating through a list of items, tuples and strings over a specified period of time or while a condition remains true
use a for loop when you know exactly how many times to repeat
<<<<<<< HEAD
# casting is a type of conversion that doesnt affect the value of the variable.
isdigit is checking if every character is a number. 
reference is is referring a variable to another variable meaning they will both have the same value.
a == b used when cheking to figure out if the both carry same contents and a is b checks to see if both boxes refer to the same value/content
=======
use .strip() to remove whitspace 
use .capitalize() for proper casing
>>>>>>> 16e772b (notes.md updates)
FUNCTION IS A NAMED REUSABLE BOCK OF CODE DESIGNED TO PERFORM A SINGLE, SPECIFIC TASK 
PARAMETER IS A VARIABLE INSIDE A FUNCTION DEFINITION THAT ACTS AS A PLACE HOLDER.
ARGUMENT THE ACTUAL VALUE PASS INTO THE FUNCTION WHEN YOU CALL IT.
PARAMETERS HELP YOU PASS DIFFERENT ARGUMENTS INTO THE SAME FUNCTION.
ONCE PYTHON HITS RETURN IT HANDS DATA BACK AND STOPS RUNNING WHILE IF PYTHON HITS PRINT IT DISPLAYS DATA AND STOPS RUNNING.
POSITIONAL ARGUMENTS MUST COME BEFORE KEYWORD ARGUMENTS.
Positional arguments are assigned according to their position.
Keyword arguments explicitly identify the parameter receiving each value.
a is b checks for if a and b are exactly same object and produces a boolean
a == b checks if a and b have same contents/values
=    → ASSIGN
==   → SAME/EQUAL VALUE?
is   → SAME EXACT OBJECT?
list are mutable
tuples arent mutable
.append()       → ADD a new item
[index] = value → REPLACE an existing item
append()       → ADD
[index] = x    → REPLACE
remove(x)      → REMOVE BY VALUE
pop(index)     → REMOVE BY INDEX
pop()          → REMOVE LAST
scope tells about the specific area of a program where a variable can be used
Global scope are variables declared outside of any function.
.2f means round to 2 decimal place.
clear() used to clear everything in a list while the list iitself remains
remove("Banana")
       ↓
remove by VALUE

pop(1)
       ↓
remove by INDEX + give item back

clear()
       ↓
remove EVERYTHING from the list

del fruits[1]
       ↓
delete by INDEX
[::2]   → forward by 2
[::-1]  → backward by 1
[::-2]  → backward by 2
A CLASS DESCRIBES WHAT SOMETHING SHOULD LOOK LIKE
A class is a blueprint.
An object is an instance created from that blueprint.
Attributes store information belonging to individual objects.
A method is essentially a function that belongs to an object/class. A function that is defined inside a class
upper() is a method associated with a string object.
append() is a method associated with a list object.
self represents the particular object using the method. So self basically allows the method to know: "Which object am I working with?". Python automatically supplies self; it represents the object currently being initialized/used. self connects the attribute to the particular object being created.
if you use return then to this play you need print buh if you use print in the function then you dont need to call the function otherwise it will ask for a return value which will display as #none
Parameter is Defined inside the function: "A placeholder waiting to receive a value."
Argument is Supplied when calling: "The actual value I'm giving the parameter."
Attribute is Stored on the object: "The value now belongs to this object."
__init__() = automatically runs when you create an object and initializes its attributes. __init__() is commonly called an initializer. self.attribute = parameter
A rule inside a method only controls behavior when that method is executed. It does not automatically protect an attribute from direct modification elsewhere.
continue means: "Skip the rest of THIS current loop iteration and go to the next one."
range() starts at 0 by default
An accumulator is simply a variable that keeps collecting/updating a result as a program runs.
isinstance(account_balance, int) # False
isinstance is used to check if a variable is of or matches a particular data type. It takes a value and the type you want to check it against, then returns a boolean, also allows you to check for multiple types at once.
