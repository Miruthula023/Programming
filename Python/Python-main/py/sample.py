str = "A B C D E"
str2 = "C O M P U T E R"

i = 2
c = 15

for x in str:

   if(x == " "):
       continue

   print(str[:i])
   i+=2

print("\n")

for o in str2:

    if(o == " "):
        continue
    print(str2[:c])
    c-=2

