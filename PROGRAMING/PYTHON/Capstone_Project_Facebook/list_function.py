


# Function returning length of list ()test and return lenth of list  

def length(my_list):
    my_len = 0

    for _ in my_list:
        my_len += 1

    return my_len

    

# Function to_string()
# Function to return string with seprator in it

def to_string(my_list, sep=', '):
    string = ''
    
    # Function to take both string and int
    
    for i in range(length(my_list)):
        if type(my_list[i]) == str:
            
            if i  < (length(my_list)-1) :
                string += my_list[i]+sep
                
            else:
                string += my_list[i]
        else:
            if i  < (length(my_list)-1) :
                string += str(my_list[i])+sep
                
            else:
                string += str(my_list[i])
   

    return string


    


# Function count()
# Function to count the occurance of given value in a given list

def count(my_list, value):
    num = 0
    for n in my_list:
        if value == n:
            num +=1
    return num
        
    

# Function find()function to find the index value of the given value 

def find(my_list, value):
    index = 0
    index_list = []
    r = -1
    for num in my_list:
        if num == value:
             index_list.append(index)
        else:
            index+=1
    if length(index_list) == 0:
        return r
    else:
        return index_list[0]
            
    
    


# Function insert_value()function to insert given value,
# To the list for the given insert postion.

def insert_value(my_list, value, insert_position):
    list_1 = []
    if insert_position <= 0:
        list_1.append(value)
        for i in range(length(my_list)):
            list_1.append(my_list[i])
    elif insert_position >= length(my_list):
        for i in range(length(my_list)):
            list_1.append(my_list[i])
        list_1.append(value)
        
    else:
        for i in range(insert_position):
            list_1.append(my_list[i])

        list_1.append(value)

        for i in range(insert_position, length(my_list)):
            list_1.append(my_list[i])
    
    return list_1
    
    

# Function remove_value()function to remove
# Element from the list for the given position

def remove_value(my_list, remove_position):
    list_1 = []
    if remove_position <= 0:
        for i in range(1,length(my_list)):
            list_1.append(my_list[i])
            
    # When remove position is more than the elements in list
    
    elif remove_position >= length(my_list):
        for i in range(length(my_list)-1):
            list_1.append(my_list[i])
            
    else:
        for i in range(remove_position):
            list_1.append(my_list[i])

        for i in range(remove_position+1, length(my_list)):
            list_1.append(my_list[i])
    
    return list_1
    
    


# Function reverse()function to reverse the string/list for given number

def reverse(my_list, number=-1):
    list_1 = []
    if number == -1:
        for i in range(length(my_list)-1,number,-1):
            list_1.append(my_list[i])
        return list_1
    else:
        list_2 = []
        
        for i in range(number-1,-1,-1):
             list_2.append(my_list[i])
             
        for i in range(number,length(my_list)):
            list_2.append(my_list[i])
            
        return list_2
    
    
