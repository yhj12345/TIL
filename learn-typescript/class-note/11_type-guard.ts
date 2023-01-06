interface Developer {
  name: string;
  skill: string;
}

interface Person {
  name: string;
  age: number;
}

const introduce = (): Developer | Person => {
  return { name: 'Tony', age: 23, skill: 'Iron Making'}
}

var tony = introduce()
// console.log(tony.skill)

if ((tony as Developer).skill) {
  var skill = (tony as Developer).skill
  console.log(skill)
} else if ((tony as Person).age) {
  var age = (tony as Person).age
  console.log(age)
}

// 타입 가드 정의
const isDeveloper = (target: Developer | Person): target is Developer => {
  return (target as Developer).skill !== undefined;
}

if (isDeveloper(tony)) {
  console.log(tony.skill)
} else {
  console.log(tony.age)
}