import recommendations
import datetime

prefers = recommendations.loadMovieLens()

startTime = datetime.datetime.now()
itemMatch = recommendations.calculateSimilarItems(prefers, n = 50)
print(recommendations.getRecommendedItems(prefers, itemMatch, "87")[0:30])
print((datetime.datetime.now() - startTime).total_seconds())

startTime = datetime.datetime.now()
print(recommendations.getRecommendedItems(prefers, itemMatch, "88")[0:30])
print((datetime.datetime.now() - startTime).total_seconds())