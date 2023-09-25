def LCS():
    file = open("string1.txt", "r")
    string_1 = file.readline()
    string_1 = string_1.strip()
    file.close

    file = open("string2.txt", "r")
    string_2 = file.readline()
    string_2 = string_2.strip()
    file.close()

    s1 = len(string_1)
    s2 = len(string_2)

    arr = [[0]*(s2+1) for _ in range(s1+1)]

    for i in range(1,s1+1):
        for j in range(1,s2+1):
            if (string_1[i-1] == string_2[j-1]):
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i][j-1], arr[i-1][j])
    length = arr[s1][s2]
    subs = helper(arr, string_1, string_2, s1, s2)
    return [length, subs]

def helper(arr, string_1, string_2, i, j):
    if(i==0 or j==0):
        return ""
    if(string_1[i-1] == string_2[j-1]):
        return helper(arr,string_1, string_2, i-1, j-1) + string_1[i-1]
    if(arr[i][j-1] > arr[i-1][j]):
        return helper(arr, string_1, string_2, i, j-1)
    return helper(arr, string_1, string_2, i-1, j)
