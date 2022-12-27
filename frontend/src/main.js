import { createApp } from "vue";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.min.css";
import router from "./routers";
import "./axios";
import Datepicker from "vue3-datepicker";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import store from "./store";

const app = createApp(App);
app.use(router);
app.use(ElementPlus);
app.use(Datepicker);
app.use(store);
app.mount("#app");
