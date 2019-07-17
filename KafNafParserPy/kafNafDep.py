import importlib
moduleName = input('dependency_data.py')
importlib.import_module(moduleName)

'''
dirname = os.path.dirname(__file__)
#into microportraits folder
path = os.path.join(dirname,"../")

for fname in os.listdir(path+"rawTest"):
		if fname.endswith(".txt"):
			orig = open(path+"rawTest/"+fname, "r", encoding="utf8")
			file = KafNafParserMod(orig, filename= fname+".naf", type = NAF)
'''

if __name__ == '__main__':
	filename = 'wp.txt'
	p = KafNafParser(filename)

	#iterate over dep? 
