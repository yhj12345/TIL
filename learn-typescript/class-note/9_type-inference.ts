var a = 'abc';
var b = 20

const getC = (c = 10) => {
  var d = 'hi'
  return c + d
}

10 + '10' // 1010

// 타입 추론 기본2
// interface Dropdown<T> {
//   value: T;
//   title: string;
// }
// var shoppingItem: Dropdown<string> = {
//   value: 'abc',
//   title: 'hello'
// }

// 타입 추론 기본3
interface Dropdown<T> {
  value: T;
  title: string;
}

interface DetailedDropdown<K> extends Dropdown<K> {
  description: string
  tag: K
}


var detailedItem: DetailedDropdown<string> = {
  title: 'abc',
  description: 'ab',
  value: 'a',
  tag: 'a'
}

// Best Common Type
var arr = [1, 2, true, 'a'];
