---
title: JavaScript Toolbox
author: Kevin Buman
website: https://github.com/McSquanchy/webpr-fs21-toolbox
logo: images/javascript.svg
---

# Functions

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

# Canvas

```javascript
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
context.fillStyle = "black";
context.fillRect(0, 0, canvas.width, canvas.height);
```

# Key Events

```javascript
const rightArrow = 39;
const leftArrow = 37;
window.onkeydown = evt => {
(evt.keyCode === rightArrow) ? ... : ...;
};
```

# Game Loop

```javascript
setInterval( () => {
    nextBoard();
    display(context);
}, 1000 / 5);
```

# Resources

* Gabriel Lebec, [Fundamentals of Lambda Calculus & Functional Programming in JavaScript](https://www.youtube.com/watch?v=3VQ382QG-y4)