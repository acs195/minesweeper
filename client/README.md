# Client API

## Install npm packages
```
npm install
```

## Usage:
```
let apiClientLib = require('./minesweeper-client/index')
let apiClient = new apiClientLib.MineSweeperClient()
apiClient.startNewGame().then(() => {
  apiClient.printBoard()
  apiClient.pickSlot(apiClient.game.id, {x:7, y:1}).then(() => {
    apiClient.printBoard()
  })
})
```

## Test
```
npm test
```