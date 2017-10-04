"""Turtle Graphics"""
from turtle import *

RADIUS= 200
radius = 200
turtle = Turtle()


def get_words_percentage(text):
	words_count = {}
	words = text.split(' ')
	for word in words:
		words_count[word] = words_count.get(word, 0) + 1 
	return words_count

#words_count.values()
#words_count.keys()

res = get_words_percentage('hello hell hell  12 web')
#res = {'hello': 1, 'hell': 2, '12': 1, 'web':1} 

per = [word_count for word, word_count in res.items() if word ]

sum_str = sum(per)

percentages = [word_count / sum_str for word_count in per]

#percentages = cal_list(per, sum_str)

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
		rollingPercent  += percent * 360
		
		color('yellow')
		setheading(rollingPercent)
		# color(clr[int_cl])
		pendown()
		forward(radius)
		penup()
		home()

segment(percentages,radius)

exitonclick()