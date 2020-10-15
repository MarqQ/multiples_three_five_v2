from three_five import multiple


n = [(pos, multiple(pos)) for pos in range(1, 101)]
print(n)
