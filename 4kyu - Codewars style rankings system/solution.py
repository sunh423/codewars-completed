#https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python
class User:
    rank_allowed = [i for i in range(-8,9) if not i == 0]
    
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def _rankup(self):
        if self.rank in User.rank_allowed:
            try:
                nxt_rank_index = User.rank_allowed.index(self.rank) + 1
                self.rank = User.rank_allowed[nxt_rank_index]
            except IndexError:
                return "You are at max level!"

    def _progress(self, num):
        self.progress += num
        while self.progress >= 100: #if for some reason, the progress is TOO much and levels more than once
                self.progress -= 100
                self._rankup()
        if self.rank == 8:
            self.progress = 0
        
    def inc_progress(self, num):
        if self.rank == num:
            self._progress(3)
        elif User.rank_allowed.index(num) - User.rank_allowed.index(self.rank)  == -1:
            self._progress(1)
        elif User.rank_allowed.index(num) - User.rank_allowed.index(self.rank)  <= -2:
            pass
        elif User.rank_allowed.index(num) - User.rank_allowed.index(self.rank) > 0:
            d = User.rank_allowed.index(num) - User.rank_allowed.index(self.rank)
            self._progress(10*d*d)
