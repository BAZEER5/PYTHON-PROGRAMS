class wordbyword:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

print(wordbyword().reverse_words('hello .py'))
