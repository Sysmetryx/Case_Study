import numpy as np
import concurrent.futures
import time


def load_csv(filename):
    return np.loadtxt(filename + ".csv", delimiter=",", skiprows=1)


def save_csv(filename, data):
    header = "lon,lat,sst,412,443,490,555"
    np.savetxt(filename + ".csv", data, fmt='%f', delimiter=",",
               header=header)


def delete_nan_rows(data):
    return data[~np.isnan(data).any(axis=1)]


def delete_999(data):
    return data[~np.any(data == -999.000000, axis=1)]


def alter_csv(i):
    filename = "foo" + str(i)
    data = load_csv(filename)
    data = delete_nan_rows(data)
    data = delete_999(data)
    save_csv(filename, data)
    del data
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nb_files = range(184)
        for i, state in zip(nb_files, executor.map(alter_csv, nb_files)):
                print("Job " + str(i) + "   is done.")
        print("All Done.")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))