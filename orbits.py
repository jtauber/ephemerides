# encoding: utf-8

import math

# first number is mean anomaly at J2000
# second number is change in mean anomaly per day
# third item is list of coefficients for the equation of center

Mercury = (174.7948, 4.09233445, [23.4400, 2.9818, 0.5255, 0.1058, 0.0241, 0.0055])
Venus = (50.4161, 1.60213034, [0.7758, 0.0033])
Earth = (357.5291, 0.98560028, [1.9148, 0.0200, 0.0003])
Mars = (19.3730, 0.52402068, [10.6912, 0.6228, 0.0503, 0.0046, 0.0005])
Jupiter = (20.0202, 0.08308529, [5.5549, 0.1683, 0.0071, 0.0003])
Saturn = (317.0207, 0.03344414, [6.3585, 0.2204, 0.0106, 0.0006])
Uranus = (141.0498, 0.01172834, [5.3042, 0.1534, 0.0062, 0.0003])
Neptune = (256.2250, 0.00598103, [1.0302, 0.0058])


def sin(deg):
    return math.sin(2 * math.pi * deg / 360)


def mean_anomaly(planet, j2000):
    return (planet[0] + planet[1] * j2000) % 360


def true_anomaly(planet, j2000):
    m = mean_anomaly(planet, j2000)
    # unlike my mars clock, this doesn't consider pertubations
    return m + sum(c * sin((i + 1) * m) for i, c in enumerate(planet[2]))


def deg2dms(deg):
    d, t = divmod(deg, 1)
    m, s = divmod(t * 3600, 60)
    return u"%d° %d′ %f″" % (d, m, s)
