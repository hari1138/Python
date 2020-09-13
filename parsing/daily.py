import instagram
import csv
import datetime
import vk

date = datetime.datetime.today()

followers = instagram.getFollowerCount('sumiagro_russia')
with open('C:\PowerBi_Report\sumiagro\sumiagro_followers.csv', mode='a') as followers_file:
    csv_writer = csv.writer(followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([date,followers])

followers = instagram.getFollowerCount('moonyrussia_official')
with open('C:\PowerBi_Report\moony_followers.csv', mode='a') as followers_file:
    csv_writer = csv.writer(followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([date,followers])

followers = vk.getFollowerCount('moonyrussiaofficial')
with open('C:\PowerBi_Report\moony_vk_followers.csv', mode='a') as followers_file:
    csv_writer = csv.writer(followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([date,followers])


