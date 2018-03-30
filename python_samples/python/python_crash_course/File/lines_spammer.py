filename='prefers_machine_over_people.txt'

with open(filename,'a') as file_object:
    for i in range(1,51):
        content='This is line number'+str(i)+str('\n')
        file_object.write(content)

print('Success!')



    


