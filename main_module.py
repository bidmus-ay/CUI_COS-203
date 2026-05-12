import input_module
import logic_module
import output_module

# Get data
name, score = input_module.get_student_data()

# Calculate grade
grade = logic_module.calculate_grade(score)

# Display result
output_module.display_result(name, score, grade)