class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_dict = {
            0: "Love", 
            1: "Fifteen", 
            2: "Thirty",
            3: "Forty"
        } 

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.get_equal_score()
        
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_advantage_or_win()
        
        else:
            score = self.standard_score()

        return score

    def get_equal_score(self):
        score = ""
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"

        return score
    
    def get_advantage_or_win(self):
        score = ""
        minus_result = self.player1_score - self. player2_score
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
                score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score


    def standard_score(self):
        return f"{self.score_dict[self.player1_score]}-{self.score_dict[self.player2_score]}"