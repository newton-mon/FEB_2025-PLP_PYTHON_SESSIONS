with open('test.txt') as f:
    text = f.read()

print (text)

g = open('test.txt','r')
print(g.readline(),end='$')

h = open('test.txt','w')
h.write('soysauce')