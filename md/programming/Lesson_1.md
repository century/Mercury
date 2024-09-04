---
title: Lesson 1
author: Grant
date: 2024-06-30
---
> Programming is a skill  

## Topics:  
- Solving problems using computation  
- Python programming language  
- Organizing modular programs  
- Some simple but important algorithms  
- Algorithmic complexity  

## Types of Knowledge
- **Declarative knowledge** is a statement of fact.
- **Imperative knowledge** is a recipe or "how-to."

### Numerical Example
- Square root of a number `x` is `y` such that `y * y` is `x`.
- Start with a guess, `g`
	1. If `g * g` is close enough to `x`, stop and say `g` is the answer.
	2. Otherwise make a new guess by averaging `g` and `x / g`.
	3. Using the new guess, repeat the process until close enough.

### Algorithm
1. Sequence of simple steps.
2. Flow of control process that specifies when each step is executed.
3. A means of determining when to stop.

### Computers are Machines that Execute Algorithms
- Two things computers do:
	- Performs simple operations
	- Remembers results
- What kind of calculations?
	- Built-in to the machine, e.g. addition, subtraction
	- Ones that you define as the programmer (made of commands built into machine)
> A computer only does what you tell it to do.

## History
- **Fixed Program Computer**
	- Fixed set of algorithms (like a calculator)
	- What we had until 1940s
- **Stored Program Computer**
	- Machine stores and executes instructions
- Key Insight: Programs are no different from other kinds of data.

### Stored Program Computer
- Sequence of instructions stored inside computer
	- Built from predefined set of primitive instructions
		- Arithmetic and logical
		- Simple tests
		- Moving data
- Special program (interpreter) executes each instruction in order
	- Use tests to change flow of control through sequence
	- Stops when it runs out of instructions or executes a halt instruction
					
### Basic Primitives
Alan Turing proved that one can compute anything with just 6 primitive instructions. He imagined a tape with values and 6 instructions that would act on the tape: left (move the tape left 1), right (move the tape right 1), print (print a symbol on the current section), scan (identify any symbols on the current square), erase (remove everything on the current section), and nothing (do nothing).
Real programming languages have a more convenient set of primitives and ways to combine primitives to make new primitives.
Anything computable in one language is computable in any other programming language (if it has these 6 primitives in it)

## Python

### Primitive Constructs
**English**: Words  
**Python**: Numbers, strings, simple operators 

### Syntax
**English:** "cat dog boy" is *not* syntactically valid  
"cat hugs boy" *is* syntactically valid  
**Programming Language**: `"hi"5` is *not* syntactically valid  
`"hi" * 5` *is* syntactically valid  

### Static Semantics
**English**: "I are hungry" syntactially valid but static semantic error  **Programming Language**: `"hi" + 5` is syntactially valid but static semantic error  
Programs have only one meaning, but the meaning may not be what programmer intended.  

### Errors
**Syntactic errors**: Common and easily caught.
**Static Semantic Errors**: Some languages check for these before running the program, and they cause unpredictable behavior.  
Even if there are no "linguistic" errors, there can be different meanings than what the programmer intended; the program could stop running before reaching its goal, it could run forever, it could give a wrong answer.  

### Python Programs
A program is a sequence of definitions and commands  
	- Definitions evaluated
	- Commands executed by Python interpreter in a shell
- Commands (statements) instruct interpreter to do something
- Can by typed directly in a **shell** or stored in a **file** that is read into the shell and evaluated

### Objects
- Programs manipulate **data objects**.
- Objects have a **type** that defines the kinds of things programs can o to theme
	- `30`
		- Is a number
		- We can add/subtract/multiply/divide/exponentiation/etc.
	- `"Word"`
		- Is a sequence of characters (a string)
		- We can grab substrings, but we can't divide it by a number (or subtract, add, etc.)
- **Scalar** (cannot be subdivided):
	- Numbers: `8.3`, `2`
	- Truth values: `True`, `False`
