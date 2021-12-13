import requests
# Steps :
# Download this : https://adventofcode.com/2021/day/1/input
# foreach item in loop
#   load the next item, compare it
#   if it is higher, increment counter by 1

def data_import(url, cookie):
    cookies = dict(session=cookie)
    r = requests.get(url, cookies=cookies)
    return list(r.text.splitlines())

def compare_numbers(x, y):
    if x > y:
        return True

def process(my_list):
    # load first item
    #
    my_counter = 0
    
    for i in range(1, len(my_list)-1):
        if(compare_numbers(int(my_list[i+1]), int(my_list[i]))):
            my_counter += 1

    return my_counter

def main():
    cookie = '<session token>'
    url = 'https://adventofcode.com/2021/day/1/input'
    print(process(data_import(url, cookie)))
    

if __name__ == '__main__':
    main()