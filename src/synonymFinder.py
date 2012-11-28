__author__ = 'msinghal'

import textwrap
from nltk.corpus import wordnet as wn

if __name__=='__main__':
	
    POS = {
        'v': 'verb', 'a': 'adjective', 's': 'satellite adjective',
        'n': 'noun', 'r': 'adverb'}

    def info(word, pos=None):
        synonymSets = wn.synsets(word, pos)
        for i, synonymSet in enumerate(synonymSets):
            synonyms = [n.replace('_', ' ') for n in synonymSet.lemma_names]
            definition= textwrap.wrap(synonymSet.definition, 64)
            print 'sense %d (%s)' % (i + 1, POS[synonymSet.pos])
            print 'definition: ' + ('\n            ').join(definition)
            print '  synonyms:', ', '.join(synonyms)
            if synonymSet.examples:
               print '  examples: ' + ('\n            ').join(synonymSet.examples)
            print

    info('happy')
