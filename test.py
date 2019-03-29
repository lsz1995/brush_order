# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import requests




def get_token():#登入获取签名
    url ='http://127.0.0.1:8000/login/'
    data={
        "username":"admin",
        "password":"qazwsx123",
    }
    res =requests.post(url,data=data).text

    print(res)

def login():#带上签名登入
    headers={
        "Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTU2MzI5MzE2LCJlbWFpbCI6IjQwOTg5NzMwM0BxcS5jb20ifQ.PntAw9tTBgRB3rgKgW3xcpfbqx2nFEwkxXCVs9_udwo"
    }
    data={
        "state":True,
        # "password":"qazwsx123",
    }


    url = 'http://127.0.0.1:8000/WithdrawSure/4/'
    res =requests.patch(url,headers=headers,data=data).text
    print(res)




if __name__ == '__main__':
    headers = {
        "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTU2MzI5MzE2LCJlbWFpbCI6IjQwOTg5NzMwM0BxcS5jb20ifQ.PntAw9tTBgRB3rgKgW3xcpfbqx2nFEwkxXCVs9_udwo"
    }


    login()