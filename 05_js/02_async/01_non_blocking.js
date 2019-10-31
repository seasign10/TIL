const nothing = () => {
  console.log('sleeping')
}

console.log('start')
setTimeout(nothing, 3000) // 단위가 밀리세컨드 => 3000 , 3초
console.log('end')
// start => end => sleeping 각자 따로 놀고있는 코드 실행 순서

function sleep_3s() {
  setTimeout(() => console.log('wake up'), 3000)
}
console.log('Start sleeping')
sleep_3s()
console.log('End of program')
// => 위와 동일, 종료될때 까지 기다리지 않고 실행 (non-blocking)

function first() {
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

first()
setTimeout(third, 1000)
second()


console.log('Hi')

setTimeout(function ssafy() {
  console.log('ssafy')
}, 100) // 마지막에 출력

console.log('bye')


function printHello() {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello, 3000)
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()





