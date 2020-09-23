import local_reverse_geocoder_india.shapegeocode as shapegeocode
import shapefile

print("****IMPORTANT*****\nIf you are using jvector maps then Andhrapradesh and Telengana are same\nIN-TG --> change it to IN-AP\n****END OF NOTICE****")
state_code_mapper = {
    'Andaman & Nicobar': 'IN-AN',
    'Arunachal Pradesh': 'IN-AR',
    'Assam': 'IN-AS',
    'Bihar': 'IN-BR',
    'Chandigarh': 'IN-CH',
    'Chhattisgarh': 'IN-CT',
    'Dadra and Nagar Haveli and Daman and Diu': 'IN-DD',
    'Daman & Diu': 'IN-DD',
    'Goa': 'IN-GA',
    'Gujarat': 'IN-GJ',
    'Haryana': 'IN-HR',
    'Himachal Pradesh': 'IN-HP',
    'Jammu & Kashmir': 'IN-JK',
    'Jharkhand': 'IN-JH',
    'Karnataka': 'IN-KA',
    'Kerala': '	IN-KL',
    'Lakshadweep': 'IN-LD',
    'Ladakh': 'IN-JK',
    'Madhya Pradesh': 'IN-MP',
    'Maharashtra': 'IN-MH',
    'Manipur': 'IN-MN',
    'Meghalaya': 'IN-ML',
    'Mizoram': 'IN-MZ',
    'Nagaland': 'IN-NL',
    'Delhi': 'IN-DL',
    'Puducherry': 'IN-PY',
    'Punjab': 'IN-PB',
    'Rajasthan': 'IN-RJ',
    'Sikkim': 'IN-SK',
    'Tamil Nadu': 'IN-TN',
    'Telangana': 'IN-TG',
    'Tripura': 'IN-TR',
    'Uttar Pradesh': 'IN-UP',
    'Uttarakhand': 'IN-UT',
    'West Bengal': 'IN-WB',
    'Odisha': 'IN-OR',
    'Andhra Pradesh': 'IN-AP'
}

#shape_file = shapefile.Reader("./States/Admin2.shp")
#print(shape_file.records())
def geocode(latitude, longitude, code_name_only = True):
    gc_base = shapegeocode.geocoder("local_reverse_geocoder_india/States/Admin2.shp")
    if(not code_name_only):
        result =  gc_base.geocode(latitude, longitude)
        if(result):
            return result
        else:
            return {"ST_NM": "UNKNOWN"}
    else:
        result =  gc_base.geocode(latitude, longitude)
        if(result):
            return state_code_mapper[result["ST_NM"]]
        else:
            return {"ST_NM": "UNKNOWN"}

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("local_reverse_geocoder_india/indian_states_lat_lon.csv")

    # print(geocode(22.5726, 88.3639))
    for index, row in df.iterrows():
        r = geocode(row["Latitude"], row["Longitude"]).split("-")[-1]
        if(r == row["Abbreviation"]):
            pass
        else:
            print(f"Issue found {r}")
            print(row)
            print("***************")
