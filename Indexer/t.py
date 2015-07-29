import PorterStemmer
foo = PorterStemmer.PorterStemmer()

print(foo.stem("factionally", 0, len("factionally")-1))