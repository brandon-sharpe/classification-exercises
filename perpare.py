def prep_iris_data(iris):
    '''
   
    '''
    iris = iris.drop(['Unnamed: 0','species_id'], axis= 1)
    iris = iris.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(iris[['species']], dummy_na=False, drop_first=[True])
    iris = pd.concat([iris, dummy_df], axis=1)
    
    return iris