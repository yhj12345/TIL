## JavaScript : 프로토타입 이해

JavaScript는 클래스라는 개념이 없습니다. 그래서 기존의 객체를 복사하여 새로운 객체를 생성하는 프로토타입 기반의 언어입니다. 프로토타입 기반 언어는 객체 원형인 프로토타입을 이용하여 새로운 객체를 만들어냅니다. 이렇게 생성된 객체 역시 또 다른 객체의 원형이 될 수 있습니다. 프로토타입은 객체를 확장하고 객체 지향적인 프로그래밍을 할 수 있게 해줍니다. 프로토타입은 크게 두 가지로 해석됩니다. 프로토타입 객체를 참조하는 prototype 속성과 객체 멤버인 proto 속성이 참조하는 숨은 링크가 있습니다. 이 둘의 차이점을 이해하기 위해서는 JavaScript 함수화 객체의 내부적인 구조를 이해 해야합니다. 이번 글에서는 JavaScript의 함수와 객체 내부 구조부터 시작하여 프로토타입에 대해 알아보겠습니다.



### 1. 함수와 객체의 내부 구조

JavaScript에서는 함수를 정의하고, 파싱단계에 들어가면, 내부적으로 수행되는 작업이 있습니다. 함수 멤버로 prototype 속성이 있습니다. 이 속성은 다른 곳에 생성된 함수이름의 프로토타입 객체를 참조합니다. 프로토타입 객체의 멤버인 constructor 속성은 함수를 참조하는 내부구조를 가집니다. 아래의 그림과 같이 표현합니다.

![](C:\Users\ghwns\AppData\Roaming\marktext\images\2023-04-25-22-39-05-image.png)

```javascript
function Person() {}
```



속성이 하나도 없는 Person이라는 함수가 정의되고, 파싱단계에 들어가면, Person 함수 Prototype 속성은 프로토타입 객체를 참조합니다. 프로토타입 객체 멤버인 constructor 속성은 Person 함수를 참조하는 구조를 가집니다. 여기서 알아햐 하는 부분은 Person 함수의 prototype 속성이 참조하는 프로토타입 객체는 new라는 연산자와 Person 함수를 통해 생성된 모든 객체의 원형이 되는 객체입니다. 생성된 모든 객체가 참조한다는 것을 기억해야 합니다. 아래의 그림과 같이 표현합니다.

![](C:\Users\ghwns\AppData\Roaming\marktext\images\2023-04-25-22-41-44-image.png)

```javascript
function Person() {}

var joon = new Person();
var jisoo = new Perosn();
```



JavaScript에서는 기본 데이터 타입인 boolean, number, string 그리고 특별한 값인 null, undefined 빼고는 모두 객체입니다. 사용자가 정의한 함수도 객체이고, new라는 연산자를 통해 생성된 것도 객체입니다. 객체 안에는 proto(비표준) 속성이 있습니다. 이 속성은 객체가 만들어지기 위해 사용된 원형인 프로토타입 객체를 숨은 링크로 참조하는 역할을 합니다.



### 2. 프로토타입 객체란?

함수를 정의하면 다른 곳에 생성되는 프로토타입 객체는 자신이 다른 객체의 원형이 되는 객체입니다. 모든 객체는 프로토타입 객체에 접근할 수 있습니다. 프로토타입 객체도 동적으로 런타임에 멤버를 추가할 수 있습니다. 같은 원형을 복사로 생성된 모든 객체는 추가된 멤버를 사용할 수 있습니다.

![](C:\Users\ghwns\AppData\Roaming\marktext\images\2023-04-25-22-48-36-image.png)

```javascript
function Person() {}

var joon = new Person();
var jisoo = new Perosn();

Person.prototype.getType = function (){
    return "인간";
};

console.log(joon.getType());  // 인간
console.log(jisoo.getType()); // 인간
```

