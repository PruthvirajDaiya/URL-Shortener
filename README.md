URL Shortener using Python

- pyshorteners library is used to use services like TinyURL, bit.ly to shorten URL's.
- 's' is the object that is created using Shortener class of pyshorteners library.
- 's.tinyurl' selects the TinyURL shortening service.
- '.short(url)' sends the original URL to the TinyURL service and retrieves the shortened version of it.
- The shortened URL is then stored in the variable short_url.
- if __name__ == "__main__": This line checks whether the script is being run directly & not imported as a module in another script.
- Calling the shorten_url() Function.
- Displaying the shortened URL with "print(f"Shortened URL: {short_url}")"
