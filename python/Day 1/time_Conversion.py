def time_conversion(s):
    hh_str = s[:2]
    mm_str = s[3:5]
    ss_str = s[6:8]
    am_pm_str = s[8:]

    hh = int(hh_str)
    mm = int(mm_str)
    ss = int(ss_str)

    if am_pm_str == "PM" and hh != 12:
        hh += 12
    elif am_pm_str == "AM" and hh == 12:
        hh = 0

    time_string = f"{hh:02d}:{mm:02d}:{ss:02d}"
    return time_string

if __name__ == "__main__":
    s = input().strip()
    result = time_conversion(s)
    print(result)
