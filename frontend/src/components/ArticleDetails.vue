<template>
  <div class="container mt-5">
    <h2>{{ article.title }}</h2>
    <p class="mt-3">
      {{ article.body }}
    </p>
    <h5>Recorded Date-Time:{{ article.date }}</h5>

    <button class="btn btn-danger mx-3 mt-3" @click="deleteArticle">
      删除
    </button>

    <button class="btn btn-danger mx-3 mt-3" @click="returnArticle">
      返回
    </button>

    <button class="btn btn-danger mx-3 mt-3" @click="confirmOrder">
      确认下单
    </button>

    <button v-if="isOperator" class="btn btn-danger mx-3 mt-3">
      Operator后台操作
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      article: {},
      isOperator: true,
    };
  },
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  methods: {
    deleteArticle() {
      fetch(`http://localhost:5000/delete/${this.id}/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then(() => {
          this.$router.push({
            name: "home",
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    returnArticle() {
      this.$router.push({
        name: "home",
      });
    },
    confirmOrder() {
      this.$router.push({
        name: "home",
      });
    },
    getUsername() {},
    getArticleData() {
      fetch(`http://localhost:5000/get/${this.id}/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          //console.log(data);
          this.article = data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  created() {
    this.getArticleData();
    console.log("user=", this.$store.state.name);
  },
};
</script>

<style></style>
