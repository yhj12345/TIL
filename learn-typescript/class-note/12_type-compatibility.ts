// 인터페이스
interface Developer {
  name: string;
  skill: string;
}

interface Person {
  name: string;
}

var developer: Developer;
var person: Person;
// developer = person
// person = developer

// 함수
var add = (a: number) => {
  //...
}

var sum = (a: number, b: number) => {
  // ...
}

// add = sum
sum = add

// 제너릭
interface Empty<T> {

}
var empty1: Empty<string>;
var empty2: Empty<number>
// empty1 = empty2
// empty2 =empty1

interface NotEmpty<T> {
  data: T
}
var notEmpty1: NotEmpty<string>;
var notEmpty2: NotEmpty<number>
// notEmpty1 = notEmpty2
// notEmpty2 = notEmpty1