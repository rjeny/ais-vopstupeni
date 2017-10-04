<template>
    <div class="block block--notifications">
        <span class="block__header">Лента событий</span>
        <div class="block__content">
            <ul class="notifications-list">
                <li class="notifications-list__item" v-for="notification in notifications">
                    30.09.2017 15:27 |
                    <a class="notifications-list__author" href="">{{ notification.author_name }}</a>
                    {{ notification.message }} <a class="notifications-list__link" href="">{{ notification.entity }}</a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    class Notification{
        constructor(author, msg, entity){
            this.author_name = author;
            this.message     = msg;
            this.entity      = entity;
        };
    }

    let notifications = [
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"'),
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"'),
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"'),
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"'),
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"'),
        new Notification('Рябинин Евгений', 'открыл для вас', 'обратная связь "Уссы в ССУ"')
    ];


    export default {
        data() {
            return {
                notifications: notifications,
            }
        }
    }
</script>

<style lang="scss">
    .content {
        .block--notifications{
            grid-column-end: span 3;
            border-color: #00770c;
        }

        .notifications-list {
            padding: 10px;
            list-style: none;
            &__item{

            }

            &__link:before {
                content: '[';
            }

            &__link:after {
                content: ']';
            }
        }
    }
</style>
