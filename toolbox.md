---
title: JavaScript Toolbox
author: Kevin Buman
website: https://github.com/McSquanchy/webpr-fs21-toolbox
logo: images/javascript.svg
---

# Week 1 - Functions

* Parameters are **not** checked

  ```js
  function fun1(arg) {
      return arg;
  }
  
  fun1(); // undefined
  fun1(42, 35, "hello"); // 42
  ```

* **No** function overloading

  ```javascript 
  function fun2(arg) {
      return 1;
  }
  
  function fun2(arg) {
      return arg;
  } 
  
  fun2(); // undefined
  fun2(42, 35, "hello"); // 42
  ```

* `return` keyword required

  ```javascript 
  function noReturn() {
      1;
  }
  
  noReturn(); // undefined
  ```

* Curly brackets constitute a function body

* Functions can be freely bound to new variables

  ```javascript
  const myfun = fun1;
  ```

* Higher-order functions

  ```javascript 
  function fun1(fun2) {
      return function fun3(arg) { 
          return fun2(arg);
      };
  }
  ```

* Curried functions

  ```javascript
  const plus = (x) => (y) => (x+y);
  const intermediate = plus(3);
  ```

  Lambda Expressions

```javascript
const sum = function (a, b) { return a + b };

// can be written as:
const sum = (a, b) => a + b;

// or
const sum = (a, b) => { return a + b };

// parentheses optional for one parameters
const sum = a => a;

// without parameters
var noop = () => {} // noop

// application:
[1,2,3,4].filter(function (value) {return value % 2 === 0});
// to:
[1,2,3,4].filter(value => value % 2 === 0);
```

## Canvas

```javascript
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
context.fillStyle = "black";
context.fillRect(0, 0, canvas.width, canvas.height);
```

## Key Events

```javascript
const rightArrow = 39;
const leftArrow = 37;
window.onkeydown = evt => {
(evt.keyCode === rightArrow) ? ... : ...;
};
```

## Game Loop

```javascript
setInterval( () => {
    nextBoard();
    display(context);
}, 1000 / 5);
```

## Resources

