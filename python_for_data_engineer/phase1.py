# 1. Python Foundation
# core concepts ( variables , data types , operators , input/output)

# varibales are nothing but name given to the value which stored in memory. variable is holding the memory location of the value
name = 'Malic'

# Data Types (int ,float , str, bool, complex)
# this all data types are immutable (meaning once it created we not do modification)
name1 = 'maxco'
age = 25
salary = 2500
is_male = True

# opearators ( arithmetic , assignment , comparison , logical , identity, membership)
"""
arithmetic --> (+ , -, *, /, //, %, **)
assignment --> (+=, -=, *=, /=, //=, %=, **=)
compersion --> (==, != , >, <, >=, <=)
logical --> (and , or , not)
membership --> (in , not in )
identity --> (is , is not)"""

# input / output 
# output --> print() function used to print the result in terminal
# name = input()
print(f'Hello, {name}')

import sys
sys.path.append("/home/ravi/Downloads/Data_eng_workspace/Python_Basices")

from python_moduls_and_packages.first_data_pipeline import reader,transformer,write

data = reader.read_data()
transformed = transformer.transform(data)
clean_data = write.writer(transformed)





