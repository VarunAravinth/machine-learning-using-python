books_list=['lost_semicolon.txt','prefers_machine_over_people.txt']
count=0
for i in books_list:
    with open(i) as file_object:
        contents=file_object.read()
        contents=contents.split()
        print i+' has '+str(len(contents)) + ' words'
        count+=1
print str(count) + ' files have been processed'
