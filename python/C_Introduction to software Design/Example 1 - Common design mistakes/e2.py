list_of_words = ['hello', 'yes', 'goodbye', 'last','hello']
to_print = ""


#hard codding by using static numbers> Using variables and assigning numbers to it allows us to make our code more 
# flexible and changable
for i in range(len(list_of_words)):
    to_print  += list_of_words[i]
    if i != len(list_of_words) - 1:
        to_print += ','
        
print(to_print)