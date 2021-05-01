
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pylab
import matplotlib.patches as mpatches


i = np.linspace(0, 7, 8, endpoint=True)
i = 0

moocolors = '#1A1E22'
moozcolor = 'beige'
nameomoon = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Third Quarter", "Waning Crescent"]
comoon = [moocolors, moocolors, moocolors, moocolors, moozcolor, moozcolor, moozcolor, moozcolor]
cowomoon = [moocolors, moocolors, moocolors, moozcolor, moozcolor, moozcolor, moozcolor, moocolors]
cowooarc = [moocolors, moozcolor, moozcolor, moozcolor, moozcolor, moocolors, moocolors, moocolors]
zwomoon = [10, 11, 10, 10, 10, 11, 10, 10]
zwooarc = [10, 10, 11, 10, 10, 10, 11, 10]

sve = input("Would you like to save the graph? ").lower()
while i < 8:
    #fig = plt.figure()
    fig, ax = plt.subplots(facecolor="black")
    #to keep the circle shape +size
    ax.axis('equal')
    ax.set_aspect('equal')
    fig.set_figwidth(12)
    fig.set_figheight(6)
    ax.set(xlim=(0, 50), ylim = (0, 30))
    plt.axis('off')

    #black big moon
    ax.text(29, 4, nameomoon[i], color = '#7CB3B2', fontsize=10)
    moon = plt.Circle((6,15), 9, color = comoon[i])
    ax.add_patch(moon)
    ax.text(0, 4, "phase seen from earth", color= '#7CB3B2' , fontsize=12)

    womoon = mpatches.Ellipse((6,15), 10, 18, color = cowomoon[i], zorder = zwomoon[i])
    ax.add_patch(womoon)
    wooarc = mpatches.Wedge((6,15), 9, theta1=270, theta2=90, fill=True, color= cowooarc[i], zorder = zwooarc[i])
    ax.add_patch(wooarc)
    #orbit
    theta = np.linspace( 0, 2 * np.pi , 160 )
    radius = 9

    a = radius * np.cos( theta )
    b = radius * np.sin( theta )

    ax.plot(a+31.7, b+15, zorder=0)
    j = (20*i)-1

    #minimoon
    moox= a[j]+31.7
    mooy = b[j]+15
    moonmoon = plt.Circle((moox,mooy), 1, color = moocolors)
    ax.add_patch(moonmoon)
    mooarc = mpatches.Wedge((moox,mooy), 1, theta1=270, theta2=90, fill=True, color='beige')
    ax.add_patch(mooarc)
    #arrows
    plt.arrow(53, 20, -4, 0,  head_width = .8, width = 0.5, color='yellow')
    plt.arrow(53, 15, -4, 0,  head_width = .8, width = 0.5, color='yellow')
    plt.arrow(53, 10, -4, 0,  head_width = .8, width = 0.5, color='yellow')
    ax.text(49, 8, "sunlight", color= '#7CB3B2', fontsize=10)
    #textwrap

    #earth
    eh = ccrs.Orthographic()
    art = fig.add_subplot(196, projection=eh)
    art.add_feature(cfeature.LAND)
    art.add_feature(cfeature.OCEAN)
    #art.set_extent((-10,10,-10,10))
    if sve == "yes":
        plt.savefig("luna_%s.pdf" %i, format="pdf")

    i +=1

plt.show()
plt.close()
