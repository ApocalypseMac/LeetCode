class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.time = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.time[tokenId] = currentTime + self.t
        
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.time and self.time[tokenId] > currentTime:
            self.time[tokenId] = currentTime + self.t
        
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for k, v in self.time.items():
            if v > currentTime:
                cnt += 1
        return cnt



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)