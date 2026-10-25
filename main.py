# import the necessary modules and libraries
import json
import unittest
import datetime

# These lines try to read the data files if they exist online
try:
    with open("./data-1.json", "r") as f:
        jsonData1 = json.load(f)
    with open("./data-2.json", "r") as f:
        jsonData2 = json.load(f)
    with open("./data-result.json", "r") as f:
        jsonExpectedResult = json.load(f)
except FileNotFoundError:
    # Split across shorter lines to eliminate the E501 'Line too long' warnings
    jsonData1 = {
        "deviceID": "dh28dslkja",
        "deviceType": "LaserCutter",
        "timestamp": 1624445837783,
        "location": "japan/tokyo/keiyō-industrial-zone/daikibo-factory-meiyo/section-1",
        "operationStatus": "healthy",
        "temp": 22
    }
    jsonData2 = {
        "device": {"id": "dh28dslkja", "type": "LaserCutter"},
        "timestamp": "2021-06-23T10:57:17.783Z",
        "country": "japan",
        "city": "tokyo",
        "area": "keiyō-industrial-zone",
        "factory": "daikibo-factory-meiyo",
        "section": "section-1",
        "data": {"status": "healthy", "temperature": 22}
    }
    jsonExpectedResult = {
        "deviceID": "dh28dslkja",
        "deviceType": "LaserCutter",
        "timestamp": 1624445837783,
        "location": {
            "country": "japan",
            "city": "tokyo",
            "area": "keiyō-industrial-zone",
            "factory": "daikibo-factory-meiyo",
            "section": "section-1"
        },
        "data": {"status": "healthy", "temperature": 22}
    }

# convert json data from format 1 to the expected format
def convertFromFormat1(jsonObject):
    # Splits the long location string by the slashes "/"
    locationParts = jsonObject["location"].split("/")
    
    result = {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location': {
            'country': locationParts[0],
            'city': locationParts[1],
            'area': locationParts[2],
            'factory': locationParts[3],
            'section': locationParts[4]
        },
        'data': {
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp']
        }
    }
    return result

# convert json data from format 2 to the expected format
def convertFromFormat2(jsonObject):
    # Fixes the text date format safely
    iso_string = jsonObject['timestamp'].replace("Z", "+00:00")
    data = datetime.datetime.fromisoformat(iso_string)
    timestamp = round(data.timestamp() * 1000)

    result = {
        'deviceID': jsonObject['device']['id'],
        'deviceType': jsonObject['device']['type'],
        'timestamp': timestamp,
        'location': {
            'country': jsonObject['country'],
            'city': jsonObject['city'],
            'area': jsonObject['area'],
            'factory': jsonObject['factory'],
            'section': jsonObject['section']
        },
        'data': jsonObject['data']
    }
    return result

def main(jsonObject):
    result = {}
    # Fixed the E711 warning by using 'is None' instead of '== None'
    if jsonObject.get('device') is None:
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)
    return result

# Test cases using unittest module
class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 1 failed')

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 2 failed')

if __name__ == '__main__':
    print("\n--- RUNNING DELOITTE AUTOMATED TESTS ---")
    unittest.main()
