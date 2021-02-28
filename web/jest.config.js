module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  collectCoverage: true,
  collectCoverageFrom: [
    'src/**/*.{ts,vue}',
    '!src/main.ts',
  ],
  transform: {
    '^.+\\.(ts|tsx)?$': 'ts-jest',
    "^.+\\.(js|jsx)$": "babel-jest",
    ".*\\.(vue)$": "vue-jest",
    '.+\\.(css|styl|less|sass|scss|svg|png|jpg|ttf|woff|woff2)$': 'jest-transform-stub',
  },
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
    // support react css files
    '\\.(css|less)$': '<rootDir>/tests/__mocks__/styleMock.js'
  },
  // set environment variables
  setupFiles: ["<rootDir>/tests/unit/mocks/setEnvVars.js",
               "<rootDir>/tests/unit/mocks/setupTests.js"],
  // ignore file path
  modulePathIgnorePatterns: [
    "<rootDir>/src/i18n.js",
  ]
};
