class Player:
    VERSION = "2.0.1"

    def betRequest(self, game_state):

        for player in game_state["players"]:
            if player["id"] == game_state["in_action"]:
                print(player["stack"])
                return int(player["stack"])

    def showdown(self, game_state):
        pass

    def get_hole_cards(self, game_state):
        hole_cards = game_state["players"][game_state["in_action"]]["hole_cards"]
        print(f"kutyámajom - hole cards: {hole_cards}")
        return hole_cards

    def get_com_cards(self, game_state):
        com_cards = game_state["community_cards"]
        print(f"kutyámajom - community cards: {com_cards}")
        return com_cards

    def get_player_bets(self, game_state):
        player_bet = 0
        for player in game_state['players']:
            if player_bet < player_bet['bet']:
                player_bet = player['bet']
        print(f"kutyámajom - player bets: {player_bet}")
        return player_bet

    def bet_everything(self, game_state):
        return game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"]
