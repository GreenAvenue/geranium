module.exports = {
	root: true,
	env: {
		node: true,
	},
	extends: [
		"airbnb-base",
	],
	plugins: [
		"@typescript-eslint/eslint-plugin",
	],
	settings: {
		"import/resolver": {
			"node": {
				"extensions": [
					".ts",
				],
			},
		},
	},
	rules: {
		"no-console": process.env.NODE_ENV === "production" ? "error" : "off",
		"no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
		"@typescript-eslint/no-unused-vars": "error",
		// sf rule: Double Quotes
		quotes: ["error", "double"],
		// sf rule: Tab Indent
		indent: ["error", "tab"],
		// sf rule: max-length is 180
		"max-len": ["error", { code: 180 }],
		// sf rule: インデントにタブは使っていい（途中のタブは駄目）
		"no-tabs": ["error", { allowIndentationTabs: true }],
		// sf rule: for ofは使っていい
		"no-restricted-syntax": ["error", "ForInStatement", "LabeledStatement", "WithStatement"],
		// sf rule: ++はloopで使っていい
		"no-plusplus": ["error", { "allowForLoopAfterthoughts": true }],
		// ts rule: disable no-inner-declarations (see: https://github.com/typescript-eslint/typescript-eslint/issues/239)
		"no-inner-declarations": "off",
		// sf rule: 一つのファイルに複数クラスを定義してもよい
		"max-classes-per-file": "off",
		// hot fix for https://stackoverflow.com/questions/59265981/typescript-eslint-missing-file-extension-ts-import-extensions
		"import/extensions": [
			"error",
			"ignorePackages",
			{
			  "ts": "never",
			  "js": "never",
			}
		 ],
		 "no-multiple-empty-lines": ["error", { "max": 1 }],
	},
	parser: "@typescript-eslint/parser",
	parserOptions: {
		parser: "@typescript-eslint/parser",
		sourceType: "module",
		project: "./tsconfig.json",
	},
};
