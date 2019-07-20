from redis import *
if __name__ == '__main__':
    try:
        date = StrictRedis()
        set_name = date.set('name','张三')
        print(set_name)
        get_name = date.get('name')
        print(get_name.decode('utf-8'))
    except Exception as e:
        print(e)
