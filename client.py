import requests
import json

class Client():
    def __init__(self, url) -> None:
        """Initialise the Client Object with the URL of the API

        Args:
            url (string): API Endpoint
        """ 
        # Todo: Make url value configurable
        self.url = url
    
    def update_data(self, id: int, data: dict[str, str]):
        """Updates the resource at the endpoint with the corresponding ID.

        Args:
            id (int): Unique id of the payload.
            data (dict[str, str]): Dictionary with the payload values. Only values which are to be changed may be provided.

        Returns:
            json: Returns JSON response from the webserver.
        """
        # Only set values for arguments which are not None
        payload = json.dumps(data)
        r = requests.put(self.url, data=payload, params={"id": id})
        return r.json()
        
    
    def fetch_data(self, id: int) -> json:
        """Fetches the json data from the endpoint by querying the API with unique ID.

        Args:
            id (int): Unique ID to be queried. 

        Returns:
            json: JSON response with the queried data.
        """
        r = requests.get(self.url, params={"id": id})
        return r.json()
    
if __name__ == "__main__":
    
    # initialise the client with the url of the API    
    c = Client("http://127.0.0.1:8000/data")

    sample_payload = {"name": "Harry",}
    print(c.update_data(2, sample_payload))
    print(c.fetch_data(1))