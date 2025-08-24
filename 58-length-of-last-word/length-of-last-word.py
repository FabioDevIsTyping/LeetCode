class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        # Scansiona da destra verso sinistra
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':   # se trovo spazio
                if counter > 0:   # ma ho già contato dei caratteri => parola finita
                    return counter
            else:
                counter += 1
        return counter
