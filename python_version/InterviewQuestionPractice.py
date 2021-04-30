# from collections import defaultdict
#
# even_grades = [("Bobasdf", 100), ("BobSSS", 100), ("Mob", 100), ("Tob", 100), ("aob", 70)]
# student_grade = defaultdict(list)
# for names, grade in even_grades:
#     student_grade[names].append[grade]
# print(student_grade)

# from collections import Counter
#
numbers = [1,2,3,4,5,5,2,1,1,1,1]

counts = Counter(numbers)
print(counts)

top2 = counts.most_common(2)
print(top2)

arr1 = [1,3,5,6]
target1 = 8

arr2 = [4,7,2,6]
target2 = 12

def two_sum(arr, target):
    values = dict()

    for i, elem in enumerate(arr):
        comp = target - elem
        if comp in values:
            return [values[comp], i]
        values[elem] = i
    return []

list1 = two_sum(arr1, target1)
print(list1)