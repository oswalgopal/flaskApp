import requests

'''
    some status codes:
    200: OK
    201: created
    400: bad request
    403: forbidden (special permission neeeded)
    404: not found
    405: method no allowed
    422: unprocessable entity
'''



def main():
    res = requests.get('https://api.github.com/')
    if res.status_code is 200:
        print(res.json())
    else:
        raise Exception('Error while running the api')
    

if __name__ == '__main__':
    main()