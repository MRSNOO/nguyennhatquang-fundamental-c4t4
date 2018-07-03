prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}
total = 0 
for keys,values in prices.items():
    print(keys,":",values)
for keys in prices:
    tich = stock[keys]*prices[keys]
    print(tich)
    total = total + tich
print("Total amount:",total)
