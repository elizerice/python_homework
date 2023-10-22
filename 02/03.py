full_line = 1400
line = 3
days = 2
if full_line / line % days  !=0:
    print(full_line / line // days + 1)
else: print(full_line / line // days)
