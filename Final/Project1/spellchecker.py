class SpellChecker:
    def __init_(self, filename):
        self.dictionary = populateDictionary(filename)
    
    def binarySearch(self, x, L):
        low = 0
        high = len(L)-1

        while low <= high:
            mid = (low+high)//2
            item = L[mid]
            if x == item:
                return mid
            elif x < item:
                high = mid-1
            else:
                low = mid+1

        return -1


    def populateDictionary(self, filename):
        words = []
        dictionary = open(filename, "r")
        for word in dictionary:
            words.append(word.strip())
        return words


    def spellCheck(self, word):
        if len(word) == 0:
            return True

        if word[0] in punctuation:
            return spellCheck(word[1:], self.dictionary)
        if word[-1] in punctuation:
            return spellCheck(word[:-1], self.dictionary)

        if binarySearch(word, dictionary) != -1:
            return True
        else:
            return word