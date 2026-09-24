#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 23rd Sep, 2026
# This program asks the use for the radius of
# a circle in mm. it then calculates and displays
# the circumference using tau.
import constants


def main():
    # get the radius from user
    radius = float(input("Enter the radius of circle (mm):"))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
