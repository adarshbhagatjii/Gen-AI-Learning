
from nltk.stem import PorterStemmer, LancasterStemmer,SnowballStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()
snow=SnowballStemmer("english")

print(porter.stem("runner"))     # runner
print(lancaster.stem("runner"))  # run
print(snow.stem("runner"))         #runner