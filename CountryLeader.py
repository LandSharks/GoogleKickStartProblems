import string
#Reads each line of the file and stores it in a list
def readFile(file):
	namesList = list()
	with open(file) as f:
		f.readline()
		numberOfNames = int(f.readline())
		for i in range(numberOfNames):
			namesList.append(f.readline().replace('\n',''))
		leader = findLeader(namesList)
		print(leader)

def findLeader(namesList):
	currentLeader = list()
	currentLeader.append(namesList.pop())
	for i in namesList:
		if(countDistinctLetters(currentLeader[0]) < countDistinctLetters(i)):
			currentLeader.clear()
			currentLeader.append(i)
		elif(countDistinctLetters(currentLeader[0]) == countDistinctLetters(i)):
			currentLeader.append(i) 

	return currentLeader


def countDistinctLetters(names):
<<<<<<< HEAD
    alphabet = [False for x in range(26)]
    count = 0
    size = len(names)
    for i in range(size):
        if names[i] == " ":
            continue
            letterIndex = string.ascii_uppercase.index(names[i])
            if alphabet[letterIndex] == False:
                    count += 1
                    alphabet[letterIndex] = True
    return count
=======
	alphabet = list()
	for i in range(26):
		alphabet.append(False)
	count = 0
	for i in names:
		letterIndex = alphabet[string.ascii_uppercase.index(i)]
		if letterIndex == False:
			count += 1
			letterIndex = True
	return count
>>>>>>> 770d636033cc5b695bd6ef2f7a5916f0351c0dbc


def countDistinct(name):
	unique = list()
	count = 0
	for i in name:
		if(not i in unique):
			unique.append(i)
			count += 1

	print(count)
	return count

def main():
	# readFile('temp.in')
	countDistinct('google')
	#c = countDistinctLetters('google')
	#print(c)

main()
