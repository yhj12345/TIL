## CHAPTER 07. 루프

#### 7.1 for of 루프

```javascript
// 배열에 대한 반복
var fruits = ['apple', 'banana', 'orange'];
for (var i=0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// 동일한 결과
var fruits = ['apple', 'banana', 'orange'];
for (const fruit of fruits) {
    console.log(fruit);
}
// apple
// banana
// orange

// 객체에 대한 반복(객체는 iterable이 아니다.)
const car = {
    maker: "BMW",
    color: "red",
    year: "2010",
};

for (const prop of Object.keys(car)) {
    const value = car[prop];
    console.log(prop, value);
}
// maker BMW
// color red
// year 2010
```



#### 7.2 for in 루프

```javascript
const car = {
    maker: "BMW",
    color: "red",
    year: "2010",
};

for (const prop in car) {
    console.log(prop, car[prop]);
}
// maker BMW
// color red
// year 2010
```



#### 7.3 for of와 for in의 차이

```javascript
let list = [4, 5, 6];

// for ...in은 키의 목록을 반환한다.
for (let i in list) {
    console.log(i); // "0", "1", "2"
} 

// for ...of는 값을 반환한다.
for (let i of list) {
    console.log(i); // 4, 5, 6
}
```



