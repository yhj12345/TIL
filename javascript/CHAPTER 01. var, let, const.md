## CHAPTER 01. var, let, const

#### 1.1 var, let, const의 차이

##### var

```
var 키워드로 선언된 변수는 함수 스코프에 종속
for 루프 내에서 var 키워드로 변수를 선언하면 밖에서도 사용 가능
```

##### let

```
let 키워드로 선언된 변수는 블록 스코프로 종속
```

##### const

```
let과 마찬가지로 블록에 종속되지만 차이점은 재할당을 통해 값이 변경될 수 없고 다시 선언될수도 없다
```

##### const에 객체가 담겼다면?

```javascript
const person = {
    name: 'Alberto',
    age: 25,
};

person.age = 26;
console.log(person.age); // 26 
// -> 속성 중 하나만 재할당하는 것이므로 문제 x

Object.freeze(person);
person.age = 30;
console.log(person.age); // 26
// -> 객체의 내용을 변경할 수 없게 고정시킬 수 있지만 
// 바꿀려고 시도해도 오류를 반환해주지는 않는다
```

#### 1.2 TDZ(temporal dead zone, 일시적 비활성 구역)

```javascript
console.log(i); // undefined
var i = "I am a variable" 

console.log(j); // ReferenceError
let j = "I am a let"

// -> var는 정의되기 전에 접근 가능 but, let과 const는 불가능
// var, let, const 모두 호이스팅의 대상이 되지만, var는 정의되기전에 undefined 값을 가지게 되지만 let은 변수가 선언될 때까지 일시적으로 TDZ에 있게 된다. 따라서 초기화 전에 변수에 접근하면 오류가 발생한다.
```

#### 1.3 var, let, const를 적재적소에 쓰는법

```
정답은 없다.
1번 의견
- 기본적으로 const를 사용하자.
- 재할당이 필요한 경우에만 let을 사용하자.
- var는 ES6에서 절대 사용하지 않는다.

2번 의견
- 여러 큰 스코프에서 공유하기 위한 최상위 변수에는 var를 사용한다.
- 작은 스코프의 로컬 변수에는 let을 사용한다.
- 코드 작성이 어느 정도 진행된 후에만 let을 const로 리팩토링한다. 변수 재할당을 막아야 하는 경우라는 것이 확실해야 한다.

-> 나는 1번 의견으로 사용
```
