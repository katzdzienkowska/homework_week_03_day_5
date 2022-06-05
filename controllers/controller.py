from flask import render_template

from app import app

from models.player import *
from models.game import *

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<player_1_choice>/<player_2_choice>')
def result(player_1_choice, player_2_choice):
    player_1 = Player("Player1", player_1_choice)
    player_2 = Player("Player2", player_2_choice)
    game = Game(player_1, player_2)
    game.result_of_the_game()
    result = game.winner
    return render_template('game.html', player_1=player_1, player_2=player_2, winner=game.winner, result=result)