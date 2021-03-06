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