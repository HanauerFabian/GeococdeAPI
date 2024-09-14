import requests
import io
import json
import time

with io.open("Städte.txt", mode="r", encoding="utf-8") as f:
    with io.open("data.json", mode="a", encoding="utf-8") as g:
        for line in f:
            print(line.strip())
            response = requests.get(f"https://geocode.maps.co/search?q={line.strip()}&api_key=")
            data = response.json()
            json.dump(data, g)
            g.write('\n')
            time.sleep(1)