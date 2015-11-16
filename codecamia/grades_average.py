grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    print total
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    print average
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    a = variance / float(len(scores))
    print a
    return a

def grades_std_deviation(variance):
    a = variance ** 0.5
    return a

variance = grades_variance(grades)
print_grades(grades)
print grades_std_deviation(variance)
