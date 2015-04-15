Running scripts:

Run postrain.py like this:

python3 postrain.py <trainfile name>  <modelfile name>
 eg: python3 postrain.py pos.train model.pos 
The script prints the accuracy and iteration numbers for reference.

Run postag.py like this:

python3 postag.py <modelfile name(created above)> < testfile > outputfile
 eg: python3 postag.py model.pos < pos.blind.test > pos.test.out
 The script takes around 20 minutes to execute all sentences, its actually the model file loading the
 dictionary takes time,once that's done tagging is very fast.So even more input can be tagged almost in same 
 amount time.
 

