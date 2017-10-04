<template>
    <div id="app">
        <div class="col-50">
            <table border="1">
                <tr>
                    <td></td>
                    <td>1 поток</td>
                    <td>2 поток</td>
                </tr>
                <tr>
                    <td>7:00</td>
                    <item-block></item-block>
                    <item-block></item-block>
                </tr>
            </table>
        </div>
        <div class="col-50">
            {{ msg }}
            <div class="drag-item"
                 v-for="object in objects"
                 draggable="true"
                 v-on:dragstart="dragStart"
                 v-on:dragenter="dragEnter"
                 v-on:dragend="dragEnd"
            >{{ object }}
            </div>
        </div>
    </div>
</template>

<script>
    let dragSrc = null;
    export default {
        name: 'app',
        data() {
            return {
                msg: 'Welcome to Your Vue.js App',
                objects: ['My', 'name', 'is', 'Jeny'],
            }
        },
        components:{
            'item-block' : {
                template: '<td v-on:drop="drop" v-on:dragover="dragOver" v-on:dragleave="dragRemove"></td>',
                methods: {
                    dragOver: function (event) {
                        event.dataTransfer.dropEffect = 'move';
                        event.target.style.background = '#f00';
                    },
                    drop: function (e) {
                        if (dragSrc !== e.target) {
                            dragSrc.innerHTML = e.target.innerHTML;
                            e.target.innerHTML = e.dataTransfer.getData('text/html');
                        }
                        return false;
                    },
                    dragRemove: function (e) {
                        event.target.style.background = '#fff';
                    },
                }
            }
        },
        methods: {
            dragStart: function (e) {
                this.msg = 'Try to move it: ' + event.target.innerText;
                e.target.style.opacity = '0.4';

                dragSrc= e.target;

                e.dataTransfer.effectAllowed = 'move';
                e.dataTransfer.setData('text/html', e.target.innerHTML)
            },
            dragEnter: function (e) {
                e.target.classList.add('over')
            },
            dragEnd: function (e) {
                e.target.style.opacity = '1.0';

                document.querySelectorAll('.drag-item').forEach(function (item) {
                    item.classList.remove('over');
                })
            }
        }
    }
</script>

<style lang="scss">
</style>