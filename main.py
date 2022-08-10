import os

from DataOperations import import_data
import matplotlib.pyplot as plt
from Interpolation import splain_params, lagrange, splain
import random


def main():
    files = [ 'SpacerniakGdansk.csv', 'MountEverest.csv', 'Hel_yeah.csv']
    for node in nodes:
        for filename in files:
            dis, height = import_data(filename)
            step = int(len(dis) / node)
            to_inter_dis = dis[0:len(dis):step]
            to_inter_height = height[0:len(height):step]

            # Lagrange
            l_inter_height = []
            l_inter_height_ = []
            # Splain
            params4 = splain_params(to_inter_dis, to_inter_height)
            s_inter_height = []

            for x in dis:
                l_inter_height.append(lagrange(to_inter_dis, to_inter_height, x))
                s_inter_height.append(splain(to_inter_dis, x, params4))
            for x in to_inter_dis:
                l_inter_height_.append(lagrange(to_inter_dis, to_inter_height, x))

            # Lagrange
            plt.semilogy(dis, height, c='blue')
            plt.semilogy(dis, l_inter_height, c='hotpink')
            plt.semilogy(to_inter_dis, l_inter_height_, 'o',
                         c='red',
                         markersize=3)
            plt.legend(["Funkcja rzeczywista ", "Funckja interpolująca", "Punkty interpolowane"])
            plt.title('Plik ' + str(filename) + ' dla ' + str(node) + ' węzłów \n Interpolacja Metodą '
                                                                                      'Lagrange', loc='right',
                      fontsize=13, color='grey', style='italic')
            plt.xlabel('Dystans')
            plt.ylabel('Wysokość')
            png_name = 'C:/Users/kacpe/Desktop/Metody Numeryczne/Projekt/pythonProject4/plots/' + 'Lagrange_' + str(filename) + '_wezlow_' + str(node) + '.png'
            plt.savefig(png_name)
            plt.show()
            # Splain
            plt.plot(dis, height, c='blue')
            plt.plot(dis, s_inter_height, c='hotpink')
            plt.plot(to_inter_dis, to_inter_height, 'o',
                     c='red',
                     markersize=3)
            plt.legend(["Funkcja rzeczywista ", "Funckja interpolująca", "Punkty interpolowane"])
            plt.title('Plik ' + str(filename) + ' dla ' + str(node) + ' węzłów \n Interpolacja Metodą '
                                                                                      'Splajnów', loc='right',
                      fontsize=13, color='grey', style='italic')
            plt.xlabel('Dystans')
            plt.ylabel('Wysokość')
            png_name = 'C:/Users/kacpe/Desktop/Metody Numeryczne/Projekt/pythonProject4/plots/' + 'Splain_' + str(filename) + '_wezlow_' + str(node) + '.png'
            plt.savefig(png_name)
            plt.show()


if __name__ == "__main__":
    # tablica liczby punktów węzłowych
    nodes = [5, 10, 25, 50, 100]
    main()
