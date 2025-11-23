# Chatper 9 Classes 

Object-oriented programming (OOP) is one of the most effective approaches to writing software
It involves creating:

- classes that represent real-world things or situations
- objects (instances) created from those classes 
 
When writing a class, you define the general behavior that a category of objects can have.
When you create individual objects (instances), each one automatically has the class’s general behavior and can also have unique traits.

Making an object from a class is called instantiation, and working with these objects means working with instances.

## Creating and Using a Class 
We'll write a simple class, Dog, that represents a dog.
Each instance created from the class will store a name and an age, and each dog will be able to sit and roll over.

[Creating a the Dog Class](chapter_9_codes/dog.py)

Defining a class and in Python, class names are capitalized by convention:
```python
class Dog:
```
The `__init__()` is a function thats part of a classed is called a *method*. Method is a special method that Python runs automatically whenever we create a new instance based on the class 

- It has two leading underscores and two trailing underscores. This naming convention helps avoid conflicts with your own method names.
```python 
def __init__()
```
The method that has been defined contains three paramters: self, name, and age.
The `self` parameter is required in the method definition, and must come first, before the other parameters
It must be included in the definition because when Python calls this method, the method call will automatically pass the `self` argument.

Every method call associated with an instance automatically pases `self` which is a reference to the instance itself.
Any variable prefixed with `self` is available to every method in the class, and be able to access these variables through any isntance created from the class

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```
This line of code takes the value associated with the parameter **name** and assigns it to the variable **name**, which is then attached to the instances being created.
Variables that are accesible through instnaces like this are called **attributes**
```python 
self.name = name 
self.age = age
```
### Making an Instance from a Class
Think of a class as a set of instructions for how to make an instnace
The Dog class is a set of instructions that tells Python how to make individual instances representing specific dogs.

In this part of the code. We tell Python to create a dog whose name is 'Willie' and whose age is 6

When Python reads this line, it calls `__init()__` method creates an instnace representing this particular dog and sets the name and age attributes using the values we provided.
Python returns an instance representing this dog. In the following code, we assign that instance to the variable my_dog.

['creating an instance from a class](chapter_9_codes/dog.py#L14-L16)
```python
my_dog = Dog('Willie', 6)
```
### Accessing Attributes 
To access the attributes of an instance, you use dot notation
```python
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```
Dog notation is used often in Python. This syntax demonstrates how python finds an attribute's value.
### Calling Methods
After creating an instance from the class, we can use dot notation to call any method defined in the class

To call a method, give the name of the instance and the method you want to call, separated by a dot.
```python
my_dog.sit()
my_dog.roll_over()
```
### Creating Multiple Instances 
You can create as many instances from a class you need.
```python 
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```
In this example of code, we created a dog named Willie and Lucy. Each dog is a separate instnace with its own attributes

## Working with Classes and Inheritance 

You can modify the attributes of an instance directly or write methods that update attributes in specific ways 

### The Car class 
Writing a class that represents a car

[The Car Class Code](chapter_9_codes/car.py)

### Setting a Default Value for an Attribute 

When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the `__init__` method, where they are assigned a default value

Adding an attribute called **odometer_reading** that always start with a value of 0

[odometer_reading attribute added](chapter_9_codes/car.py#L7)

This time Python calls the __init__ method to create a new instance, it stores the variables as attributes.Then Python creates a new attribute called odometer_reading and set its initial value to 0.
Not many car are sold with exactly 0 miles on teh odometer, so we need a way to change the value of this attribute

### Modifying Attributes Value
Three ways to change an attribute's value in three ways:
1. you can change the value directly through an instance
2. set a value through a method
3. increment the value (add a certain amount to it) through a method 

#### Modifying an Attribute's Value Directly 
Simplest way to modify the value of an attribute is to access teh attribute directly through an instance

[Attribute's Value Directly](chapter_9_codes/car.py#L21)
```python
my_new_car.odometer_reading = 23
```
We use the dot notation to access the car's odometer_reading attribtue, and set its value directly 
#### Modifying an Attribute's Value Through a Method 
It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.

- [Line 15-17](chapter_9_codes/car.py#L15-17)

- [Line 28](chapter_9_codes/car.py#L28)

We can extend the method update_odometer() to do additional work every time the odometer reading is modified. Let's add a little logic to make sure no one tries to roll back the odometer reading
- [Line 17-20](chapter_9_codes/car.py#L17-20)

#### Incrementing an Attribute's Value through a Method 
Sometimes you'll wnat to increment an attribute's value by a certain amount, rather than set entirely new value. 

Saw we buy a used car and put 100 miles on it between the time we buy it and the time we register it.
Here's a method that allows us to pass this incremental amount and add that value to the odometer reading:

- [Line 21-23](chapter_9_codes/car.py#L21-23)
You can modify this method to reject negative increments so no one uses this function to roll back on odometer as well 

***Note***: You can use methods liek this to control how users of your program update values such as an odometer reading, but anyonewith access to the program can set the odometer reading to any value by accessing the attribute directly. Effective security takes extreme attention to detail in addition to basic checks like thos shown here 

### Inheritance 
If the class you're writing is a specialized version of another class you wrote, you can use ***inheritance***. When one class *inherits* from another, it takes on the attributes and methods of the first class. 

The original class is called the ***parent class*** , and the new class is called the ***child class***

The child class can inherit any or all of the attributes and methods of its parent class, but it's also free to define new attributes and method of its own 
#### The __init__() Method for a Child Class 

When writing a new class based on an existing class, you'll often want to call __init__() method from the parent class.
This will initialize any attributes in the child class 
- [Line 25-28)](chapter_9_codes/electric_car.py#L25-L28)

Starting with Car. 
1. When creating a child class, the parent class must be part of the current file and must appear before the child class in the file.
2. Define the child class, Electric Car. The name of the parent class must be included in parentheses in the definition of a child class. The __init__() mehtod takes in the information rquired to make a Car 
3. the `super().__init__()` function is a special function that allows you to call method from the parent class. 

The name *super* comes from a convention of calling the parent class a *superclass* and the child class a *subclass*

### Defining Attributes and Methods for the Child Class 
Once you have a child clas that inherits from a parent class, you can add any new attributes and method necessary to differentiate the child class form the parent class 
- [Line 30-32](chapter_9_codes/electric_car.py#L30-32)