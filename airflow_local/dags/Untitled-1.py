def test_data(**kwargs):
    read_path="/opt/data/DATA_CENTER/DATA_LAKE"
    ticker=kwargs['ticker']
    latest = np.max([float(file.split("_")[-1]) for file in os.listdir(read_path)if ticker in file])
    latest_file = [file for file in os.listdir(read_path) if str(latest)in file][0]
    
    file=open(read_path+latest_file)
    data=json.load(file)

    condition_1 = len(data.keys())==2
    condition_2 = 'Time Series (5min)' in data.keys()
    condition_3 = 'Meta Data' in data.keys()

    if condition_1 and condition_2 and condition_3:
        pass
    else:
        raise Exception('The data integrity has been compromised')
def clean_market_data(**kwargs):
    read_path="/opt/airflow/data/DATA_CENTER/DATA_LAKE"
    ticker=kwargs['tickers']
    for tick in ticker:
        latest = np.max([float(file.split("_")[-1]) for file in os.listdir(read_path)if tick in file])
        latest_file = [file for file in os.listdir(read_path) if str(latest)in file][0]

        output_path="/opt/airflow/data/DATA_CENTER/CLEAN_DATA"
        file=open(read_path+latest_file)
        data=json.load(file)#read from somewhere #we will read the json from our raw datalake
        clean_data=pd.DataFrame(data['Time Series (5min)']).T
        clean_data['ticker']= data['Meta Data']['2. Symbol']
        clean_data['meta_data']=str(data['Meta Data'])
        clean_data['timestamp']= pd.to_datetime('now')

        #we will want to store the result in the clean data lake
        clean_data.to_csv(output_path+tick+'_snapshot_intraday_'+str(pd.to_datetime('now'))+'.csv')

     task_1 = PythonOperator(task_id = "clean_market_data", python_callable = clean_market_data, op_kwargs = {'tickers' : list_of_stocks})   
    task_1 = PythonOperator(task_id = "test_market_data", python_callable = test_data, op_kwargs = {'tickers' : list_of_stocks})