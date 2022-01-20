import pandas as pd
from pathlib import Path
import os
print("__file__: {}".format(__file__))

BASE_DIR = Path(__file__).resolve().parent

filenameTitanic = "titanic_custom.csv"
filenameCustomerChurn = "Customer Churn Model.txt"
fileNameColumnsCostumerChurn = "Customer Churn Columns.csv"
pathData = r"data\python-ml-course-master\datasets"

mainpathTitanic = os.path.join(BASE_DIR,pathData+r"\titanic",filenameTitanic)
mainpathCustumerChurn = os.path.join(BASE_DIR,pathData+r"\customer-churn-model",filenameCustomerChurn)
mainpathCustumerChurnColumns = os.path.join(BASE_DIR,pathData+r"\customer-churn-model",fileNameColumnsCostumerChurn)
#########PARAMETROS DE READ CSV
# pd.read_csv(
#     filepath = "",
#     sep = ",",
#     dtype = None, 
#     header = 0, 
#     names={"column1","column2"},
#     skiprows =12,
#     index_col=None,
#     skip_blank_lines= False,
#     na_filter=False
# )
##DATA TITANIC
dataTitanic = pd.read_csv(mainpathTitanic)
#print(dataTitanic.head())
###DATA CUSTUMER CHURN
dataCustumerChurn = pd.read_csv(mainpathCustumerChurn)
#print(dataCustumerChurn.head())
dataCustumerChurnColumns = pd.read_csv(mainpathCustumerChurnColumns)
#print(dataCustumerChurnColumns)
dataColumnslist = dataCustumerChurnColumns["Column_Names"].tolist()
#print(dataColumnslist)
dataCustumerChurn.columns = dataColumnslist
print(dataCustumerChurn["U"])















