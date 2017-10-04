<template>
    <div class="test-description">
        <h2> {{ instructions.name }} </h2>
        <h3>Описание</h3>
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum
        lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum lorem insperum

        <h3>Инструкция</h3>
    </div>
</template>

<script>

    export default {
        data() {
            return {
                name: '',
            }
        },
        components: {
        },
        props:{
            instructions: {
                type: Object,
                default: function () {
                    return {
                        name: '',
                        description: '',
                        instruction: ''
                    }
                }
            }
        }
    }
</script>

<style lang="scss">


</style>
