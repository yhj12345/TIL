## CHAPTER 02. 화살표 함수

#### 2.1 화살표 함수

```javascript
// ES5에서 일반적으로 함수를 선언하는 방법
const greeting = function(name) {
    return "hello" + name;
};

// 화살표 함수
var greeting = (name) => {
    return `hello ${name}`;
};

// 매개변수가 하나일 때 괄호도 생략 가능
var greeting = name => {
    return `hello ${name}`;
};

// 매개변수가 없다면 빈 괄호
var greeting = () => {
    return "hello";
};
```



#### 2.2 암시적 반환

```javascript
// 화살표 함수에서는 명시적인 반환을 생략하고 다음과 같이 반환 가능
const greeting = name => `hello ${name}`;

// -> 간결하고 좋지만 가독성이 좋아야한다.
// 만약 같이 하는 팀원이 있다면, 그 팀원이 이 문법에 익숙하지 않다면 조금은 풀어쓰는게 나을 수도 있다.

// 객체 리터럴을 암시적으로 반환해야 한다면
const race = "100m dash";
const runners = ["Usain Bolt", "Justin Gatlin", "Asafa Powell"];

const results = 
      runners.map((runner, i) => ({name: runner, race, place: i+1}));
console.log(results);
```



#### 2.3 화살표 함수는 익명 함수

```javascript
// 참조할 이름이 필요하다면 함수를 변수에 할당
const greeting = name => `hello ${name}`;

greeting("Tom");
```



#### 2.4 화살표 함수와 this 키워드

```
화살표 함수를 사용할 때 this 키워드는 상위 스코프에 상속
```



#### 2.5 화살표 함수를 피해야 하는 경우

```javascript
// 여기서 this는 Window 객체를 가리킴
const button = document.querySelector("btn");
button.addEventListener("click", () => {
    this.classList.toggle("on")
});

// 이번 예시도 마찬가지
const person1 = {
    age: 10,
    grow: function {
    	this.age++;
    	console.log(this.age);
	},
};

person1.grow(); // 11

const person2 = {
    age: 10,
    grow: () => {
        this.age++;  // -> 여기서 에러
        console.log(this.age);
    },
};

person2.grow();

// 피해야하는 경우 2
// 일반 함수
function example() {
    console.log(arguments[0]);
};

example(1, 2, 3); // 1

const showWinner = function() {
    const winner = arguments[0];
    console.log(`${winner} was the winner`);
};

showWinner("Usain Bolt", "Justin Gatlin", "Asafa Powell") // Usain Bolt was the winner

// 화살표 함수 사용 틀린 예
const showWinner = () => {
    const winner = arguments[0];
    console.log(`${winner} was the winner`);
};

showWinner("Usain bolt", "Justin Gatlin", "Asafa Powell") // ReferenceError: arguments is not defined

// 화살표 함수 사용 맞는 예
const showWinner = (...args) => {
    const winner = args[0];
    console.log(`${winner} was the winner`);
};

showWinner("Usain Bolt", "Justin Gatlin", "Asafa Powell") // Usain Bolt was the winner
```

