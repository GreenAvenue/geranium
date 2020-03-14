import expressPromiseRouter from "express-promise-router";

const router = expressPromiseRouter();

router.get("/", (req, res) => {
	res.json({
		meta: {
			status: 200,
		},
		data: {
			values: "hoge",
		},
	});
});
