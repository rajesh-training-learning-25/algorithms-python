from typing import List


class SuffixArray:
    def __init__(self, text: str) -> None:
        """
        Initializes the class with the input text and builds the suffix and LCP arrays.
        """
        self.text = text
        self.suffix_array = self.build_suffix_array()
        self.lcp_array = self.build_lcp_array()

    def build_suffix_array(self) -> List[int]:
        """
        Builds the suffix array for the input string.
        Returns the suffix array (a list of starting indices of suffixes in sorted order).

        Example:
        >>> sa = SuffixArray("banana")
        >>> sa.suffix_array
        [5, 3, 1, 0, 4, 2]
        """
        n = len(self.text)
        suffixes = sorted(range(n), key=lambda i: self.text[i:])
        return suffixes

    def build_lcp_array(self) -> List[int]:
        """
        Builds the LCP (Longest Common Prefix) array for the suffix array.
        LCP[i] gives the length of the longest common prefix of the suffixes starting at suffix_array[i] and suffix_array[i-1].

        Example:
        >>> sa = SuffixArray("banana")
        >>> sa.lcp_array
        [0, 1, 3, 0, 0, 2]
        """
        n = len(self.text)
        suffix_array = self.suffix_array
        rank = [0] * n
        lcp = [0] * n

        # Build the rank array where rank[i] gives the position of the suffix starting at index i
        for i, suffix in enumerate(suffix_array):
            rank[suffix] = i

        h = 0
        for i in range(n):
            if rank[i] > 0:
                j = suffix_array[rank[i] - 1]
                while (
                    (i + h < n) and (j + h < n) and self.text[i + h] == self.text[j + h]
                ):
                    h += 1
                lcp[rank[i]] = h
                if h > 0:
                    h -= 1
        return lcp

    def display(self) -> None:
        """
        Displays the suffix array and LCP array for the input string.

        Example:
        >>> sa = SuffixArray("banana")
        >>> sa.display()
        Suffix Array:
        5: a
        3: ana
        1: anana
        0: banana
        4: na
        2: nana

        LCP Array:
        LCP between a and ana: 1
        LCP between ana and anana: 3
        LCP between anana and banana: 0
        LCP between banana and na: 0
        LCP between na and nana: 2
        """
        print("Suffix Array:")
        for idx in self.suffix_array:
            print(f"{idx}: {self.text[idx:]}")

        print("\nLCP Array:")
        for i in range(1, len(self.lcp_array)):
            print(
                f"LCP between {self.text[self.suffix_array[i - 1]:]} and {self.text[self.suffix_array[i]:]}: {self.lcp_array[i]}"
            )


# Example usage:
if __name__ == "__main__":
    text = "banana"
    sa = SuffixArray(text)
    sa.display()
