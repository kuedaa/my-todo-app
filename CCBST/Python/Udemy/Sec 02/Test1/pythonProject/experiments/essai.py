file = open('sort.txt', 'r' )
content = file.readlines()
file.close()
for index, item in enumerate (content) :
    print(f"{index+1} - {item}")
print(content[1])