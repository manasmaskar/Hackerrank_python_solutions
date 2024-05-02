if __name__ == '__main__':
    n = int(input())  
    #n takes the input till where we want to take up[ the input!!!
    arr = list(map(int, input().split()))
    #idhar list use kiya because we will be using the list sorting method to arrange the scores in an ascending order.. using map funtion to convert the input(n) to convert it into integers
    #using the split function so that blank spaces ke baad hum define kare ki number is one paricular string eg(1 2 3 4) => ("1","2","3","4") this is how split is used !!!
    largest_number = max(arr)
    #finding the largest number in the string <= unnecessarry step but chalega just to check if we are going in the right direction
    arr.sort()
    #sorting the list in an ascending order!!
    print(arr[arr.index(max(arr))-1])
    #printing the second largest number iske liye we used indexing method and we have given the input of maximum numbers index number using max(arr) -1 to print the second largest number
