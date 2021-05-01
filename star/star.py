
import numpy as np
from astropy.io import fits
import synphot as syn
from textwrap import wrap
import matplotlib.pyplot as plt
#intro
print ("Welcome! By entering a few values below, you can classify any star.")
#available temps in ascendng order
print("\033[1;33;40m  \n")
mfile = np.loadtxt('models.txt')
mfile.sort()
print ("Here is the list of temperatures available:", mfile)
#temp input
print("\033[1;32;40m  \n")
temp = int(input("First enter the star's temperature in Kelvin: "))
#output
print("\033[1;36;40m  \n")
if temp == any(mfile):
    print ("This temp is available!")
    table = fits.getdata('kp00_%s.fits'%temp, memmap=True)
    #print(file.info())
else:
    print("This temp was not available but this is the closest temperature:")
    absolute_difference_function = lambda list_value : abs(list_value - temp)
    closest_value = min(mfile, key=absolute_difference_function)
    cv = int(closest_value)
    print(cv,"-")
    table = fits.getdata('kp00_%s.fits'%cv, memmap=True)
    #print(table.info())
#gravity input
print("\033[1;35;40m  \n")
print ("Here is the list of gravity available:", table.dtype.names [1:])
gravity = int(input("Now enter the gravity number of the star: "))
if gravity == 0 or gravity == 5:
    gravity = "g0%s"%gravity
else:
    gravity = "g%s"%gravity
#plotting on star spectra
y_min = min(table[gravity])
y_max = max(table[gravity])
if (y_min, y_max) == (0,0):
    print("\033[1;31;40m  \n")
    print ("try again! This star does not exist")
else:
    plt.figure()
    #plt.plot(table['wavelength'],table[gravity])
    plt.loglog(table['wavelength'],table[gravity])
    plt.tight_layout()
    til = "Graph of a star with a metalicity of 0,\n a temperature of "+ str(cv) + "\n and a gravity of " + str(gravity)
    #plt.title(til, fontsize=11)
    plt.text(.9,.1,til, ha='right',transform=plt.gca().transAxes )
    plt.xlabel('wavelength')
    plt.ylabel('gravity')
    #same prompt
    print("\033[1;31;40m  \n")
    sve = input("Would you like to save the graph? ").lower()
    if sve == "yes":
        plt.savefig("star_spectra_plot.pdf", format="pdf")
        plt.show()
        plt.close()
    else:
        plt.show()
        plt.close()
        print("Thank you!")
