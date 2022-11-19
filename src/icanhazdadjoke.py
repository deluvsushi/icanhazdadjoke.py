from requests import get

class Icanhazdadjoke:
	def __init__(self) -> None:
		self.api = "https://icanhazdadjoke.com"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def get_random_dad_joke(self) -> dict:
		return get(
			f"{self.api}/",
			headers=self.headers).json()
	
	def get_random_dad_joke_as_slack(self) -> dict:
		return get(
			f"{self.api}/slack",
			headers=self.headers).json()
	
	def get_dad_joke(self, joke_id: str) -> dict:
		return get(
			f"{self.api}/j/{joke_id}",
			headers=self.headers).json()
	
	def get_dad_joke_as_image(self, joke_id: str) -> str:
		return f"{self.api}/j/{joke_id}.png"
	
	def search_dad_jokes(
			self,
			page: int = 1,
			limit: int = 20, # max = 30
			term: str = "list all jokes") -> dict:
		return get(
			f"{self.api}/search?page={page}&limit={limit}&term={term}",
			headers=self.headers).json()
