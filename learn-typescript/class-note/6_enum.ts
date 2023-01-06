enum Shoes {
  Newbalance,
  Vans
}

var myShoes = Shoes.Newbalance;
console.log(myShoes) // 0

enum Shoe {
  Nike = '나이키',
  Adidas = '아디다스'
}

var myShoe = Shoe.Adidas;
console.log(myShoe) // '아디다스'

// 예제
enum Answer {
  Yes = 'Y',
  No = 'N'
}

function askQuestion(answer: Answer) {
  if (answer === Answer.Yes) {
    console.log('정답입니다.')
  }
  if (answer === Answer.No) {
    console.log('오답입니다.')
  }
}

askQuestion(Answer.Yes)