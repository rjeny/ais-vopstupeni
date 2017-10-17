<template>
    <div class="content">
        <div class="persona">
            <div class="persona__avatar">
                <img src="/src/assets/images/iam.jpg">
            </div>
            <div class="persona__full_name">
                {{ $store.getters.getUserInfo.last_name }}
                {{ $store.getters.getUserInfo.first_name }}
                {{ $store.getters.getUserInfo.middle_name }}
            </div>
            <div></div>
            <div class="persona__info">
                <dl>
                    <dt>Email</dt>
                    <dd>{{ $store.getters.getUserInfo.email }}</dd>
                    <dt>Телефон</dt>
                    <dd>+7(921)895-15-39</dd>
                    <dt>Университет</dt>
                    <dd>СПБГУТ им. проф. М.А. Бонч-Бруевича</dd>
                    <dt>Организация</dt>
                    <dd>Студенческий совет СПХФА</dd>
                    <dt>Должность</dt>
                    <dd>Консультант-тренер</dd>
                </dl>
            </div>
        </div>

        <notifications></notifications>

        <div class="block block--tests">
            <span class="block__header">Тесты</span>
            <div class="block__content">
                <span>7</span> тестов доступно
            </div>
        </div>
        <div class="block block--applications"><span class="block__header">Мои заявки</span>
            <div class="block__content">
                <span>1</span> заявка
            </div>
        </div>

    </div>
</template>

<script>
    import Notifications from './Notifications.vue';

    export default {
        data() {
            return {
                name: '',
            }
        },
        components: {
            notifications: Notifications,
        },
        computed: {
            fullName: function () {
                let user = this.$store.getters.getUserInfo;
               return user.last_name + ' ' + user.first_name + ' ' + user.middle_name;
            }
        }
    }
</script>

<style lang="scss">
    .content {
        .block {

            &--tests {
                border-color: #aa770c;

                .block__content span {

                    color: #aa770c;
                }
            }

            &--applications {
                border-color: #aa0c77;

                .block__content span {

                    color: #aa0c77;
                }
            }
        }

    }

    .persona {
        grid-column-end: span 4;
        background: #fff;
        min-height: 300px;

        display: grid;
        grid-template-columns: 200px auto;
        grid-template-rows: 50px 50px 200px;

        &__avatar {
            grid-row-start: 1;
            grid-row-end: 4;
            img {
                height: 100%;
            }
        }

        &__full_name {
            padding: 10px;
            font-size: 30px;
            border-bottom: 1px solid #dddddd;
        }

        &__info {
            padding: 10px;
            dl {
                dt, dd {
                    float: left;
                }

                dt {
                    font-weight: bold;
                    clear: left;
                }
                dt::after {
                    content: ':';
                }

                dd {
                    padding-left: 5px;
                }
            }
        }
    }

</style>
