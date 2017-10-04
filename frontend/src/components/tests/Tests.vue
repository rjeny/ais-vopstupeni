<template>
    <div class="content-flex">
        <test-list v-on:loadData="loadData"></test-list>
        <test-description v-bind:instructions="test_data"></test-description>
    </div>
</template>

<script>
    import TestList from './TestList.vue';
    import TestDescription from './TestDescription.vue';

    export default {
        data() {
            return {
                test_data: {
                    name: '',
                    description: '',
                    instruction: ''
                },
            }
        },
        components: {
            TestList, TestDescription
        },
        methods: {
            loadData: function (name) {
                console.log(this.test_data);
                this.test_data.name = name;
            }
        }
    }
</script>

<style lang="scss">


</style>
