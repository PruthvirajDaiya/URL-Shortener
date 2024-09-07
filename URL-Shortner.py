import pyshorteners

def shorten_url(url):
    # Create a Shortener object
    s = pyshorteners.Shortener()
    
    # Using TinyURL to shorten the URL
    short_url = s.tinyurl.short(url)
    
    return short_url

if __name__ == "__main__":
    # Input a URL
    url = input("Enter the URL to shorten: ")
    
    # Call the function and display the shortened URL
    short_url = shorten_url(url)
    print(f"Shortened URL: {short_url}")
