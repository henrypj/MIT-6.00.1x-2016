# Example 0
def permutations(word):
    if len(word) == 1:
        return [word]
    else:
        # get all permutations of length N-1
        perms = permutations(word[1:])
        char = word[0]
        result = []   # a list of all permutations of word
        for perm in perms:
            for i in range(len(perm)+1):
                result.append(perm[:i] + char + perm[i:])
        return result

print("Example 0") 
print(permutations('abc'))
        

# Example 1
def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

print("Example 1")
print(Permute('abc'))

# Example 2
def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l


data = list('abc')
print('Example 2')
for p in perm1(data):
    print(p)

# Example 3
def perm2(lst):
    if len(lst) == 0:
        yield ['']
    elif len(lst) == 1:
        yield str(lst)
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm2(xs):
                yield x+p
        return l

data = 'abc'
print('Example 3')
for p in perm2(data):
    print(p)
    