#https://www.codewars.com/kata/5739174624fc28e188000465/train/python
class PokerHand(object):
    s_p = ["S", "C", "D", "H"]          #Suits possible, this table is used to check suits of hand.
    v_c = {"A":14, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13} #value conversion, converting card values to numerical values for easier comparison.
    attributes_tier = {"high_card": 1, "pair":2, "two_pair":3, "three_of_a_kind":4,"straight":5, "flush":6, "full_house":7, "four_of_a_kind":8, "straight_flush":9, "royal_flush":10}

    def __init__(self, hand):
        self.hand_values = [PokerHand.v_c[a] for a in [v[0] for v in hand.split()]]           #Splitting the parameter and separating them to to values and suits to create a dictionary.
        self.hand_suits = [v[1] for v in hand.split()]
        self.tier = 0                                             #We will be using tiers to 'rate' different types of hands.
        self.v_tier = 0                                           #Assuming same type of hand, value tier will be used to break ties.
        self.kickers = set()
        self.pairs = set()
        self.attributes = set()
        self._value_check()
        self._tier_check()
    
    def _value_check(self):
        for suit in PokerHand.s_p:
            if suit in self.hand_suits:
                if list(self.hand_suits).count(suit) == 5:   #checking for flush
                    self.attributes.add("flush")
        self.hand_check = sorted(list(self.hand_values))
        self._max = max(self.hand_check)
        self._min = min(self.hand_check)
        if self._max - self._min == 4:             #beginning of straight check
            self.straight_check = [i for i in range(self._min,self._max+1)]
            if self.straight_check == self.hand_check:
                self.attributes.add("straight")
                self.v_tier = self._max
            if self._min == 10 and self._max == 14 and "flush" in self.attributes:
                self.attributes.clear()
                self.attributes.add("royal_flush")
        for value in self.hand_check:                #checking for 2, 3 and 4 of a kind.
            if self.hand_check.count(value) == 4:
                self.attributes.add("four_of_a_kind")
                self.v_tier = value
            elif self.hand_check.count(value) == 3:
                self.attributes.add("three_of_a_kind")
                self.v_tier = value
            elif self.hand_check.count(value) == 2:
                self.pairs.add(value)
                if "pair" in self.attributes and len(self.pairs) == 2:
                    self.attributes.add("two_pair")
                else:
                    self.attributes.add("pair")
                if "three_of_a_kind" not in self.attributes:
                    self.v_tier = max(self.pairs)
            if self.hand_check.count(value) == 1: #adding single cards to kickers to compare in the case of tie
                self.kickers.add(value)
        if "straight" in self.attributes and "flush" in self.attributes:
            self.attributes.clear()
            self.attributes.add("straight_flush")
        if "two_pair" in self.attributes and "pair" in self.attributes:
            self.attributes.remove("pair")
        if "three_of_a_kind" in self.attributes and "pair" in self.attributes:
            self.attributes.clear()
            self.attributes.add("full_house")
        if not any(n for n in list(PokerHand.attributes_tier.keys()) if n in self.attributes and n != "high_card"): #If no value patterns, vtier is = highest num
            self.attributes.add("high_card")
            self.v_tier = max(self.kickers)
                    
    def _tier_check(self):                                        #assigns a value, higher value the bigger. ie. a flush would always beat a pair. Will be used for comparison later.
        for attribute in self.attributes:
            self.tier = PokerHand.attributes_tier.get(attribute)
        
    def _kicker_tb(self, other):
        try:
            while max(self.kickers) == max(other.kickers):
                self.kickers.remove(max(self.kickers))
                other.kickers.remove(max(other.kickers))
        except:
            return "Tie"
        try:
            if max(self.kickers) > max(other.kickers):
                return "Win"
            if max(self.kickers) < max(other.kickers):
                return "Loss"
        except:
            return "Tie"
        
    def compare_with(self, other):
        if self.tier > other.tier:
            return "Win"
        elif self.tier < other.tier:
            return "Loss"
        else:
            if self.v_tier > other.v_tier:
                return "Win"
            elif self.v_tier < other.v_tier:
                return "Loss"
            else:
                if self.tier == 5 or self.tier == 9 or self.tier == 10:
                    return "Tie"
                elif self.tier == 8 or self.tier == 6 or self.tier == 4 or self.tier == 2 or self.tier == 1: #four of a kind; tie breaker
                    return self._kicker_tb(other)
                elif self.tier == 7: #Fullhouse tie breaker
                    if max(self.pairs) > max(other.pairs):
                        return "Win"
                    elif max(self.pairs) < max(other.pairs):
                        return "Loss"
                    else:    
                        return "Tie"    
                elif self.tier == 3:  #two pair tiebreaker
                    try:
                        while max(self.pairs) == max(other.pairs): 
                            self.pairs.remove(max(self.pairs))
                            other.pairs.remove(max(other.pairs))
                    except:
                        pass
                    return self._kicker_tb(other)
