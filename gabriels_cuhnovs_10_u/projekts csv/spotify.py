import csv
import json

file_name='projekts csv/spotify.csv'
json_file_name='projekts csv/spotify.csv'

songs_list = []

with open(file_name, 'r', encoding='UTF8') as data_file:
    for line in csv.DictReader(data_file):
        songs_list.append(line)

with open(json_file_name, 'w', encoding='UTF8') as json_file:
    json.dump(songs_list, json_file, indent=4)

#UZDEVUMS 1
#Lai programma izvada terminālī tikai dziesmas nosaukumus

for song in songs_list:
    print(f"{song['Title']} {song['Popularity']}")

#UZDEVUMS 2
#Izveido sarakstu ar unikāliem dziesmas gadiem

song_years = []
song_genres = []
for song in songs_list:
    if song['Year'] not in song_years:
        song_years.append(song['Year'])
    if song['Genre'] not in song_genres:
        song_genres.append(song['Genre'])

song_years.sort()
print(song_years)
song_genres.sort()
print(song_genres)
