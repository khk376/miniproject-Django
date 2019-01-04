import json

## read json file
with open('skorea_municipalities_geo_simple.json', 'rb') as f:
  root = json.load(f)

a=[]
for i in range(0, len(root['features'])):
    if root['features'][i]['properties']['name']=='강릉시' or root['features'][i]['properties']['name']=='고성군' or root['features'][i]['properties']['name']=='동해시' or root['features'][i]['properties']['name']=='삼척시' or root['features'][i]['properties']['name']=='강릉시' or root['features'][i]['properties']['name']=='고성군' or root['features'][i]['properties']['name']=='동해시' or root['features'][i]['properties']['name']=='속초시' or root['features'][i]['properties']['name']=='강릉시' or root['features'][i]['properties']['name']=='고성군' or root['features'][i]['properties']['name']=='동해시' or root['features'][i]['properties']['name']=='양구군' or root['features'][i]['properties']['name']=='양양군' or root['features'][i]['properties']['name']=='영월군' or root['features'][i]['properties']['name']=='원주시' or root['features'][i]['properties']['name']=='인제군' or root['features'][i]['properties']['name']=='정선군' or root['features'][i]['properties']['name']=='정선군' or root['features'][i]['properties']['name']=='철원군' or root['features'][i]['properties']['name']=='춘천시' or root['features'][i]['properties']['name']=='태백시' or root['features'][i]['properties']['name']=='평창군' or root['features'][i]['properties']['name']=='홍천군' or root['features'][i]['properties']['name']=='화천군' or root['features'][i]['properties']['name']=='횡성군':
        a.append(root['features'][i])

class aaa(models.Model):
    def geo(h):
        h=[]
        for j in range(0, len(a)):
            for i in range(0, len(a[j]['geometry']['coordinates'][0])):
                d=a[j]['geometry']['coordinates'][0][i][0]
                c=a[j]['geometry']['coordinates'][0][i][1]
                a[j]['geometry']['coordinates'][0][i][0]=c
                a[j]['geometry']['coordinates'][0][i][1]=d
                a[j]['geometry']['coordinates'][0][i]
                h.append(a[j]['geometry']['coordinates'][0][i])
        return h



