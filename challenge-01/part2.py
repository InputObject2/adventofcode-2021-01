import requests
# Steps :
# Download this : https://adventofcode.com/2021/day/1/input
# foreach item in loop
#   load the the two next items
#       get the sum
#   create a new list of series and their sum
#       redo the compare from #1
#           (aka if it is higher, increment counter by 1)

def data_import(url, cookie):
    cookies = dict(session=cookie)
    r = requests.get(url, cookies=cookies)
    return list(r.text.splitlines())

def generate_rolling_window_list(my_list, set_size):
    modulo = len(my_list) % set_size

    my_sets =  [0] * (len(my_list)-modulo)

    print("There are " + str(modulo) + " items not in a set and the list has " + str(len(my_list)) + " elements in it")
    for i in range(0,len(my_list)-modulo):
        for x in range(0, set_size):
            my_sets[i] += int(my_list[i+x])
            
    return my_sets
        

def compare_numbers(x, y):
    if x > y:
        return True

def process(my_list):
    # load first item
    #
    my_counter = 0
    
    for i in range(0, len(my_list)-1):
        if(compare_numbers(int(my_list[i+1]), int(my_list[i]))):
            my_counter += 1

    return my_counter

def main():
    cookie = '<session token>'
    url = 'https://adventofcode.com/2021/day/1/input'
    number_in_set = 3

    l = generate_rolling_window_list(data_import(url, cookie),number_in_set)
    print(process(l))
    

if __name__ == '__main__':
    main()