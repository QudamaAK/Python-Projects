import pyshorteners

def shortener1(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    print(short_url)

if __name__ == "__main__":
    url = input('ENTER THE URL: ')
    shortener1(url)