from flask import render_template, request

from app import app

from models.player import *
from models.game import *

import random

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
    return render_template('game.html', title="Results - ", player_1=player_1, player_2=player_2, winner=game.winner, result=result)

@app.route("/play", methods=["get"])
def play():
    return render_template("play.html", title="Play - ")

@app.route("/play", methods=["post"])
def game():
    name = request.form["name"]
    choice = request.form["choice"]
    player_1 = Player(name, choice)
    c_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(c_list)
    player_2 = Player("Computer", computer_choice)
    game = Game(player_1, player_2)
    game.result_of_the_game()
    result = game.winner
    return render_template('game.html', title="Results - ", player_1=player_1, player_2=player_2, winner=game.winner, result=result)
