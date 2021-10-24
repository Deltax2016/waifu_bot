s = "карл у клары украл кораллы, клара у карла украла кларнет"


sp = s.split(' ')

text = ""
text2 = ""
flag = 1
for i in sp:
	if len(text) + len(i) <= 23 and flag:
		text += ' ' + i
	else:
		if flag == 1:
			text2 += i
			flag = 0
		else:
			text2 += ' ' + i


print(text[1:])
print(text2)
