// 배열로 이루어진 숫자들을 모두 더하는 함수
const numberAddEach = numbers => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberSubEach = numbers => {
  let sub = 0
  for (const number of numbers) {
    sub += number
  }
  return sub
}

// 배열로 이루어진 숫자들을 모두 곱하는 함수
const numberMulEach = numbers => {
  let mul = 0
  for (const number of numbers) {
    mul += number
  }
  return mul
}

// 세 함수의 공통점 : 숫자로 이루어진 배열의 요소들을 각각 [???] 한다.
// [???]를 claaback 함수에서 처리하는 일로 바꿀 수 있다.

// base template 역할
const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

// 더하기
const addEach = (number, acc = 0) => {
  return acc + number
}

// 빼기
const subEach = (number, acc = 0) => {
  return acc - number
}

// 곱하기
const mulEach = (number, acc = 1) => {
  return acc * number
}

const NUMBERS = [1, 2, 3, 4, 5,]
console.log(numbersEach(NUMBERS, addEach))
console.log(numbersEach(NUMBERS, subEach))
console.log(numbersEach(NUMBERS, mulEach))

// 하지만 addEach, subEach, mulEach 를 다시 재사용 하지 않을 것 같다면
// numbersEach 이후의 제어를 함수 정의 없이 매번 자유롭게 하려면 어떻게 ?
console.log(numbersEach(NUMBERS, (number, acc=0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc * number))