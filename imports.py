import Imports.grade_average_service as grade_service
import Imports.standardlib as stock_libs

random_int = stock_libs.random.randrange(1, 1000)
print(random_int)

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81
}

grade_service.calculate_homework(homework_assignment_grades)