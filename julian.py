import time

JD_AT_UNIX_EPOCH = 2440587.5
SECS_PER_DAY = 86400
JD_AT_1_JAN_2000 = 2451545.0
DAYS_PER_CENTURY = 36525


def unix2jd_ut(unix_time=None):
    """
    calculate the Julian Date (UT) given seconds since unix epoch
    (or current Julian Date if no argument is given)
    """
    if unix_time is None:
        unix_time = time.time()
    return JD_AT_UNIX_EPOCH + (unix_time / SECS_PER_DAY)


TAI_UTC_DIFF = [
    (2441317.5, 10.0),
    (2441499.5, 11.0),
    (2441683.5, 12.0),
    (2442048.5, 13.0),
    (2442413.5, 14.0),
    (2442778.5, 15.0),
    (2443144.5, 16.0),
    (2443509.5, 17.0),
    (2443874.5, 18.0),
    (2444239.5, 19.0),
    (2444786.5, 20.0),
    (2445151.5, 21.0),
    (2445516.5, 22.0),
    (2446247.5, 23.0),
    (2447161.5, 24.0),
    (2447892.5, 25.0),
    (2448257.5, 26.0),
    (2448804.5, 27.0),
    (2449169.5, 28.0),
    (2449534.5, 29.0),
    (2450083.5, 30.0),
    (2450630.5, 31.0),
    (2451179.5, 32.0),
    (2453736.5, 33.0),
    (2454832.5, 34.0),
    (2456109.5, 35.0),
]


def tt_utc_diff(jd_ut):
    """
    calculate the difference between terrestrial time and UT for a given
    Julian Date (UT)
    """
    prev_offset = None
    for start, offset in TAI_UTC_DIFF:
        if jd_ut < start:
            if prev_offset is None:
                t = jd_ut - JD_AT_1_JAN_2000 / DAYS_PER_CENTURY
                return 64.184 + 59 * t - 51.2 * t ** 2 - 67.1 * t ** 3 - 16.4 * t ** 4
            else:
                break
        else:
            prev_offset = offset
    return prev_offset + 32.184


def jd_ut2tt(jd_ut):
    """
    calculate Julian Date (Terrestrial Time) from Julian Date (UT)
    """
    return jd_ut + (tt_utc_diff(jd_ut) / SECS_PER_DAY)


def jd_ut2_j2000(jd_ut):
    """
    calculate days since J2000 (TT) epoch
    """
    return jd_ut2tt(jd_ut) - JD_AT_1_JAN_2000


def j2000_now():
    """
    days since J2000 (TT) epoch
    """
    return jd_ut2_j2000(unix2jd_ut())
