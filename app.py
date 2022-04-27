## this is a program that outputs a gilvasunner mashup in mp3
print("Welcome to the gilvasunner mashup maker!")
## connect to the youtube api system
import google 
import youtube_dl
## ask the user what song they want to download
song = input("What song do you want to download? ")
## download the song
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([song])
    ## ask which folder to save
    folder = input("What folder do you want to save it in? ")
    ## move the file to the folder
    import shutil
    shutil.move(song + ".mp3", folder)


print("Please enter the name of the song you would like to make:")
song_name = input()
print("Please enter the name of the artist you would like to rip:")
artist_name = input()
print("Please enter the name of the album you would like to rip:")
album_name = input()
### enter how many iterations you would like to rip
print("How many iterations would you like to rip?")
iterations = int(input())
### enter the name of the output file
print("What would you like to name the output file?")
output_file = input()
### enter the name of the output file
print("What would you like to name the output file?")
output_file = input()
## use ffmpeg to generate a mashup of the name from the youtube database

ffmpeg=song(song_name,artist_name,album_name,iterations)
print("Your mashup is ready!")
