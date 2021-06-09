from mrjob.job import MRJob
import re
from collections import defaultdict




def sublistCheck(data, list_data):
    for i in list_data:
        for x in data:
            if(x in i):
                return 0

    return 1


word_lower = []

line_regex = re.compile(r"[\w']+")
class MRSimilarWord(MRJob):
    def mapper(self, _, file):
        for text in line_regex.findall(file):
            word_lower.append(text.lower())

        word_lower.sort()
        # when list object is passed to defaultdict then values of dictionary is list
        dict_listdata = defaultdict(list)
        # looping over each word in list
        for word in word_lower:
            dict_listdata[str(sorted(word))].append(word)
        # similar pairs
        sim_pairs = list(dict_listdata.values())

        temp = []
        for i in sim_pairs:
            if (len(i) > 1):
                cond = sublistCheck(i, temp)
                if (cond == 1):
                    temp.append(i)
                    yield i, len(i)
    def reducer(self, word, cond):
        yield word, len(word)


if __name__ == '__main__':
    MRSimilarWord.run()
