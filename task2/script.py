"""Turtle Graphics"""

import re
from turtle import *

turtle = Turtle()

def search(st):
	document_text = st
	text_string = document_text.lower()
	match_pattern = re.findall(  r'\w*', text_string)
	frequency = { }
	word_ret = {}
	for word in match_pattern:
		count = frequency.get(word,0)
		frequency[word] = count + 1

	frequency_list = frequency.keys()

	for words in frequency_list:
		word_ret[words] = frequency[words] 
	
	return word_ret


res = search('hello hell hell  12 web')


per = []

for item in res:
	if item != '':
		per.append(res[item])

sum_str = sum(per)

def cal_list( x, y ):
	new_l = []
	for i in x:
		my_r = i / y * 1
		new_l.append(my_r)
	return new_l

percentages = cal_list(per, sum_str)

radius = 200

color_num = ['blue','red','green','white','yellow', 'violet','orange']

penup()
forward(radius)
left(90)
pendown()
# color('palegreen')
begin_fill()
circle(radius)
end_fill()
home()
right(90)
# color('yellow')
def segment(percentages, radius):
	rollingPercent = 0
	for percent in percentages:
		segment = percent * 360
		rollingPercent += segment
		color('yellow')
		setheading(rollingPercent)
		# color(clr[int_cl])
		pendown()
		forward(radius)
		penup()
		home()

segment(percentages,radius)

exitonclick()