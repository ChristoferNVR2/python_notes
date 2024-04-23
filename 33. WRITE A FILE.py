text = 'Oh no, this text was overwritten!\n'


with open('test.txt', 'w') as file:  # 'w' means write mode
    file.write(text)

with open('test.txt', 'a') as file:  # 'a' means append mode
    file.write('This text was appended!\n')
  
