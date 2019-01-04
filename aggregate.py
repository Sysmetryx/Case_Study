import numpy as np
import time


def aggregate(i, fullFile):
    if i == 0 :
        filename = "fichiers_csv/" + "foo" + str(i) + ".csv"
        file = np.loadtxt(filename, delimiter=",", skiprows=1)
        return file
        del file
    else:
        filename = "fichiers_csv/" + "foo" + str(i) + ".csv"
        file = np.loadtxt(filename, delimiter=",", skiprows=1)
        new = np.append(fullFile, file, axis=0)
        del file
        return new
        del new


def main():
    fullFile = []
    for i in range(184):
        fullFile = aggregate(i, fullFile)
        print(i)
    header = "lon,lat,sst,412,443,490,555"
    np.savetxt("fullFile.csv", fullFile, delimiter=",", header=header, fmt='%f')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))