

import sys
sys.path.insert(0,'../')
import perceplearn

script, trainingfile, modelfile = sys.argv



training_handle = open(trainingfile,'r',errors='ignore')
learning_content = training_handle.read()
sentence = learning_content.split("\n")
sentence.remove("")
train_formatted = 'trainfile.pos'
trainfile_handle = open(train_formatted,'w',errors='ignore')



for sen in sentence:
	sen = "BOS/BOS" + " " + sen +  " " + "EOS/EOS"
	#print (sen)	
	tokens = sen.split(" ")
	#print (tokens)model
	for tok in tokens:
		if tok == "BOS/BOS" or tok == "EOS/EOS" or tok == "":
			continue
		
		index = len(tok) - 1 - tok[::-1].index('/')
		word = tok[:index] 
		tag = tok[index+1:]		
		
		#print (tag)
				
		trainfile_handle.write(str(tag))
		trainfile_handle.write(" ")
		trainfile_handle.write("current:")
		trainfile_handle.write(str(word))
		trainfile_handle.write(" ")
		trainfile_handle.write("next:")
		nextword = tokens[(tokens.index(tok) + 1)]
		index = len(nextword)
		if not nextword.find('/') == -1:
			index = len(nextword) - 1 - nextword[::-1].index('/')
		next = nextword[:index]
		trainfile_handle.write(str(next))
		trainfile_handle.write(" ")
		trainfile_handle.write("prev:")
		prevword = tokens[(tokens.index(tok) - 1)]
		index = len(prevword)
		if not prevword.find('/') == -1:
			index = len(prevword) - 1 - prevword[::-1].index('/')
		prev = prevword[:index]
		#prev = (tokens[(tokens.index(tok) - 1)]).split("/")
		trainfile_handle.write(str(prev))
		trainfile_handle.write("\n")
	
	


trainfile_handle.close()
perceplearn.percepLearn(train_formatted,modelfile)

#print (learning_content)
#tokens = learning_content.split("\n")

#for tok in tokens:
	

#print (tokens)







