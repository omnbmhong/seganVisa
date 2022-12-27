<template>
  <form @submit.prevent="handleSubmit">
    <h3>Sign Up 新用户注册</h3>
    <div class="form-group">
      <label> First Name</label>
      <input
        type="text"
        class="form-control"
        v-model="first_name"
        placeholder="名"
      />
    </div>

    <div class="form-group">
      <label> Last Name</label>
      <input
        type="text"
        class="form-control"
        v-model="last_name"
        placeholder="姓"
      />
    </div>

    <div class="form-group">
      <label> Phone Number</label>
      <input
        type="text"
        class="form-control"
        v-model="phone"
        placeholder="手机号或微信号"
      />
    </div>

    <div class="form-group">
      <label> Email</label>
      <input
        type="text"
        class="form-control"
        v-model="email"
        placeholder="电子邮箱"
      />
    </div>

    <div class="form-group">
      <label> Password</label>
      <input
        type="text"
        class="form-control"
        v-model="password"
        placeholder="设置您的密码"
      />
    </div>

    <div class="form-group">
      <label> Re-Confirm Password</label>
      <input
        type="text"
        class="form-control"
        v-model="password_confirm"
        placeholder="再次确认您的密码"
      />
    </div>

    <button class="btn btn-primary btn-block">Sign Up</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "MyRegister",
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      password: "",
      password_confirm: "",
    };
  },
  methods: {
    async handleSubmit() {
      const response = await axios.post("register", {
        first_name: this.first_name,
        last_name: this.last_name,
        password: this.password,
        password_confirm: this.password_confirm,
        email: this.email,
        phone: this.phone,
      });
      console.log(response);
      //@@@@尝试使用 render template后端路由时，暂时停用该转向
      this.$router.push("/login");
    },
  },
};
</script>

<style scoped>
button,
h3,
label,
span {
  font-weight: 600;
  font-size: 16px;
  font-family: "Fira Sans", sans-serif;
  margin: 5px;

  padding: 6px 6px 6px 15px;
}
</style>
