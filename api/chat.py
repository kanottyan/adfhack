#coding:utf-8
import json

def get_message(id):
    message_id = int(id)
    messages = []
    messages.append([0,u"今日オシャレなカフェ見つけたー!!今度いこーよ！",'man'])
    messages.append([1,u"えっ、本当!?行きたいっ!","woman"])
    messages.append([2,u"4/1どう?",'man'])
    messages.append([3,u"あ、ごめん...。その日無理だぁ",'woman'])
    messages.append([4,u"4/3は?","woman"])
    messages.append([5,u"うん、大丈夫だよー!","man"])
    messages.append([6,u"本当!?わーい(*^_^*)楽しみ♡","woman"])
    messages.append([6,u"本当!?わーい(*^_^*)楽しみ♡","woman"])
    messages.append([6,u"本当!?わーい(*^_^*)楽しみ♡","woman"])
    data = []
    for message in messages:
        data.append({
            "message_id": message[0],
            "text": message[1],
            "chater": message[2]
        })
    return json.dumps(data[message_id])