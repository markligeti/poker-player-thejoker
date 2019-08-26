from random import randint


class Player:
    VERSION = "1.5.3"

    def bet_request(self, game_state):
        # small_blind = game_state['small_blind']
        #
        # highest_bet = self.get_player_bets(game_state)
        #
        # if highest_bet > small_blind * 2:
        #     return highest_bet + small_blind
        #
        # else:
        # print(f"kutyámajom!")
        return game_state["current_buy_in"] - game_state["players"]["in_action"]["bet"]

    def showdown(self, game_state):
        pass

    def get_hole_cards(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "TheJoker":
                return player["hole_cards"]

    def get_com_cards(self, game_state):
        return game_state["community_cards"]

    def get_player_bets(self, game_state):
        player_bet = 0

        for player in game_state['players']:
            if player_bet < player['bet']:
                player_bet = player['bet']

        return player_bet
