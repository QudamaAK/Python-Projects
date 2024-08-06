import pywhatkit as kit

def play_song_on_youtube():
    command = input('ENTER SONG YOU WANNA PLAY: ')
    try:
        print(f"Searching and playing {command} on YouTube...")
        kit.playonyt(command)
        print("Playing...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    play_song_on_youtube()
