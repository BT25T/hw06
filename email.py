s = input("Email: ");
add = None

for i in range(len(s)):
    if s[i] == '@':
        add = i
        break

if add is None or add == 0 or add == len(s) - 1:
    print("Invalid email")
else:
    print(f"Username: {s[:add]}")
    print(f"Domain: {s[add+1:]}")