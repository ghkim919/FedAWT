import json
from typing import Any, Dict

class ConfigReader:
	def __init__(self, file_path: str):
		self.file_path = file_path

	def read(self) -> Dict[str, Any]:
		with open(self.file_path, 'r', encoding='utf-8') as f:
			return json.load(f)
