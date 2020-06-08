def give_gife_money(money):
    def child_buy(target, price):
        nonlocal money
        if price < money:
            money -=  price
            print('buy the ', target, '錢剩下', money)
        else:
            print('I don\'t have enough money')
    return child_buy

action = give_gife_money(20000)
action('IronMan-1',1200)
action('IronMan-2',5600)
action('IronMan-X',37000)