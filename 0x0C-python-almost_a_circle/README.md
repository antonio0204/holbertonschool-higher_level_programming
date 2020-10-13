![Python - Almost a circle](https://files.realpython.com/media/args-and-kwargs-in-Python_Watermarked.508ab9494cb5.jpg)   
# What * args and * kwargs mean as parameters
## Entendiendo *args
-----
In Python, the * args special parameter in a function is used to optionally pass a variable number of positional arguments.

Hahaha, what definition paranoia. Let's see it in detail:

- What really indicates that the parameter is of this type is the symbol '*', the name args is used by convention.
- The parameter receives the arguments as a tuple.
- It is an optional parameter. The function can be invoked making use of it, or not.
- The number of arguments when invoking the function is variable.
- They are positional parameters, so, unlike named parameters, their value depends on the position in which they are passed to the function.

python makes it a language very loved by many for the infinity of applications that it can be given.

-----

## Understanding ** kwargs
Let's now look at the use of ** kwargs as a parameter.

In Python, the ** kwargs special parameter in a function is used to optionally pass a variable number of named arguments.

The main differences from * args are:

- What really indicates that the parameter is of this type is the symbol '**', the name kwargs is used by convention.
- The parameter receives the arguments as a dictionary.
- As it is a dictionary, the order of the parameters does not matter. - The parameters are associated based on the dictionary keys.

------
# Python creator
## Guido van Rossum