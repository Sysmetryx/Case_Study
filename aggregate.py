import numpy as np
import time


def aggregate(i):
    filename = "foo" + str(i) + ".csv"
    file = np.loadtxt(filename, delimiter=",", skiprows=1)
    with open("fullFile.csv", "a") as text_file:
        file.tofile(text_file, ",", "%.10s")
    del filename
    del file


def main():
    for i in range(184):
        aggregate(i)
        print(i)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))