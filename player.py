class Player:
    VERSION = "1.9"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["id"] == game_state["in_action"]:
                print(player["stack"])
                return int(player["stack"])

        # return int(game_state["players"][game_state["in_action"]]["stack"])

    def showdown(self, game_state):
        pass

    def get_player_bets(self, game_state):
        player_bet = 0

        for player in game_state['players']:
            if player_bet < player_bet['bet']:
                player_bet = player['bet']

        return player_bet
