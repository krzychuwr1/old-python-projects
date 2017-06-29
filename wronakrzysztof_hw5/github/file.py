from collections import Counter
import re


class File:
    """
    Class containing name of file, its content, length and score.
    File score is calculated by count_score.
    pointed_words is a static tuple which contains words which are awarded scores.
    """
    pointed_words = ("variable", "equivalent", "epiphany", "variables", "exception", "#", "class", "dutch")

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.length = len(content)
        self.score = 0

    def count_score(self):
        """
        Pretty self-explanatory, counts points using other __count functions.
        :return: none
        """
        self.__check_pointed()
        self.__count_white()
        self.score /= (self.length+1)

    def __count_words(self):
        """
        Counts different words and puts the result to dictionary called counts.
        :return:
        """
        self.counts = Counter()
        self.counts.update(word.strip("\"").lower() for word in re.split('\)|\(|;|,|\n| |=|\[|\]|\.', self.content))

    def __check_pointed(self):
        """
        Gives 1000 points for every occurrence of a pointed word.
        :return:
        """
        self.__count_words()
        for word in File.pointed_words:
            self.score += self.counts[word]*1000

    def __count_white(self):
        """
        Gives 100 points for every endline.
        :return:
        """
        self.score += self.content.count('\n')*100
