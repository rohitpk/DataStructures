
global accumalator
accumalator = ''
END = '_LAST'
test = "An Apple a Day is better than Appricot"
sentence = test.lower().split()

def make_trie(words=sentence):
    '''
    Function to create Trie
    '''
    trie_dict = dict()
    #Iterate Word by Word
    for word in words:
        lc = 0
        holding_dict = trie_dict
        #Iterate each letter to construct TRIE
        for letter in word:
            lc+=1
            holding_dict = holding_dict.setdefault(letter, {})
            #Store letter count in lc for each word in the _LAST node
        holding_dict[END] = lc

    return trie_dict


def find_prefixes(trie, prefix):
    '''
    Function to populate trie for the given prefix
    '''
    curr_node = trie.copy()
    #Iterate and proceed if the character exist; raise otherwise
    for character in prefix:
        if character in curr_node:
            curr_node = curr_node[character]
        else:
            print "Now Exiting"
            raise ValueError('Input Prefix Does not Exist')
    return curr_node

def iterate_for_prefix(dictionary, key=END):
    '''
    Recursive function to iterate the remaning prefix dictionary till the end.
    '''
    global accumalator
    for k, v in dictionary.iteritems():
        #Check till end and keep on forming the word char by char
        if k!=END:
            accumalator=accumalator+k
        #Accumalate and return it when found end of the branch
        else:
            temp = accumalator
            accumalator=''
        if k == key:
            yield {v:temp}
        #Recursive call to iterate through the dictionary
        elif isinstance(v, dict):
            for result in iterate_for_prefix(v):
                yield result


def suggest_longest_prefix(word):
    '''
    Wrapper function to suggest longest prefix
    '''
    longest_suggestion = []
    max_=0
    #Create Trie
    trie =  make_trie(sentence)
    #Get Prefix Tree by given Prefix
    suggestion_trie = find_prefixes(trie,word)
    #Iterate Prefix tree brances to formulate the word(Recursive)
    suggestions = list(iterate_for_prefix(suggestion_trie))

    #Sort and get longest suggestions
    for suggestion in suggestions:
        val =suggestion.keys()[0]
        #Populate the maximum suggestion
        if  val > max_:
            longest_suggestion.append(word+suggestion[val])
            max_ = val
        #Populate if there are two suggestions of same length
        elif val==max_:
            longest_suggestion.append (word+suggestion[val])

    return longest_suggestion

if __name__=='__main__':
    print "Input:",test
    print "Suggestion:",suggest_longest_prefix('ap')
    
    '''
    Input: An Apple a Day is better than Appricot
    Suggestion: ['appricot']
    '''
    
