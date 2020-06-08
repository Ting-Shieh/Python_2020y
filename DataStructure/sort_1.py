
def quick(l, low, high):
    x = l[low]
    while low < high:

        while l[high] > x and high > low:
            print("內部_up:", l[high], '>', x)
            high -= 1

        l[low] = l[high]
        while l[low] <= x and low < high:
            print("內部_down:", l[low], '<=', x)
            low += 1

        l[high] = l[low]
        print("外部")
    l[low] = x
    print("over:",l)


if __name__ == '__main__':
    l01 = [3,20,5,17,19,6,11,4,18]
    quick(l01,0,len(l01)-1)