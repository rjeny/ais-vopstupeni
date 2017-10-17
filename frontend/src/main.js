/**
 *
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import interactjs from 'interactjs'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetable from 'vuetable-2'
import VueCookie from 'vue-cookie'
import Vuex from 'vuex'

import Auth from './components/Auth.vue'

//Router Components
import Empty from './components/Empty.vue'
import Dashboard from './components/dashboard/Dashboard.vue'
import Tests from './components/tests/Tests.vue'
import EduBlocs from './components/edu_blocks/EduBlocks.vue'
import Requests from './components/requests/Requests.vue'

// Стили
import './assets/css/animation.css'
import './assets/css/base.css'

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: Empty},
        { path: '/dashboard', component: Dashboard},
        { path: '/tests', component: Tests},
        { path: '/edu_blocks', component: EduBlocs},
        { path: '/requests', component: Requests},
    ]
});

let ais$http = axios.create({
    baseURL: 'http://api.vopstupeni.rjeny.ru/',
    timeout: 1000,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'xsrfHeaderName',
});

Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(VueAxios, ais$http);
Vue.use(Vuetable);
Vue.use(VueCookie);

const store = new Vuex.Store({
    state: {
        user: {
            first_name: '',
            last_name: '',
            middle_name: '',
            email: '',
            university: '',
            avatar: '',
        }
    },
    mutations: {
        updateUser (state, user) {
            state.user.first_name = user.first_name;
            state.user.last_name = user.last_name;
            state.user.middle_name = user.middle_name;
            state.user.email = user.email;
            state.user.avatar = user.avatar;
        }
    },
    getters: {
        getUserInfo: (state) => {
            return state.user
        }
    }
});

const app = new Vue({
    el: '#app',
    router: router,
    store: store,
    data: {
        not_authenticated: false,
        user: '',
    },
    methods: {
      authorize: function (response) {
          console.log(response.data);
          this.$http.defaults.headers.common['Authorization'] = 'JWT ' + response.data.token;
          this.access_token  = response.data.token;
          this.$cookie.set('token', response.data.token);
          console.log(this.axios.defaults.headers.common);
          this.not_authenticated = false;
          store.commit('updateUser', response.data.user);

          let a = this.$http.get('users/');
          console.log(a);
      }
    },
    components: {
        'auth': Auth
    },

    created: function () {
        let token = this.$cookie.get('token');
        if (token) {
            this.$http.post('token/check/', {token: token}).then(response => {
                this.$http.defaults.headers.common['Authorization'] = 'JWT ' + response.data.token;
                this.not_authenticated = false;
                store.commit('updateUser', response.data.user);
                this.$router.replace('/dashboard');
            })
        } else {
            this.not_authenticated = true;
        }
    }
});

interactjs('.content-flex div:first-child').resizable({
    enabled: true,
    edges: {
        top: false,
        left: false,
        bottom: false,
        right: true,
    },
    max: Infinity,
    preserveAspectRatio: true,
    onmove: function (event) {
        let target = event.target;
        let min = 300;
        let max = 800;
        let new_width = event.rect.width;

        if (new_width < max && new_width > min) {
            target.style.width = new_width + 'px';
        }
    }
});