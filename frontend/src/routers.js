import { createRouter, createWebHistory } from "vue-router";
import Home from "./components/Home";
import HelloWorld from "./components/HelloWorld";
import MyLogin from "./components/MyLogin";
import Create from "./components/Create";
import ArticleDetails from "./components/ArticleDetails";
import MyRegister from "./components/MyRegister";

const routes = [
  {
    path: "/",
    name: "welcome",
    component: HelloWorld,
  },
  {
    path: "/home",
    name: "home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: MyLogin,
  },

  {
    path: "/register",
    name: "register",
    component: MyRegister,
  },
  {
    path: "/create",
    name: "create",
    component: Create,
  },
  {
    path: "/details/:id",
    name: "details",
    component: ArticleDetails,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
