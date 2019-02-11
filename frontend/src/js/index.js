import Vue from 'vue'
import App from './App.vue'
import init from './plain/main'

new Vue({
  el: '#app',
  render: h => h(App),
  components: [
      App
  ]
});

init();

