mixed = (1,2,3,4,0)

# for loop and tuple 
for i in mixed:
    print(i)
# NOTE - You can use while loop too 

# tuple with one element
nums = (1)
words = ("word1",)
print(type(nums))
print(type(words))

# tuple without parenthesis
guitars = 'yamaha','baton rouge', 'taylor'
print(type(guitars))



# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie Van Der Meer', 'Andrew Foy')
guitarists1, guitarists2, guitarists3 = (guitarists)
# print(guitarists1)



# list inside tuples
favourites = ('southern magnolia', ['Tokyo Ghoul Theme', 'landscape'])
favourites[1].pop()
favourites[1].append("we made it")
print(favourites)


# min() , max(, sum())
print(sum(mixed))