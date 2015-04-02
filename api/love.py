#coding:utf-8:
import MeCab

positive = ["本当", "!?", "!", "わーい","(*^_^*)", "楽しみ"]
negative = ["ごめん", "...。", "無理"]

def get_love_value(val,text):
    love_value = int(val)
    diff = 0

    mecab = MeCab.Tagger("-Owakati")
    words = mecab.parse(text.encode('utf-8')).split()

    for word in words:
        if word in positive:
            diff += 5
        elif word in negative:
            diff -= 2
    return str(love_value + diff)