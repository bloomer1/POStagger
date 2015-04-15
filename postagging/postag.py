from sys import argv
import pickle
import sys
import ast
import re
import io


script, modelfile = argv

model_handle = open(modelfile,'r',errors='ignore')
content = model_handle.read()
learning = content.split("\n")

clList = []
sizeList = {}
globallistOfWeightDict = {}

clList = ast.literal_eval(learning[1])
sizeList = ast.literal_eval(learning[3])

#print (sizeList)

#file_hand = open('temp.txt','w',errors='ignore')
#file_hand.write(str(learning[5]))
#file_hand.close()
#file_hand = open('temp.txt','r',errors='ignore')

#for iclass in sizeList:
#	d = ast.literal_eval(file_hand.read(sizeList[iclass]))
#	print (d)
#	break

#pickle.dump(ast.literal_eval(learning[3]), open("save.p", "wb"))
#globallistOfWeightDict = pickle.load( open ( "save.p", "rb"))
globallistOfWeightDict = ast.literal_eval(learning[5])
#print (len(clList))
listWeights = {}
equalList = []

def maxfn(listWeights):
	z = ""
	maxweight = float("-inf")
	for k,v in listWeights.items():
		if maxweight < v:
			maxweight = v
			z = k
		
	return z


def checkEqual(equalList):
	prev = equalList[0]
	count = 1
	for item in equalList[1:]:
		if item == prev:
			count = count + 1

	if count == len(equalList):
		return True
	else:
		return False


#print (clList)

#inputDoc = sys.stdin.readlines()
in_stream = io.TextIOWrapper(sys.stdin.buffer, errors = 'ignore')
inputDoc = in_stream.readlines()
#sen = re.findall(r"[\w']+|[.,!?;]", inputDoc)

for doc in inputDoc:
	ans = ""
	sen = re.findall(r'(\S+)', doc)	
	#sen = doc.split(" ")
	tokenList = []
	sen.insert(0,"BOS")
	sen.append("EOS")

	#print (sen) 

	for tok in sen:
		if tok == "BOS" or tok == "EOS":
			continue
		next = sen[sen.index(tok) + 1]
		prev = 	sen[(sen.index(tok) - 1)]
		tokenList.append("current:" + tok + " " + "next:" + next + " " + "prev:" + prev)	

	

	for token in tokenList:
		tokens = token.split(" ")
		for iclass in clList:
			d = globallistOfWeightDict[iclass + "Weights"]
			sumOfWeights = 0
		
			for word in tokens:
				if word in d:
					sumOfWeights += d[word]
			listWeights[iclass] = sumOfWeights
			equalList.append(sumOfWeights)	
		z = maxfn(listWeights)
		dec = checkEqual(equalList)
		equalList = []
		if dec == True:
			z = clList[0]
		ans = ans + (tokens[0])[8:] + "/" + z + " "
	ans = ans[:-1]
	print (ans)	
	#print (token)	
	#print (z)
		# also flush the output
	#sys.stdout.flush()
	
			
	





