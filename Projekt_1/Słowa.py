import argparse
from ascii_graph import Pyasciigraph
from collections import Counter

listword = []
listnumber = []

parser = argparse.ArgumentParser(description="Opis")
parser.add_argument('file',help = 'name of file') #string domyślnie
parser.add_argument('-n','--number',help = 'number',type = int, default = 20) #numerek ile wyrazów
args = parser.parse_args()

print(f'File name: {args.file}')
print(f'{args.number = }')


with open(args.file,encoding = 'utf8') as f:
    words = f.read().strip().split()
    counter1 = Counter(words)
    #print(counter1)
    most = counter1.most_common()
   # print(most)
    for x in range(args.number):
        mostword = most[x][0]
        mostwordnumber = most[x][1]
        listword.append(mostword)
        listnumber.append(mostwordnumber)

#print(listword)
#print(listnumber)


graph = Pyasciigraph(separator_length=10 )
data = [(listword[i],listnumber[i] )for i in range(args.number)]
data.sort(key = lambda e: e[1],reverse = True)

for line in graph.graph('GRAF',data):
    print(line)



