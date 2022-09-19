## CHAPTER 13. 프로미스

#### 13.1 콜백 지옥

비동기 코드를 동기식으로 작동하는 것처럼 하기 위해 콜백으로 여러 코드블록을 차례로 연결해 작성할 때 발생하는 상황을 콜백지옥이라고 부르기도 한다.

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

프로미스는 비동기 작업의 최종 성공 또는 실패를 나타내는 객체이다.

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

