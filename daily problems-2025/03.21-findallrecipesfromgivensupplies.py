# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. 
# The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, 
# and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.
from collections import deque

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        available = set(supplies)

        q = deque(range(len(recipes)))
        created = []
        last = -1

        while len(available) > last:
            last = len(available)
            size = len(q)

            while size > 0:
                size -= 1
                i = q.popleft()
                if all(ingredient in available for ingredient in ingredients[i]):
                    available.add(recipes[i])
                    created.append(recipes[i])
                else:
                    q.append(i)

        return created
