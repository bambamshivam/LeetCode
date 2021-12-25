class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        s=set(supplies);ans=set()
        for i in range(100):
            for i in range(len(recipes)):
                if s&set(ingredients[i])==set(ingredients[i]):
                    s.add(recipes[i]);ans.add(recipes[i])
        return list(ans)