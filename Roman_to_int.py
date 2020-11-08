"""Given a roman numeral, convert it to an integer."""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 ," ":0 }
        num = 0
        s = s+" "
        j = 0
        while j < (len(s)-1):
            
            if roman[s[j]] >= roman[s[j+1]]:
                num += roman[s[j]]

            if roman[s[j]] < roman[s[j+1]]:
                c = abs(roman[s[j]] - roman[s[j+1]])
                num += c
                j+=1 
            j+=1
        return num
