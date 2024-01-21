class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict to store anagrams grouped by their sorted representation
        map_anagram = defaultdict(list)

        # Iterate through all the words in the input list
        for word in strs:
            # Sort the characters of the word and use it as a key in the map_anagram
            sorted_word = ''.join(sorted(word))
            map_anagram[sorted_word].append(word)

        # Return the grouped anagrams as a list of lists
        return list(map_anagram.values())
