<template>
    <div class="auth">
        <div class="auth__grid">
            <div class="auth__logo">
                <img src="/src/assets/images/logo-white-400px.png"/>
            </div>
            <div class="auth__form">
                <div class="form-group">
                    <input name="auth_login" title="login" placeholder="Ваш e-mail" v-model="login"/>
                </div>
                <div class="form-group">
                    <input name="auth_password" title="password" placeholder="Пароль" type="password" v-model="password"/>
                </div>
                <button class="btn btn-important" @click="authorise()">ВОЙТИ</button>
                <button class="btn btn-gray">РЕГИСТРАЦИЯ</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                login: '',
                password: ''
            }
        },
        methods:{
            authorise: function () {
                this.$http.post('api/token/', {
                    email: this.login,
                    password: this.password
                }).then(response => {
                    this.$emit('authenticate', response);
                }).catch(response => {
                    console.log(response);
                });
            }
        }
    }
</script>

<style lang="scss">
    $red: rgb(119,0,12);

    .auth {
        position: fixed;
        z-index: 100;
        left: 0;
        display: inline-block;
        height: 100vh;
        max-width: 400px;
        width: 33%;
        background: $red;
        color: #fff;
        overflow: hidden;

        &__grid {
            height: 100%;
            width: 100%;
            display: grid;
            grid-template-rows: auto 300px auto;
        }

        &__form {
            grid-row: 2;
            height: 100%;
            text-align: center;
            padding: 0 20px;

            input{
                padding: 10px;
                width: 100%;
                border: 0;
            }
        }

        &__logo{
            align-self: center;
            padding: 20px;

            img {
                width: 100%;
            }
        }
    }
</style>
