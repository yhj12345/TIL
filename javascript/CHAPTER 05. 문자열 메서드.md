## CHAPTER 05. 문자열 메서드

#### 5.1 기본적인 문자열 메서드

```javascript
// indexOf()
const str = "this is a short sentence";
str.indexOf("short"); // 출력: 10

// slice()
const str = "pizza, orange, cereals";
str.slice(0, 5); // 출력: "pizza"

// toUpperCase()
const str = "i ate an apple";
str.toUpperCase(); // 출력: "I ATE AN APPLE"

// toLowerCase()
const str = "I ATE AN APPLE"
str.toLowerCase(); // 출력: "i ate an apple"
```



#### 5.2 새로운 문자열 메서드

```javascript
// ES6의 새로운 문자열 메서드
// startsWith() -> 매개변수로 받은 값으로 시작하는지 확인
const code = "ABCDEFG";
code.startsWith("ABB"); // false
code.startsWith("abc"); // false 대소문자 구별함
code.startsWith("ABC"); // true

// 검사 시작점을 지정 가능
const code = "ABCDEFGHI";
code.startsWith("DEF", 3) // true, 3개의 문자를 지나 검사 시작

// endsWith()
const code = "ABCDEF";
code.endsWith("DDD") // false
code.endsWith("def") // false, 대소문자 구별함
code.endsWith("DEF") // true

// 얼만큼 확인할지 전달 가능
const code = "ABCDEFGHI";
code.endsWith("EF", 6) // true, 첫 6개 문자인 ABCDEF만을 고려

// includes() -> 포함되어 있는지 확인
const code = "ABCDEF";
code.includes("ABB"); // false
code.includes("abc"); // false, 대소문자 구별함
code.includes("CDE"); // true

// repeat() -> 반복해줌
let hello = "Hi";
console.log(hello.repeat(10)); // HIHIHIHIHIHIHIHIHIHI
```