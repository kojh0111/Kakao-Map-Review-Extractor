import csv
from kakao_restaurant_menu import kakao_menu_list

with open("kakao_restaurant_menu.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(kakao_menu_list)
