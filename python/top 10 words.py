#given a word document. Essay or book. Top ten most used words
#return top 10 words in Essay or book

def top10words(document):
    #WHITELIST = 'abcdefghijklmnopqrstuvwxyz'
    
    document = document.lower()
    words = document.split(' ')
    
    dictionary = {}
    
    for word in words: 
        if word in dictionary:
            dictionary[word] +=1
        
        else:
            dictionary[word] = 1
            
    #{word: 1, like: 2 , this: 3}
    #after for loop we have dictionary of word counts
    
    top_10 = {}
    
    for word in dictionary:
        
        if len(top_10) < 10:
            top_10[word] = dictionary[word]
            
        elif dictionary[word] > min(top_10):
            top_10[word] = dictionary[word]
            
            #check to find the smallest and remove it
            for i in top_10:
                if top_10[i] == min(top_10):
                    top_10.pop(i)
                    
    #top 10 should have only top 10 words used in document
    
    return [i for i in top_10] 
            
        
                    
document = 'testing for Facebook for'
docuemnt = 'testing for facebook for '
words = ['testing', 'for', 'facebook', 'for']

dictionary ={}

word = testing
dictionary = {testing: 1}

word = for
dictionary = {testing: 1, for: 1}

word = facebook
dictionary = {testing: 1, for: 1, facebook: 1}

word = for
dictionary = {testing: 1, for: 2, facebook: 1}

#pretend 
#dictionary = {testing: 1, for: 2, facebook:1, this: 3}


top_10 =  {}

for word in dictionary:
    word = testing
    len(top_10)=0 < 3:
        top_10 = {testing: dictionary[testing]}= {testing: 1}
        
    word = for
    len(top_10)=1 < 3:
        top_10 = {testing: 1, for:2}
        
    
    word = facebook
    len(top_10) = 2 < 3:
        top_10 = {testing:1, for: 2, facebook: 1}
        
    word = this
    len(top_10) =3 !<3:
    
    is dictionary(this) > min(top_10) => 3 > 1 => True
        insert word into top_10 => top_10 = {testing: 1, for: 2, facebook:1 , this:3}
        
        for i in top_10:
            i = testing
            top_10[testing] = 1 == min(top_10) =1 => yes so remove 'testing' from top_10
                top_10.pop(testing) => {for: 2, facebook: 1, this: 3}
                
    
    return [for, facebook, this]
                
            
        
            
    
