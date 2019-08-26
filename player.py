
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        small_blind = game_state['small_blind']
        return small_blind * 2

    def showdown(self, game_state):
        pass

