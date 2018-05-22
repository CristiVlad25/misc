import sys

if sys.argv[1]=='--help':
        print("\nUsage: python hexcalc.py address1 operator address2\n"+
               "Example: python hexcalc.py 0x3f + 0x3a\n"+
               "Possible operators: + (or 'add'), - (or 'sub'), mul, and div\n")

else:

        try:

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

        except:
                print("\nUsage: python hexcalc.py address1 operator address2\n"+
                       "Example: python hexcalc.py 0x3f + 0x3a\n"+
                       "Possible operators: + (or 'add'), - (or 'sub'), mul, and div\n")
