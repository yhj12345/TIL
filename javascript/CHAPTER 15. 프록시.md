## CHAPTER 15. 프록시

### 15.1 프록시

> 프록시 객체는 기본작업(예: 속성 조회, 할당, 열거, 함수 호출 등)에 대해 사용자 지정 동작을 추가로 정의하는 데 사용된다.



### 15.2 프록시 생성

```javascript
var x = new Proxy(target, handler);
```

- target은 객체, 함수, 다른 프록시 등 무엇이든 가능하다.
- handler는 작업이 수행될 때 프록시의 동작을 정의하는 객체이다.



```javascript
// 원복 객체
const dog = {breed: "German Shephard", age: 5};

// 프록시 객체
const dogProxy = new Proxy(dog, {
    get(target, breed) {
        return target[breed].toUpperCase();
    },
    set(target, breed, value) {
        console.log("changing breed to...");
        target[breed] = value;
    }
})

console.log(dogProxy.breed);
// "GERMAN SHEPHARD"
console.log(dogProxy.breed = "Labrador");
// changing breed to...
// "Labrador"
console.log(dogProxy.breed)
// "LABRADOR"
```



### 15.3 프록시 활용

##### 데이터를 검증

```javascript
const validdateAge = {
    set: function(object, property, value) {
        if (property === 'age') {
            if (value < 18 ) {
                throw new Error('you are too young!')
            }
            else {
                // 기본 동작
                object[property] = value;
                return true
            }
        }
    }
}

const user = new Proxy({}, validateAge);
user.age = 17
// Uncaught Error: you are too young!
user.age = 21
// 21
```

##### 동일한 내용의 게터와 세터를 많은 속성에 적용해야할 때

```javascript
const dog = {
    _name: 'pup',  // ( '_' 기호는 private 속성 설정)
    _age: 7,
    get name() {
        console.log(this._name);
    },
    get age() {
        console.log(this._age);
    },
    set name(newName) {
        this._name = newName;
        console.log(this._name);
    },
    set age(newAge) {
        this._age = newAge;
        console.log(this._age);
    }
}

dog.name;
// pup
dog.age;
// 7
dog.breed;
// undefined
dog.age = 8;
// 8
```

