from board import *
import pandas as pd


# TODO: count the number of simulations locally

class Results:

    def __init__(self):
        # Generate an empty array to save the times a player has passed a tile
        self.hits = [0] * 41

    def addHitResults(self, hits):
        # Add hits given to the local hits array
        for i in range(0, 41):
            self.hits[i] += hits[i]

    def write(self, totalGame, totalRound):

        out = pd.DataFrame({'Place': Board.TILE_NAME,  'Hit' : self.hits, 'Color':Board.color, 'Number of Games': totalGame,
                            'Number of Round': totalRound, 'Ev/Otel Dikme Ücreti': Board.ev, 'Tapu': Board.fiyat, '0 Ev Kira': Board.kira0,
                            '1 Ev Kira': Board.kira1, '2 Ev Kira': Board.kira2, '3 Ev Kira': Board.kira3, '4 Ev Kira': Board.kira4,
                            'Otel Kira': Board.kiraOtel})

        out.to_csv('out.csv', encoding='utf-8')
