"""
http 服務程序
如果瀏覽器請求內容 /
    響應馬  200 OK，獎 index.html作為響應內容

如果瀏覽器請求內容 是其他的
    響應馬  404 Not Found，內容為 sorry
"""

from socket import *


# 搭建網路
def main():
    # tcp 服務端
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口立即重弄
    s.bind(('127.0.0.1', 4294))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print("Connect from ", addr)
        # TODO處理客戶端請求
        handle(conn)




def handle(c):
    """
        與客戶端交互
    :param c:
    :return:
    """
    # get http request
    data = c.recv(4096).decode()
    # print(data)
    request_line = data.split('\n')[0] # 請求行
    # print(request_line)
    info = request_line.split(" ")[1] # 請求內容
    print(info)
    if info == "/":
        with open('./index.html', mode = 'r', encoding='utf8') as f:
            response = "HTTP/1.1 200 OK\r\n"  # 響應頭
            response += "Content-Type: text/html\r\n"  # 響應行
            response += "\r\n"  # 空行　　
            response += f.read()  # 響應體
    else:

        response = "HTTP/1.1 404 Not Found\r\n"  # 響應頭
        response += "Content-Type: text/html\r\n"  # 響應行
        response += "\r\n"  # 空行　　
        response += "<h1>Sorry....</h1>"  # 響應體
    c.send(response.encode())


def read_index(origin_str):

    f = open('./index.html', mode = 'r', encoding='utf8')
    # f.read()
    for line in f:
        origin_str += line

    return origin_str






# print(data.decode())

# html = """HTTP/1.1 200 OK
# Content-Type: text/html
#
# """
# res = read_index(html)
# c.send(html.encode())
# c.close()
# s.close()

if __name__ == '__main__':
    main()