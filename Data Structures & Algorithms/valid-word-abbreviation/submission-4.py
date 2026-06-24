class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pw = pabbr = 0
        while pw < len(word) and pabbr < len(abbr):
            if abbr[pabbr].isdigit():
                num = 0
                pnum = pabbr
                while pnum < len(abbr) and abbr[pnum].isdigit():
                    if not num and abbr[pnum] == '0':
                        break
                    num = num * 10 + int(abbr[pnum])
                    pnum += 1
                
                if not num:
                    return False
          
                if pabbr + num > len(word):
                    return False

                pabbr = pnum
                pw += num

            elif abbr[pabbr] != word[pw]:
                return False
            else:
                pabbr += 1
                pw += 1

        return pw == len(word) and pabbr == len(abbr)

