//1.创建vue根实例
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// step1：引入 axios
import Axios from 'axios'
//引入vue-cookies
import VueCookies from 'vue-cookies'

Vue.config.productionTip = false

// step2：把axios挂载到vue的原型中，在vue中每个组件都可以使用axios发送请求,
// 不需要每次都 import一下 axios了，直接使用 $axios 即可
Vue.prototype.$axios = Axios
Vue.prototype.$cookies = VueCookies

// step3：使每次请求都会带一个 /api 前缀 
Axios.defaults.baseURL = '/api'

Vue.use(ElementUI);

new Vue({
    el: '#app',
    components: {
        App
    },
    template: '<App/>'
})
