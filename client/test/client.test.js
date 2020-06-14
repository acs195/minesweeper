// This is the test module for the minesweeper client api

let chai = require('chai')
let nock = require('nock')
let gameStartResponse = require('./gameStartResponse')
let gamePickSlotResponse = require('./gamePickSlotResponse')

let apiClientLib = require('../minesweeper-client/index')
let apiClient = new apiClientLib.MineSweeperClient()

describe('Test class import', () => {
  it('should not be null', () => {
    chai.assert.isNotNull(apiClient)
  })
})


describe('Test to start a new game', () => {
  beforeEach(() => {
    // Mock backend api response
    nock('https://cloudaleapi.ue.r.appspot.com')
      .post('/api/v1/games/start')
      .reply(200, gameStartResponse)
  })
  it('should return a game object', async () => {
    let game = await apiClient.startNewGame()
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


describe('Test to pick a slot in the board', () => {
  beforeEach(() => {
    // Mock backend api response
    nock('https://cloudaleapi.ue.r.appspot.com')
      .post('/api/v1/games/4e6b3ce8-e3e1-4b6c-a304-a7677ec3005d/pick-slot')
      .reply(200, gamePickSlotResponse)
  })
  it('should return a game object with new state', async () => {
    let game = await apiClient.pickSlot(
      '4e6b3ce8-e3e1-4b6c-a304-a7677ec3005d', { x: 8, y: 8 }
    )
    chai.assert.equal(game.board.slots[7][7].available, false)
  })
})