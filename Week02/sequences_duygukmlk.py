
my_list = [1,3,5,7,9,11,13,13,15,17,19]

my_tuple = ("tek","çift",1)

my_set = {"Friends", "HIMYM", "Broklyn Nine-Nine"}

my_dict = {
    "Name": "Duygu",
    "Surname": "Kamalak",
    "Age": "22",
    "Birth_date": "26.10.2001",
    
}


def remove_duplicates(my_list):
    return list(set(my_list))
     



def list_counts(my_list):
    return {item: my_list.count(item) for item in my_list}



def reverse_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

print(remove_duplicates(my_list))
print(list_counts(my_list))
print(reverse_dict(my_dict))
