import os
import pandas as pd

# reading from CSV File 
# storing the data to a new variable "data"
data = pd.read_csv(
    "Test_Student.csv", 
    na_values=['NA', '?'])

## i have named each column has A, B, C

#using sort function, i have sorted pandas dataframe row according to the first column
# storing the sorted data to a new variable result
result = data.sort_index(by=['A'], ascending=[True])

display(result[0:16])

#export csv is used to store the result variable in a .CSV format
export_csv = result.to_csv (r'Result_Test_student.csv', index = None, header=True)
