
import importlib,sys
importlib.reload(sys)


fr = open('xyj.txt', 'r')

characters = []
status = {}

for line in fr:
	#get rid of the ' ' at start and end
	line = line.strip()

	if len(line) == 0:
		#skip if this line is blank
		continue
	# line = line.encode('utf8').decode('unicode_escape')
	#deal with Chinese

	for x in range(0, len(line) - 1):
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		if line[x] not in characters:
			characters.append(line[x])
		if line[x] not in status:
			status[line[x]] = 0
		status[line[x]] += 1

print(len(characters))
print(len(status))



sorted_dict = sorted(status.items(), key=lambda item: item[1], reverse=True)

for x in range(0,10):
	print(sorted_dict[x][0], sorted_dict[x][1])





fr.close()
