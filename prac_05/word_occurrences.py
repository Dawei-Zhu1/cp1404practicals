"""
CP1404 Practical 5: Word Occurrences
By Dawei Zhu
"""


def main():
    text = input('Text: ')
    words = text.split(' ')
    # Get unique elements
    unique_words = get_list_with_unique_elements(words)
    # Align style property
    display_width_of_word = get_longest_length(unique_words)
    for each_word in unique_words:
        print(f'{each_word:{display_width_of_word}} : {words.count(each_word)}')


def get_list_with_unique_elements(words):
    """Make the elements in the list unique"""
    words = list(set(words))
    words.sort()
    return words


def get_longest_length(words):
    """Get the length of the longest word"""
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    return length


main()
