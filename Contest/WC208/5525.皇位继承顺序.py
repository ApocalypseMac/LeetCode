class TreeNode:
    def __init__(self, name, children):
        self.name = name
        self.alive = True
        self.children = children
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.dict = dict()
        self.root = TreeNode(kingName, [])
        self.dict[kingName] = self.root


    def birth(self, parentName: str, childName: str) -> None:
        curr = self.dict[parentName]
        succ = TreeNode(childName, [])
        self.dict[childName] = succ
        curr.children.append(succ)


    def death(self, name: str) -> None:
        curr = self.dict[name]
        curr.alive = False
        return 


    def getInheritanceOrder(self) -> List[str]:
        res = []
        curr = self.root
        stack = [curr]
        while stack:
            curr = stack.pop()
            if curr.alive:
                res.append(curr.name)
            stack += curr.children[::-1]
        return res
            
        



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()