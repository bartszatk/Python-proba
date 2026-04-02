class Analyzer:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r") as f:
            return f.read()

    def word_count(self):
        return len(self.read().split())

    def char_count(self):
        return len(self.read())

    def most_common_word(self):
        words = self.read().lower().split()
        freq = {}

        for w in words:
            freq[w] = freq.get(w, 0) + 1

        return max(freq, key=freq.get)


with open("text.txt", "w") as f:
    f.write("ala ma kota ala ma psa ala")

a = Analyzer("text.txt")

print(a.word_count())
print(a.char_count())
print(a.most_common_word())
