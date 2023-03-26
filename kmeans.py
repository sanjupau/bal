import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc(
    "axes",
    labelweight="bold",
    labelsize="large",
    titleweight="bold",
    titlesize=14,
    titlepad=10,
)

df = pd.read_excel("kmeans.xlsx")
X = df.loc[:, ["MedInc", "Latitude", "Longitude"]]
X.head()

# Create cluster feature
kmeans = KMeans(n_clusters=5)
X["Cluster"] = kmeans.fit_predict(X)
X["Cluster"] = X["Cluster"].astype("category")
X.head()

sns.relplot(
    x="Longitude", y="Latitude", hue="Cluster", data=X, height=5,
);