* Gabriel Lebec, [Fundamentals of Lambda Calculus & Functional Programming in JavaScript](https://www.youtube.com/watch?v=3VQ382QG-y4)

## Example

A function `plus` that returns the sum of its arguments:

```javascript
const plus = x => y => x + y;
```

# Week 2 - Lambda

## JavaScript Variables

Only use `let` and `const`:

```javascript
let x = ...; 	// mutable,   local scope
const x = ...; 	// immutable, local scope
```

**`let`** vs **`var`**: **`let`** allows you to declare variables that are limited to the scope of a [block](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block) statement, or expression on which it is used, unlike the [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var) keyword, which declares a variable globally, or locally to an entire function regardless of block scope. The other difference between [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var) and `let` is that the latter is initialized to a value only when a [parser evaluates it (see below)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone).

## IIFE

> immediately invoked function expression

```javascript
function foo() {..}; foo()
( function foo() {..} ) ()
( function() {..} ) ()
( () => {..} ) ()
```

## Alpha Translation

```javascript
const id = x => x
const id = y => y
```

## Beta Reduction

```javascript
( f => x => f(x) ) (id) (1)
(	   x => id(x))		(1)
(			id(1))
(x => x) (1)
1
```

## Eta Reduction

```javascript
x => y => plus (x) (y)
x => 	  plus (x)
		  plus
```

## Examples

`F3` is a proper eta reduction of `F2`

```javascript
const id = x => x;
const konst = x => y => x;

const F1 = x => y => konst (id) (x) (y);
const F2 = x =>      konst (id) (x);
const F3 = 	         konst (id);
```

`a1` is a proper beta expansion of `a2`

```javascript
const id = x => x;

const a1 = y => id(y);
const a2 = y => y;
```

`a2` is a proper beta reduction of `a1`

```javascript
const id = x => x;

const a1 = y => id(y);
const a2 = y => y;
```

`id1` and `id2` are alpha-equivalent

```javascript
const id1 = x => x;
const id2 = y => y;
```

# Week 3 - Lambda

## Atomic Lambda Terms  

```javascript
// atoms
const id = x => x;
const konst = x => y => x;

// derived true, false, and, or, equals, …
const F = …;
const T = …;
```

## Pair, Product Type

```javascript
const pair = x => y => f => f(x)(y);
const fst = p => p(T);
const snd = p => p(F);
```

## Pair encoding

```javascript
const person =
				firstname =>
				lastname =>
				age =>
				pair (pair(firstname)(lastname)) (age);

const firstn = p => fst(fst(p));
const lastn  = p => snd(fst(p));
const age    = p => snd(p);
```

## Either, Co-Product, Sum

```javascript
// dual of the product
const pair = x => y => f => f(x)(y); 	// one ctor
const fst  = p => p(T); 			 	// accessor 1
const snd  = p => p(F);      		 	// accessor 2

// here we have now the basic sum type
const Left   = x => f => g => f(x); 	// ctor 1
const Right  = x => f => g => g(x); 	// ctor 2
const either = e => f => g => e(f)(g); 	// accessor
```

## Special Case: Maybe

```javascript
// go around null / undefined
const Nothing = Left ();
const Just 	  = Right;
const maybe   = either;

maybe (expressionThatMightGoWrong)
	  (handleBad)
	  (handleGood);
```

## Example

```javascript
// error handling with either
const eShow = result => result (msg => msg) (val => "Result is:" + val);
```

# Week 4 - Map/Filter/Reduce

## Map

```javascript
const times = a => b => a * b;

const twoTimes = times(2);

[1, 2, 3].map(x => times(2)(x));
[1, 2, 3].map(times(2));
[1, 2, 3].map(twoTimes);
```

## Filter

```javascript
const odd = x => x % 2 === 1;

[1, 2, 3].filter(x => x % 2 === 1);
[1, 2, 3].filter(x => odd(x));
[1, 2, 3].filter(odd);
```

## Reduce

```javascript
const plus = (accu, cur) => accu + cur;

[1, 2, 3].reduce((accu, cur) => accu + cur);
[1, 2, 3].reduce(plus);

// variant with initial accu value as 2nd argument
// then cur starts at first element
[1, 2, 3].reduce(plus, 0);
```

## Examples

```javascript
// function that checks which numbers in an array are divideable 
// by the given argument
const divides = x => y => y % x === 0;
```

```javascript
// function that joins values of an array together with given argument
const join = (a) => (b, c) => b + a + c;
```

```js
// function that doubles its argument
const twice = (a) => a * 2;
const numbers = [1, 2, 3].map(twice); // yields [2,4,6]
```

# Week 5 - Scripting, PWA, Plotter, Excel

## Why Scripting?

- Command Line
- Automation
- Build System
- Templating
- Code Distribution
- Formulae
- Business Rules
- Smart Configuration
- Product Lines
- DSL
- Self Modifying Code
- much more

## Scripting Characteristics

* Interpreted, not compiled (in principle)
* Lenient type system
* *Best Effort* approach

## Progressive Web App

Loading test suite dynamically :

```javascript
document.write('<script src=...');
```

## Function Plotter: eval

Works as if the code was copied verbatim in the place of the eval. => You share the scope.

```javascript
eval('some code'); // not side effect free!
```

## Function Plotter: Function()

`Function()` is like `eval()` but declares parameters and executes in the global scope. It creates a reference.

```javascript
const add = Function('x', 'y', 'return x+y'); // only evaluated once!
add(1, 2);
add(2, 3); // no need to re-parse
```

## Scripting Caution

*In JavaScript you cannot exclude possibly harmful side effects from scripts that are loaded from foreign sources...*

* **Privacy, Security, Stability**

## Examples

Calculate the bonus with given attributes:

```javascript
const bonusCalculation = x => x.bonus = eval(x.revenue) * factor_;
```

Calculate the bonus with given attributes using Function():

```javascript
const bonusCalculation = Function('x', 'return x.bonus = x.revenue *' + factor_);
```

# Week 6 - Objects

**What are objects?**

* Data structures + methods for access and management (+ a location for mutable state, + abstraction and polymorphism)

## Open & dynamic

* JS Objects

```javascript
const good = {
	firstname : "Good",
	lastname : "Boy",
	getName : function() {
		return this.firstname + " " + this.lastname
	}
};
// no safety but super dynamic
// unobvious how to share structure
// beware of "this"! See Adam Breindl last week.
```

## Closed & explicit

Closure scope, no this.

```javascript
function Person(first, last) {
	let firstname = first; // optional
	let lastname = last;
	return {
		getName: function() {
			return firstname + " " + lastname }
		}
	}
}
// best safety, easy to share structure, but no class
```

## Mixed & classified

Depends on new. Is the default construction.

Still dynamic but all instances can be changed at once by changing the prototype!

```javascript
const Person = ( () => { // lexical scope
	function Person(first, last) { // ctor, binding
		this.firstname = first;
		this.lastname = last;
	}
	Person.prototype.getName = function() {
		return this.firstname + " " + this.lastname;
	};
	return Person;
}) (); // IIFE
// new Person("Good", "Boy") instanceof Person
```

## Prototype

* Classifies objects similar to a type
* Manages shared properties
* Is itself an object
* Can be checked, e.g by instanceof

## New

* Creates a **new** Runtime-Scope
* Calls the **constructor**-Function (cannot be a lambda)
* Sets the prototype  

## Example

Check whether two Arrays are equal:

```javascript
Array.prototype.eq = function(array) {
    if (this.length !== array.length) return false;
    for (let i = 0; i < array.length; i++) {
        if (this[i] !== array[i]) return false;
    }
    return true;
}
```

# Week 07 - Classes

## `class` Keyword

```javascript
class Person {
	constructor(first, last) {
		this.firstname = first;
		this.lastname = last
	}
	getName() {
		return this.firstname + " " + this.lastname
	}
}
// new Person("Good", "Boy") instanceof Person
```

## `extends` Keyword

```javascript
class Student extends Person {
	constructor (first, last, grade) {
		super(first, last); // never forget
		this.grade = grade;
	}
}
const s = new Student("Top","Student", 5.5);
```

## Prototype chain

```javascript
const s = new Student()
// s.__proto__ === Student.prototype;
// Object.getPrototypeOf(s) === Student.prototype;
// => s instanceof Student
```

## Example

Function composition -> it must work for all functions!

```javascript
Function.prototype.then = function(fun) {
    // this(number -> result of the first function 
    // with the value at the end f.e. ..(1))
    const compose = fun => number => fun( this(number) );
    return compose(fun);
}
```

# Week 08 - Moves and User Interfaces

## Compare with Dancing

1. You must learn the moves.
2. Then you can combine the moves and adapt to the situation at hand.

## Recognize Moves

- Become aware what you do.
- We program collaboratively and look for moves.

## Task 1: Improve the Tests

- More structure.
- Better reports when tests fail.
- smooth transition.

## Task 2: Todo List Example

- What is the expected result?
- What is the simplest thing that could possibly work?

## Moves - Your Choice

### 0. Explore

- Technical feasibility, hypotheses, border cases.
- The goal is to learn and verify, delete when finished.
- Give yourself a timebox.

### 1. Start at the End

- Make static *sketch* of the result before adding dynamic features.
- Dynamic sketches: all JS, CSS in a single HTML file.

### 2. Extract

- Replace static values with variables.
- Replace repetitions with mappings and loops.

### 3. Abstract

- Discover the concept behind what you have extracted. Give it a name.
- It should work for itself and in combination.
- Revert if you cannot find one.

### 4. Reorganize

- Organize and re-factor to make your future work easier.
- Facilitate extensions or improvements.
- Prepare for release.

### 5. Release

- The solution must stand on its own without tacit knowledge or external help.
- Tests, documentation, examples.
- Before every push to the Repository.

### 6. Retrospective

- What to keep?
- What to try differently next time?

## Observations

- Balance & distance
- Which technologies support my moves: dynamic exploration, refactoring
- Per feature, per project, whole career, ...

## Example

Failsafe callback:

```javascript
const failSafe = defaultValue => callback => argToCallback => {
    return argToCallback === null ? defaultValue : callback(argToCallback);
}
```

# 9. UI Engineering, MVC

> Frameworks and APIs change fast. Software design principles are evergreen. Learn principles that translate across language barriers.
>
> - Eric Elliot

## Callback - Higher Order Function

Higher-order Function.

```javascript
function test(name, callback) {
	const assert = Assert();		// prework
	callback(assert);				// callback
	report(name, assert.getOk());	// postwork
}
```

## Observable

```javascript
const Observable = value => {
	const listeners = []; // many
	return {
		onChange: callback => listeners.push(callback),
		getValue: () => value,
		setValue: val => {
			if (value === val) return; // protection
			// ordering
            value = val;
			listeners.forEach(notify => notify(val));
		}
	}
};
```

## Red-Green-Refactor

![image-20210426110431979](docs\images\rgrf.png)

Red-Green-Refactor is a basic concept in **Test-driven Development (TDD)** and consists of three stages:

* **RED**: Write unit tests for whatever it is you want to code
* **GREEN**: Write a minimal implementation such that the unit tests all pass
* **REFACTOR**: Refactor the basic implementation and test again, making sure that all tests are still passing

## MVC

![MVC Bild](docs\images\mvc.PNG)

## Example

Using Observable that it keeps track of the sum of all values:

```javascript
trackable.onChange( _ => sum += trackable.getValue());
```

# 10. Async Programming

![image-async](docs\images\async.png)

## Testing

```javascript
test("todo-memory-leak", assert => {
	const todoController = TodoController();

    todoController.onTodoAdd(todo => {
		todoController.onTodoRemove( (todo, removeMe) => {
			removeMe(); // idea: self remove
		});
	});

    for (let i=0; i<10000; i++){
		const todo = todoController.addTodo();
		todoController.removeTodo(todo);
	}
});
```

## Callback, Events

```javascript
function start() {
	//...
	window.onkeydown = evt => {
		// doSomething();
	};
	setInterval(() => {
		// doSomething();
	}, 1000 / 5);
}
```

## Promise

Most prominent use:

```javascript
fetch ('http://fhnw.ch/json/students/list')
.then(response => response.json())
.then(students => console.log(students.length))
.catch (err => console.log(err)
```

Success / Failure callbacks:

```javascript
// definition
const processEven = i => new Promise( (resolve, reject) => {
	if (i % 2 === 0) {
		resolve(i);
	} else {
		reject(i);
	}
});

// use
processEven(4)
.then ( it => {console.log(it); return it} ) // auto promotion
.then ( it => processEven(it+1))
.catch( err => console.log( "Error: " + err))
```

## Async / Await

```javascript
const foo = async i => {
	const x = await processEven(i).catch( err => err);
	console.log("foo: " + x);
};
foo(4);
```

Other variant:

```javascript
async function foo(i) {
	try {
		const x = await processEven(i);
		console.log("foo: " + x);
	}
	catch(err) { console.log(err); }
};
foo(4);
```

## Example

A NullSafe construction in the style of a `Promise`:

```javascript
const NullSafe = x => {
    const isNullSafe = y => y && y.then;
    const maywrap = y => isNullSafe(y) ? y : NullSafe(y);
    return {
        then: fn => (x !== null && x != undefined)
        			? maywrap(fn(x)) 
        			: NullSafe(x)
    }
};
```
