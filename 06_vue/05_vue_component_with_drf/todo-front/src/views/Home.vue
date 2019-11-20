<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <!-- 왼쪽 : 부모 component에서 실행할 method, 오른쪽 : 받아온 데이터-->
    <TodoInput @createTodo="createTodo"/>
    <!-- 왼쪽, 자식리스트(props) 오른쪽, 받는 todos -->
    <TodoList :todos="todos" />
  </div>
</template>

<script>
import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex'

export default {
  name: 'home',
  components: {
    TodoList, TodoInput
  },
  data() {
    return {
      todos: [], // 여기에 todolist 가 올 것
    }
  },
  computed: {
    // spread 문법 => 각각의 getters
    // mapGetthers 함수의 인자로 들어가는 배열에는 getters 에서 정의한 함수들 중에서 가지고 오고 싶은 getter 들을 작성
    // mapGetters : vuex에서 제공하는 특수메서드, ... : (배열을 가져오는 축약어)
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  methods: {
    checkLoggedIn() {
      // this.$session.start()
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
        .then(res => {
          console.log(res)
          this.todos = res.data.todo_set
        })
        .catch(err => {
          console.log(err)
        })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      const requestForm = new FormData()
      // Postman의 body로 들어가는 코드
      requestForm.append('user', this.userId)
      requestForm.append('title', title) // createTodo 의 title (자식이 보낸 인자)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
        .then(res => {
          this.todos.push(res.data)
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부를 체크
  mounted() {
    this.checkLoggedIn(),
    this.getTodos()
  },
}
</script>