- **Non-scalar** (have internal structure that can be accessed)
	- Lists
	- Dictionaries
	- Sequence of characters: `"abc"`

#### Scalar Objects
- `int` ‚Äî represents integers, (`5`, `-100`)
- `float` ‚Äî represents floating point numbers (`3.27`, `2.0`)
- `bool` ‚Äî represents Boolean values (`True` and `False`)
- `NoneType` ‚Äî Special and has one value, `None`
- `type()` shows type of an objcets
	> > > type(5)
	int
	> > > type(3.0)
	float
There are infinite amount of ints and floats, whereas there are only two bools (`True` and `False`) and only one NoneType (`None`)  

### Type Conversions
This does not change the object, it makes a new object (for example, if you have integer `3` in memory, casting it to a float does not *change* the integer `3` but rather creates a new float `3.0` in memory).  
`float(3)` casts the int `3` into float `3.0`  
`int(3.9)` casts (note the truncation!) the float `3.9` to int `3`  
Some operations perform *implicit* casts:  
`round(3.9)` returns the int `4`  

### Expressions
Combine objects and operators to form expressions.
	- `3 + 2`
	- `5 / 3`
An expression has a value, which as a type.
	- `3 + 2` has value `5` and type int
	- `5 / 3` has value `1.6666667` and type float
Python evaluates experssions and stores the value . It doesn't store expressions.
Syntax for a simple expression:
`<object> <operator> <object>`
Computations work left-to-right. Parentheses override left-to-rightness

### Operators on `int` and `float`
- `i + j` ‚Äî the sum (if both `i` and `j` are ints, result is int. Otherwise, result is float)
- `i - j` ‚Äî the difference (if both `i` and `j` are ints, result is int. Otherwise, result is float)
- `i * j` ‚Äî the product (if both `i` and `j` are ints, result is int. Otherwise, result is float)
- `i / j` ‚Äî division (result is always a float)
- `i // j` ‚Äî truncates the division to a float ( result is always an integer)
- `i % j` ‚Äî the remainder when `i` is divided by `j` (result is always an integer)
- `i ** j` ‚Äî `i` to the power of `j` (if both `i` and `j` are ints, result is int. Otherwise, result is float)

### Variables
`pi = 3.141592653594230985703` because we don't want to write out `3.141592653594230985703` every time we use pi.
**Math Variables**: Are abstract and can represent many valuables (i.e. a + 2 = b - 1)
**CS Variables**: Is bound to one single value at a given time and can be bound to an expression. (i.e. `m = 10`, `F = m * 9.98`. In this case, m = 10 and F = 99.8)

#### Binding Values to Variables
In Computer Science, an equal sign ( "=") is an **assignment**. One value to one variable. An equal sign is **not** equality, not ‚Äúsolve for x‚Äù.
An assignment binds a value to a name.
- **Step 1**: Compute the value on the right-hand side (the value), which is then stored in computer memory.
- **Step 2**: Store it (bind it) to the left-hand side (the variable). 
		 
### Abstracting Expressions
Choose variable names wisely. Code should be readable in a year (and longer) by you and others.
```python
pi = 355/113  
radius = 2.2  
area = pi * (radius**2)  
circumference = pi * (radius*2)  
```

### Comments
Comments tell others (and yourself) what your code is doing. They start with a `#`. 
```python
# This is a comment
message = "This is code"
```

### Code Style
```python
# Do calculations  
a = 335/113 * (2.2**2)  
c = 335/113 * (2.2 *2)
```
This is pretty bad code.

```python
p = 355/113  
r = 2.2  
# Multiply p with r squared  
a = p*(r**2)  
# Multiply p with r times 2  
c = p*(r*2)
```
This is ok code.

```python
# Calculate area and circumference of a circle using an approximation for pi  
pi = 355/113  
radius = 2.2  
area = pi * (radius**2)  
circumference = pi * (radius * 2)
```
This is good code.

### Change Bindings
You can rebind variable names using new assignment statements. Previous value may still stored in memory but lost the handle for it.