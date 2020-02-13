

# Scrapy exam


## Target
url : [Constellations](http://astro.click108.com.tw/)

Get as below data:
* 當天日期
* 星座名稱
* 整體運勢的評分及說明
* 愛情運勢的評分及說明
* 事業運勢的評分及說明
* 財運運勢的評分及說明



## Solutions

### Running

```
docker-compose up -d --build
docker-compose run spider scrapy crawl click108
```

Output data format:
```javascript=
  {
    "constellation_name": "巨蟹座",
    "overall_score": 4,
    "overall_description": "今天你的心情可謂是陽光明媚，燦爛的笑容對異性很有殺傷力，但也要時刻提防爛桃花哦。財運很旺，微笑待人，獲得意外之財的機率很大。工作上不斷接到新的任務，但不乏他人的幫助。",
    "love_score": 3,
    "love_description": "今日是適合來場精神交流，多點關心噓寒問暖，讓情人感動一下吧！",
    "work_score": 4,
    "work_description": "事業運不錯，能攻能守的運作自如，只要懂得尊敬上位者，上司多能給予你正面的肯定。",
    "money_score": 4,
    "money_description": "財運一路暢通，各方面的力量合聚一起，一切在穩步增漲。也要注意適當的控制發展的速度，避免因發展過快帶來的負面影響。",
    "date": "2020-02-13"
  },
```

### SQL Scheme
![SQL Scheme](https://i.imgur.com/QOaiMBK.png)

### Import to db
![Database status](https://i.imgur.com/eONJNye.png)
