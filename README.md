# streamlit-highcharts

Simple wrapper for Highcharts JS libs

## Installation instructions 

```sh
pip install streamlit-highcharts
```

## Usage instructions

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

