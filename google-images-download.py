from google_images_download import google_images_download as gid

def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def lastDay(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    m[1] = 29 if isLeapYear(year) else 28
    return m[month - 1]

def download(month, year=2018, keywords='한글폰트', num=100):

    day = lastDay(year, month)
    time_range = f'{{\"time_min\":\"{int(month):02}/01/{year}\", \"time_max\":\"{int(month):02}/{day}/{year}\"}}'

    print('time_info:', time_range)

    out_folder = f'한글폰트_{year}_{month:02}'
    print('out_folder: ', out_folder)

    arg = {
        'keywords': keywords,
        'limit': num,
        'time_range': time_range,
        'image_directory': out_folder
    }

    res = gid.googleimagesdownload().download(arg)
    return arg['image_directory']

folders = [download(m) for m in range(1, 13)]
folders
