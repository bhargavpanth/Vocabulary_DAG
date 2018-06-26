from __future__ import division
import json
from sets import Set
import sys

class GraphMatch():


    def __init__(self, vocab_list):
        prefix_graph = dict()
        uri_detail = dict()

        cross_domain = dict()
        geography = dict()
        life_science = dict()

        # clean this section into a higher order function
        with open('./src/lib/graph/cache/graph-lov.json') as pref_graph:
            prefix_graph = json.loads(pref_graph.read())

        with open('./src/lib/graph/cache/lov-prefix-uri.json') as uri_graph:
            uri_detail = json.loads(uri_graph.read())

        with open('./src/lib/graph/cache/domain/cross-domain/cross_domain.json') as cr_domain:
            cross_domain = json.loads(cr_domain.read())

        with open('src/lib/graph/cache/domain/geography/geography.json') as geo:
            geography = json.loads(geo.read())

        with open('src/lib/graph/cache/domain/life-science/life-science.json') as ls:
            life_science = json.loads(ls.read())

        self.prefix_graph = prefix_graph
        self.uri_detail = uri_detail
        
        self.cross_domain = cross_domain
        self.geography = geography
        self.life_science = life_science
        
        self.vocab_list = vocab_list


    # returns vocab set from each domain passed
    def utils_vocab_set_generator(self, domain):
        domain_set = Set()
        for each_cross_domain_dataset in domain:
            for vocab_space in each_cross_domain_dataset['vocab']:
                domain_set.add(vocab_space)
        return domain_set


    def utils_common_vocab_list(self, domain_set):
        # set(A) - (set(A) - set(B))
        return set(domain_set) - (set(domain_set) - set(self.vocab_list))


    def naive_bayes(self):
        pass


    def match(self):
        '''
        '''
        cross_dom = self.utils_vocab_set_generator(self.cross_domain)
        # self.utils_common_vocab_list(cross_dom)
        geo_dom = self.utils_vocab_set_generator(self.geography)
        # self.utils_common_vocab_list(geo_dom)
        life_science = self.utils_vocab_set_generator(self.life_science)
        # self.utils_common_vocab_list(life_science)
        cd = len(self.utils_common_vocab_list(cross_dom))
        gd = len(self.utils_common_vocab_list(geo_dom))
        lsd = len(self.utils_common_vocab_list(life_science))
        
        # print 'Cross Domain : ', (cd / (cd + gd + lsd))
        # print 'Geography : ', (gd / (cd + gd + lsd))
        # print 'Life Sciences : ', (lsd / (cd + gd + lsd))
        


def main():
    # list_vocab = sys.argv[1]
    test = GraphMatch(["http://dbpedia.org/ontology/",
                       "http://www.w3.org/2000/01/rdf-schema#",
                       "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                       "http://www.w3.org/ns/prov#"])
    
    test.match()

if __name__ == '__main__':
    main()
