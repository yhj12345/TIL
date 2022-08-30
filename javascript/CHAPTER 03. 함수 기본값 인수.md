## CHAPTER 03. 함수 기본값 인수

#### 3.1 함수 인수의 기본값(ES6 이전)

```javascript
// ES6 이전에는 함수 인자의 기본값을 설정하는 것이 쉽지 않다,,,
function getLocation(city, country, continent) {
    if (typeof country === 'undefined') {
        country = 'Italy';
    }
    if (typeof continent === 'undefined') {
        continent = 'Europe';
    }
    console.log(continent, country, city);
}

getLocation('Millan'); // Europe Italy Milan

getLocaion('Paris', 'France'); // Europe France Paris
```



#### 3.2 함수 기본값 인수

```javascript
function calculatePrice(total, tax=0.1, tip=0.05) {
    // tax나 tip에 값을 할당하지 않으면 기본값으로 0.1과 0.05가 쓰인다.
    return total + (total * tax) + (total * tip);
}

// 이렇게 쓰면 tip에 0.15를 할당하게 된다.
calculatePrice(100, undefined, 0.15)
// -> 원하는 대로 나오지만 깔끔하지 못하다

// 디스트럭처링
function calculatePrice({tatal=0,tax=0.1,tip=0.05,} = {}) {
    return total + (total * tax) + (total * tip);
}

const bill = calculatePrice({tip:0.15, tatal:150}); // 187.5
```

