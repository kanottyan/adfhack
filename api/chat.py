#coding:utf-8
import json
def get_message(message_id):
    messages = []
    messages.append(1,u"今日オシャレなカフェ見つけたー!!今度いこーよ！",'man')
    messages.append(2,u"えっ、本当!?行きたいっ!","woman")
    messages.append(3,u"4/1どう?",'man')
    messages.append(4,u"あ、ごめん...。その日無理だぁ",'woman')
    messages.append(5,u"4/3は?","woman")
    messages.append(6,u"うん、大丈夫だよー!","man")
    messages.append(7,u"本当!?わーい(*^_^*)楽しみ♡","woman")
    json = []
    for message in messages:
        json.append({
            "message_id": message[0],
            "text": message[1],
            "chater": message[2]
        })
    if message_id < 7:
        return json.dumps(json[message_id])
    else:
        return json.dumps(json[6])
