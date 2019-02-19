<style lang="scss" scoped>
.v-marquee {
  width: 100%;
  display: block;
  white-space: nowrap;
  overflow: hidden;
  > div {
    display: inline-block;
    animation: marquee linear infinite;
    transition: 0.5s
  }
  .pause {
    animation-play-state: paused;
  }
  .running {
    animation-play-state: running;
  }
}
</style>

<template>
    <div class="v-marquee" @click="$emit('click',$event)">
        <div :style="{'animation-duration':time,'animation-name':name, 'visibility': visibility}" :class="animate?'running':'pause'">
            <slot>
                <div v-html="content"></div>
            </slot>
        </div>
    </div>
</template>

<script>
export default {
  name: 'VTextMarquee',
  props: {
    speed: {
      type: Number,
      default: 50
    },
    content: String,
    animate: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      time: 0,
      name: 'marquee',
      styleEl: document.createElement('style'),
      visibility: 'hidden'
    }
  },
  watch: {
    content () {
      this.start()
    },
    speed () {
      this.start()
    }
  },
  methods: {
    getTime () {
      return Math.max(this.$el.firstChild.offsetWidth, this.$el.offsetWidth) / this.speed + 's'
    },
    prefix (key, value) {
      return ['-webkit-', '-moz-', '-ms-', ''].map(el => `${el + key}:${value};`).join('')
    },
    keyframes () {
      const from = this.prefix('transform', `translateX(${this.$el.offsetWidth + 50}px)`)
      const to = this.prefix('transform', `translateX(-${this.$el.firstChild.offsetWidth + 50}px)`)
      const v = `@keyframes ${this.name} {
                  from { ${from} }
                  to { ${to} }
                }`
      this.styleEl.innerHTML = v

      document.head.appendChild(this.styleEl)
    },
    start () {
      this.$nextTick(() => {
        this.visibility = 'inherit'
        this.time = this.getTime()
        this.keyframes()
      })
    }
  },
  mounted () {
    const marq = this
    window.onresize = function () {
      marq.start()
    }
  }
}
</script>
