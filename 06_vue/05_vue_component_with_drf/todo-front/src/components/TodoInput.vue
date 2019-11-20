<template>
  <div class="todo-input">
    <form class="input-group mb-3" @submit.prevent="createTodo"> <!-- prevent : 기본적인 리다이렉트를 막음 -->
      <input type="text" class="form-control" v-model="title">
      <button type="submit" class="btn btn-primary mx-2">+</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'TodoInput',
    data() {
      return {
        title: '' // empty
      }
    },
    methods: {
      createTodo() {
        this.$emit('createTodo', this.title)
        this.title = '' // 보내고 난 후 초기화
      }
    },
  }
</script>

<style>

</style>