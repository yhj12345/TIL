// 함수의 파라미터에 타입을 정의하는 방식
function sum(a: number, b: number) {
  return a + b
}
sum(10, 20)

// 함수의 반환 값에 타입을 정의하는 방식
function add(): number {
  return 10
}

// 함수에 타입을 정의하는 방식
function sum2(a: number, b:number): number {
  return a + b
}

// 파라미터를 제한하는 특성을 가짐
// sum2(10, 20, 30)

// 함수의 옵셔널 파라미터
function log(a: string, b?: string) {
  
}
log('hello world')
log('heloo ts', 'abc')

