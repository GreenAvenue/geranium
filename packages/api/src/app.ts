import * as express from "express";
import * as bodyParser from "body-parser";
import * as awsServerlessExpressMiddleware from "aws-serverless-express/middleware";

// import usersController from "./controllers/users";

// declare a new express app
const app = express();
app.use(bodyParser.json());
app.use(awsServerlessExpressMiddleware.eventContext());

// Enable CORS for all methods
app.use((req, res, next) => {
	res.header("Access-Control-Allow-Origin", "*");
	next();
});

const router = require("express-promise-router")();
router.get("/", async (req, res) => {
	res.json({
		meta: {
			status: 200,
		},
		data: {
			url: req.url,
		},
	});
});
app.use(router);

app.use("/", router);

app.listen(3000, () => {
	console.log("App started");
});

export default app;
