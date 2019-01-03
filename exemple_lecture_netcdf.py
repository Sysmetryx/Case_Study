
# coding: utf-8

# ### Lecture des donnees pour etude de cas :
# ## _Etude de la variabilité du phytoplancton au niveau de la Mer Méditerranée en utilisant les cartes auto-organisatrices (SOM)_

# In[1]:


# -*- coding: utf-8 -*-
import os
import glob
import netCDF4


# ### _Exemple de lecture des données `Chl` :_

# In[2]:


# repertoires de donnees pour chaque parametre
datadir1 = '../data/Chl'


# In[3]:


# listes de fichiers 
filelist1 = glob.glob(datadir1 + os.sep + "*.nc")


# In[4]:


datadir1 + os.sep + "*.nc"


# In[5]:


#filelist1


# In[6]:


# Lecture d'un fichier NetCDF ...
ific = 0


# ### lecture  ... à mettre dans une boucle pour lire tous les données Chl  ...
# 
# ### idem pour les autres variables  ...
# 

# In[7]:


# lecture de l'element ific, ...a mettre dans un boucle pour lire tous les autres ...
ncfile = filelist1[ific]


# In[8]:


ficnom = os.path.basename(ncfile) # recupere le nom du fichier, sans le chemin

# recupere la date a partir du nom (encadree entre le premier et deuxieme tiret bas '_')
i0 = ficnom.find('_')  # cherche la position du premier '_', 
i1 = ficnom.find('_',i0+1)  # cherche la position du deuxieme '_'
j0 = ficnom[i0:i1].find('-')  # cherche dans l'intervalle la position du premier '-', 

# recupere les caracteres qui devraient correspondre a la date de depart
date_ini = int(ficnom[(i0+1):(i0+j0)]);

# recupere les caracteres qui devraient correspondre a la date de fin
date_fin = int(ficnom[(i0+j0+1):(i1)]);

# data ini et fin au format numerique, a vous de la separer
# en annee, mois et jour, si vous en avez besoin
print(date_ini,date_fin)


# In[9]:


# Lecture d'un fichier NetCDF ...
nc = netCDF4.Dataset(ncfile);
liste_var = nc.variables;       # mois par mois de janvier 1930 à decembre 1960 I guess

# Prospection pour connaitre le nom des variables contenues dans le fichier
# a faire manuellement pour les autres donnees: PFT, SST, 412, ...
print("\n Fichier NetCDF:\n    {}\n\n Variables trouvées dans ce fichier:".format(ficnom))
for ivar,var in enumerate(liste_var.keys()) :
    print("    var {:d} ... ''{:s}''".format(ivar,var))


# In[10]:


# Extraction des variables d'un fichier NetCDF

# les coordonnees
lon = liste_var['lon']
lat = liste_var['lon']

# recupere la Chlorophylle (elle s'appelle 'CHL-OC5_mean') ...
chl_tmp = liste_var['CHL-OC5_mean']

# etc, etc, etc

