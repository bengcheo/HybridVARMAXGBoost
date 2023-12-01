#HELPER FUNCTIONS

#train test split function
def ts_train_test_split(df, period):
    train = df[df.index < period]
    test = df[df.index >= period] 
    
    return train, test

#checking for stationarity

#johansen integration test function
def joh_output(res):
    output = pd.DataFrame([res.lr2,res.lr1], index=['max_eig_stat',"trace_stat"])
    rank = np.linalg.matrix_rank(output)
    print(output.T,'\n')
    print("Critical values(90%, 95%, 99%) of max_eig_stat\n",res.cvm,'\n')
    print("Critical values(90%, 95%, 99%) of trace_stat\n",res.cvt,'\n')
    print("Rank of matrix,",rank)