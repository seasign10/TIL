<template>
  <div>
    <!-- input => change 로 바꾸면 하나하나 쿼리값이 날라가지 않고 enter 를 쳐야 쿼리 값이 나간다. -->
    <input @change="onInput" type="text">
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
        this.$emit('inputChange', e.target.value)
      }
    }
  }
</script>


<style scoped>
  /* scoped => 이 vue에만 bootstrap css 적용 */
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>