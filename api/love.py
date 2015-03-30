#coding:utf-8:
import MeCab

def get_love_value(val,text):
    #love_value = 50
    love_value = int(val)
    diff = 0
    tagger = MeCab.Tagger('-Ochasen')

    node = tagger.parseToNode(text.encode("utf-8"))
    words =[]
    positive = ["本当", "!?", "!", "わーい","(*^_^*)", "楽しみ"]
    negative = ["ごめん", "...。", "無理"]
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
    print love_value + diff
    return str(love_value + diff)