s = input()
first = s.find('f')
last = s.rfind('f')
print(f"{first} {last}" if first != last and first != -1 else first if first != -1 else "", end="")