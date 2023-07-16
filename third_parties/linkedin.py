import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str) -> dict:
    """
    Function to scrape a LinkedIn profile using ProxyCurl API.
    :param linkedin_profile_url: LinkedIn profile URL as a string
    :return: A dictionary containing cleaned profile data
    """

    # Endpoint for ProxyCurl's LinkedIn scraping API
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    # Get the ProxyCurl API key from environment variables
    api_key = os.environ.get("PROXYCURL_API_KEY")

    # Construct headers with authorization
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        # Note: proxycurl has only 10 free credits. For development, a gist is used instead.
        # If you want to use the real API, uncomment the following line and comment the one below it:
        # response = requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=headers)

        response = requests.get(
            "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        )
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"Error scraping LinkedIn profile: {err}") from err

    data = response.json()

    # Clean the data
    cleaned_data = clean_json(data)

    return cleaned_data


def clean_json(data: dict) -> dict:
    """
    Function to clean JSON data by removing empty fields and specific keys.
    :param data: A dictionary containing raw profile data
    :return: A dictionary containing cleaned profile data
    """

    # Remove any key-value pairs where the value is None or empty
    clean_data = {k: v for k, v in data.items() if v}

    # If 'groups' key exists, remove 'profile_pic_url' from each group
    if "groups" in clean_data:
        for group in clean_data["groups"]:
            if "profile_pic_url" in group:
                del group["profile_pic_url"]

    return clean_data
