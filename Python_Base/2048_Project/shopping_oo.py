# TODO 模型類
class CommodityModel:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price


class OrderModel:
    def __init__(self, commodity, count, id= 0):
        self.id = id
        self.commodity = commodity
        self.count = count


# TODO 購物車控制器
class ShoppingCartController:
    __init_order_id = 0
    def __init__(self):
        self.__list_order = []
        self.__list_commodity_info = self.__load_commodity()


    # 只讀屬性(私有變量)
    @property
    def list_order(self):
        return self.__list_order

    # 只讀屬性(私有變量)
    @property
    def list_commodity_info(self):
        return self.__list_commodity_info

    # 私有功能
    def __load_commodity(self):
        """
        加仔商品
        :return:  商品列表
        """
        return [
            CommodityModel(101, "紅茶", 10),
            CommodityModel(102, "綠茶", 15),
            CommodityModel(103, "奶茶", 20),
            CommodityModel(104, "咖啡", 45),
            CommodityModel(105, "鴛鴦", 60),
            CommodityModel(105, "精品咖啡", 80),
        ]

    def add_order(self, order_info):
        """
        添加訂單
        獲取訂單訊息，生成id生成id
        :param good:
        :return:
        """
        order_info.id = self.__generate_order_id()
        self.__list_order.append(order_info)

    # 私有功能
    def __generate_order_id(self):
        """
        產生ID
        :return:
        """
        ShoppingCartController.__init_order_id += 1
        return ShoppingCartController.__init_order_id


    def get_total_price(self):
        total_price = 0
        for item in self.__list_order:
            total_price += item.count * item.commodity.price
        return total_price

    def get_commodity_by_id(self, id):
        """
        通過id確認商品是否存在
        :return: None => False。有對象 => True。
        """
        for item in self.list_commodity_info:
            if id == item.id:
                return item



# TODO 視圖類
class ShoppingConsoleView:
    def __init__(self):
        self.__controller = ShoppingCartController()

    def __select_menu(self):
        while True:
            option = input("1鍵購買，2鍵結算，q鍵退出。")
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == 'q':
                break

    def __print_commodity(self):
        """
        打印商品
        :return:
        """
        for item in self.__controller.list_commodity_info:
            print("編號:%d, 名稱:%s, 單價:%d。" % (item.id, item.name, item.price))

    def __create_order(self):
        while True:
            """
            如果商品存在即退出
            不存在則加入
            """
            cid = int(input("請輸入商品編號:"))

            if self.__controller.get_commodity_by_id(cid):
                break
            else:
                print("商品不存在，請重新輸入。")

        count = int(input("請輸入商品數量:"))
        order = OrderModel(cid, count)
        self.__controller.add_order(order)

    def __print_order(self):
        """
        打印訂單
        :return:
        """
        for item in self.__controller.list_order:
            print("商品:%s, 單價:%d, 數量:%d。" %(item.commodity.name, item.commodity.price, item.count))

    def __paying(self, total_price):
        """
        接受用戶輸入，完成支付
        :return:
        """
        while True:
            money = int(input("假價格%d元, 請輸入:" % total_price))
            if money >= total_price:
                print("購買成功，找零 %d" % (money - total_price))
                break
            else:
                print("金額不足，請重新輸入。")


    def __settlement(self):
        """
        打印訂單
        計算總價格
        結算訂單
        :return:
        """
        self.__print_order()
        total_price = self.__controller.get_total_price()
        self.__paying(total_price)

        
    def __buying(self):
        """
        打印商品訊息
        創建訂單
        :return:
        """
        self.__print_commodity()


    def main(self):
        # 出現菜單
        self.__select_menu()



# c = ShoppingCartController()
# c.