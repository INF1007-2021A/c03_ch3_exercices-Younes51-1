#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    result=(a+b+c)/3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degs=angle_degs+(angle_mins+angle_secs/60)/60
    degs_to_rads=degs*math.pi/180
    return degs_to_rads


def to_degrees(angle_rads: float) -> tuple:
    deg = math.degrees(angle_rads)
    min = (deg % 1) * 60
    sec = (min % 1) * 60
    return deg - min, min - sec, sec


def to_celsius(temperature: float) -> float:
    celsius=(temperature-32)/1.8
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit=temperature*1.8+32 
    return farenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
