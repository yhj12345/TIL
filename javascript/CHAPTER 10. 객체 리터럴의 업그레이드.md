## CHAPTER 10. 객체 리터럴의 업그레이드

#### 10.1 변수를 키와 값으로 하는 객체 만들기

```javascript
const name = "Alberto";
const surname = "Montalesi";
const age = 25;
const nationality = "Italian";

// 일반적인 객체 리터럴 만들기
const person = {
    name: name.
    surname: surname,
    age: age,
    nationality: nationality,
};

// ES6에서
const person = {
    name,
    surname,
    age,
    nationality
}
```



#### 10.2 객체에 함수 추가하기

```javascript
const person = {
    name: "Alberto",
    greet: function() {
        console.log("Hello");
    },
};

person.greet(); // Hello

// ES6에서
const person = {
    name: "Alberto",
    greet() {
        console.log("Hello");
    },
};

person.greet(); // Hello
```



#### 10.3 객체의 속성을 동적으로 정의하기

```javascript
// ES5에서 객체의 속성을 동적으로 정의하는 방법
var name = "myname";
var person = {};
person[name] = "Alberto";
console.log(person.myname); // Alberto

// ES6에서
const name = "myname";
const person = {
    [name]: "Alberto",
};
console.log(person.myname); // Alberto
```

