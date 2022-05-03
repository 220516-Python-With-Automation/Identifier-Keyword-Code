# Day 1 - Keywords and Identifiers

Welcome to your first day of programming at Revature. These mini projects are designed to get your more comfortable with programming in Python in general without having to focus on making sure your environemnt is working. It is essentially after this week to have your environment working but in the meantime, to get more comfortable with programming in general, these tasks have been provided.

The topics that need to be covered in your program will be shown below, a set of automated tests will need to pass in order for you to see the solution. If you are stuck, reach out to your team mates.

Remember, you will need to write the code yourself. Do not copy and paste, if you do need help, type out the code by hand at the very least. You only learn programming by actually typing.

## Keywords
Keywords are some predefined and reserved words that Python uses which hold a special meaning and have their own syntax to how they are used. Because they are inherent to Pythons own language, they cannot be used as an identifier, name, function, or a variable name. 

Keywords are always lower case, with the only notable exception being True and False. There are many keywords out there and you can find the total list on the Python documentation:

https://docs.python.org/3/reference/lexical_analysis.html#keywords

### Guide
1. Write some code to check if a user has inputted a keyword or not
2. There is an inbuilt function for taking in a users input
     ```python
    # This function will wait for a user to type something into the console
    input() 
    # This line will read in the user input and save it to a variable name
    userInput = input() 
    # Putting inside input("")  a quote will display something to the user in the console but it
    # will not count as the input. It just will make it easier for the user to know what to give
    userInput2 = input("Type something in ... ")
    ```
3. There is an inbuilt function that can be used to check if a variable is a keyword
   ```python
    # the keyword is an object that is imported at the top of the main.py
    # if it is not there then include it like so
    import keyword

    # use this objects methods to test if a variable is a keyword or not, for example
    var = "True"
    print(keyword.iskeyword(var)) # True
   ```
   1. Make sure that the variable you are checking is a string and not the keyword itself
4. Test out your code with the available keywords to Python, then you will need to run the automated tests
    1. There are other automated tests that will need to pass before you are finished but they do not need to all be done at once


## Identfiers

The identifer is a name sued to identify a variable, function, class, module, etc. The identifier is a combination of character digits and underscore. The identifer should start with a character or underscore then if you want to use a digit, after them only. Characters include A-Z or a-z, an underscore is ( _ ), and digits mean (0 - 9). Do not use special characters like (#, @, $, %, !) in identifiers.

Examples of valid identifiers:
1. var1
2. _var1
3. _1_var
4. var_1

Examples of invalid identifiers:
1. !var1
2. 1var
3. 1_var
4. var#1


### Guide
1. Write some code to check if a variable identifier is a valid identifier
2. An identifier is declared like so
   ```python
   name1 = "This is a string"
   # ^ that is the identifier
   ```
3. There is an inbuilt method in Python to check if it is an identifer, the isidentifier() built-in function
   ```python
   name1 = "this is a string"
   print(name1.isidentifier())
   # This will print a boolean saying whether the variable is an identifier
    ```
4. However if you want to match whether or not it is a valid identifier then you will need to use a regular expression
    1. Regular expressions are very helpful to find a specific pattern but I don't expect you to create it yourself, a regular expression has been provided to check if it is a valid identifier
    2. You will however have to implement the search ability yourself 


# Instructions

Write some code that can take in a users input and test to see if it is either:
1. A keyword
2. A valid identifier
3. An invalid identifer

If it is a keyword then it should stop there and print out a statement indicating that like so
```python
# True is a keyword
# False is a keyword
# and is a keyword
# import is a keyword
```

If it is not a keyword then it should check to see if it is a valid or invalid identifier like so
```python
# var1 is a valid identifier
# var2 is a valid identifier
# 1var is not a valid identifier
# 2_var is not a valid identifier
```
4. Run the automated tests on your application to see if it passes, if it has then you can proceed to submit

## Hints
You will need to use conditional logic (control flow) and user inputs a lot, if you haven't used them before and you want to see how they are implemented use these links:

### Control Flow

https://www.educative.io/edpresso/what-are-control-flow-statements-in-python

https://jakevdp.github.io/WhirlwindTourOfPython/07-control-flow-statements.html

https://pynative.com/python-control-flow-statements/

### User Input

Only use the Python 3 examples

https://www.w3schools.com/python/python_user_input.asp

https://www.geeksforgeeks.org/taking-input-in-python/

### String formatting

This is not required but to make your life easier I would recommend learning Python string formatting. Here are some helpful resources:

https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

