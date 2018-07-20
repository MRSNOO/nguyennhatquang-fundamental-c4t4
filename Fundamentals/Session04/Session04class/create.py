favorite = ["eat", "play", "sleep"]

print("Hi there here are your favorite things so far")
print()
print(*favorite,sep=", ")
thing=input(" Name one thing you want to add:")
favorite.append(thing)
print(*favorite,sep=", ")
