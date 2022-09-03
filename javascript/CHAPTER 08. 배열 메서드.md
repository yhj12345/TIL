## CHAPTER 08. 배열 메서드

#### 8.1 Array.from()

배열처럼 보이지만 배열이 아닌 객체를 받아서 실제 배열로 변환해 반환

```html
// HTML
<div class="fruits">
  <p> Apple </p>
  <p> Banana </p>
  <p> Banana </p>
</div>
```

```javascript
const fruits = document.querySelectorAll(".fruits p");
// fruits는 3개의 p 태그를 포함한 노드 리스트(배열과 비슷한 구조)이다.
// 이제 fruits를 반환하자 
const fruitArray = Array.from(fruits);
console.log(fruitArray); // [p, p, p]

// 이제 배열로 취급하므로 map()을 사용할 수 있다.
const fruitNames = fruitArray.map(fruit => fruit.textContent);
console.log(fruitNames); // ["Apple", "Banana", "Orange"]

// 다음과 같이 단순화도 가능
const fruitArray = Array.from(document.querySelectorAll(".fruits p"));
const fruitNames = fruitArray.map(fruit => fruit.textContent);
console.log(fruitNames); // ["Apple", "Banana", "Orange"]

// 두번째 인자 활용
const fruits = document.querySelectorAll(".fruits p");
const fruitArray = fruitArray.map(fruits, fruit => {
	console.log(fruit);
    // <p> Apple </p>
    // <p> Banana </p>
    // <p> Orange </p>
    return fruit.textContent;
});
console.log(fruitArray); // ["Apple", "Banana", "Orange"]
```



#### 8.2 Array.of()

```javascript
// 전달받은 모든 인수로 배열을 생성
const digits = Array.of(1, 2, 3, 4 ,5);
console.log(digits); // [1, 2, 3, 4 ,5]
```



#### 8.3 Array.find()

```javascript
// 제공된 테스트 함수를 충족하는 배열의 첫번째 원소를 반환 
// 없을 시, undefined 반환
const array = [1, 2, 3, 4, 5];

// 배열의 원소 중 3보다 큰 첫 원소를 반환한다
let found = array.find(e => e > 3);
console.log(found); // 4
```



#### 8.4 Array.findIndex()

```javascript
// 조건과 일치하는 첫 번째 원소의 인덱스를 반환
const greetings = ["hello", "hi", "byebye", "goodbye", "hi"];

let foundIndex = greetings.findIndex(e => e === "hi");
console.log(foundIndex); // 1
```



#### 8.5 Array.some()과 Array.every()

```javascript
// .some()은 조건과 일치하는 원소가 있는지 검색 첫번째 일치하는 원소 찾으면 중지
// .every()는 모든 원소가 주어진 조건과 일치하는지 확인
const array = [1, 2, 3, 4, 5 ,6, 1, 2, 3, 1];

let arraySome = array.some(e => e > 2);
console.log(arraySome); // true

let arrayEvery = array.every(e => e > 2);
console.log(arrayEvery); // false
```

