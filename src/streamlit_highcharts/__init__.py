from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

SAMPLE={

    "title": {
        "text": 'U.S Solar Employment Growth by Job Category, 2010-2020'
    },

    "subtitle": {
        "text": 'Source: <a href="https://irecusa.org/programs/solar-jobs-census/" target="_blank">IREC</a>'
    },

    "yAxis": {
        "title": {
            "text": 'Number of Employees'
        }
    },

    "xAxis": {
        "accessibility": {
            "rangeDescription": 'Range: 2010 to 2020'
        }
    },

    "legend": {
        "layout": 'vertical',
        "align": 'right',
        "verticalAlign": 'middle'
    },

    "plotOptions": {
        "series": {
            "label": {
                "connectorAllowed": False
            },
            "pointStart": 2010
        }
    },

    "series": [{
        "name": 'Installation & Developers',
        "data": [43934, 48656, 65165, 81827, 112143, 142383,
            171533, 165174, 155157, 161454, 154610]
    }, {
        "name": 'Manufacturing',
        "data": [24916, 37941, 29742, 29851, 32490, 30282,
            38121, 36885, 33726, 34243, 31050]
    }, {
        "name": 'Sales & Distribution',
        "data": [11744, 30000, 16005, 19771, 20185, 24377,
            32147, 30912, 29243, 29213, 25663]
    }, {
        "name": 'Operations & Maintenance',
        "data": ["null", "null", "null", "null", "null", "null", "null",
            "null", 11164, 11218, 10077]
    }, {
        "name": 'Other',
        "data": [21908, 5548, 8105, 11248, 8989, 11816, 18274,
            17300, 13053, 11906, 10073]
    }],

    "responsive": {
        "rules": [{
            "condition": {
                "maxWidth": 500
            },
            "chartOptions": {
                "legend": {
                    "layout": 'horizontal',
                    "align": 'center',
                    "verticalAlign": 'bottom'
                }
            }
        }]
    }

}
SAMPLE2={

    "chart": {
        "type": 'streamgraph',
        "marginBottom": 30,
        "zoomType": 'x'
    },

    "title": {
        "floating": True,
        "align": 'left',
        "text": 'Winter Olympic Medal Wins'
    },
    "subtitle": {
        "floating": True,
        "align": 'left',
        "y": 30,
        "text": 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
    },

    "xAxis": {
        "maxPadding": 0,
        "type": 'category',
        "crosshair": True,
        "categories": [
            '',
            '1924 Chamonix',
            '1928 St. Moritz',
            '1932 Lake Placid',
            '1936 Garmisch-Partenkirchen',
            '1940 <i>Cancelled (Sapporo)</i>',
            '1944 <i>Cancelled (Cortina d\'Ampezzo)</i>',
            '1948 St. Moritz',
            '1952 Oslo',
            '1956 Cortina d\'Ampezzo',
            '1960 Squaw Valley',
            '1964 Innsbruck',
            '1968 Grenoble',
            '1972 Sapporo',
            '1976 Innsbruck',
            '1980 Lake Placid',
            '1984 Sarajevo',
            '1988 Calgary',
            '1992 Albertville',
            '1994 Lillehammer',
            '1998 Nagano',
            '2002 Salt Lake City',
            '2006 Turin',
            '2010 Vancouver',
            '2014 Sochi'
        ],
        "labels": {
            "align": 'left',
            "reserveSpace": False,
            "rotation": 270
        },
        "lineWidth": 0,
        "margin": 20,
        "tickWidth": 0
    },

    "yAxis": {
        "visible": False,
        "startOnTick": False,
        "endOnTick": False
    },

    "legend": {
        "enabled": False
    },

    "annotations": [{
        "labels": [{
            "point": {
                "x": 5.5,
                "xAxis": 0,
                "y": 30,
                "yAxis": 0
            },
            "text": 'Cancelled<br>during<br>World War II'
        }, {
            "point": {
                "x": 18,
                "xAxis": 0,
                "y": 90,
                "yAxis": 0
            },
            "text": 'Soviet Union fell,<br>Germany united'
        }],
        "labelOptions": {
            "backgroundColor": 'rgba(255,255,255,0.5)',
            "borderColor": 'silver'
        }
    }],

    "plotOptions": {
        "series": {
            "label": {
                "minFontSize": 5,
                "maxFontSize": 15,
                "style": {
                    "color": 'rgba(255,255,255,0.75)'
                }
            },
            "accessibility": {
                "exposeAsGroupOnly": True
            }
        }
    },
    "series": [{
        "name": "Finland",
        "data": [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7,
            7, 6, 12, 7, 9, 5, 5
        ]
    }, {
        "name": "Austria",
        "data": [
            0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10,
            21, 9, 17, 17, 23, 16, 17
        ]
    }, {
        "name": "Sweden",
        "data": [
            0, 2, 5, 3, 7, 0, 0, 10, 4, 10, 7, 7, 8, 4, 2, 4, 8, 6, 4,
            3, 3, 7, 14, 11, 15
        ]
    }, {
        "name": "Norway",
        "data": [
            0, 17, 15, 10, 15, 0, 0, 10, 16, 4, 6, 15, 14, 12, 7, 10,
            9, 5, 20, 26, 25, 25, 19, 23, 26
        ]
    }, {
        "name": "U.S.",
        "data": [
            0, 4, 6, 12, 4, 0, 0, 9, 11, 7, 10, 7, 7, 8, 10, 12, 8, 6,
            11, 13, 13, 34, 25, 37, 28
        ]
    }, {
        "name": "East Germany",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 14, 19, 23, 24, 25,
            0, 0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "West Germany",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 5, 10, 5, 4, 8, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Germany",
        "data": [
            0, 0, 1, 2, 6, 0, 0, 0, 7, 2, 8, 9, 0, 0, 0, 0, 0, 0, 26,
            24, 29, 36, 29, 30, 19
        ]
    }, {
        "name": "Netherlands",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 9, 9, 6, 4, 0, 7, 4,
            4, 11, 8, 9, 8, 24
        ]
    }, {
        "name": "Italy",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 4, 4, 5, 4, 2, 2, 5, 14,
            20, 10, 13, 11, 5, 8
        ]
    }, {
        "name": "Canada",
        "data": [
            0, 1, 1, 7, 1, 0, 0, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 5, 7,
            13, 15, 17, 24, 26, 25
        ]
    }, {
        "name": "Switzerland",
        "data": [
            0, 3, 1, 1, 3, 0, 0, 10, 2, 6, 2, 0, 6, 10, 5, 5, 5, 15,
            3, 9, 7, 11, 14, 9, 11
        ]
    }, {
        "name": "Great Britain",
        "data": [
            0, 4, 1, 0, 3, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0,
            2, 1, 2, 1, 1, 4
        ]
    }, {
        "name": "France",
        "data": [
            0, 3, 1, 1, 1, 0, 0, 5, 1, 0, 3, 7, 9, 3, 1, 1, 3, 2, 9,
            5, 8, 11, 9, 11, 15
        ]
    }, {
        "name": "Hungary",
        "data": [
            0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Unified Team",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Soviet Union",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 21, 25, 13, 16, 27, 22, 25,
            29, 0, 0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Russia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 18, 13, 22, 15, 33
        ]
    }, {
        "name": "Japan",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 1, 1, 1, 7,
            5, 10, 2, 1, 5, 8
        ]
    }, {
        "name": "Czechoslovakia",
        "data": [
            0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 4, 3, 1, 1, 6, 3, 3,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Poland",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 2, 6, 6
        ]
    }, {
        "name": "Spain",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "China",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
            3, 8, 8, 11, 11, 9
        ]
    }, {
        "name": "South Korea",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,
            6, 6, 4, 11, 14, 8
        ]
    }, {
        "name": "Czech Republic",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 3, 4, 6, 8
        ]
    }, {
        "name": "Belarus",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 2, 1, 1, 3, 6
        ]
    }, {
        "name": "Kazakhstan",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 2, 0, 0, 1, 1
        ]
    }, {
        "name": "Bulgaria",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
            0, 1, 3, 1, 0, 0
        ]
    }, {
        "name": "Denmark",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0
        ]
    }, {
        "name": "Ukraine",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 0, 2, 0, 2
        ]
    }, {
        "name": "Australia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 2, 2, 3, 3
        ]
    }, {
        "name": "Belgium",
        "data": [
            0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0
        ]
    }, {
        "name": "Romania",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Liechtenstein",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 2, 1, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Yugoslavia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Luxembourg",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "New Zealand",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "North Korea",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 0, 0, 0, 0
        ]
    }, {
        "name": "Slovakia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 3, 1
        ]
    }, {
        "name": "Croatia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 4, 3, 3, 1
        ]
    }, {
        "name": "Slovenia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            3, 0, 1, 0, 3, 8
        ]
    }, {
        "name": "Latvia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 2, 4
        ]
    }, {
        "name": "Estonia",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 3, 3, 1, 0
        ]
    }, {
        "name": "Uzbekistan",
        "data": [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0
        ]
    }],

    "exporting": {
        "sourceWidth": 800,
        "sourceHeight": 600
    }

}
SAMPLE3={

    "chart": {
        "type": 'bubble',
        "plotBorderWidth": 1,
        "zoomType": 'xy'
    },

    "title": {
        "text": 'Highcharts bubbles with radial gradient fill'
    },

    "xAxis": {
        "gridLineWidth": 1,
        "accessibility": {
            "rangeDescription": 'Range: 0 to 100.'
        }
    },

    "yAxis": {
        "startOnTick": False,
        "endOnTick": False,
        "accessibility": {
            "rangeDescription": 'Range: 0 to 100.'
        }
    },

    "series": [{
        "data": [
            [9, 81, 63],
            [98, 5, 89],
            [51, 50, 73],
            [41, 22, 14],
            [58, 24, 20],
            [78, 37, 34],
            [55, 56, 53],
            [18, 45, 70],
            [42, 44, 28],
            [3, 52, 59],
            [31, 18, 97],
            [79, 91, 63],
            [93, 23, 23],
            [44, 83, 22]
        ],
        "marker": {
            "fillColor": {
                "radialGradient": { "cx": 0.4, "cy": 0.3, "r": 0.7 },
                "stops": [
                    [0, 'rgba(255,255,255,0.5)'],
                    [1, 'rgba(124,181,236,0.5)']
                ]
            }
        }
    }, {
        "data": [
            [42, 38, 20],
            [6, 18, 1],
            [1, 93, 55],
            [57, 2, 90],
            [80, 76, 22],
            [11, 74, 96],
            [88, 56, 10],
            [30, 47, 49],
            [57, 62, 98],
            [4, 16, 16],
            [46, 10, 11],
            [22, 87, 89],
            [57, 91, 82],
            [45, 15, 98]
        ],
        "marker": {
            "fillColor": {
                "radialGradient": { "cx": 0.4, "cy": 0.3, "r": 0.7 },
                "stops": [
                    [0, 'rgba(255,255,255,0.5)'],
                    [1, 'rgba(67,67,72,0.5)']
                ]
            }
        }
    }]

}
SAMPLE4={

   "chart":{
      "type":"packedbubble",
      "height":"100%"
   },
   "title":{
      "text":"Carbon emissions around the world (2014)"
   },
   "tooltip":{
      "useHTML":True,
      "pointFormat":"<b>{point.name}:</b> {point.value}m CO<sub>2</sub>"
   },
   "plotOptions":{
      "packedbubble":{
         "minSize":"20%",
         "maxSize":"100%",
         "zMin":0,
         "zMax":1000,
         "layoutAlgorithm":{
            "gravitationalConstant":0.05,
            "splitSeries":True,
            "seriesInteraction":False,
            "dragBetweenSeries":True,
            "parentNodeLimit":True
         },
         "dataLabels":{
            "enabled":True,
            "format":"{point.name}",
            "filter":{
               "property":"y",
               "operator":">",
               "value":250
            },
            "style":{
               "color":"black",
               "textOutline":"none",
               "fontWeight":"normal"
            }
         }
      }
   },
   "series":[
      {
         "name":"Europe",
         "data":[
            {
               "name":"Germany",
               "value":767.1
            },
            {
               "name":"Croatia",
               "value":20.7
            },
            {
               "name":"Belgium",
               "value":97.2
            },
            {
               "name":"Czech Republic",
               "value":111.7
            },
            {
               "name":"Netherlands",
               "value":158.1
            },
            {
               "name":"Spain",
               "value":241.6
            },
            {
               "name":"Ukraine",
               "value":249.1
            },
            {
               "name":"Poland",
               "value":298.1
            },
            {
               "name":"France",
               "value":323.7
            },
            {
               "name":"Romania",
               "value":78.3
            },
            {
               "name":"United Kingdom",
               "value":415.4
            },
            {
               "name":"Turkey",
               "value":353.2
            },
            {
               "name":"Italy",
               "value":337.6
            },
            {
               "name":"Greece",
               "value":71.1
            },
            {
               "name":"Austria",
               "value":69.8
            },
            {
               "name":"Belarus",
               "value":67.7
            },
            {
               "name":"Serbia",
               "value":59.3
            },
            {
               "name":"Finland",
               "value":54.8
            },
            {
               "name":"Bulgaria",
               "value":51.2
            },
            {
               "name":"Portugal",
               "value":48.3
            },
            {
               "name":"Norway",
               "value":44.4
            },
            {
               "name":"Sweden",
               "value":44.3
            },
            {
               "name":"Hungary",
               "value":43.7
            },
            {
               "name":"Switzerland",
               "value":40.2
            },
            {
               "name":"Denmark",
               "value":40
            },
            {
               "name":"Slovakia",
               "value":34.7
            },
            {
               "name":"Ireland",
               "value":34.6
            },
            {
               "name":"Croatia",
               "value":20.7
            },
            {
               "name":"Estonia",
               "value":19.4
            },
            {
               "name":"Slovenia",
               "value":16.7
            },
            {
               "name":"Lithuania",
               "value":12.3
            },
            {
               "name":"Luxembourg",
               "value":10.4
            },
            {
               "name":"Macedonia",
               "value":9.5
            },
            {
               "name":"Moldova",
               "value":7.8
            },
            {
               "name":"Latvia",
               "value":7.5
            },
            {
               "name":"Cyprus",
               "value":7.2
            }
         ]
      },
      {
         "name":"Africa",
         "data":[
            {
               "name":"Senegal",
               "value":8.2
            },
            {
               "name":"Cameroon",
               "value":9.2
            },
            {
               "name":"Zimbabwe",
               "value":13.1
            },
            {
               "name":"Ghana",
               "value":14.1
            },
            {
               "name":"Kenya",
               "value":14.1
            },
            {
               "name":"Sudan",
               "value":17.3
            },
            {
               "name":"Tunisia",
               "value":24.3
            },
            {
               "name":"Angola",
               "value":25
            },
            {
               "name":"Libya",
               "value":50.6
            },
            {
               "name":"Ivory Coast",
               "value":7.3
            },
            {
               "name":"Morocco",
               "value":60.7
            },
            {
               "name":"Ethiopia",
               "value":8.9
            },
            {
               "name":"United Republic of Tanzania",
               "value":9.1
            },
            {
               "name":"Nigeria",
               "value":93.9
            },
            {
               "name":"South Africa",
               "value":392.7
            },
            {
               "name":"Egypt",
               "value":225.1
            },
            {
               "name":"Algeria",
               "value":141.5
            }
         ]
      },
      {
         "name":"Oceania",
         "data":[
            {
               "name":"Australia",
               "value":409.4
            },
            {
               "name":"New Zealand",
               "value":34.1
            },
            {
               "name":"Papua New Guinea",
               "value":7.1
            }
         ]
      },
      {
         "name":"North America",
         "data":[
            {
               "name":"Costa Rica",
               "value":7.6
            },
            {
               "name":"Honduras",
               "value":8.4
            },
            {
               "name":"Jamaica",
               "value":8.3
            },
            {
               "name":"Panama",
               "value":10.2
            },
            {
               "name":"Guatemala",
               "value":12
            },
            {
               "name":"Dominican Republic",
               "value":23.4
            },
            {
               "name":"Cuba",
               "value":30.2
            },
            {
               "name":"USA",
               "value":5334.5
            },
            {
               "name":"Canada",
               "value":566
            },
            {
               "name":"Mexico",
               "value":456.3
            }
         ]
      },
      {
         "name":"South America",
         "data":[
            {
               "name":"El Salvador",
               "value":7.2
            },
            {
               "name":"Uruguay",
               "value":8.1
            },
            {
               "name":"Bolivia",
               "value":17.8
            },
            {
               "name":"Trinidad and Tobago",
               "value":34
            },
            {
               "name":"Ecuador",
               "value":43
            },
            {
               "name":"Chile",
               "value":78.6
            },
            {
               "name":"Peru",
               "value":52
            },
            {
               "name":"Colombia",
               "value":74.1
            },
            {
               "name":"Brazil",
               "value":501.1
            },
            {
               "name":"Argentina",
               "value":199
            },
            {
               "name":"Venezuela",
               "value":195.2
            }
         ]
      },
      {
         "name":"Asia",
         "data":[
            {
               "name":"Nepal",
               "value":6.5
            },
            {
               "name":"Georgia",
               "value":6.5
            },
            {
               "name":"Brunei Darussalam",
               "value":7.4
            },
            {
               "name":"Kyrgyzstan",
               "value":7.4
            },
            {
               "name":"Afghanistan",
               "value":7.9
            },
            {
               "name":"Myanmar",
               "value":9.1
            },
            {
               "name":"Mongolia",
               "value":14.7
            },
            {
               "name":"Sri Lanka",
               "value":16.6
            },
            {
               "name":"Bahrain",
               "value":20.5
            },
            {
               "name":"Yemen",
               "value":22.6
            },
            {
               "name":"Jordan",
               "value":22.3
            },
            {
               "name":"Lebanon",
               "value":21.1
            },
            {
               "name":"Azerbaijan",
               "value":31.7
            },
            {
               "name":"Singapore",
               "value":47.8
            },
            {
               "name":"Hong Kong",
               "value":49.9
            },
            {
               "name":"Syria",
               "value":52.7
            },
            {
               "name":"DPR Korea",
               "value":59.9
            },
            {
               "name":"Israel",
               "value":64.8
            },
            {
               "name":"Turkmenistan",
               "value":70.6
            },
            {
               "name":"Oman",
               "value":74.3
            },
            {
               "name":"Qatar",
               "value":88.8
            },
            {
               "name":"Philippines",
               "value":96.9
            },
            {
               "name":"Kuwait",
               "value":98.6
            },
            {
               "name":"Uzbekistan",
               "value":122.6
            },
            {
               "name":"Iraq",
               "value":139.9
            },
            {
               "name":"Pakistan",
               "value":158.1
            },
            {
               "name":"Vietnam",
               "value":190.2
            },
            {
               "name":"United Arab Emirates",
               "value":201.1
            },
            {
               "name":"Malaysia",
               "value":227.5
            },
            {
               "name":"Kazakhstan",
               "value":236.2
            },
            {
               "name":"Thailand",
               "value":272
            },
            {
               "name":"Taiwan",
               "value":276.7
            },
            {
               "name":"Indonesia",
               "value":453
            },
            {
               "name":"Saudi Arabia",
               "value":494.8
            },
            {
               "name":"Japan",
               "value":1278.9
            },
            {
               "name":"China",
               "value":10540.8
            },
            {
               "name":"India",
               "value":2341.9
            },
            {
               "name":"Russia",
               "value":1766.4
            },
            {
               "name":"Iran",
               "value":618.2
            },
            {
               "name":"Korea",
               "value":610.1
            }
         ]
      }
   ]
}
SAMPLE5={
   "chart":{
      "type":"column"
   },
   "title":{
      "align":"left",
      "text":"Browser market shares. January, 2022"
   },
   "subtitle":{
      "align":"left",
      "text":"Click the columns to view versions. Source: <a href=\"http://statcounter.com\" target=\"_blank\">statcounter.com</a>"
   },
   "accessibility":{
      "announceNewData":{
         "enabled":True
      }
   },
   "xAxis":{
      "type":"category"
   },
   "yAxis":{
      "title":{
         "text":"Total percent market share"
      }
   },
   "legend":{
      "enabled":False
   },
   "plotOptions":{
      "series":{
         "borderWidth":0,
         "dataLabels":{
            "enabled":True,
            "format":"{point.y:.1f}%"
         }
      }
   },
   "tooltip":{
      "headerFormat":"<span style=\"font-size:11px\">{series.name}</span><br>",
      "pointFormat":"<span style=\"color:{point.color}\">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>"
   },
   "series":[
      {
         "name":"Browsers",
         "colorByPoint":True,
         "data":[
            {
               "name":"Chrome",
               "y":63.06,
               "drilldown":"Chrome"
            },
            {
               "name":"Safari",
               "y":19.84,
               "drilldown":"Safari"
            },
            {
               "name":"Firefox",
               "y":4.18,
               "drilldown":"Firefox"
            },
            {
               "name":"Edge",
               "y":4.12,
               "drilldown":"Edge"
            },
            {
               "name":"Opera",
               "y":2.33,
               "drilldown":"Opera"
            },
            {
               "name":"Internet Explorer",
               "y":0.45,
               "drilldown":"Internet Explorer"
            },
            {
               "name":"Other",
               "y":1.582,
               "drilldown":"null"
            }
         ]
      }
   ],
   "drilldown":{
      "breadcrumbs":{
         "position":{
            "align":"right"
         }
      },
      "series":[
         {
            "name":"Chrome",
            "id":"Chrome",
            "data":[
               [
                  "v65.0",
                  0.1
               ],
               [
                  "v64.0",
                  1.3
               ],
               [
                  "v63.0",
                  53.02
               ],
               [
                  "v62.0",
                  1.4
               ],
               [
                  "v61.0",
                  0.88
               ],
               [
                  "v60.0",
                  0.56
               ],
               [
                  "v59.0",
                  0.45
               ],
               [
                  "v58.0",
                  0.49
               ],
               [
                  "v57.0",
                  0.32
               ],
               [
                  "v56.0",
                  0.29
               ],
               [
                  "v55.0",
                  0.79
               ],
               [
                  "v54.0",
                  0.18
               ],
               [
                  "v51.0",
                  0.13
               ],
               [
                  "v49.0",
                  2.16
               ],
               [
                  "v48.0",
                  0.13
               ],
               [
                  "v47.0",
                  0.11
               ],
               [
                  "v43.0",
                  0.17
               ],
               [
                  "v29.0",
                  0.26
               ]
            ]
         },
         {
            "name":"Firefox",
            "id":"Firefox",
            "data":[
               [
                  "v58.0",
                  1.02
               ],
               [
                  "v57.0",
                  7.36
               ],
               [
                  "v56.0",
                  0.35
               ],
               [
                  "v55.0",
                  0.11
               ],
               [
                  "v54.0",
                  0.1
               ],
               [
                  "v52.0",
                  0.95
               ],
               [
                  "v51.0",
                  0.15
               ],
               [
                  "v50.0",
                  0.1
               ],
               [
                  "v48.0",
                  0.31
               ],
               [
                  "v47.0",
                  0.12
               ]
            ]
         },
         {
            "name":"Internet Explorer",
            "id":"Internet Explorer",
            "data":[
               [
                  "v11.0",
                  6.2
               ],
               [
                  "v10.0",
                  0.29
               ],
               [
                  "v9.0",
                  0.27
               ],
               [
                  "v8.0",
                  0.47
               ]
            ]
         },
         {
            "name":"Safari",
            "id":"Safari",
            "data":[
               [
                  "v11.0",
                  3.39
               ],
               [
                  "v10.1",
                  0.96
               ],
               [
                  "v10.0",
                  0.36
               ],
               [
                  "v9.1",
                  0.54
               ],
               [
                  "v9.0",
                  0.13
               ],
               [
                  "v5.1",
                  0.2
               ]
            ]
         },
         {
            "name":"Edge",
            "id":"Edge",
            "data":[
               [
                  "v16",
                  2.6
               ],
               [
                  "v15",
                  0.92
               ],
               [
                  "v14",
                  0.4
               ],
               [
                  "v13",
                  0.1
               ]
            ]
         },
         {
            "name":"Opera",
            "id":"Opera",
            "data":[
               [
                  "v50.0",
                  0.96
               ],
               [
                  "v49.0",
                  0.82
               ],
               [
                  "v12.1",
                  0.14
               ]
            ]
         }
      ]
   }
}
SAMPLE6={
   "chart":{
      "type":"tilemap",
      "inverted":True,
      "height":"80%"
   },
   "accessibility":{
      "description":"A tile map represents the states of the USA by population in 2016. The hexagonal tiles are positioned to geographically echo the map of the USA. A color-coded legend states the population levels as below 1 million (beige), 1 to 5 million (orange), 5 to 20 million (pink) and above 20 million (hot pink). The chart is interactive, and the individual state data points are displayed upon hovering. Three states have a population of above 20 million: California (39.3 million), Texas (27.9 million) and Florida (20.6 million). The northern US region from Massachusetts in the Northwest to Illinois in the Midwest contains the highest concentration of states with a population of 5 to 20 million people. The southern US region from South Carolina in the Southeast to New Mexico in the Southwest contains the highest concentration of states with a population of 1 to 5 million people. 6 states have a population of less than 1 million people; these include Alaska, Delaware, Wyoming, North Dakota, South Dakota and Vermont. The state with the lowest population is Wyoming in the Northwest with 584,153 people.",
      "screenReaderSection":{
         "beforeChartFormat":"<h5>{chartTitle}</h5>""+""<div>{chartSubtitle}</div>""+""<div>{chartLongdesc}</div>""+""<div>{viewTableButton}</div>"
      },
      "point":{
         "valueDescriptionFormat":"{index}. {xDescription}, {point.value}."
      }
   },
   "title":{
      "text":"U.S. states by population in 2016"
   },
   "subtitle":{
      "text":"Source:<a href=\"https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population\">Wikipedia</a>"
   },
   "xAxis":{
      "visible":False
   },
   "yAxis":{
      "visible":False
   },
   "colorAxis":{
      "dataClasses":[
         {
            "from":0,
            "to":1000000,
            "color":"#F9EDB3",
            "name":"< 1M"
         },
         {
            "from":1000000,
            "to":5000000,
            "color":"#FFC428",
            "name":"1M - 5M"
         },
         {
            "from":5000000,
            "to":20000000,
            "color":"#FF7987",
            "name":"5M - 20M"
         },
         {
            "from":20000000,
            "color":"#FF2371",
            "name":"> 20M"
         }
      ]
   },
   "tooltip":{
      "headerFormat":"",
      "pointFormat":"The population of <b> {point.name}</b> is <b>{point.value}</b>"
   },
   "plotOptions":{
      "series":{
         "dataLabels":{
            "enabled":True,
            "format":"{point.hc-a2}",
            "color":"#000000",
            "style":{
               "textOutline":False
            }
         }
      }
   },
   "series":[
      {
         "name":"",
         "data":[
            {
               "hc-a2":"AL",
               "name":"Alabama",
               "region":"South",
               "x":6,
               "y":7,
               "value":4849377
            },
            {
               "hc-a2":"AK",
               "name":"Alaska",
               "region":"West",
               "x":0,
               "y":0,
               "value":737732
            },
            {
               "hc-a2":"AZ",
               "name":"Arizona",
               "region":"West",
               "x":5,
               "y":3,
               "value":6745408
            },
            {
               "hc-a2":"AR",
               "name":"Arkansas",
               "region":"South",
               "x":5,
               "y":6,
               "value":2994079
            },
            {
               "hc-a2":"CA",
               "name":"California",
               "region":"West",
               "x":5,
               "y":2,
               "value":39250017
            },
            {
               "hc-a2":"CO",
               "name":"Colorado",
               "region":"West",
               "x":4,
               "y":3,
               "value":5540545
            },
            {
               "hc-a2":"CT",
               "name":"Connecticut",
               "region":"Northeast",
               "x":3,
               "y":11,
               "value":3596677
            },
            {
               "hc-a2":"DE",
               "name":"Delaware",
               "region":"South",
               "x":4,
               "y":9,
               "value":935614
            },
            {
               "hc-a2":"DC",
               "name":"District of Columbia",
               "region":"South",
               "x":4,
               "y":10,
               "value":7288000
            },
            {
               "hc-a2":"FL",
               "name":"Florida",
               "region":"South",
               "x":8,
               "y":8,
               "value":20612439
            },
            {
               "hc-a2":"GA",
               "name":"Georgia",
               "region":"South",
               "x":7,
               "y":8,
               "value":10310371
            },
            {
               "hc-a2":"HI",
               "name":"Hawaii",
               "region":"West",
               "x":8,
               "y":0,
               "value":1419561
            },
            {
               "hc-a2":"ID",
               "name":"Idaho",
               "region":"West",
               "x":3,
               "y":2,
               "value":1634464
            },
            {
               "hc-a2":"IL",
               "name":"Illinois",
               "region":"Midwest",
               "x":3,
               "y":6,
               "value":12801539
            },
            {
               "hc-a2":"IN",
               "name":"Indiana",
               "region":"Midwest",
               "x":3,
               "y":7,
               "value":6596855
            },
            {
               "hc-a2":"IA",
               "name":"Iowa",
               "region":"Midwest",
               "x":3,
               "y":5,
               "value":3107126
            },
            {
               "hc-a2":"KS",
               "name":"Kansas",
               "region":"Midwest",
               "x":5,
               "y":5,
               "value":2904021
            },
            {
               "hc-a2":"KY",
               "name":"Kentucky",
               "region":"South",
               "x":4,
               "y":6,
               "value":4413457
            },
            {
               "hc-a2":"LA",
               "name":"Louisiana",
               "region":"South",
               "x":6,
               "y":5,
               "value":4649676
            },
            {
               "hc-a2":"ME",
               "name":"Maine",
               "region":"Northeast",
               "x":0,
               "y":11,
               "value":1330089
            },
            {
               "hc-a2":"MD",
               "name":"Maryland",
               "region":"South",
               "x":4,
               "y":8,
               "value":6016447
            },
            {
               "hc-a2":"MA",
               "name":"Massachusetts",
               "region":"Northeast",
               "x":2,
               "y":10,
               "value":6811779
            },
            {
               "hc-a2":"MI",
               "name":"Michigan",
               "region":"Midwest",
               "x":2,
               "y":7,
               "value":9928301
            },
            {
               "hc-a2":"MN",
               "name":"Minnesota",
               "region":"Midwest",
               "x":2,
               "y":4,
               "value":5519952
            },
            {
               "hc-a2":"MS",
               "name":"Mississippi",
               "region":"South",
               "x":6,
               "y":6,
               "value":2984926
            },
            {
               "hc-a2":"MO",
               "name":"Missouri",
               "region":"Midwest",
               "x":4,
               "y":5,
               "value":6093000
            },
            {
               "hc-a2":"MT",
               "name":"Montana",
               "region":"West",
               "x":2,
               "y":2,
               "value":1023579
            },
            {
               "hc-a2":"NE",
               "name":"Nebraska",
               "region":"Midwest",
               "x":4,
               "y":4,
               "value":1881503
            },
            {
               "hc-a2":"NV",
               "name":"Nevada",
               "region":"West",
               "x":4,
               "y":2,
               "value":2839099
            },
            {
               "hc-a2":"NH",
               "name":"New Hampshire",
               "region":"Northeast",
               "x":1,
               "y":11,
               "value":1326813
            },
            {
               "hc-a2":"NJ",
               "name":"New Jersey",
               "region":"Northeast",
               "x":3,
               "y":10,
               "value":8944469
            },
            {
               "hc-a2":"NM",
               "name":"New Mexico",
               "region":"West",
               "x":6,
               "y":3,
               "value":2085572
            },
            {
               "hc-a2":"NY",
               "name":"New York",
               "region":"Northeast",
               "x":2,
               "y":9,
               "value":19745289
            },
            {
               "hc-a2":"NC",
               "name":"North Carolina",
               "region":"South",
               "x":5,
               "y":9,
               "value":10146788
            },
            {
               "hc-a2":"ND",
               "name":"North Dakota",
               "region":"Midwest",
               "x":2,
               "y":3,
               "value":739482
            },
            {
               "hc-a2":"OH",
               "name":"Ohio",
               "region":"Midwest",
               "x":3,
               "y":8,
               "value":11614373
            },
            {
               "hc-a2":"OK",
               "name":"Oklahoma",
               "region":"South",
               "x":6,
               "y":4,
               "value":3878051
            },
            {
               "hc-a2":"OR",
               "name":"Oregon",
               "region":"West",
               "x":4,
               "y":1,
               "value":3970239
            },
            {
               "hc-a2":"PA",
               "name":"Pennsylvania",
               "region":"Northeast",
               "x":3,
               "y":9,
               "value":12784227
            },
            {
               "hc-a2":"RI",
               "name":"Rhode Island",
               "region":"Northeast",
               "x":2,
               "y":11,
               "value":1055173
            },
            {
               "hc-a2":"SC",
               "name":"South Carolina",
               "region":"South",
               "x":6,
               "y":8,
               "value":4832482
            },
            {
               "hc-a2":"SD",
               "name":"South Dakota",
               "region":"Midwest",
               "x":3,
               "y":4,
               "value":853175
            },
            {
               "hc-a2":"TN",
               "name":"Tennessee",
               "region":"South",
               "x":5,
               "y":7,
               "value":6651194
            },
            {
               "hc-a2":"TX",
               "name":"Texas",
               "region":"South",
               "x":7,
               "y":4,
               "value":27862596
            },
            {
               "hc-a2":"UT",
               "name":"Utah",
               "region":"West",
               "x":5,
               "y":4,
               "value":2942902
            },
            {
               "hc-a2":"VT",
               "name":"Vermont",
               "region":"Northeast",
               "x":1,
               "y":10,
               "value":626011
            },
            {
               "hc-a2":"VA",
               "name":"Virginia",
               "region":"South",
               "x":5,
               "y":8,
               "value":8411808
            },
            {
               "hc-a2":"WA",
               "name":"Washington",
               "region":"West",
               "x":2,
               "y":1,
               "value":7288000
            },
            {
               "hc-a2":"WV",
               "name":"West Virginia",
               "region":"South",
               "x":4,
               "y":7,
               "value":1850326
            },
            {
               "hc-a2":"WI",
               "name":"Wisconsin",
               "region":"Midwest",
               "x":2,
               "y":5,
               "value":5778708
            },
            {
               "hc-a2":"WY",
               "name":"Wyoming",
               "region":"West",
               "x":3,
               "y":3,
               "value":584153
            }
         ]
      }
   ]
}
SAMPLE7={
   "chart":{
      "type":"pie"
   },
   "title":{
      "text":"Browser market shares. January, 2022"
   },
   "subtitle":{
      "text":"Click the slices to view versions. Source: <a href=\"http://statcounter.com\" target=\"_blank\">statcounter.com</a>"
   },
   "accessibility":{
      "announceNewData":{
         "enabled":True
      },
      "point":{
         "valueSuffix":"%"
      }
   },
   "plotOptions":{
      "series":{
         "dataLabels":{
            "enabled":True,
            "format":"{point.name}: {point.y:.1f}%"
         }
      }
   },
   "tooltip":{
      "headerFormat":"<span style=\"font-size:11px\">{series.name}</span><br>",
      "pointFormat":"<span style=\"color:{point.color}\">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>"
   },
   "series":[
      {
         "name":"Browsers",
         "colorByPoint":True,
         "data":[
            {
               "name":"Chrome",
               "y":61.04,
               "drilldown":"Chrome"
            },
            {
               "name":"Safari",
               "y":9.47,
               "drilldown":"Safari"
            },
            {
               "name":"Edge",
               "y":9.32,
               "drilldown":"Edge"
            },
            {
               "name":"Firefox",
               "y":8.15,
               "drilldown":"Firefox"
            },
            {
               "name":"Other",
               "y":11.02,
               "drilldown":"null"
            }
         ]
      }
   ],
   "drilldown":{
      "series":[
         {
            "name":"Chrome",
            "id":"Chrome",
            "data":[
               [
                  "v97.0",
                  36.89
               ],
               [
                  "v96.0",
                  18.16
               ],
               [
                  "v95.0",
                  0.54
               ],
               [
                  "v94.0",
                  0.7
               ],
               [
                  "v93.0",
                  0.8
               ],
               [
                  "v92.0",
                  0.41
               ],
               [
                  "v91.0",
                  0.31
               ],
               [
                  "v90.0",
                  0.13
               ],
               [
                  "v89.0",
                  0.14
               ],
               [
                  "v88.0",
                  0.1
               ],
               [
                  "v87.0",
                  0.35
               ],
               [
                  "v86.0",
                  0.17
               ],
               [
                  "v85.0",
                  0.18
               ],
               [
                  "v84.0",
                  0.17
               ],
               [
                  "v83.0",
                  0.21
               ],
               [
                  "v81.0",
                  0.1
               ],
               [
                  "v80.0",
                  0.16
               ],
               [
                  "v79.0",
                  0.43
               ],
               [
                  "v78.0",
                  0.11
               ],
               [
                  "v76.0",
                  0.16
               ],
               [
                  "v75.0",
                  0.15
               ],
               [
                  "v72.0",
                  0.14
               ],
               [
                  "v70.0",
                  0.11
               ],
               [
                  "v69.0",
                  0.13
               ],
               [
                  "v56.0",
                  0.12
               ],
               [
                  "v49.0",
                  0.17
               ]
            ]
         },
         {
            "name":"Safari",
            "id":"Safari",
            "data":[
               [
                  "v15.3",
                  0.1
               ],
               [
                  "v15.2",
                  2.01
               ],
               [
                  "v15.1",
                  2.29
               ],
               [
                  "v15.0",
                  0.49
               ],
               [
                  "v14.1",
                  2.48
               ],
               [
                  "v14.0",
                  0.64
               ],
               [
                  "v13.1",
                  1.17
               ],
               [
                  "v13.0",
                  0.13
               ],
               [
                  "v12.1",
                  0.16
               ]
            ]
         },
         {
            "name":"Edge",
            "id":"Edge",
            "data":[
               [
                  "v97",
                  6.62
               ],
               [
                  "v96",
                  2.55
               ],
               [
                  "v95",
                  0.15
               ]
            ]
         },
         {
            "name":"Firefox",
            "id":"Firefox",
            "data":[
               [
                  "v96.0",
                  4.17
               ],
               [
                  "v95.0",
                  3.33
               ],
               [
                  "v94.0",
                  0.11
               ],
               [
                  "v91.0",
                  0.23
               ],
               [
                  "v78.0",
                  0.16
               ],
               [
                  "v52.0",
                  0.15
               ]
            ]
         }
      ]
   }
}
SAMPLE8={
   "title":{
      "text":"Sales of petroleum products March, Norway",
      "align":"left"
   },
   "xAxis":{
      "categories":[
         "Jet fuel",
         "Duty-free diesel",
         "Petrol",
         "Diesel",
         "Gas oil"
      ]
   },
   "yAxis":{
      "title":{
         "text":"Million liter"
      }
   },
   "labels":{
      "items":[
         {
            "html":"Total liter",
            "style":{
               "left":"50px",
               "top":"18px",
               "color":"black"
            }
         }
      ]
   },
   "series":[
      {
         "type":"column",
         "name":"2020",
         "data":[
            59,
            83,
            65,
            228,
            184
         ]
      },
      {
         "type":"column",
         "name":"2021",
         "data":[
            24,
            79,
            72,
            240,
            167
         ]
      },
      {
         "type":"column",
         "name":"2022",
         "data":[
            58,
            88,
            75,
            250,
            176
         ]
      },
      {
         "type":"spline",
         "name":"Average",
         "data":[
            47,
            83.33,
            70.66,
            239.33,
            175.66
         ],
         "marker":{
            "lineWidth":2,
            "fillColor":"black",
         }
      },
      {
         "type":"pie",
         "name":"Liter",
         "data":[
            {
               "name":"2020",
               "y":619,
               "color": "#7cb4ec"
               
            },
            {
               "name":"2021",
               "y":586,
               "color": "#434348"
            },
            {
               "name":"2022",
               "y":647,
               "color":"#90ed7d"
            }
         ],
         "center":[
            80,
            70
         ],
         "size":100,
         "showInLegend":False,
         "dataLabels":{
            "enabled":False
         }
      }
    ]
}
SAMPLE9={
   "chart":{
      "type":"solidgauge",
      "height":"90%"
   },
   "title":{
      "text":"Activity",
      "style":{
         "fontSize":"24px"
      }
   },
   "tooltip":{
      "borderWidth":0,
      "backgroundColor":"none",
      "shadow":False,
      "style":{
         "fontSize":"16px"
      },
      "valueSuffix":"%",
      "pointFormat":"{series.name}<br><span style=\"font-size:2em; color: {point.color}; font-weight: bold\">{point.y}</span>",
      "positioner":{
         "x":"50px",
         "y":100
      }
   },
   "pane":{
      "startAngle":0,
      "endAngle":360,
      "background":[
         {
            "radius":"112%",
            "innerRadius":"88%",
            "borderWidth":0
         },
         {
            "radius":"87%",
            "innerRadius":"63%",
            "borderWidth":0
         },
         {
            "radius":"62%",
            "innerRadius":"38%",
            "borderWidth":0
         }
      ]
   },
   "yAxis":{
      "min":0,
      "max":100,
      "lineWidth":0,
      "tickPositions":[
         
      ]
   },
   "plotOptions":{
      "solidgauge":{
         "dataLabels":{
            "enabled":False
         },
         "linecap":"round",
         "stickyTracking":False,
         "rounded":True
      }
   },
   "series":[
      {
         "name":"Move",
         "data":[
            {
               "color":"lightgreen",
               "radius":"112%",
               "innerRadius":"88%",
               "y":80
            }
         ]
      },
      {
         "name":"Exercise",
         "data":[
            {
               "color":"red",
               "radius":"87%",
               "innerRadius":"63%",
               "y":65
            }
         ]
      },
      {
         "name":"Stand",
         "data":[
            {
               "color":"blue",
               "radius":"62%",
               "innerRadius":"38%",
               "y":50
            }
         ]
      }
   ]
}
SAMPLE10={

    "chart": {
        "type": 'gauge',
        "plotBackgroundColor": "white",
        "plotBackgroundImage": "white",
        "plotBorderWidth": 0,
        "plotShadow": False,
        "height": '80%'
    },

    "title": {
        "text": 'Speedometer'
    },

    "pane": {
        "startAngle": -90,
        "endAngle": 89.9,
        "background": "null",
        "center": ['50%', '75%'],
        "size": '110%'
    },

    "yAxis": {
        "min": 0,
        "max": 200,
        "tickPixelInterval": 72,
        "tickPosition": 'inside',
        "tickColor": '#FFFFFF',
        "tickLength": 20,
        "tickWidth": 2,
        "minorTickInterval": "null",
        "labels": {
            "distance": 20,
            "style": {
                "fontSize": '14px'
            }
        },
        "plotBands": [{
            "from": 0,
            "to": 120,
            "color": '#55BF3B', 
            "thickness": 20
        }, {
            "from": 120,
            "to": 160,
            "color": '#DDDF0D',
            "thickness": 20
        }, {
            "from": 160,
            "to": 200,
            "color": '#DF5353', 
            "thickness": 20
        }]
    },

    "series": [{
        "name": 'Speed',
        "data": [80],
        "tooltip": {
            "valueSuffix": ' km/h'
        },
        "dataLabels": {
            "format": '{y} km/h',
            "borderWidth": 0,
            "color": '#333333',
            "style": {
                "fontSize": '16px'
            }
        },
        "dial": {
            "radius": '80%',
            "backgroundColor": 'gray',
            "baseWidth": 12,
            "baseLength": '0%',
            "rearLength": '0%'
        },
        "pivot": {
            "backgroundColor": 'gray',
            "radius": 6
        }
    }]

}
SAMPLE11={

    "title": {
        "text": 'Highcharts Dependency Wheel'
    },

    "accessibility": {
        "point": {
            "valueDescriptionFormat": '{index}. From {point.from} to {point.to}: {point.weight}.'
        }
    },

    "series": [{
        "keys": ['from', 'to', 'weight'],
        "data": [
            ['Brazil', 'Portugal', 5],
            ['Brazil', 'France', 1],
            ['Brazil', 'Spain', 1],
            ['Brazil', 'England', 1],
            ['Canada', 'Portugal', 1],
            ['Canada', 'France', 5],
            ['Canada', 'England', 1],
            ['Mexico', 'Portugal', 1],
            ['Mexico', 'France', 1],
            ['Mexico', 'Spain', 5],
            ['Mexico', 'England', 1],
            ['USA', 'Portugal', 1],
            ['USA', 'France', 1],
            ['USA', 'Spain', 1],
            ['USA', 'England', 5],
            ['Portugal', 'Angola', 2],
            ['Portugal', 'Senegal', 1],
            ['Portugal', 'Morocco', 1],
            ['Portugal', 'South Africa', 3],
            ['France', 'Angola', 1],
            ['France', 'Senegal', 3],
            ['France', 'Mali', 3],
            ['France', 'Morocco', 3],
            ['France', 'South Africa', 1],
            ['Spain', 'Senegal', 1],
            ['Spain', 'Morocco', 3],
            ['Spain', 'South Africa', 1],
            ['England', 'Angola', 1],
            ['England', 'Senegal', 1],
            ['England', 'Morocco', 2],
            ['England', 'South Africa', 7],
            ['South Africa', 'China', 5],
            ['South Africa', 'India', 1],
            ['South Africa', 'Japan', 3],
            ['Angola', 'China', 5],
            ['Angola', 'India', 1],
            ['Angola', 'Japan', 3],
            ['Senegal', 'China', 5],
            ['Senegal', 'India', 1],
            ['Senegal', 'Japan', 3],
            ['Mali', 'China', 5],
            ['Mali', 'India', 1],
            ['Mali', 'Japan', 3],
            ['Morocco', 'China', 5],
            ['Morocco', 'India', 1],
            ['Morocco', 'Japan', 3],
            ['Japan', 'Brazil', 1]
        ],
        "type": 'dependencywheel',
        "name": 'Dependency wheel series',
        "dataLabels": {
            "color": '#333',
            "style": {
                "textOutline": 'none'
            },
            "textPath": {
                "enabled": True,
                "attributes": {
                    "dy": 5
                }
            },
            "distance": 10
        },
        "size": '95%'
    }]

}
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"streamlit_highcharts", path=str(frontend_dir)
)

def streamlit_highcharts(
    options=SAMPLE,
    height=410,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        options=options,key=key,height=height
    )

    return component_value


# def main():
#     st.write("## Example")
#     selSample=st.selectbox("Choose a sample",[SAMPLE,SAMPLE2,SAMPLE3,SAMPLE4,SAMPLE5,SAMPLE6,SAMPLE7,SAMPLE8,SAMPLE9,SAMPLE10],format_func=lambda x: str(x["title"]["text"])
# )
#     value = streamlit_highcharts(selSample,640)
#     with st.expander("Show code...",expanded=False):
#         st.code(str(selSample).replace("},","},\r\n"),language="python")



# if __name__ == "__main__":
#     main()
