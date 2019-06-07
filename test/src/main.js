import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import User from "./components/User";
import Home from "./components/Home";

Vue.use(VueRouter);
Vue.config.productionTip = false;

const routes = [
  { path: "/users/:Id", component: User },
  { path: "/home", component: Home }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
