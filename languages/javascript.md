# Javascript

## Unique to Javascript

* Javascript supports automatic type conversion.
* Variable typing is allowed. This just means you can change the type of a variable at runtime.
* You can use concatenation and mathematical operations within the same line of code.
* Anonymous functions are functions that don't have a name assigned to them.  They are inaccessible after declaration.

```javascript
3 + 5 = "7" // 3 + 5 = 8, 8 + "7" = 87
```

* All variables within javascript are objects.
* Strict mode can be used to solve some unsafe operations that javascript allows. This can be done with "use strict"; This can be used at any scope. If you put it within the scope of a function, it only runs within the function.

## Data Types

 * number
 * boolean
 * string
 * object
 * undefined

 ### Reference Types vs. Primitive Types

 * THere are two types of datatypes within javascript. Primitive types are simple types like number and boolean. Reference types are strings, objects.

### Undeclared vs. Undefined

* Undeclared is a variable that has not yet been set in the program. Undefined just means that the value has not been given a value. null is a value that must be explicitely set within the program. It is of type object.

## First Class Functions and Nested Functions

* All functions in javascript are firt class objects, meaning that they can be passed to other functions, assigned as variables, etc.

## Operators

### === vs. ==

* Triple equals is not only for checking equality, but for checking type. Double equals just does equality check regardless of type. For example,
``` javascript
'0' == 0 // true
'0' === 0 // false
null == undefined // true
null === undefined // false
```
* You should almost always use '==='. This way you are never comparing cross types. This is also only for comparing primitive types.

## Prototypes (Inheritance within Javascript)

### ES5 Way

* Defining a class:
```javascript
function Bird(type, color) {
    this.type = type;
    this.color = color;
    this.eggs = 0;

    this.talk = function() {
        this.eggs++;
        console.log('${this.type} ${this.color} said, chirp chirp!')
    }
}

// alternative preferred way. This way, a new function isn't created for every object instantiation.
Bird.prototype.talk = function() { /* do something */ }
```
* Inheritance
```javascript
function Parrot(type, color) {
    // parent constructor call
    Bird.call(this, type, color); 
    // method override
    this.talk = function() {
        console.log('${this.type} ${this.color} said, hello because Im a parrot!')
    }
}

Parrot.prototype = Object.create(Bird.prototype);
Parrot.prototype.constructor = Parrot;

var parakeet = new Parrot('parakeet', 'red');
```

### ES6 Way 

* ES6 defined new and simpler ways that reflect other languages better pertaining to object-oriented programming. It is still using prototypes under the hood.
```javascript
class Bird {
    constructor(type, color) {
        this.type = type;
        this.color = color;
    }
    talk() { ... }
}

class Parrot extends Bird {
    constructor(type, color) {
        super(type, color);

        // this MUST be used AFTER calling super within the constructor.
        this.color = 'yellow';
    }

    talk() {
        super.talk();
    }

    // you can also declare static classes
    static create(type, color) { ... }

    // new getters and setters in es6
    get type() {
        return this.type;
    }

    get color() {
        return this.color;
    }
}

let parakeet = new Parrot('parakeet', 'green');
parakeet.color = 'purple' // setter changed value

```

## DOM Manipulation

```javascript
// Creates an empty element p to the <body>
var p = document.createElement("p");
// create text node
var textNode = document.createTextNode(" This is a new text node");
// append text node to p
p.appendChild(textNode);
// append p to #pid
document.getElementById("pid").appendChild(newP); 
```

### Modifying CSS
```javascript
document.getElementById('eId').style.fontSize = "20px"
// or
document.getElementById('eId').className = 'className'
```

## Strings and Lists

* character at a String
```
s.charAt(pos)
```

## Closures

* A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

## Mutability

* A mutable object is an object that can be modified. Strings and numbers are immutable. Objects are mutable.