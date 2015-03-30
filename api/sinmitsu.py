#coding:utf-8:
import MeCab

sinmitsu = 50
diff = 0

tagger = MeCab.Tagger('-Ochasen')

comments = []
sample_comment= u"今日オシャレなカフェ見つけたー!!今度いこーよ！"
sample_comment2= u"えっ、本当!?行きたいっ!"
sample_comment3= u"4/1どう?"
sample_comment4= u"あ、ごめん...。その日無理だぁ"
sample_comment5= u"4/3は?"
sample_comment6= u"うん、大丈夫だよー!"
sample_comment7= u"本当!?わーい(*^_^*)楽しみ"

comments.append(sample_comment)
comments.append(sample_comment2)
comments.append(sample_comment3)
comments.append(sample_comment4)
comments.append(sample_comment5)
comments.append(sample_comment6)
comments.append(sample_comment7)

positive = ["本当", "!?", "!", "わーい","(*^_^*)", "楽しみ"]
negative = ["ごめん", "...。", "無理"]

for sample_comment in comments:
    sample_comment = sample_comment.encode("utf-8")
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
    print sinmitsu + diff