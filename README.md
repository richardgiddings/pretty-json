# README

A simple python script that takes a json file that is in a difficult to read form and make it easier to read.

Usage:
    python pretty_json.py <data.json>
where data.json is the file you want to format.

For example given a file data.json containing:
```
{"Locations": {"Location": [{"latitude": "54.9375", "longitude": "-2.8092", "name": "Carlisle Airport"},{"latitude": "53.3336","longitude": "-2.85","name": "Liverpool John Lennon Airport"}]}}
```

the script creates a file pretty_data.json containing:

```
{
    "Locations": {
        "Location": [
            {
                "latitude": "54.9375", 
                "longitude": "-2.8092", 
                "name": "Carlisle Airport"
            }, 
            {
                "latitude": "53.3336", 
                "longitude": "-2.85", 
                "name": "Liverpool John Lennon Airport"
            }
        ]
    }
}
```