import unittest
import requests
import json

class api_testing(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'
        
    
    def test_get(self):
        self.get_request = requests.get(f'{self.base_url}/posts')
        self.response = json.loads(self.get_request)
        assert self.get_request.status_code == 200 and "qui" in self.response['title']
    
    def test_post(self):
        pass
    
    def test_put(self):
        pass
    
    def test_delete(self):
        pass
    
    def tearDown(self) -> None:
        pass
    
if __name__ =="__main__":
    unittest.main()
    
    