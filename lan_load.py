# -*- coding: utf-8 -*-
"""
loading CDF4
@author:LNA_
"""
import os
import glob
import netCDF4
import numpy as np
import matplotlib.pyplot as plt
import math
#plt stuff to be pretty
plt.rcParams['figure.figsize'] = 10,10
plt.close()
#where to find files
mainDir = 'D:\\Users\\NATHZN\\Desktop\\Nouveau dossier (4)\\'
datadir1 =  mainDir + '412'
filelist1 = glob.glob(datadir1 + os.sep + "*.nc")
#loading the actual files
ncFile = []
for i in range(0,len(filelist1),1):    
    ncFile +=  [filelist1[i]]
#extracting the netcdf
nc = []
for i in range(0,len(ncFile),1):
    nc += [netCDF4.Dataset(ncFile[i])]
#displays the different variable names and info
listVar = []
for i in range(0,len(nc),1):
    listVar += [nc[i].variables] 
for ivar,var in enumerate(listVar[0].keys()) :
    print("    var {:d} ... ''{:s}''".format(ivar,var))
#Actually does something with data :
temp = []
for i in range(0,len(nc),1): 
    #Print the Matrix as map
    sst = nc[i].variables['SST'][:,:]
#    plt.matshow(sst)
#    plt.colorbar()
#    plt.title('Estimation de la SST en °C ', fontsize=22)
#    plt.show()
#    print(i)
    #Flattends the matrix, removes NAN values, do average
#    for x in sst:
#        for y in x:
#            if not(math.isnan(y)):
#                temp.append(y)
#Display Boxplot
#plt.boxplot(temp, notch = False, vert=True,showfliers=False)
#plt.title('Boite moustache de la sst moyenne', fontsize=22)
#plt.show()
#Display info
temp2 = []
for i in range(0,len(nc)):
    print(i)
    temp2 += [np.nanmin(nc[i].variables['SST'][:,:])]
    print(temp2[i])
print('test = '+str(np.min(temp2)))
#print('Moyenne des sst  = ' + str(np.average(temp)))
#print('Variance des sst = ' + str(np.std(temp)))
#print('Valeur minimum des sst  = ' + str(np.min(temp)))
#print('Valeur maximum des sst  = ' + str(np.max(temp)))