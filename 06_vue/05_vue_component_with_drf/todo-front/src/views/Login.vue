<template>
  <div>
    <!-- 아래를 케밥으로 쓰면 위도 케밥으로 써야하는데, 파스칼로 하면 둘다 사용 가능하다. 파스칼을 권장 -->
    <LoginForm/>
  </div>
</template>

<script>
  // 3step => import => 등록 => 파스칼 or 케밥
  // @ 는 `/src` 의 alias
  // import LoginForm from '../components/LoginForm' // 상대경로 - 눈으로 추적해야하기 때문에 비효율 적
  import LoginForm from '@/components/LoginForm' // 절대경로 /src => @
  export default {
    name: 'login',
    components: {
      LoginForm,
    }
  }
</script>

<style>

</style>