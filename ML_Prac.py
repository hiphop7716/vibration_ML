import pandas as pd

#顯示所有列
pd.set_option('display.max_columns', None)
#顯示所有行
pd.set_option('display.max_rows', None)
#設置value的顯示長度為100，預設為50
pd.set_option('max_colwidth',100)

def corr_matrix(df, size=6, method="pearson"):
    from matplotlib import pyplot as plt
    import numpy as np

    correlations = df.corr(method)
    # plot correlation matrix
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, size, 1)
    # ax.set_xticks(ticks)
    # ax.set_yticks(ticks)
    # ax.set_xticklabels(labels)
    # ax.set_yticklabels(labels)

    plt.xticks(range(len(correlations.columns)), correlations.columns)
    plt.yticks(range(len(correlations.columns)), correlations.columns)
    plt.show()

def scatter_matrix(df):
    from matplotlib import pyplot as plt
    from pandas.plotting import scatter_matrix

    scatter_matrix(df)
    plt.show()

#========================================================================#

# 讀入 csv 文字檔
csv_file = "ML_Data_1563467378.csv"
vib_df = pd.read_csv(csv_file, encoding='utf-8')
# print(type(vib_df))
vib_df.head()


# print(vib_df.iloc[1][4])

vib_df_transpose = vib_df.transpose()
vib_df_transpose.to_csv(csv_file[:-4] + '_output.csv', index=False, encoding='big5')

# scatter_matrix(vib_df) #plot scatter form of correlation matrix
# corr_matrix(vib_df, 12, "kendall") #plot correlation matrix
#kendall
#spearman

#For output corr result
# corr_df = vib_df.corr()
# corr_df.to_csv('output.csv', index=False, encoding='big5')