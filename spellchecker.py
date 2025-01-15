from trie import Trie

class SpellChecker:
    def __init__(self):
        self.trie = Trie()

    def check(self, word):
        return self.trie.search(word)

    def search(self, prefix):
        return self.trie.find_all_words_with_prefix(prefix)

    def change_dictionary(self, filename):
        try:
            with open(filename) as filehandle:
                words = filehandle.read()
                words = ''.join((x for x in words if not x.isdigit()))
                words = words.replace(' .', '')
                words = words.split("\n")
                for word in words:
                    self.trie.insert(word)
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")

    def get_all_words(self):
        return self.trie.get_all_words()

    def remove_word(self, word):
        return self.trie.remove_word(word)

    def main(self):
        while True:
            print("1. Check a word")
            print("2. Get word suggestions")
            print("3. Change dictionary")
            print("4. Print all words")
            print("5. Remove one word")
            print("6. Quit\n")

            inp = input("What would you like to do: ")

            if inp == "1":
                inpCheck = input("Enter word to check correct spelling: ")
                if self.check(inpCheck):
                    print("Word is spelled correctly.")
                else:
                    print("Word is not in the dictionary.")

            if inp == "2":
                inpSearch = input("Enter word to get suggestions: ")
                suggestions = self.search(inpSearch)
                if suggestions:
                    print(suggestions[:10])
                else:
                    print("No suggestions found.")

            if inp == "3":
                inpChange = input("Change dictionary: ")
                try:
                    self.change_dictionary(inpChange)
                    print("We have Change file.")
                except FileNotFoundError:
                    print("No file in that name.")

            if inp == "4":
                all_words = self.get_all_words()
                print("All words in the dictionary:", all_words)

            if inp == "5":
                inpRemove = input("Enter word to remove: ")
                if self.remove_word(inpRemove):
                    print("Word removed successfully.")
                else:
                    print("Word removed successfully.")

            if inp == "6":
                break

if __name__ == '__main__':
    sp = SpellChecker()
    sp.main()
