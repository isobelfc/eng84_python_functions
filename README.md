# Functions
## DRY

- Don't Repeat Yourself
- If you are doing the same thing multiple times, write a function to do it

## Functions

- A function is a way to reduce the amount of code written
- If the same process is being performed multiple times, once you have declared a function you can perform the process with just one line of code
- It also reduces the chances of error, as the steps of the function only need to be written once, and can be easily checked
- `def` is a keyword that tells the interpreter that a function is being declared
- This is followed by the name of the function, and then any arguments (or args) in parentheses
```python
def greetings(name):
    print("Welcome on board, " + name)
```
- In this example, `name` is the argument, and the value given is then used within the function
- Defining a function will not execute it. It must be called
```python
greetings("James")
```
- A function should do one job