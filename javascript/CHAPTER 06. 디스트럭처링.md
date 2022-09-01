## CHAPTER 06. 디스트럭처링

#### 6.1 객체 디스트럭처링

```javascript
var person = {
    first: "Alberto",
    last: "Montalesi",
};

var first = person.first;
var last = person.last;

// ES6 이후
const person = {
    first: "Alberto",
    last: "Montalesi",
};

const { first, last } = person;

// 중첩된 경우
const person = {
    name: "Alberto",
    last: "Montalesi",
    links: {
        social: {
            facebook: "https://www.facebook.com/alberto.mon",
        },
        website: "https://albertomo.github.io"
    },
};

const { facebook } = person.links.social;

// 변수 이름 바꾸기
const { facebook: fb} = person.links.social;
console.log(fb) // https://www.facebook.com/alberto.mon
console.log(facebook) // ReferenceError:

// 기본값 설정
const { facebook: fb = "https://www.facebook.com"} = person.links.social;
```



#### 6.2 배열 디스트럭처링

```javascript
const person = ["Alberto", "Montalesi", 25]
const [name, surname, age] = person;

// 변수의 수가 배열의 원소보다 적다면
const person = ["Alberto", "Montalesi", 25]
const [name, surname] = person;
// 25는 어떤 변수에도 할당되지 않는다.
console.log(name, surname) // Alberto, Montelesi

// 나머지 모든 값을 얻고 싶을 때
const person = ["Alberto", "Montalesi", "pizza", "ice cream", "cheeze cake"];
const [name, surname, ...food] = person;
console.log(food); // ["pizza", "ice cream", "cheeze cake"]
```



#### 6.3 디스트럭처링을 이용하여 변수 교체하기

```javascript
let hungry = "yes";
let full = "no";
// 식후에는 배고프지 않고 배부를 것이다. 값을 교체하자

[hungry, full] = [full, hungry];
console.log(hungry, full); // no yes
```