## CHAPTER 04. 템플릿 리터럴

#### 4.1 문자열 삽입

```javascript
// ES5에서의 문자열 삽입 코드
var name = "Alberto"
var greeting = 'hello my name is ' + name;
console.log(greeting); // hello my name is Alberto

// ES6에서의 문자열 삽입 코드
let name = "Alberto"
const greeting = `Hello my name is ${name}`
console.log(greeting) // Hello my name is Alberto
```



#### 4.2 표현식 삽입

```javascript
// ES5에서의 표현식 삽입 코드
var a = 1;
var b = 10;
console.log('1 * 10 is ' + (a * b)) // 1 * 10 is 10

// ES6에서의 표현식 삽입 코드
var a = 1;
var b = 10;
console.log(`1 * 10 is ${a * b}`) // 1 * 10 is 10
```



#### 4.3 여러 줄 문자열 생성

```javascript
// ES5에서의 HTML 프래그먼트 등에 사용할 여러 줄로 이뤄진 문자열
// 행마다 백슬래쉬를 삽입
var text = "hello, \
my name is Alberto \
how are you?\ ";

// ES6에서의 여러 줄로 이뤄진 문자열
const content = `hello,
my name is Alberto
how are you?`;
```



#### 4.4 중첩 템플릿

```javascript
const people = [{
    	name: 'Alberto',
      	age: 27,
	}, {
      	name: 'Caroline',
      	age: 27,
  	}, {
     	 name: 'josh',
      	age: 31,
  	}
];

const markup = `
<ul>
  ${people.map(person => `<li> ${person.name}</li>`)}
</ul>
`;
console.log(markup);
// <ul>
//   <li> Alberto</li>, <li> Caroline</li>,<li> Josh</li>
// <ul>
```



#### 4.5 삼항 연산자 추가하기

```javascript
const isDiscounted = false;

function getPrice() {
    console.log(isDiscounted ? "$10" : "$20");
}

getPrice(); // $20

// name, age와 함께 artist를 생성
const artist = {
    name: "Bon Jovi",
    age: 56
};

// artist 객체에 song 프로퍼티가 있을 때만 문장에 추가하고,
// 없으면 아무것도 반환하지 않음
const text = `
	<div>
		<p> ${artist.name} is ${artist.age} years old ${artist.song ? `and wrote the song ${artist.song}` : ''}
		</p>
	</div>
`;
// <div>
//   <p> Bon Jovi is 56 yearts old
//   </p>
// </div>

const artist = {
    name: "Trent Reznor",
    age: 53,
    song: 'Hurt',
};
// <div>
//   <p> Trent Reznor is 53 years old and wrote the song Hurt
//   </p>
// </div>
```



#### 4.6 템플릿 리터럴에 함수 전달하기

```javascript
const groceries = {
    meat: "pork chop",
    veggie: "salad",
    fruit: "apple",
    others: ['mushrooms', 'instant noodles', 'instant soup'],
};

// groceries의 각 값에 대해 map()을 수행하는 함수
function groceryList(others) {
    return `
    	<p>
    		${others.map(other => `<span>${other}			</span>`).join('\n')}
    	</p>
    `;
}

// p태그 내 모든 groceries를 출력. 마지막은 **others** 배열의 모든 원소를 포함
const markup = `
	<div>
		<p>${groceries.meat}</p>
		<p>${groceries.veggie}</p>
		<p>${groceries.fruit}</p>
		<p>${groceryList(groceries.others)}</p>
	</div>
`;
// <div>
//   <p>pork chop</p>
//   <p>salad</p>
//   <p>apple</p>
//   <p>
//     <span>mushrooms</span>
//     <span>instant noodles</span>
//     <span>instant soup</span>
//	 </p>
// </div>
```



#### 4.7 태그된 템플릿 리터럴

```javascript
let person = "Alberto";
let age = 25;

function myTag(strings, personName, personAge) {
    // strings: ["That ", " is a ", "!"]
    let str = strings[1]; // " is a "
    let ageStr;
    
    personAge > 50 ? ageStr = "grandpa" : ageStr = "youngster";
    
    return personName + str + ageStr;
}

let sentence = myTag`That ${person} is a ${age}!`;
console.log(sentence) // Alberto is a youngster
```

