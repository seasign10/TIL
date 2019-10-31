const me = {
  name: 'ssafy', // key가 한 단어 일 때
  'phone number': '01012345678', // key가 여러단어 일 때
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // key가 여러 단어인 경우 반드시 []로 접근

console.log(me.appleProducts) // { ipad: '2018pro', iphone: '7', macbook: '2019pro' }
console.log(me.appleProducts.ipad)

// Object Literal (객체 표현법) 
// ES5
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}
console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// EX6+
// object 의 Key 와 Value 가 같다면, 마치 배열처럼 한번만 작성 가능
let bookShop2 = {
  books,
  comics,
  magazines,
}
console.log(bookShop2)

// JSON
const jsonData = JSON.stringify({ // JSON => String
  coffe: 'Americano',
  iceCream: 'Mint Choco', // 트레일링 콤마는 JSON에서 쓸수 없다는 것을 유의 객체에서만 가능
})
console.log(jsonData)
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData) // object (객체)

console.log()


