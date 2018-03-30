
sample=''
def formatter(first_name,last_name):
    global sample
    sample=first_name + ' ' +last_name
    return sample.title()

print(formatter('varun','aravinth'))
print(sample)
