import sys
def value(x,y):
	return (x+1+n*y)

def clauses(n):
	row_col = 2*n + n*n*(n-1)
	diagonal = (n*(n-1)*((2*n)-1))/3
	return (row_col+diagonal)

n = int(input())

file_handle = open(sys.argv[1], 'w')
file_handle.write('p ' + "cnf " + str(n*n) + ' ')
file_handle.write(str(clauses(n)) + '\n')
for i in range(n):		#i is in y axis
	for j in range(n):	#j is in x axis
		file_handle.write(str(value(j,i)) + ' ')
	file_handle.write(str(0) + '\n')

for i in range(n):
	for j in range(n):
		file_handle.write(str(value(i,j)) + ' ')
	file_handle.write(str(0) + '\n')

for i in range(n):
	for j in range(n):
		k = j+1
		while k<n :
			a = -1*value(j,i)
			b = -1*value(k,i)
			file_handle.write(str(a) + ' ' + str(b) + ' ')
			k += 1
			file_handle.write(str(0) + '\n')

for i in range(n):
	for j in range(n):
		k = j + 1
		while (k<n):
			file_handle.write(str(-1*value(i,j)) + ' ' + str(-1*value(i,k)) + ' ')
			file_handle.write(str(0) + '\n')
			k += 1

for i in range(n):
	for j in range(n):
		l = i + 1
		k = j + 1
		while l < n and k < n :
			file_handle.write(str(-1*value(j,i)) + ' ' + str(-1*value(k,l)) + ' ')
			file_handle.write(str(0) + '\n')
			l += 1
			k += 1

for i in range(n):
	for j in range(n):
		l = i - 1
		k = j + 1
		while l >= 0 and k < n :
			file_handle.write(str(-1*value(j,i)) + ' ' + str(-1*value(k,l)) + ' ')
			file_handle.write(str(0) + '\n')
			l -= 1
			k += 1

file_handle.close()