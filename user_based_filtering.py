import recommendations
import datetime

prefers = recommendations.loadMovieLens()

startTime = datetime.datetime.now()
similarityValue = recommendations.calculateSimilarityValue(prefers)
print(recommendations.getRecommendationsImproved(prefers, "87", similarityValue)[0:30])
print((datetime.datetime.now() - startTime).total_seconds())

startTime = datetime.datetime.now()
print(recommendations.getRecommendationsImproved(prefers, "88", similarityValue)[0:30])
print((datetime.datetime.now() - startTime).total_seconds())

