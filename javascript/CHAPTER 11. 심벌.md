## CHAPTER 11. 심벌

#### 11.1 심벌의 고유성

심벌은 항상 고유하며 객체 속성의 식별자로 사용할 수 있다.

```javascript
const me = Symbol("Alberto");
console.log(me); // Symbol(Alberto)

const clone = Symbol("Alberto");
console.log(clone); // Symbol(Alberto)

console.log(me == clone); // false
console.log(me === clone); // false

// 두 심벌의 값은 동일하지만, 각 심벌은 항상 고유하므로 다른 심벌과 겹치지 않는다.
```



#### 11.2 객체 속성에 대한 식별자

```javascript
const office = {
    "Tom": "CEO",
    "Mark": "CIO",
    "Mark": "CIO",
};

for (person in office) {
    console.log(person);
}
// Tom
// Mark
// -> 이름이 같기 때문에 3명이지만 2명만 나옴

const office = {
    [Symbol("Tom")]: "CEO",
    [Symbol("Mark")]: "CIO",
    [Symbol("Mark")]: "CIO",
};

for (person in office) {
    console.log(person);
}
// undefined

// -> 심벌은 열거 가능하지 않기 때문에 for ... in으로는 반복할 수 없다.

// -> 배열을 만든 후 맵으로 반복해야한다.
const symbols = Object.getOwnPropertySymbols(office);
const value = symbols.map(symbol => office[symbol]);
console.log(value);
// 0: "CEO"
// 1: "CIO"
// 2: "CIO"
```

