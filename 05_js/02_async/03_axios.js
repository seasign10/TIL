const axios = require('axios')

// axios.get('http://jsonplaceholder.typicode.com/posts')
//   .then(function(response) {
//     console.log(response)
//   })
//   .catch(function(err) {
//     console.log(err)
//   })


// refectoring
axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(response => {
    console.log(response)
  })
  .catch(err => {
    console.log(err)
  })






  