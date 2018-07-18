nhapx = int(input("x = "))
nhap_tinh = input("Operation(+,-,*,/) :")
nhapy = int(input("y = "))
if nhap_tinh == "+":
    s = (nhapx + nhapy)
    print(nhapx," + ", nhapy, "=", s)
elif nhap_tinh == "-":
    s = (nhapx - nhapy)
    print(nhapx," - ", nhapy, "=", s)
elif nhap_tinh == "*":
    s = (nhapx * nhapy)
    print(nhapx," * ", nhapy, "=", s)
elif nhap_tinh == "/":
    s = float(nhapx / nhapy)
    print(nhapx," / ", nhapy, "=", s)
else : 
    print("Invalid")
    
