
def fill_missing_values(df):
    """ This function fill the missing values 
        of columns with object datatype using 
        mode and columns with numeric datatypes
        with median"""
    objectTypeCols = [col_name for col_name in df.columns.tolist() if df.dtypes[col_name] == object]
    numericTypeCols = [col_name for col_name in df.columns.tolist() if col_name not in objectTypeCols]
    print(objectTypeCols)

    #for object type columns use mode
    for col in objectTypeCols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    #for numeric type columns use median
    for col in numericTypeCols:
        df[col] = df[col].fillna(df[col].median())
    return df
    
def Handle_missing_values(df,drop_rows=True,drop_cols=True):
        """ This function handles missing values
            by removing columns with more than 30%
            null values and filling others"""

        # removed columns containing null values of more than 30%
        row,col = df.shape
        if drop_cols:
            df.dropna(axis='columns',thresh=row*0.7,inplace=True)

        # for columns still with missing values drop rows
        if drop_rows:
            df.dropna()

        # for columns still with missing values fill appropriately
        else:
            df = fill_missing_values(df)

        
        return df