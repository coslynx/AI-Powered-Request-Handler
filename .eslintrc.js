module.exports = {
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module",
    "project": "./tsconfig.json" 
  },
  "plugins": [
    "@typescript-eslint",
    "prettier"
  ],
  "rules": {
    "indent": ["error", 2],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "double"],
    "semi": ["error", "always"],
    "no-unused-vars": "warn", 
    "no-console": "warn", 
    "prettier/prettier": [
      "error",
      {
        "endOfLine": "lf",
        "printWidth": 100,
        "singleQuote": true,
        "tabWidth": 2,
        "trailingComma": "es5",
        "bracketSpacing": true,
        "jsxBracketSameLine": false,
        "arrowParens": "always",
        "proseWrap": "never",
        "htmlWhitespaceSensitivity": "css",
        "vueIndentScriptAndStyle": true,
        "embeddedLanguageFormatting": "auto"
      }
    ]
  }
};