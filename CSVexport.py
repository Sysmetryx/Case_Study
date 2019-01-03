import os
import glob
import netCDF4
import numpy as np
import concurrent.futures
import time


def get_file_list(directory):
    """This function returns a listing of all .nc files in a directory

    Parameters
    ----------
    directory : str
            name or path of the directory
    """

    if directory is None:
        print("Directory missing")
        return None
    return glob.glob(directory + os.sep + "*.nc")


def get_list(file_list, i, variable):
    """This function returns a list of all data referenced as variable.
        it transforms the netCDF4 file to a flattened ndarray.

        Parameters
        ----------
        file_list : list
                the list in which to extract the data
        i : int
                The file from the list to work on
        variable : str
                the variable to extract
        Returns
        ----------
            flattened ndarray.
        """
    dataset = netCDF4.Dataset(file_list[i]).variables[variable][:, :]
    return np.array(dataset).flatten().tolist()


def export_csv(i):
    """This function saves all the data in a csv.

            Parameters
            ----------
            i : int
                    The file from the list to work on
            Returns
            ----------
                True if function ended correctly.
            """

    header = 'lon,lat,sst,412,443,490,555'
    full_list = [get_file_list('412'), get_file_list('443'),
                 get_file_list('490'), get_file_list('555'),
                 get_file_list('SST')]
    buffer = [np.loadtxt("lon.csv", delimiter=",").flatten().tolist()]
    buffer += [np.loadtxt("lat.csv", delimiter=",").flatten().tolist()]
    buffer += [get_list(full_list[4], i, 'SST')]
    buffer += [get_list(full_list[0], i, 'NRRS412_mean')]
    buffer += [get_list(full_list[1], i, 'NRRS443_mean')]
    buffer += [get_list(full_list[2], i, 'NRRS490_mean')]
    buffer += [get_list(full_list[3], i, 'NRRS555_mean')]
    buffer = np.array(buffer).T
    np.savetxt("fichiers_csv/" + "foo" + str(i) + ".csv", buffer, fmt='%f',
               delimiter=",",
               header=header)
    del buffer
    return True


def main():
    """This is the main function. it is multithreaded using concurrent.futures.
    Performances drop might be observed if used on a slow hard drive due to
    high Input/Output.
            """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nb_files = range(184)
        for i, state in zip(nb_files, executor.map(export_csv, nb_files)):
                print(str(i) + "   is " + str(state))
        print("All Done.")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
