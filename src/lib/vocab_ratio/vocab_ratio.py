import json
import os


class VocabRatio:
    
    '''
    Given an array of vocabularies - returns the ratio of open vocabularies to the closed vocabularies used
    '''

    def __init__(self):

        prefix_graph = dict()
        uri_detail = dict()
        
        with open('./src/lib/graph/cache/graph-lov.json') as pref_graph:
            prefix_graph = json.loads(pref_graph.read())
        
        with open('./src/lib/graph/cache/lov-prefix-uri.json') as uri_graph:
            uri_detail = json.loads(uri_graph.read())

        self.prefix_graph = prefix_graph
        self.uri_detail = uri_detail



    def get_ratio(self, vocab_list=[]):
        '''
        returns the list of open vocabularies
        '''
        count = 0
        total_count = len(vocab_list)
        
        open_vocab_list = list()

        open_vocab_set = list()
        closed_vocab_set = list()

        # index all open vocab in a list
        for each_uri in self.uri_detail:
            open_vocab_list.append(each_uri['uri'])

        if vocab_list:
            for each_vocab in vocab_list:
                if each_vocab in open_vocab_list:
                    count += 1
                    open_vocab_set.append(each_vocab)     
                else:
                    closed_vocab_set.append(each_vocab)   
        else:
            return None
        
        print open_vocab_set
        print closed_vocab_set
        return True

def main():
    test = VocabRatio().get_ratio(['http://purl.org/acco/ns','https:/github.com'])

if __name__ == '__main__':
    main()
    

