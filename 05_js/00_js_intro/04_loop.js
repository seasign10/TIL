// while
let i = 0

while (i < 6) { // true인 동안만 구문이 돌 것 0 1 2 3 4 5
  console.log(i)
  i++
}

//for
for (let j = 0; j < 6; j++) {
  console.log(j)
}


const numbers = [0, 1, 2, 3, 4, 5,]

for (let number of numbers) {
  console.log(number)
}


for (const number of numbers) { // 재 할당 하지 않겠다 => const
  console.log(number)
}
// 전부 0, 1, 2, 3, 4, 5 가 출력
