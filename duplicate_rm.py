import pandas

def dup_rm(file):
    df = pandas.read_csv(file, header=0)
    data_list = df.drop_duplicates()
    data_list.to_csv(file)
    print("done")

