

def get_access(func):
    def access_func(*args, **kwargs):
        print("你驗證成功")
        return func(*args, **kwargs)
    return access_func


@get_access
def enter_background():
    print("進入後台")
@get_access
def delete_order():
    print("刪除訂單")

enter_background()
delete_order()