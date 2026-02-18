import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

def check_site_status(url):
    """
    Checks the HTTP status code of a given URL.
    Returns the status code and a message.
    """
    # Ensure the URL has a scheme for a proper request
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Use HEAD request as it only fetches headers, which is faster than GET
        # set a timeout to prevent the script from hanging indefinitely
        response = requests.head(url, timeout=5) 
        
        # A 2xx status code generally means "Success"
        if 200 <= response.status_code < 300:
            return response.status_code, "Website is UP and reachable"
        elif 300 <= response.status_code < 400:
            return response.status_code, "Redirection response"
        elif 400 <= response.status_code < 500:
            return response.status_code, "Client error (e.g., Not Found)"
        elif 500 <= response.status_code < 600:
            return response.status_code, "Server error"
        else:
            return response.status_code, "Unknown status"
            
    except ConnectionError:
        return None, "Failed to reach a server. Check your network connection or the URL."
    except Timeout:
        return None, "The request timed out."
    except RequestException as e:
        return None, f"An error occurred: {str(e)}"

# Example Usage:
site_url = "www.google.com"
status_code, message = check_site_status(site_url)

if status_code:
    print(f"URL: {site_url}")
    print(f"Status Code: {status_code}")
    print(f"Message: {message}")
else:
    print(f"URL: {site_url}")
    print(f"Message: {message}")
