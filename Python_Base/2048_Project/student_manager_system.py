# TODO 數據模型類(Models)
class StudentModel:
    """
    學生模型
    """
    def __init__(self,name=" ", age=0, score=0, id=0):
        """
        創建學生對象
        :param id: 編號
        :param name: 姓名
        :param age: 年齡
        :param score: 分數
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score
# TODO Controller
class StudentManagerController:
    """
    學生管理控制器
    處理業務邏輯
    """
    __stu_id = 1000
    def __init__(self):
        self.__stu_list = []

    # 只讀
    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        # 為學生設置ID
        #  crl+alt+M  =>快速設置函數
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)

    def __generate_id(self):
        StudentManagerController.__stu_id += 1
        return StudentManagerController.__stu_id

    def remove_student(self,id):
        # 依據ID刪除
        # 刪除後返回結果
        for stu in self.__stu_list:
            if id == stu.id:
                self.__stu_list.remove(stu)
                return True
        #raise ValueError("無此ID")
        return False

    def update_student(self, updatestu):
        for stu in self.__stu_list:
            if updatestu.id == stu.id:
                stu.name = updatestu.name
                stu.age = updatestu.age
                stu.score = updatestu.score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score > self.__stu_list[c].score:
                    self.__stu_list[i], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[i]

        return self.__stu_list


# 測試
# manager = StudentManagerController()
# manager.add_student(StudentModel("Ting",28,82))
# print(manager.stu_list[0].name)
# manager = StudentManagerController()
# manager.add_student(StudentModel("Ting", 28, 82))
# manager.add_student(StudentModel("Ting2", 28, 92))
# print(manager.remove_student(1005))
# print(manager.remove_student(1002))
# manager = StudentManagerController()
# manager.add_student(StudentModel("Ting", 28, 82))
# s2 = StudentModel("Ting2", 28, 92)
#
# print(manager.update_student(StudentModel("Ting22", 28, 92, 1002)))
# for item in manager.stu_list:
#     print(item.name)



# TODO Views
class StudentManagerView:
    # 一個視圖，只創立一個控制器
    def __init__(self):
        # 只會創建一個list
        self.__manager = StudentManagerController()

    # 終端顯示訊息 => 用戶不必知道
    def __displaymenu(self):
        print("+-------------------------------+")
        print("| 1)添加學生訊息                 |")
        print("| 2)顯示學生訊息                 |")
        print("| 3)刪除學生訊息                 |")
        print("| 4)修改學生訊息                 |")
        print("| 5)按照成績生續排序             |")
        print("+-------------------------------+")

    # 終端選擇 => 用戶不必知道
    def __select_menu(self):

        option = input("請輸入:")
        if option == '1':
            self.__input_students()
        elif option == '2':
            self.__output_students(self.__manager.stu_list)
        elif option == '3':
            self.__delete_student()
        elif option == '4':
            self.__modify_student()
        elif option == '5':
            self.__output_student_by_score()

    # 輸入學生
    def __input_students(self):
        name = input("請輸入姓名:")
        age = int(input("請輸入年紀:"))
        score = int(input("請輸入成績:"))
        stu = StudentModel(name=name, age=age, score=score)
        self.__manager.add_student(stu)

    # 輸出學生
    def __output_students(self,list):
        # self.__manager
        for item  in  list:
            print(item.name,item.age, item.score, item.id)

    # 刪除學生
    def __delete_student(self):
        # 需要用戶輸入學生id
        id = int(input("請輸入欲刪除學生ID:"))
        # 調用管理器對象的刪除學生方法
        res = self.__manager.remove_student(id)
        # 如果結果為True，顯示刪除成功
        # 否則顯示刪除失敗
        if res:
            print("學生ID:%d，刪除成功!" % id)
        else:
            print("學生ID:%d，刪除失敗!" % id)


    # 修改學生
    def __modify_student(self):
        # 收集用戶輸入的訊息保持到對象
        # 調用管理器對象的修改方法
        id = int(input("請輸入欲刪除學生ID:"))
        name = input("請輸入新的姓名:")
        age = int(input("請輸入新的年紀:"))
        score = int(input("請輸入新的成績:"))
        stu = StudentModel(name=name, age=age, score=score, id=id)
        if self.__manager.update_student(stu):
            print("學生ID:%d，修改成功!" % id)
        else:
            print("學生ID:%d，修改失敗!" % id)

    # 顯示排序
    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


    #
    def main(self):
        """
        界面入口
        :return:
        """
        while True:
            self.__displaymenu()
            self.__select_menu()




view_test = StudentManagerView()
view_test.main()