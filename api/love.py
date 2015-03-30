#coding:utf-8:
#import MeCab

def get_love_value(love_value,text):
    #love_value = 50
    diff = 10
    """

    tagger = MeCab.Tagger('-Ochasen')

    text = text.encode("utf-8")
    node = tagger.parseToNode(sample_comment)
    words =[]
    while node:
        #print node.surface
        words.append(node.surface)
        node = node.next
    for word in words:
        if word in positive:
            #点数は一旦固定
            diff += 5
            print "%s:posi!" %word
        elif word in negative:
            diff -= 2
            print "%snega!" %word
            """
    return love_value + diff
