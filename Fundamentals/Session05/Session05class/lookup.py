dictionary = {
    "hc" : "học",
    "ng" : "người",
    "pt" : "phát triển",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu",
    "ns" : "noi",
    "ngta": "nguoi ta",
    "lm" : "lam",
    "r" : "roi",
    "stt" : "status",

}
for key in dictionary.keys():
    print(key,end="\t")

print()
tra = True 
while tra:
    nhapcode = input("Your Code?").upper()
    if nhapcode in dictionary :
        print("* "*20)
        print()
        print("Code:",nhapcode)
        print("Translation:",dictionary[nhapcode])
        print()
        print("* "*20,)
        print()
    else :

        question = input("Not Found, Do you want to add it(Y/N)?").upper()
        if question == "N":
            tra=False
        else :
            nhapdich = input("Enter your translation:")
            dictionary[nhapcode] = nhapdich
            print("Code:",nhapcode)
            print("Translation:",dictionary[nhapcode])
            print("Updated")
            print()
            for key in dictionary:
                print(key)


    


