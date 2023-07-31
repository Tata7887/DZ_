'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из
документации к языку.
'''

import re

data = "Среди домашних животных у кошки самые большие глаза относительно размеров тела. Как и у большинства хищников, \
глаза кошки направлены вперёд, и их зрительные поля перекрываются. Поэтому кошки обладают стереоскопическим зрением, \
 позволяющим оценивать расстояние до предмета наблюдения. Около 60 % кошек способны к движениям глаз, при которых \
  зрительные оси сходятся и расходятся. Кошки умеют различать цвета, но по сравнению с человеком восприятие цвета у \
  них слабее — менее контрастное и яркое. У кошек (как и большинства других млекопитающих, кроме приматов) есть два \
  типа колбочек — чувствительные к более длинноволновому и коротковолновому свету. Кошки превосходно видят в условиях \
слабого освещения. За сетчаткой глаза располагается особый слой — тапетум, который у кошек, как и у большинства \
содержит большое количество люминесцентного пигмента (tapetum lucidum). Функция тапетума заключается \
в отражении обратно на сетчатку той части света, которая проходит сквозь полупрозрачный слой светочувствительных \
 клеток и которая без тапетума безвозвратно терялась бы. Благодаря тапетуму и другим механизмам светочувствительность \
 глаза кошки в 7 раз выше, чем у человека, и кошки могут хорошо видеть даже при слабом освещении, но при ярком свете \
 они видят хуже человека. Из-за интенсивной пигментации тапетума кошачьи глаза при их освещении в темноте светятся \
 жёлто-зелёным.  "

data = re.sub(r'[^\w\s]','', data)
print(data)
data_list = []
data_list = data.split()
print(data_list)
list_1 = [el.lower() for el in data_list]

print(list_1)

dct = {}
for el in list_1:
    val = list_1.count(el)
    dct[el] = val
print(dct)


sorted_data = {}
sorted_data = sorted(dct.items(), key=lambda x: x[1], reverse=True)

sort_data_dict = dict(sorted_data)
print(sort_data_dict)

i = 0
for key, value in sort_data_dict.items():
    print(key, value)
    i = i + 1
    if i == 10:
        break