import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/",
		name: "Home",
		component: () => import("@/pages/home/HomePage.vue"),
	},
	{
		path: "/shop/:id",
		name: "Store",
		component: () => import("@/pages/shop/stores.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
