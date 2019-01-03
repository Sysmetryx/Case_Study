from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt


# chargement des donées
data = np.loadtxt("fichiers_csv/" + "foo3" + ".csv", delimiter=",",
                  skiprows=1, usecols=[2, 3,
                                                                       4, 5,
                                                                       6])
# normalisation
X = StandardScaler().fit_transform(data)
# Calcul de la pca
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data=principalComponents,
                           columns=['principal component 1',
                                    'principal component 2'])
# Tracer la figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
ax.scatter(principalDf['principal component 1'],
           principalDf['principal component 2'])
ax.grid()
plt.show()
