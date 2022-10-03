# streamlit-highcharts

Simple wrapper for Highcharts JS libs

## Installation instructions 

```sh
pip install streamlit-highcharts
```

## Usage instructions

For chart definition, please refer to https://www.highcharts.com/demo
You'll find a lot of samples, just coipy the JS definition as JSON and think about the following:
- Convert in pure JSON, all keys must be in double quote.
- Replace boolean value true or false by Python correct values True or False
- Double quote "null" values
- Remove any JS functions

```python
import streamlit as st

from streamlit_highcharts import streamlit_highcharts

chart_def={
   "title":{
      "text":"Sales of petroleum products March, Norway",
      "align":"left"
   },
   "xAxis":{
      "categories":["Jet fuel","Duty-free diesel"]
   },
   "yAxis":{
      "title":{"text":"Million liter"}
   },
   "series":[
        {"type":"column",
            "name":"2020",
            "data":[59,83]},
        {"type":"column",
            "name":"2021",
            "data":[24,79]
        },
        {"type":"column",
            "name":"2022",
            "data":[58,88]
        },
        {"type":"spline",
            "name":"Average",
            "data":[47,83.33],
            "marker":{
                "lineWidth":2,
                "fillColor":"black",
            }
        }
    ]
}
value = streamlit_highcharts(chart_def,640) #640 is the chart height


