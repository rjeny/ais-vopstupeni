<template>
    <div class="test-list">
        <h2>Тесты</h2>
        <ul>
            <li v-for="test in tests" v-on:click="load_description(test)">{{test}}</li>
        </ul>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                tests: ['Тестирование для 1 ступени',
                    'Тестирование для 2 ступени',
                    'Тестирование для 3 ступени',
                    'Просто аккред'],
                test_data: this.test_data,

            }
        },
        methods: {
            load_description: function (test) {
                this.$emit('loadData', test);
            }
        }
    }
</script>

<style lang="scss">
    .test-list {

        ul {
            list-style: none;

            li {
                padding:10px 15px;
                font-size: 18px;
                border-bottom: 1px solid #ddd;
                cursor: pointer;

                &:hover {
                    background: #ddd;
                }
            }
        }
    }
</style>
