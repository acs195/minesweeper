// This is the minesweeper client module

let fetch = require("isomorphic-unfetch")

class MineSweeperClient {
  // This is the API Client class for minesweeper
  constructor() {
    this.basePath = "https://cloudaleapi.ue.r.appspot.com/api/v1"
  }

  async request(endpoint = "", options = {}) {
    // Make a request to the backend API
    let url = this.basePath + endpoint
    let headers = {"Content-type": "application/json"}
    let config = {...options, headers}

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
    let options = {method: "POST"}
    let response = await this.request(url, options)
    return response
  }
}

exports.MineSweeperClient = MineSweeperClient
