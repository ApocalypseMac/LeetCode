class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        k = dict(knowledge); return __import__("re").sub(r'\(([a-z]+)\)', lambda x: k.get(x.group(1), '?'), s) 