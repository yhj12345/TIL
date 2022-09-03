## CHAPTER 09. 스프레드 연산자와 레스트 매개변수

#### 9.1 스프레드 연산자

MDN - 스프레드 문법을 사용하면 0개 이상의 인수(함수 호출용) 또는 원소(배열 리터럴용)가 예상되는 위치에서 배열  표현식 또는 문자열과 같은 이터러블 항목을 확장하거나 0개 이상의 키/값 쌍(객체 리터럴용)이 예상되는 위체에서 객체 표현식을 확장할 수 있다.

##### 배열의 결합

```javascript
const veggie = ["tomato", "cucumber", "beans"];
const meat = ["pork", "beef", "chicken"];

const menu = [...veggie, "pasta", ...meat];
console.log(menu);
// ["tomato", "cucumber", "beans", "pasta", "pork", "beef", "chicken"]
```

##### 배열의 복사

```javascript
// 같은걸 참조하므로 제대로 복사가 안됨
const veggie = ["tomato", "cucumber", "beans"];
const newVeggie = veggie;
veggie.push("peas");
console.log(veggie); // ["tomato", "cucumber", "beans", "peas"]
console.log(newVeggie); // ["tomato", "cucumber", "beans", "peas"]

// ES5 이전의 복사
const veggie = ["tomato", "cucumber", "beans"];
const newVeggie = [].concat(veggie);
veggie.push("peas");
console.log(veggie); // ["tomato", "cucumber", "beans", "peas"]
console.log(newVeggie); // ["tomato", "cucumber", "beans"]

// 스프레드 문법 사용시
const veggie = ["tomato", "cucumber", "beans"];
const newVeggie = [...veggie];
veggie.push("peas");
console.log(veggie); // ["tomato", "cucumber", "beans", "peas"]
console.log(newVeggie); // ["tomato", "cucumber", "beans"]
```

##### 함수와 스프레드 연산자

```javascript
// 기존 방식
function doStuff (x, y, z) {
    console.log(x + y + z);
}
var args = [0, 1, 2];

// 함수 호출, 인수 전달
doStuff.apply(null, args);

// 스프레드 문법 사용
doStuff(...args); // 3 (0 + 1 + 2)
console.log(args); // [0, 1, 2]

// 다른 예
const name = ["Alberto", "Montalesi"];

function greet(first, last) {
    console.log(`hello ${first} ${last}`);
}
greet(...name) // hello Alberto Montalesi

// 저장한 인수보다 더 많은 값을 제공한다면?
const name = ["Jon", "Paul", "Jones"];

function greet(first, last) {
    console.log(`hello ${first} ${last}`)
}
greet(...name); // hello Jon Paul
// -> 마지막 인수 제외
```

##### 객체 리터럴과 스프레드(ES2018)

```javascript
let person = {
    name: "Alberto",
    surname: "Montalesi",
    age: 25,
};
let clone = {...person};
```



#### 9.2 레스트 매개변수

레스트 문법은 점 3개로 스프레드 문법과 똑같지만 기능적으로는 그 반대이다. 스프레드는 확장 레스트는 압축이다.

```javascript
const runners = ["Tom", "Paul", "Mark", "Luke"];
const [first, second, ...losers] = runners;

console.log(...losers); // Mark Luke
```

