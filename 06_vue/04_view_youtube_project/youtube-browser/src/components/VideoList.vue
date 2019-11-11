<template>
  <!-- list 로 띄울 것이기 때문에 div 대신 ul 태그 -->
  <ul class="col-lg-4 list-group">
    <!-- 태그 안의 내용이 길 경우에는 enter로 줄바꿈을 함으로서 깔끔하게 정리해준다. -->
    <video-list-item 
    v-for="video in videos" 
    :key="video.etag" 
    :video="video"
    @videoSelect="onVideoSelect">
    </video-list-item>
  </ul>
</template>

<script>
  import VideoListItem from './VideoListItem'

  export default {
    name: 'VideoList',
    components: {
      VideoListItem,
    },
  methods: {
    onVideoSelect(video) {
      // 받을 인자가 있기 때문에 this.video가 아닌 video
      this.$emit('videoSelect', video)
    }
  },
  props: {
    videos: {
      type: Array,
      required: true,
      },
    },
  }
</script>

<style>
</style>