"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of longest word)) 
lookup time making it an optimal approach when space is not an issue.
"""


class TrieNode:
    def __init__(self):
        self.nodes = dict()  # Mapping from char to TrieNode
        self.is_leaf = False

    def insert_many(self, words: [str]):
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def match(self, prefix: str) -> [str]:
        """
        gets the list of all the words that
        are followed by certain prefix.
    
        long-url: https://www.geeksforgeeks.org/prefix-matching-python-using-pytrie-module/
        :param prefix: the prefix to be matched
        :return: List of prefix-matched words.

        """
        pass


        def search(t: TrieNode, prefix: str) -> TrieNode:

            '''
            Different search function that returns the sub trie
            instead of True or False
            :param t: self
            :param prefix: prefix to be searched
            :return: a new sub-trie
            
            '''
            curr = t
            for char in prefix:
                if char not in curr.nodes:
                    return False
                    break
                curr = curr.nodes[char]
            return curr

        def dfs(root: TrieNode, s: str, prefix: str, lst):
            """Returns a list with prefixes and their TrieNode"""
            for i in root.nodes:
                if root.is_leaf:
                    lst.append((prefix + s, root.nodes[i]))
                else:
                    dfs(root.nodes[i], s + i, prefix, lst)
            return lst

        sub_trie= search(self, prefix)
        if sub_trie==False:
            return False
        else:
            lst=[]
            l= dfs(sub_trie, '', prefix, lst)
            return l




    def delete(self, word: str):
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """

        def _delete(curr: TrieNode, word: str, index: int):
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str):
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)


def test_trie():
    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    root.insert_many(words)
    # print_words(root, "")
    assert all(root.find(word) for word in words)
    assert root.find("banana")
    assert not root.find("bandanas")
    assert not root.find("apps")
    assert root.find("apple")
    assert root.find("all")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")
    assert root.match("ban")
    return True


def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "works!" if passes else "doesn't work :(")


def pytests():
    assert test_trie()


def main():
    """
    >>> pytests()
    """
    print_results("Testing trie functionality", test_trie())


if __name__ == "__main__":
    main()
