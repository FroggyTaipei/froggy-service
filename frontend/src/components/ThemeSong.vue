<template>
    <div @click="playToggle" class="theme-song" :class="{ 'sound-on' : play }">
        <div v-show="!play" class="pulse-button"></div>
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
  methods: {
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
        this.volumeIncrease()
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
      cursor: pointer;
    }
    .pulse-button {
      position: fixed;
      top: 16px;
      left: 16px;
      width: 1px;
      height: 1px;
      border: none;
      box-shadow: 0 0 0 0 rgb(58, 58, 58);
      border-radius: 50%;
      -webkit-animation: pulse 1.5s infinite cubic-bezier(0.66, 0, 0, 1);
      -moz-animation: pulse 1.5s infinite cubic-bezier(0.66, 0, 0, 1);
      -ms-animation: pulse 1.5s infinite cubic-bezier(0.66, 0, 0, 1);
      animation: pulse 1.5s infinite cubic-bezier(0.66, 0, 0, 1);
    }

    @-webkit-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}
    @-moz-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}
    @-ms-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}
    @keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}
</style>
