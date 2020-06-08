
"""
tcp 套接字服務端流程
注意:
    功能性代碼，注重流程和函數使用
如何測試:
    在終端機上: telnet  ipv4  port
"""

import socket
# 創接 tcp 套接字對象
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 綁定地址(ip, port(隨意))
sockfd.bind(('192.168.10.100', 4294))

# 設置監聽
sockfd.listen(5)



# 等待處理客戶端連接請求
while True:
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        # ctrl+c 退出程序
        print("Server Exit")
        break
    except Exception as e:
        print(e)
        continue
    # 消息收發
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive: ", data.decode())
        # if data.decode() == "Q":
        #     break
        n = connfd.send(b"Thanks!!\n")
        print('Send %d byte' % n)
    # 關閉套接字
    connfd.close()  # 負責 和對應的客戶端進行消息收發


sockfd.close()  # 負責 和客戶端建立連皆