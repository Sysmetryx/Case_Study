from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt

# chargement des donées
data = np.loadtxt("fichiers_csv/foo0.csv", delimiter=",",
                  skiprows=1, usecols=[2, 3, 4, 5, 6])
# normalisation
X = StandardScaler().fit_transform(data)
# Calcul de la pca
pca = PCA(n_components=5)
pca.fit(X)

print(pca.components_)
# plt.figure()
# plt.barh(y=[1, 0] , width=pca.explained_variance_)
# plt.show()
# principalComponents = pca.fit_transform(X)
# colors = X[:, 2]
# principalDf = pd.DataFrame(data=principalComponents,
#                            columns=['principal component 1',
#                                     'principal component 2'])
# # Tracer la figure
# fig = plt.figure(figsize=(30, 30))
# ax = fig.add_subplot(1, 1, 1)
# ax.set_xlabel('Principal Component 1', fontsize=15)
# ax.set_ylabel('Principal Component 2', fontsize=15)
# ax.set_title('2 component PCA', fontsize=20)
# ax.scatter(principalDf['principal component 1'],
#            principalDf['principal component 2'], c=colors, cmap='jet', s=40)
# ax.grid()
# plt.show()
#cercle de correlation
fig, axes = plt.subplots(figsize=(15,15))
axes.set_xlim(-1, 1)
axes.set_xlim(-1, 1)
header = ['lon', 'lat', 'sst', '412', '443', '490', '555']
corvar = np.zeros((5, 5))

sqrt_eigval = np.sqrt(pca.explained_variance_)
for k in range(5):
    corvar[:, k] = pca.components_[k, :] * sqrt_eigval[k]

for j in range(5):
    plt.annotate(s=header[j], xy=(corvar[j,0], corvar[j,1]))

plt.plot([-1,1],[0,0],linestyle='-',linewidth=1)
plt.plot([0,0],[-1,1],linestyle='-',linewidth=1)
cercle = plt.Circle((0,0),1,color='blue',fill=False)
axes.add_artist(cercle)
plt.show()
