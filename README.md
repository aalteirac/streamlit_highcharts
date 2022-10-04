# streamlit-highcharts

Simple wrapper for Highcharts JS libs

## Installation instructions 

```sh
pip install streamlit-highcharts
```

## Tips

For chart definition, please refer to https://www.highcharts.com/demo
You'll find a lot of samples, just copy the JS definition as JSON and think about the following:
- Convert in pure JSON, all keys must be in double quote, you can use https://jsonformatter.curiousconcept.com/#
- Replace boolean values true or false by Python correct values True or False
- Double quote "null" values
- Remove any JS functions
- Make data dynamic :-)

## Sample Streamlit Application

https://aalteirac-streamlit-highcharts-test-app-main-3vgde6.streamlitapp.com/

## Usage 

```python
import streamlit as st
import streamlit_highcharts as hct

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

hct.streamlit_highcharts(chart_def,640) #640 is the chart height
#The component bundles some sample chart definitions, from SAMPLE1 to ...SAMPLE10
hct.streamlit_highcharts(hct.SAMPLE1,640) #640 is the chart height


