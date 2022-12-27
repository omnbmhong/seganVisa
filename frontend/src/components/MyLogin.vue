<template>
  <form @submit.prevent="handleSubmit">
    <h1>欢迎登录</h1>

    <div class="form-group">
      <label> 注册手机号</label>
      <input
        type="phone"
        class="form-control"
        v-model="phone"
        placeholder="手机号或微信号"
      />
    </div>
    <div class="form-group">
      <label> Password</label>
      <input
        type="password"
        class="form-control"
        v-model="password"
        placeholder="密码"
      />
    </div>

    <button class="btn btn-primary btn-block">Login</button>
    <h2>Response Status={{ log_status }} UserName={{ log_name }}</h2>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "MyLogin",
  data() {
    return {
      phone: "",
      password: "",
      log_status: " OFF",
      log_name: "None",
    };
  },
  methods: {
    async handleSubmit() {
      const response = await axios.post("vuelogin", {
        phone: this.phone,
        password: this.password,
      });
      console.log("Return=", response);
      if (response.data.status == "Success") {
        this.log_status = "ON";
        this.log_name = response.data.username;
        this.$router.push({
          name: "home",
          params: { username: this.log_name },
        });
      }
    },
  },
};
</script>

<style scoped>
h1 {
  text-align: left !important;
  font-weight: 800;
  color: rgba(36, 109, 225, 0.884);
}

label,
button {
  text-align: left !important;
  font-weight: 800;
  font-size: 25px;
  margin: 0;
  line-height: 1;
  padding-bottom: 10px;
}
</style>
