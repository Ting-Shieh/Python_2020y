
def show_scores():
    while True:
        try:
            score = int(input("請輸入成績:"))
            return score
        except Exception:
            print("異常發生")
        # else:
        #     return score
            # break
        # finally:
        #     print("Over!!")

if __name__ == '__main__':
    print(show_scores())