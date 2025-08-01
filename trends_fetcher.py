from pytrends.request import TrendReq

def get_related_queries(keyword):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
       
        related = pytrends.related_queries()[keyword]['top']
        if related is not None:
          return related.head(10).to_dict(orient='records')
        else:
          return [{ 'query': 'No related queries found', 'value': 0}]
    except Exception as e:
        return [{'query': f'Error: {str(e)}', 'value': 0}]