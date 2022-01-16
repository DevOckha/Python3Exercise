# bellek yer işgal etmeyen bir iterator üretiyor


# def cube():
#     for i in range(5):
#         yield i ** 3

# for i in cube():
#     print(i)


generator = (i**3 for i in range(5))
print(generator)