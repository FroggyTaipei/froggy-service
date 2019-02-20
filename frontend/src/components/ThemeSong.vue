<template>
    <div @click="playToggle" class="theme-song" :class="{ 'sound-on' : play }">
        <font-awesome-icon v-show="play" icon="volume-up" />
        <font-awesome-icon v-show="!play" icon="volume-off" />
    </div>
</template>

<script>
export default {
  name: 'theme-song',
  data: () => ({
    play: false,
    interacted: false,
    audio: new Audio('https://storage.googleapis.com/froggy-service/frontend/assets/theme_song.mp3')
  }),
  created () {
    this.audio.volume = 0.01
    this.audio.loop = true
  },
  mounted () {
    document.addEventListener('click', this.startSound)
  },
  methods: {
    startSound () {
      this.audio.play()
      this.play = true
      this.volumeIncrease()
      document.removeEventListener('click', this.startSound)
    },
    volumeIncrease () {
      if (this.audio.volume < 0.1) {
        setTimeout(() => {
          this.audio.volume += 0.01
          this.volumeIncrease()
        }, 1000)
      }
    },
    playToggle () {
      this.play = !this.play
      if (this.play) {
        this.audio.play()
      } else {
        this.audio.pause()
      }
    }
  }
}
</script>

<style scoped>
    .sound-on {
        color: royalblue;
    }
    .theme-song{
        position: fixed;
        margin-left: 8px;
        font-size: x-large;
        z-index: 9999;
    }
</style>
