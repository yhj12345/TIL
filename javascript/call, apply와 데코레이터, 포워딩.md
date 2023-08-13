## call/apply와 데코레이터, 포워딩

#### 코드 변경 없이 캐싱 기능 추가하기

CPU를 많이 잡아먹지만 안정적인 함수 `slow(x)`가 있다고 가정해봅시다. 결과가 안정적이라는 말은 `x`가 같으면 호출 결과도 같다는 것을 의미합니다.

`slow(x)`가 자주 호출된다면, 결과를 어딘가에 저장(캐싱)해 재연산에 걸리는 시간을 줄이고 싶을 겁니다.

아래 예시에선 `slow(x)` 안에 캐싱 관련 코드를 추가하는 대신, 래퍼 함수를 만들어 캐싱 기능을 추가 할 예정입니다.

```js
function slow(x) {
    alert(`slow(${x})을/를 호출함`);
return x;
}

function cachingDecorator(func) {
    let cache = new Map();

    return function(x) {
        if (cache.has(x)) { // cache에 해당 키가 있으면
            return cache.get(x); // 대응하는 값을 cache에서 읽어옵니다.
        }

        let result = func(x); // 그렇지 않은 경우엔 func를 호출하고,

        cache.set(x, result); // 그 결과를 캐싱(저장)합니다.
        return result;
    };
}

slow = cachingDecorator(slow);

alert( slow(1) ); // slow(1)이 저장되었습니다.
alert( "다시 호출: " + slow(1) ); // 동일한 결과

alert( slow(2) ); // slow(2)가 저장되었습니다.
alert( "다시 호출: " + slow(2) ); // 윗줄과 동일한 결과
```

`cachingDecorator`같이 인수로 받은 함수의 행동을 변경시켜주는 함수를 *데코레이터* 라고 부릅니다.

모든 함수를 대상으로 `cachingDecorator`를 호출 할 수 있는데, 이 때 반환되는 것은 캐싱 래퍼입니다. 함수에 `cachingDecorator`를 적용하기만 하면 캐싱이 가능한 함수를 원하는 만큼 구현할 수 있기 때문에 데코레이터 함수는 아주 유용하게 사용됩니다.

#### 'func.calll'를 사용해 컨텍스트 지정하기

위에서 구현한 캐싱 데코레이터는 객체 메서드에 사용하기엔 적합하지 않습니다.

```js
// worker.slow에 캐싱 기능을 추가해봅시다.
let worker = {        
    someMethod() {
        return 1;
    },

    slow(x) {
        // CPU 집약적인 작업이라 가정
        alert(`slow(${x})을/를 호출함`);
        return x * this.someMethod(); // (*)
    }
};

// 이전과 동일한 코드
function cachingDecorator(func) {
    let cache = new Map();

    return function(x) {
        if (cache.has(x)) {
            return cache.get(x);
        }

        let result = func(x); // (**)

        cache.set(x, result);    
        return result;
    };
}

alert( worker.slow(1) ); // 기존 메서드는 잘 동작합니다.

worker.slow = cachingDecorator(worker.slow); // 캐싱 데코레이터 적용

alert( worker.slow(2) ); // 에러 발생!, Error: Cannot read property 'someMethod' of undefined


```

`(*)`로 표시한 줄에서 `this.someMethod` 접근에 실패했기 때문에 에러가 발생했습니다.

원인은 `(**)`로 표시한 줄에서 래퍼가 기존 함수 `func(x)`를 호출하면 `this`가 `undefined`가 되기 때문입니다.

래퍼가 기존 메서드 호출 결과를 전달하려 했지만 `this`의 컨텍스트가 사라졌기 때문에 에러가 발생하는 것입니다.

`this`를 명시적으로 고정해 함수를 호출할 수 있게 해주는 특별한 내장 함수 메서드 func.call을 이용하면 이러한 문제를 해결할 수 있습니다.

문법은 다음과 같습니다.

```js
func.call(context, arg1, arg2, ...)
```

메서드를 호출하면 메서드의 첫 번째 인수가 `this`, 이어지는 인수가 `func`의 인수가 된 후, `func`가 호출됩니다.

래퍼 안에서 `call`을 사용해 컨텍스트를 원본 함수로 전달하면 에러가 발생하지 않습니다.

```js
let worker = {
    someMethod() {
        return 1;
    },

    slow(x) {
        alert(`slow(${x})을/를 호출함`);
        return x * this.someMethod(); // (*)
    }
};

function cachingDecorator(func) {
    let cache = new Map();

    return function(x) {
        if (cache.has(x)) {
            return cache.get(x);
        }

        let result = func.call(this, x); // 이젠 'this'가 제대로 전달됩니다.

        cache.set(x, result);
        return result;
    };
}

worker.slow = cachingDecorator(worker.slow); // 캐싱 데코레이터 적용

alert( worker.slow(2) ); // 제대로 동작합니다.
alert( worker.slow(2) ); // 제대로 동작합니다. 다만, 원본 함수가 호출되지 않고 캐시 된 값이 출력됩니다
```

1. 데코레이터를 적용한 후에 `worker.slow`는 래퍼 `function (x) {...}`가 됩니다.

2. `worker.slow(2)`를 실행하면 래퍼는 `2`를 인수로 받고, `this=worker`가 됩니다.

3. 결과가 캐시되지 않은 상황이라면 `func.call(this, x)`에서 현재 `this` (`=worker`)와 인수 (`=2`)를 원본 메서드에 전달합니다.




