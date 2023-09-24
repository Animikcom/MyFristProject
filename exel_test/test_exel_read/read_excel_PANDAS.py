import pandas as pd

excel_data = pd.read_excel('sales.xlsx', header=None)
data = pd.DataFrame(excel_data)
print("The content of the file is:\n", data)
count_row = data.shape[0]
trnsmital= (data.loc[0, 9])
contract= (data.loc[12, 9])
print (trnsmital)
print (contract)
x= 26
while x < count_row:
    val= (data.loc[x, 9])
    if str(val)!="nan":
        print (val)
    x+=1
