<template>
  <div>
    <p> Welcome to the frizTracker.</p>
    <p> This is a test to see if the endpoint for a random number API generator is working:
      {{ randomNumber }}
    </p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0
    }
  },
  name: 'Home.vue',
  methods: {
    getRandom () {
      this.randomNumber = this.getAPIrandint()
    },
    getAPIrandint () {
      const path = 'http://localhost:5000/api/random'
      axios.get(path).then(
        response => {
          this.randomNumber = response.data.randomNumber
        }
      ).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
