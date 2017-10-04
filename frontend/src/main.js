/**
 *
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import interactjs from 'interactjs'

import Auth from './components/Auth.vue'

//Router Components
import Dashboard from './components/dashboard/Dashboard.vue'
import Tests from './components/tests/Tests.vue'
import EduBlocs from './components/edu_blocks/EduBlocks.vue'

// Стили
import './assets/css/animation.css'
import './assets/css/base.css'

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: Dashboard},
        { path: '/tests', component: Tests},
        { path: '/edu_blocks', component: EduBlocs},
    ]
});

Vue.use(VueRouter);

const app = new Vue({
    el: '#app',
    router: router,
    data: {
        not_authenticated: false
    },

    components: {
        'auth': Auth
    },
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