<template>
  <li @click="onVideoSelect" class="list-group-item">
    <img :src="thumbnailUrl" alt="img">
    <div class="media-body" v-html="video.snippet.title"></div>
    {{ video.snippet.title }}
  </li>
</template>

<script>
  export default {
    name: 'VideoListItem',
    props: {
      video: {
        type: Object,
        required: true,
      },
    },
    methods: {
      onVideoSelect() {
        // 인자가 없이 때문에 this.video
        this.$emit('videoSelect', this.video)
      }
    },
    computed: {
      thumbnailUrl(){
        return this.video.snippet.thumbnails.default.url
      }
    }
  }
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: #eee;
  }
</style>