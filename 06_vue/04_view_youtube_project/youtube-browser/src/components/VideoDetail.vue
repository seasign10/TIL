<template>
  <!-- video 값이 true 일 때만 돌도록 -->
  <div v-if="video" class="col-lg-8">
    <div class="embed-responsive embed-responsive-16by9">
      <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
    </div>
    <div class="details">
      <!-- html형식으로 title을 넣어주어야 글씨 깨짐이 없다. -->
      <h4 v-html="video.snippet.title"></h4>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'VideoDetail',
    props: {
      video: {
        type: Object,
        // video 선택이 안될수도 있기 때문에 required는 생략 (null이 나올수도 있음)
      }
    },
    computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        // return this.data
        return `http://www.youtube.com/embed/${videoId}`
      }
    }
  }
</script>

<style scoped>
  .details {
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>