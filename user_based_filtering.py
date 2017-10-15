import recommendations
import datetime

prefers = recommendations.loadMovieLens()

startTime = datetime.datetime.now()
print(recommendations.getRecommendations(prefers, "87")[0:30])
print((datetime.datetime.now() - startTime).total_seconds())

startTime = datetime.datetime.now()
print(recommendations.getRecommendations(prefers, "88")[0:30])
print((datetime.datetime.now() - startTime).total_seconds())
