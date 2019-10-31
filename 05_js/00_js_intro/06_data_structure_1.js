const numbers = [1, 2, 3, 4,]

console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index만 가능
console.log(numbers.length) // 4

// 원본 파괴
console.log(numbers.reverse())
console.log(numbers) //reverse는 원본을 바꿔서 뒤집어놓는다.
console.log(numbers.reverse()) // 한번 더 사용함으로서 원본으로 되돌려 놓음

// push - 값을 집어넣지만 배열의 길이를 return
console.log(numbers.push('a')) // 5
console.log(numbers) // [1, 2, 3, 4, 'a']

// pop - 배열의 가장 마지막 요소 제거 후 return
console.log(numbers.pop()) // a
console.log(numbers) // [1, 2, 3, 4]

// unshift - 배열의 가장 앞에 요소를 추가, return은 배열의 길이
console.log(numbers.unshift('a')) // a
console.log(numbers) // ['a', 1, 2, 3, 4]

// shift - 배열의 가장 앞에 요소 제거 후 return
console.log(numbers.shift()) // a
console.log(numbers) // [1, 2, 3, 4]

// boolean return
console.log(numbers.includes(1)) // true
console.log(numbers.includes(0)) // false

// indexOf
console.log(numbers.push('a', 'a')) // 6
console.log(numbers) // [1, 2, 3, 4, 'a', 'a']
console.log(numbers.indexOf('a')) // 4 => 중복이 존재한다면 처음 찾은 요소의 index를 return
console.log(numbers.indexOf('b')) // -1 => 찾고자 하는 요소가 없으면 -1 return

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return
console.log(numbers.join()) // '1,2,3,4,a,a'  => 아무것도 넣지 않으면 ,를 기준으로 가져옴
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'
console.log(numbers) // [1, 2, 3, 4, 'a', 'a'] => 원본은 변화하지 않음
