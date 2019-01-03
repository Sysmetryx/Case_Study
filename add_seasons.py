import numpy as np
import concurrent.futures
import time


def one_file_season(i):
    year = 99
    week = 99
    year_check = np.floor(i/52)
    if year_check == 0:
        year = 2014
        week = i
    elif year_check == 1:
        year = 2015
        week = i - 1
    elif year_check == 2:
        year = 2016
        week = i - 2
    elif year_check == 3:
        year = 2017
        week = i - 3
    if year != 99 and week != 99:
        header = "lon,lat,sst,412,443,490,555,year,week"
        file = np.loadtxt("foo" + str(i) + ".csv", delimiter=",",
                   skiprows=1)
        print(file.shape)
        year = [year]*len(file[:, 0])
        print(len(year))
        file = np.append(file, year, axis=1)
        week = [week] * len(file[:, 0])
        file = np.append(file, week, axis=1)
        np.savetxt("foo" + str(i) + ".csv", file, fmt=['f', 'f', 'f', 'f',
                                                       'f', 'f', 'f', 'd' 'd'],
                   delimiter=",",
                   header=header)


def get_year(i):
    return np.floor((i + 1)/52) - 1


def get_week(i, year):
    return i - (year * 52)


def get_season(week):
    if week >= 12 and week < 25:
        return 1
    elif week >= 25 and week < 38:
        return 2
    elif week >= 38 and week < 51:
        return 3
    else:
        return 0


def append_week_year_season(i):
    original_file = np.loadtxt("fichiers_csv/" + "foo" + str(i) + ".csv",
                               delimiter=",",
                   skiprows=1)
    final_header = "lon,lat,sst,412,443,490,555,year,week,season"
    year = get_year(i)
    week = get_week(i, year)
    season = get_season(week)
    temp = np.array([year]*original_file.shape[0])
    print(original_file.shape)
    print(temp.shape)
    original_file = np.insert(original_file, original_file.shape[1],
                              temp, axis=1)
    temp = np.array([week] * original_file.shape[0])
    original_file = np.insert(original_file, original_file.shape[1],
                              temp, axis=1)
    temp = np.array([season] * original_file.shape[0])
    original_file = np.insert(original_file, original_file.shape[1],
                              temp, axis=1)
    np.savetxt("foo" + str(i) + ".csv", original_file, delimiter=",", fmt='%f',
               header=final_header)



def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nb_files = range(184)
        for i, state in zip(nb_files, executor.map(append_week_year_season, nb_files)):
                print("Job " + str(i) + "   is done.")
        print("All Done.")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))