<template>
  <div class="container mt-5">
    <h2>Welcome Home, Hello,{{ this.$route.params.username }}</h2>
    <ul class="navbar-nav ms-auto"></ul>
    <div v-for="article in articles" :key="article.id">
      <h5>
        <router-link
          class="link-style"
          :to="{ name: 'details', params: { id: article.id } }"
        >
          {{ article.title }}记录时间：{{ article.date }}
        </router-link>
      </h5>
      <hr />
    </div>
    <div class="btn">
      <router-link class="btn btn-primary" aria-current="page" to="/create"
        >Create 提交新订单</router-link
      >
    </div>
    <div class="btn">
      <router-link class="btn btn-success" aria-current="page" to="/login"
        >LogOut 退出账号</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: [],
    };
  },
  methods: {
    getArticles() {
      fetch("http://localhost:5000/get", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          //console.log(data);
          this.articles.push(...data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  getUsername() {},

  created() {
    this.getArticles();
    this.currentUsername = this.$route.params.username;
    console.log("getting=", this.currentUsername);
    if (!(this.currentUsername == undefined)) {
      this.$store.commit("getUsername", this.$route.params.username);
    }
  },
};
</script>

<style>
.link-style,
h2 {
  font-weight: bold;
  color: goldenrod;
  text-decoration: none;
}

.link-style:hover {
  color: greenyellow;
  text-decoration: none;
}

.btn {
  margin-left: 6px;
  float: left;
}
</style>
