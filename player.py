from random import randint


class Player:
    VERSION = "1.7.3"

    def bet_request(self, game_state):
        # small_blind = game_state['small_blind']
        #
        # highest_bet = self.get_player_bets(game_state)
        #
        # if highest_bet > small_blind * 2:
        #     return highest_bet + small_blind
        #
        # else:

        for player in game_state["players"]:
            if player["name"] == "TheJoker":
                return player["stack"]

        # return game_state["players"][game_state["in_action"]]["stack"]

    def showdown(self, game_state):
        pass

    def get_player_bets(self, game_state):

        player_bet = 0

        for player in game_state['players']:
            if player_bet < player_bet['bet']:
                player_bet = player['bet']

        return player_bet
