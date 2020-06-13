// This is the test module for the minesweeper client api

let chai = require('chai')
let nock = require('nock')
let gameStartResponse = require('./gameStartResponse')

let apiClientLib = require('../minesweeper-client/index')
let apiClient = new apiClientLib.MineSweeperClient()

describe('Test class import', () => {
  it('should not be null', () => {
    chai.assert.isNotNull(apiClient)
  })
})

 describe('Test start new game', () => {
  beforeEach(() => {
    // Mock backend api response
    nock('https://cloudaleapi.ue.r.appspot.com')
      .post('/api/v1/games/start')
      .reply(200, gameStartResponse)
  })
  it('should return a 200 response', async () => {
    const response = await apiClient.startNewGame()
    game = await response.json()
    chai.assert.equal(response.status, 200)
    chai.assert.property(game, 'id')
    chai.assert.property(game, 'board')
    chai.assert.property(game, 'player')
    chai.assert.property(game.board, 'id')
    chai.assert.property(game.board, 'slots')
    chai.assert.property(game.board, 'mines')
    chai.assert.property(game.board, 'rows')
    chai.assert.property(game.board, 'cols')
    chai.assert.property(game.player, 'id')
  })
})
