class Player:
    VERSION = "2.2"

    players = None
    my_id = None

    def betRequest(self, game_state):
        self.players = game_state["players"]
        self.my_id = game_state["in_action"]

        bet = self.get_my_stack()
        return bet

    def get_my_stack(self):
        for player in self.players:
            if player["id"] == self.my_id:
                stack = int(player["stack"])
                return stack

    def showdown(self, game_state):
        pass