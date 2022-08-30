## CHAPTER 0. 자바스크립트 기초

#### 0.1. 변수

```
- var : 재할당 o
- let : 재할당 o 
- const : 재할당 x

-> 값을 재할당해야 할 상황이 아니라면 항상 const를 사용하도록 하자
-> 실수로 재할당을 하려했을 때 오류를 바로 발견 가능
-> 재할당이 필요하다면 그 때 const를 let으로만 바꿔주면 된다.
```



##### 변수 명명법

```javascript
// 변수명은 숫자로 시작할 수 없음
let 1apple = "one apple" // x

// 변수명에는 공백, 기호, 마침표가 들어갈 수 없음
let hello! = "hello" // x

// 예약어는 사용할 수 없다
// ex) try, void, do, const, await 등등...

// 변수 이름 자체가 변수를 설명할 수 있는 방식으로 짓자
// 두문자어, 약어, 의미없는 이름 사용 자제
// 나쁜 예
let cid = 12; // cid가 뭐지...???
// 좋은 예
let clientId = 12; // 아, 클라이언트 ID구나

// 카멜케이스 아니면 스네이크케이스 둘 중 상관은 없지만 일관성있게 사용
```



#### 0.2. 자료형

##### 원시 자료형 

-> 객체가 아닌 자료형, 메서드를 가지지 않는다

```
- string: 문자열
- number: 숫자
- boolean: 불린
- null: 널 (값이 없음)
- undefined: 정의되지 않음 (정의되지 않은 값)
- symbol: 심벌 (고유하고 변경할 수 없는 값, ES6에서 추가되었다.)
```



##### 객체(object)

-> 여러 속성의 모음을 저장하는 데 사용할 수 있다.

```javascript
const car = {
    wheels: 4,
    color: 'red',
    drive: () => {
        console.log("vroom vroom")
    },
};
console.log(Object.keys(car)[0]); // whells
console.log(typeof Object.keys(car)[0];) // string
car.drive(); // vroom vroom
```



##### 빈 객체 생성하기

```javascript
// 객체 생성
const car = new Object();
const car = {}; // 일반적으로 사용(객체 리터럴)

// 속성 추가(점 표기법)
car.color = 'red';

// 속성 접근
const car = {
    wheels: 4,
    color: "red",
    "goes fast": true
};
console.log(car.wheels); // 4(점 표기법, 여러 단어로 이뤄진 속성은 사용불가)
console.log(car['color']); // red(대괄호 표기법)
```



##### 객체의 복사

```javascript
let car = {
    color: 'red',
};
let secondCar = car; // 참조(주소)를 복사(얕은복사)

car.wheels = 4;
console.log(car); // {color: 'red', wheels: 4}
console.log(secondCar); // {color: 'red', wheels: 4}

console.log(car == secondCar); // true
console.log(car === secondCar); // true

// 주소가 다르면 다르다
const emptyObj1 = {};
const emptyObj2 = {};
console.log(emptyObj1 == emptyObj2) // false
console.log(emptyObj1 === emptyObj2) // false

// 깊은 복사
const car = {
    color: 'red',
};
const secondCar = Object.assign({}, car);
car.wheels = 4;
console.log(car) // {color: 'red', wheels: 4}
console.log(secondCar) // {color: 'red'}
```



##### 배열

-> 순서대로 값을 저장하는 객체

```javascript
const fruitBasket = ['apple', 'banana', 'orange']
// 인덱스로 속성 접근
console.log(fruitBasket[0]) // apple
```



#### 0.3. 함수

```javascript
// 기본형
fuction greet(name) {
    console.log("hello " + name);
}
greet("Alberto");

// 함수 표현식
const greeter = function greet(name) {
    console.log("hello " + name)
};
greeter("Alberto");

// 익명 함수
const greeter = function(name) {
    console.log("hello " + name)
};
greeter("Alberto");

// 화살표 함수
const greeter = (name) => {
    console.log("hello " + name)
};
greeter("Alberto");
```



#### 0.4. 함수 스코프와 this 키워드의 이해

##### 스코프

```
- 전역 스코프 : 어느곳에서나 접근 가능
- 블록 스코프 : 변수가 선언된 블록 내부에서만 접근 가능

블록 : 함수, 루프, 중괄호로 구분되는 모든 영역 
```



##### this 키워드

```javascript

```

