프로토타입 객체에 getType()이라는 함수를 추가하면 멤버를 추가하기 전에 생성된 객체에서도 추가된 멤버를 사용할 수 있습니다. 같은 프로토타입을 이용하여 생성된 joon과 jisoo 객체는 getType()을 사용할 수 있습니다.



여기서 알아두어야 할 것은 프로토타입 객체에 멤버를 추가, 수정, 삭제할 때는 함수 안의 prototype 속성을 사용해야 합니다. 하지만 프로토타입 멤버를 읽을 때는 함수 안의 prototype 속성 또는 객체 이름으로 접근합니다.

![](C:\Users\ghwns\AppData\Roaming\marktext\images\2023-04-25-22-52-51-image.png)

```javascript
Person.prototype.getType = function (){
    return "사람";
};

console.log(jisoo.getType());  // 사람
```

결론을 내리면, 프로토타입 객체는 새로운 객체가 생성되기 위한 원형이 되는 객체입니다. 같은 원형으로 생성된 객체가 공통으로 참조하는 공간입니다. 프로토타입 객체의 멤버를 읽는 경우에는 객체 또는 함수의 prototype 속성을 통해 접근할 수 있습니다. 하지만 추가, 수정, 삭제는 함수의 prototype 속성을 통해 접근해야합니다.



### 3. 프로토타입이란?

JavaScript에서 기본 데이터 타입을 제외한 모든 것이 객체입니다. 객체가 만들어지기 위해서는 자신을 만드는 데 사용된 프로토타입 객체를 이용하여 객체를 만듭니다. 이때 만들어진 객체 안에 `__proto__`(비표준) 속성이 자신을 만들어낸 원형을 의미하는 프로토타입 객체를 참조하는 숨겨진 링크가 있습니다. 이 숨겨진 링크를 프로토타입이라고 정의합니다.

![](C:\Users\ghwns\AppData\Roaming\marktext\images\2023-04-25-22-58-24-image.png)

```javascript
function Person() {}

var joon = new Person();
```

프로토타입을 크게 두 가지로 해석된다 했습니다. 함수의 멤버인 prototype 속성은 프로토타입 객체를 참조하는 속성입니다. 그리고 함수와 new 연산자가 만나 생성한 객체의 프로토타입 객체를 지정해주는 역할을 합니다. 객체 안의 `__proto__`(비표준) 속성은 자신을 만들어낸 원형인 프로토타입 객체를 참조하는 숨겨진 링크로써 프로토타입을 의미합니다.



JavaScript에서는 숨겨진 링크가 있어 프로토타입 객체 멤버에 접근할 수 있습니다. 그래서 이 프로토타입 링크를 사용자가 정의한 객체에 링크가 참조되도록 설정하면 코드의 재사용과 객체 지향적인 프로그래밍을 할 수 있습니다.



### 4. 코드의 재사용

코드의 재사용 하면 떠오르는 단어는 바로 상속입니다. 클래스라는 개념이 있는 Java에서는 중복된 코드를 상속받아 코드 재활용을 할 수 있습니다. 하지만 JavaScript에서는 클래스가 없는, 프로토타입 기반 언어입니다. 그래서 프로토타입을 이용하여 코드 재사용을 할 수 있습니다.



이 방법에도 크게 두 가지로 분류할 수 있습니다. classical 방식과 prototypal 방식이 있습니다. classical 방식은 new 연산자를 통해 생성한 객체를 사용하여 코드를 재사용 하는 방법입니다. 마치 Java에서 객체를 생성하는 방법과 유사하여 classical 방식이라고 합니다. prototypal 방식은 리터럴 또는 Object.create()를 이용하여 객체를 생성하고 확장해 가는 방식입니다. 두 가지 방법 중 JavaScript에서는 prototypal 방식을 더 선호합니다. 그 이유는 classical 방식보다 간결하게 구현할 수 있기 때문입니다. 밑의 예제 1~4번까지는 classical 방식의 코드 재사용 방법이고, 5번은 prototypal 방식인 Object.create()를 사용하여 코드의 재사용을 보여줍니다.




