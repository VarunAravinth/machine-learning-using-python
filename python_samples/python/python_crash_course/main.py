books_list=['lost_semicolon.txt','prefers_machine_over_people.txt']
count=0
for i in books_list:
    with open(i) as file_object:
        contents=i.read()
        contents=contents.split()
        print i+'has'+str(contents)
        count+=1
print str(count) + 'has been processed'
