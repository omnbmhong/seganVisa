<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>Welcome to MMTEK Inc.</p>
    <h3>Welcome to GAS Monitor System.</h3>

    <h3>Please Log In your user account</h3>
    <ul class="navbar-nav ms-auto">
      <li class="nav-item mx-3">
        <a>
          <router-link aria-current="page" to="/login"
            >已有用户直接登陆</router-link
          >
        </a>
      </li>
      <li class="nav-item mx-3">
        <a>
          <router-link aria-current="page" to="/register"
            >我要注册新用户</router-link
          >
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.text-style {
  font-size: 55px !important;
  display: flex;
  font-weight: 400;
  font-family: "Fira Sans", sans-serif;
  color: rgb(42, 108, 206) !important;
}
</style>
