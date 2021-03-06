import tweepy
import settings
import dataset

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
dataset.freeze(result, format='csv', filename=settings.CSV_NAME)