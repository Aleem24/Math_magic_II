num = int(input("Enter The Number:"))

original_num = num

reverse_num = 0

while(num > 0):
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

if original_num == reverse_num:
    print(f"{original_num} is a palindrome number!")

else:
    print(f"{original_num} is not a plaindrome number!")