# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    _ = int(input())
    s = set([int(x) for x in input().split(' ')])
    _ = input()
    arr = [int(x) for x in input().split(' ')]

    print(len(s.symmetric_difference(arr)))
