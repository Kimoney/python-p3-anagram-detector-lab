# your code goes here!
anagrams = [
    "inlets",
    "angered",
    "are",
    "beak",
    "ear"
]

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, word):
        self._word = word

    def match(self, anagrams):
        input_word = sorted(self.word.lower())
        matched_list = list()
        for i in anagrams:
            if (sorted(i.lower()) == input_word and i.lower() != self.word.lower()):
                matched_list.append(i)
        print(matched_list)
        return matched_list

mine = Anagram("rae")
print(mine.word)
mine.match(anagrams)