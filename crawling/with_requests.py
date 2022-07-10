import json
import requests

url = "https://navercomp.wisereport.co.kr/v2/company/cF4002.aspx?cmp_cd=042500&frq=0&rpt=5&finGubun=MAIN&frqTyp=0&cn=&encparam=K1RPTFZSSFBlOGk1VHBEeUpkdDY1dz09"

response = requests.request("GET", url)
json_data = json.loads(response.text)
column_filter = [f"DATA{i}" for i in range(1, 6)] + ["YYOY"]
columns = [_.replace("<br />", " ") for _ in json_data.get("YYMM")]

result = {
  "EPS": [ round(float(value)) for key, value in json_data["DATA"][0].items() if value and key in column_filter],
  "BPS": [ round(float(value)) for key, value in json_data["DATA"][4].items() if value and key in column_filter],
  "CPS" : [ round(float(value)) for key, value in json_data["DATA"][8].items() if value and key in column_filter],
  "SPS" : [ round(float(value)) for key, value in json_data["DATA"][12].items() if value and key in column_filter],
  "PER" : [ round(float(value), 2) for key, value in json_data["DATA"][16].items() if value and key in column_filter],
  "PBR" : [ round(float(value), 2) for key, value in json_data["DATA"][19].items() if value and key in column_filter],
  "PCR" : [ round(float(value), 2) for key, value in json_data["DATA"][22].items() if value and key in column_filter],
  "PSR" : [ round(float(value), 2) for key, value in json_data["DATA"][25].items() if value and key in column_filter],
  "EV_EBITDA" : [ round(float(value), 2) for key, value in json_data["DATA"][28].items() if value and key in column_filter],
  "DPS" : [ round(float(value), 2) for key, value in json_data["DATA"][31].items() if value and key in column_filter],
}

for key, value in result.items():
  if len(value) < len(column_filter):
    result[key] = [0] * (len(column_filter) - len(value)) + value

for k,v in result.items():
  print(k, v)
