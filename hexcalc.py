
import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

d = "0x{:x}".format(int(a,16))
e = "0x{:x}".format(int(c,16))

if (b == "+" or b == "add"):
    g = "0x{:x}".format(int(d,16)+int(e,16))
    print("\nThe result of adding "+d+" and "+e+" is: "+g+"\n")

if (b == "-" or b == "sub"):
    g = "0x{:x}".format(int(d,16)-int(e,16))
    print("\nThe result of subtracting "+d+" and "+e+" is: "+g+"\n")

if b == "mul":
    g = "0x{:x}".format(int(d,16)*int(e,16))
    print("\nThe result of multiplying "+d+" and "+e+" is: "+g+"\n")

if b == "div":
    g = "0x{:x}".format(int(d,16)/int(e,16))
    print("\nThe result of dividing "+d+" and "+e+" is: "+g+"\n")
