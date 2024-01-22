####
def left_child(i):
    return i*2+1
def right_child(i):
    return i*2+2
def parent(i):
    return (i-1)/2
def heap_checker(a,n):
    max_check = True
    for i in range(int((n-2)/2)+1):
    
        if a[i] < a[left_child(i)]:
            max_check = False

        if right_child(i) < n and a[i] < a[right_child(i)]:
            max_check = False
  
    return max_check

if __name__ == "__main__":
    a=[]
    ins = input("Enter the array to test: ").split(" ")
    for i in ins:
        a.append(int(i))
    n=int(input("Enter heap size: "))
    max_check = heap_checker(a,n)
    print()
    print(max_check)

