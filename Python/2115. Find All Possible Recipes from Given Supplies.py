class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        graph = defaultdict(list)
        indegree = {recipe: 0 for recipe in recipes}
        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in supply_set:
                    indegree[recipe] += 1
                    graph[ing].append(recipe)
        queue = deque()
        for recipe in recipes:
            if indegree[recipe] == 0:
                queue.append(recipe)
        
        result = []
        while queue:
            curr_recipe = queue.popleft()
            result.append(curr_recipe)
            supply_set.add(curr_recipe)
            for dependent in graph[curr_recipe]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        
        return result
