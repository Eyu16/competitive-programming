class Solution:
    def freqAlphabets(self, s: str) -> str: 
        combinations = {
        '1': 'a','2': 'b','3': 'c','4': 'd','5': 'e','6': 'f','7': 'g','8': 'h','9': 'i','10': 'j','11': 'k','12': 'l','13': 'm','14': 'n','15': 'o','16': 'p','17': 'q','18': 'r','19': 's','20': 't','21': 'u','22': 'v','23': 'w','24': 'x','25': 'y','26': 'z',
    }
        digits = s.split("#")
        string = ""
        if '#' in s:
            for digit in digits:
                if digit != '':
                    if len(digit) > 2:
                        for i in range(len(digit)-2):
                            string += combinations[digit[i]]
                        string += combinations[digit[-2:]]
                    else:
                        if digit == s[-2:]:
                            for char in digit:
                                string += combinations[char]
                        else:
                            string += combinations[digit]
        else:
            for char in digits[0]:
                string += combinations[char]

        return string
        