import requests
import json
import chess.pgn
import io
import pandas as pd
import math
import numpy as np

def get_data_by_month(username, year, month):
    url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month}"
    data = requests.get(url)
    if data.status_code != 200:
        raise Exception("The following response was returned: " + str(data.status_code))
    else:
        data = json.loads(data.text)
        games = data["games"]
        
        all_games=[]
    for game in games:
        pgn = (game['pgn'])
        pgn = io.StringIO(pgn)
        game = chess.pgn.read_game(pgn)
        all_games.append(game)