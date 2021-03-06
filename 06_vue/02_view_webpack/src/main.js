// Vue 인스턴스를 최종으로 만드는 파일

// 1. 설치된 vue 를 추가
// (내가 만든 파일이 아닌 경우) 현재 위치에서 vue 이름을 가진 폴더가 없음 => 자동으로 node_modules 에서
import Vue from 'vue'

// 2. 최상위 컴포넌트 추가
// (내가 만든 파일) 상대 경로 표시
import App from './App.vue'

// new Vue({
//   render: function (createElement) {
//     return createElement()
//   }
// })
new Vue({
  render: h => h(App)
}).$mount('#app') // el: '#app'와 기능적으로 같으나 지금 방법이 더 유연하여 선호됨