# Client API

## Usage:
```
let apiClientLib = require('../minesweeper-client/index');
let apiClient = new apiClientLib();

apiClient
  .startNewGame()
  .then(data => console.log(data));
```

## Test
```
npm test
```