// This is the minesweeper client module

let fetch = require("isomorphic-unfetch")

class MineSweeperClient {
  // This is the API Client class for minesweeper
  constructor() {
    this.basePath = process.env.BASE_URL || "https://cloudaleapi.ue.r.appspot.com/api/v1"
    this.debug = parseInt(process.env.DEBUG || 0)
    this.game = null
  }

  async request(endpoint = "", options = {}) {
    // Make a request to the backend API
    let url = this.basePath + endpoint
    let headers = { "Content-type": "application/json" }
    let config = { ...options, headers }

    try {
      const response = await fetch(url, config)
      return response
    } catch (error) {
      return error
    }

  }
  async startNewGame() {
    // Start a new game
    let url = "/games/start"
    let options = { method: "POST" }
    let response = await this.request(url, options)
    if (response.ok) {
      this.game = await response.json()
      if (this.debug) {
        this.printBoard()
      }
      return this.game
    } else {
      let error = await response.json()
      console.log(error)
      return error
    }
  }

  async pickSlot(gameId, pick) {
    // Pick a slot in the board
    let options = {
      method: "POST",
      body: JSON.stringify(pick)
    }
    let response = await this.request("/games/" + gameId + "/pick-slot", options)
    if (response.ok) {
      this.game = await response.json()
      if (this.debug) {
        this.printBoard()
      }
      return this.game
    } else {
      let error = await response.json()
      console.log(error)
      return error
    }
  }

  printBoard() {
    // Print board in console
    console.log(' ')
    let header = '   ' + [...Array(this.game.board.slots[0].length).keys()].join(' ')
    console.log(header)
    for (let i = 0; i < this.game.board.slots.length; i++) {
      let row = i + ' '
      for (let j = 0; j < this.game.board.slots[i].length; j++) {
        let slot = this.game.board.slots[i][j]
        if (slot.available && slot.mine) {
          row += ' ~'
        } else if (slot.available && !slot.mine) {
          row += ' ·'
        } else if (!slot.available && slot.mine) {
          row += ' X'
        } else if (!slot.available && !slot.mine) {
          row += '  '
        }
      }
      console.log(row)
    }
    console.log(' ')
  }
}

exports.MineSweeperClient = MineSweeperClient