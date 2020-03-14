import * as awsServerlessExpress from "aws-serverless-express";
import app from "./app";

const server = awsServerlessExpress.createServer(app);

exports.handler = (event, context) => {
	console.log(`EVENT: ${JSON.stringify(event)}`);
	awsServerlessExpress.proxy(server, event, context);
};
