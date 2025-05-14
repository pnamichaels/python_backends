'''
String Formatting
'''

first_name = "Payton"
last_name = "Michaels"
sentence = "hi {}"
print("Hi " + first_name)
print(f"Hi {first_name} {last_name}")
print(sentence.format(first_name, last_name))