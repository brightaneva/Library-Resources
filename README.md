
## Authors

- [@brightaneva](https://www.github.com/brightaneva)

  
# Library Resources

This repo retrieve Free Ebooks, Statistics on covid-19, Meaning of words in a dictionary, quotes by famous people and anime characters.All in one repo


## Tech Stack

**Programming Language:** Python


  
## Features

- Free Ebooks
- Global News
- Dictionary
- Quotes 
- Covid-19 Statistics


  
## Demo

**Ebooks:** https://github.com/brighaneva/Library-Resources/blob/master/ebooks_test.py

**News:** 
https://github.com/brighaneva/Library-Resources/blob/master/news_test.py

**Dictionary:** 
https://github.com/brighaneva/Library-Resources/blob/master/dictionary_test.py


**Quote:** https://github.com/brighaneva/Library-Resources/blob/master/quote_test.py


**Covid_Statistics:** https://github.com/brighaneva/Library-Resources/blob/master/covid_19_test.py
## Optimizations

Used OOP throughout the code to make is easier for accessibility

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`pip install quote`
`pip install lxml`
`pip install request`

  
## API Reference

#### News API

```http
  GET /api.mediastack.com/v1/news?access_key=API_Key/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Covid_19 API

```http
  GET / covid-19-coronavirus-statistics.p.rapidapi.com /v1/stats/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Covid_19 API

```http
  GET / api.dictionaryapi.dev/api/v2/entries/en/item
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. No of item to fetch |

#### fuction('item')

Takes one or more items and return a json format of the result.

  
## Feedback

If you have any feedback, please reach out to me at techwithbright@gmail.com

  
## FAQ

#### How to use ... module

See the Demo section in Readme.md

### Can I contribute to the code

Absoulutly Yes.
  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## 🚀 About Me
- I'm a backend python developer
- Loves coding in python
- Available for contributions in repo

  