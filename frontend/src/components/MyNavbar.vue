<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <router-link class="navbar-brand text-style" to="/">
        VISA Service 送签资料服务
      </router-link>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item mx-3">
            <router-link class="btn btn-primary" aria-current="page" to="/"
              >Home</router-link
            >
          </li>

          <!-- <li class="nav-item mx-3">
            <router-link
              class="btn btn-success"
              aria-current="page"
              to="/create"
              >Create</router-link
            >
          </li> -->
          <li class="nav-item mx-3">
            <router-link class="btn btn-primary" aria-current="page" to="/login"
              >Login</router-link
            >
          </li>
          <li class="nav-item mx-3">
            <router-link
              class="btn btn-primary"
              aria-current="page"
              to="/register"
              >Sign Up</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "MyNavbar",
};
</script>

<style scoped>
.text-style {
  font-size: 55px !important;
  display: flex;
  font-weight: 400;
  font-family: "Fira Sans", sans-serif;
  color: rgb(42, 108, 206) !important;
}
</style>
