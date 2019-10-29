console.log(a) // undefined
var a = 10
console.log(a) // 10

// JS 가 이해한 코드
var a
console.log(a) // undefinde
a = 10
console.log(a)


// // let은 되지 않는다. ReferenceError
// console.log(b)
// let b = 10
// console.log(b)

// // 마찬가지로 아래와 같은 과정을 거친다
// let b
// console.log(b)
// b = 10
// console.log(b)

if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y ===3) {
    var x = 1
  }
  console.log(y) // 3 
}

if (x === 1) {
  console.log(y) // 3 
}

// JS 가 이해한 코드
var x
var y
if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y ===3) {
    var x = 1
  }
  console.log(y) // 3 
}

if (x === 1) {
  console.log(y) // 3 
}