## CHAPTER 13. 프로미스

#### 13.1 콜백 지옥

- 비동기 코드를 동기식으로 작동하는 것처럼 하기 위해 콜백으로 여러 코드블록을 차례로 연결해 작성할 때 발생하는 상황을 콜백지옥이라고 부르기도 한다.

```javascript
// 콜백지옥 예시
const makePizza = (ingredients, callback) => {
    mixIngredients(ingredients, function(mixedIngredients)) {
    	bakePizza(mixedIngredients, function(bakedPizza)) {
        	console.logI('finished!')
    	}
    }
}
```



#### 13.2 프로미스

- 프로미스는 비동기 작업의 최종 성공 또는 실패를 나타내는 객체이다.

```javascript
// 프로미스 안에서 즉시 resolve를 호출 하면, 첫번쨰 매개변수로 전달된 값이 콘솔에 출력됨
const myPromise = new Promise((resolve, reject) => {
    resolve("The value we get from the promise");
});

myPromise.then(
	data => {
        console.log(data); // The value we get from the promise
    });

// setTimeout()을 사용하면 resolve가 호출되기 전까지 일정 시간을 기다릴 수 있다.
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("The value we get from the promise");
    }, 2000);
});

myPromise.then(
	data => {
        console.log(data); // (2초 기다린후) The value we get from the promise
    });

// reject를 이용한 오류 처리 방법
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        reject(new Error("this is our error"));
    }, 2000);
});

myPromise
	.then(data => {
    	console.log(data);
})
	.catch(err => {
    	console.log(err);
});
// Error: this is our error
// Stack trace:
// myPromise</<@debugger eval code:3:14
```



#### 13.3 프로미스 체이닝

- 프로미스의 성공 또는 실패 여부와 무관하게 이전 프로미스에서 반환된 것을 후속 프로미스의 기반으로 사용하여 프로미스를 계속 **체이닝**할 수 있다.
- 원하는 만큼 많은 프로미스를 연결할수 있으며, 그 코드는 위에서 봤던 콜백 지옥의 코드보다 더 읽기 쉽고 간결하다.

```javascript
const myPromise = new Promise((resolve, reject) => {
  resolve();
)}

myPromise
  .then(data => {
	return 'working...'
  })
  .then(data => {
    // 이전 프로미스에서 받은 값을 출력
    console.log(data);
    throw 'falied';
  })
  .catch(err => {
    // 프로미스 수행 중 발생한 오류를 받아서 출력
    console.error(err);
    // failed!
  })

// 실패한 경우에도 체이닝 가능
const myPromise = new Promise((resolve, reject) => {
  resolve();
)}

myPromise
  .then(data => {
	throw new Error("ooops");
	console.log("first value")
  })
  .catch(() => {
    console.error("catched an error");
  })
  .then(data => {
    console.log("second value");
  })
// catched an error
// second value
```



#### 13.4 Promise.resolve()와 Promise.reject()

```javascript
// Promise.resolve()
Promise.resolve('Success').then(function(value) {
    console.log('Success');
    // Success
}, function(value) {
    console.log('fail')
});

// Promis.reject()
Promise.reject(new Error('fail')).then(function() {
    // not called
}, function(error) {
    console.log(error);
    // Error: fail
});
```



#### 13.5 Promise.all()과 Promise.race()

- Promise.all()은 모든 프로미스가 성공할 경우에만 성공하는 하나의 프로미스를 반환한다.

```javascript
const promise1 = new Promise((resolve, reject) => {
    setTimeout(resolve, 500, 'first value');
});
const promise2 = new Promise((resolve, reject) => {
    setTimeout(resolve, 1000, 'second value');
});

promise1.then(data => {
    console.log(data);
});
// 500ms 후
// first value
promise2.then(data => {
    console.log(data);
});
// 1000ms 후
// second value

// Promise.all()을 사용한다면,,,
const promise1 = new Promise((resolve, reject) => {
    setTimeout(resolve, 500, 'first value');
});
const promise2 = new Promise((resolve, reject) => {
    setTimeout(resolve, 1000, 'second value');
});

Promise
	.all([promise1, promise2])
	.then(data => {
    	const [promise1data, promise2data] = data;
    	console.log(promise1data, promise2data);
});
// 1000ms 후
// first value secondvalue

// Promise.all()을 사용시 하나라도 실패한다면,,,
const promise1 = new Promise((resolve, reject) => {
    resolve("my first value")
});
const promise2 = new Promise((resolve, reject) => {
    reject(Error("oooops error"));
});

Promise
	.all([promise1, promise2])
	.then(data => {
    	const [promise1data, promise2data] = data;
    	console.log(promise1data, promise2data);
});
// Error: oooops error
```



- Promise.race는 이터러블에 포함된 프로미스들 중 가장 먼저 성공 또는 실패한 결과를 반환한다.

```javascript
const promise1 = new Promise((resolve, reject) => {
    setTimeout(resolve, 500, 'first value');
});
const promise2 = new Promise((resolve, reject) => {
    setTimeout(resolve, 1000, 'second value');
});

Promise.race([promise1, promise2]).then(function(value) {
    console.log(value);
    // 둘 다 성공하지만 promise2가 더 빨리 성공
});
// second value
// 비어있는 이터러블을 전달하면 .race()는 영원히 보류된 상태로 남아 있게 됨
```

