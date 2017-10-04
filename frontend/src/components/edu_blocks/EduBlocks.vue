<template>
    <div class="content">
        <div class="header-block">
            <h1>Образовательные блоки</h1>
        </div>
        <div class="header-block" v-if="visited.length != 0">
            <h2>Посещенные мной</h2>
        </div>
        <div class="block block--visited" v-for="block in visited">
            <div class="block__header">
                {{ block.name }}
            </div>
            <div class="block__content">
                <div class="block__author"><a href=""> {{ block.author }} </a></div>
                <ul>
                    <li>Узнать больше</li>
                    <li>Написать обратную связь</li>
                </ul>
            </div>
        </div>
        <div class="header-block" v-if="own.length != 0">
            <h2>Мои обрблоки</h2>
        </div>
        <div class="block block--visited" v-for="block in own">
            <div class="block__header">
                {{ block.name }}
            </div>
            <div class="block__content">
                <div class="block__author"><a href=""> {{ block.author }} </a></div>

                <ul>
                    <li>Редактировать</li>
                    <li>Прочитать обратную связь</li>
                </ul>
            </div>
        </div>

        <div class="add-new">
            <span class="fa-stack fa-2x">
                        <i class="fa fa-circle fa-stack-2x"></i>
                        <i class="fa fa fa-plus fa-stack-1x fa-inverse"></i>
            </span>
            Добавить Обр. блок
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                visited: [
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'},
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'},
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'},
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'},
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'}
                ],
                own: [
                    {id: 12, name: 'УССЫ В ССУ', author: 'Рябинин Евгений'},
                ]
            }
        },
    }
</script>

<style lang="scss">
    .block--visited {
        border-color: #aaaaaa;

        .block__author {
            font-size: 15px;
            border-bottom: 1px solid #ddd;
        }

        ul {
            list-style: none;

            li {
                padding: 10px;
            }
        }
    }

    .add-new {
        color: #00924E;
        font-size: 25px;

        align-self: center;

        .fa-inverse {
            color: #fff;
        }
    }

</style>
