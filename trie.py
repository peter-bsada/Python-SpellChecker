from node import TrieNode

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def find_all_words_with_prefix(self, prefix):
        results = []

        def dfs(node, current_prefix):
            if node.is_end_of_word:
                results.append(current_prefix)

            for char, child_node in node.children.items():
                dfs(child_node, current_prefix + char)

        node = self.root
        for char in prefix:
            if char not in node.children:
                return results
            node = node.children[char]

        dfs(node, prefix)
        return results

    def get_all_words(self):
        results = []
        self._get_all_words_recursive(self.root, "", results)
        return results

    def _get_all_words_recursive(self, node, current_word, results):
        if node.is_end_of_word:
            results.append(current_word)

        for char, child_node in node.children.items():
            self._get_all_words_recursive(child_node, current_word + char, results)

    def remove_word(self, word):
        return self._remove_word_recursive(self.root, word, 0)

    def _remove_word_recursive(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False

        should_delete = self._remove_word_recursive(node.children[char], word, index + 1)

        if should_delete:
            del node.children[char]

        return len(node.children) == 0
