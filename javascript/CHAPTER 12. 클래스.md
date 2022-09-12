## CHAPTER 12. 클래스

클래스는 일차적으로 자바스크립트의 기존 프로토타입 기반 상속에 대한 문법적 설탕이다. 클래스 문법이 자바스크립에 새로운 객체 지향 상속 모델을 도입하는 것은 아니다.

```javascript
// 프로토타입 상속
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    console.log("Hello, my name is " + this.name); 
}

const alberto = new Person("Alberto", 26);
const caroline = new Pesron("Caroline", 26);

alberto.greet(); // Hello, my name is Alberto
caroline.greet(); // Hello, my name is Caroline
```



#### 12.1 클래스 생성

```javascript
// 클래스 선언
class Person {

}

// 클래스 표현식
const person = class Person {
};
```

```javascript
class Peson {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old`)
    } // 메서드와 메서드 사이에는 쉼표가 없음
    farewell() {
        console.log("goodbye friend");
    }
}

const alberto = new Peson("Alberto", 26);

alberto.greet(); // Hi, my name is Alberto and I'm 26 years old
alberto.farewell(); // goodbye friend
```



#### 12.2 정적 메서드

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
}
    static info() {
        console.log("I am Person class, nice to meet you");
    }
}
const alberto = new Person("Alberto", 26);

alberto.info(); // TypeError
Person.info(); // I am Person class, nice to meet you
```



#### 12.3 set와 get

```javascript
class Person {
    constructor(name, surname) {
        this.name = name;
        this.surname = surname;
        this.nickname = "";
	}
    set nicknames(value) {
        this.nickname = value;
        console.log(this.nickname);
    }
    get nicknames() {
        console.log(`your nickname is ${this.nickname}`);
    }
}

const alberto = new Person("Alberto", "Montalesi");

// 세터를 호출
alberto.nicknames = "Albi"; // "Albi"

// 게터를 호출
alberto.nicknames; // "Your nickname is Albi"
```



#### 12.4 클래스 상속하기

```javascript
// 기존 클래스
class Peson {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log(`Hi, my name is ${this.name} and I'm ${this.age} years old`)
    }
}

// 상속을 통해 만든 새 클래스
class Adult extends Person {
    constructor(name, age, work) {
        this.name = name;
        this.age = age;
        this.work = work;
    }
}

const alberto = new Adult("Alberto", 26, "software developer")
// ReferenceError

// super()를 호출하여 Person을 만들고 Adult를 만들어야함
class Adult extends Person {
    constructor(name, age, work) {
        super(name, age);
        this.work = work;
    }
}

const alberto = new Adult("Alberto", 26, "software developer");

console.log(alberto.age); // 26
console.log(alberto.work); // software developer
alberto.greet(); // Hi, my name is Alberto and I'm 26 years old
```



#### 12.5 배열 확장하기

```javascript
class Classroom extends Array {
    // 레스트 연산자를 사용해 가변 인수로 입력받은 학생들의 정보를
    // 배열 형태로 students에 할당
    constructor(name, ...students) {
        // 스프레드 연산자를 사용해 배열 원소들을 다시 풀어헤쳐 생성자를 호출한다.
        // 스프레드 연산자를 사용하지 않으면
        // '학생들의 정보가 들어 있는 배열'을 원소로 가진 Array가 생성
        super(...students);
        this.name = name;
    }
    // 학생들을 추가하기 위한 새로운 메서드를 추가
    add(student) {
        this.push(student);
    }
}

const myClass = new Classroom('1A',
	{name: "Tim", mark: 6},	
    {name: "Tom", mark: 3},	
    {name: "Jim", mark: 8},
    {name: "Jon", mark: 10},                             
)

// 새로운 학생 추가
myClass.add({name: "Timmy", mark: 7});
myClass[4]; // {name: "Timmy", mark: 7}

// for of 루프를 사용하여 반복 가능
for (const studunt of myClass) {
    console.log(student);
}
```

