import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
import pandas as pd
import time
from sklearn.cluster import MiniBatchKMeans

# np.set_printoptions(suppress=True)
pd.set_option('display.float_format', lambda x: '%.2f' % x) #为了直观的显示数字，不采用科学计数法
# train_df.describe()


data = pd.read_csv('loc1.txt')
data.head()
print(data)
print(data.shape)
x = data.iloc[:,:]
print(x)
plt.figure(figsize=(10,10),dpi=80)
plt.scatter(x.iloc[:,1],x.iloc[:,0],marker="o")
plt.show()

start_time = time.time()
#传统kmean
mod = KMeans(n_clusters=15,random_state=9)

#最小化kmean
# mbk = MiniBatchKMeans(
#     init="k-means++",
#     n_clusters=15,
#     batch_size=45,
#     n_init=10,
#     max_no_improvement=10,
#     verbose=0,
# )
# mod = mbk.fit(x)

y_pre = mod.fit_predict(x)
end_time = time.time()
print(end_time-start_time)
plt.figure(figsize=(10,10),dpi=80)
plt.scatter(x.iloc[:,1],x.iloc[:,0],c=y_pre)
plt.show()
r1 = pd.Series(mod.labels_).value_counts()
r2 = pd.DataFrame(mod.cluster_centers_)
r = pd.concat([r2,r1],axis=1)
r.columns = ["x","y","num"]
print(r)