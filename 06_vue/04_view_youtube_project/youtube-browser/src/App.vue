<template>
  <div id="app">
    <!-- inputChange 이벤트가 일어나면 onInputChange 라는 method 가 실행 됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>

    <div class="row">
      <!-- 값을 넘겨받은 selectedVideo를 바인드 -->
      <video-detail :video="selectedVideo"></video-detail>

      <!--오른쪽에서 왼쪽으로 할당, 왼쪽의 videos는 다르게 써도 상관 없지만 오른쪽의 "videos"는 이미 우리가 지정한 name이기 때문에 이름 그대로 써야 한다. -->
      <video-list @videoSelect="onVideoSelect" :videos="videos"></video-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만 명시적으로 작성한다.
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return { // return 값을 할 때에는 모든 객체가 return되기 때문에 객체를 한번 더 감싸서 구분을 주어야 한다. (component 의 data만)
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onVideoSelect(video) {
      // 최종적으로 video를 받은 다음에 selectedVideo로 넘긴다.
      this.selectedVideo = video
    },
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then(response => {
          this.videos = response.data.items
        })
        .catch(error => {
          console.log(error)
        }) // 함수 vs 함수기 때문에 arrow function 사용
    }
  }
}
</script>

<style>
</style>
