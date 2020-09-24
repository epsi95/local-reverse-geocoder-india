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
    'Dadra and Nagar Haveli and Daman and Diu': 'IN-DN',
    'Daman & Diu': 'IN-DD',
    'Goa': 'IN-GA',
    'Gujarat': 'IN-GJ',
    'Haryana': 'IN-HR',
    'Himachal Pradesh': 'IN-HP',
    'Jammu & Kashmir': 'IN-JK',
    'Jharkhand': 'IN-JH',
    'Karnataka': 'IN-KA',
    'Kerala': 'IN-KL',
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

state_code_mapper_v1 = {
    'Andaman & Nicobar Island': 'IN-AN',
    'Arunanchal Pradesh': 'IN-AR',
    'Assam': 'IN-AS',
    'Bihar': 'IN-BR',
    'Chandigarh': 'IN-CH',
    'Chhattisgarh': 'IN-CT',
    'Dadara & Nagar Havelli': 'IN-DN',
    'Daman & Diu': 'IN-DD',
    'Goa': 'IN-GA',
    'Gujarat': 'IN-GJ',
    'Haryana': 'IN-HR',
    'Himachal Pradesh': 'IN-HP',
    'Jammu & Kashmir': 'IN-JK',
    'Jharkhand': 'IN-JH',
    'Karnataka': 'IN-KA',
    'Kerala': 'IN-KL',
    'Lakshadweep': 'IN-LD',
    'Madhya Pradesh': 'IN-MP',
    'Maharashtra': 'IN-MH',
    'Manipur': 'IN-MN',
    'Meghalaya': 'IN-ML',
    'Mizoram': 'IN-MZ',
    'Nagaland': 'IN-NL',
    'NCT of Delhi': 'IN-DL',
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

state_code_mapper_v2 = {
    'ANDAMAN AND NICOBAR ISLANDS': 'IN-AN',
    'Arunachal Pradesh': 'IN-AR',
    'Assam': 'IN-AS',
    'Bihar': 'IN-BR',
    'CHANDIGARH': 'IN-CH',
    'Chhattisgarh': 'IN-CT',
    'DADRA AND NAGAR HAVELI': 'IN-DN',
    'DAMAN AND DIU': 'IN-DD',
    'Goa': 'IN-GA',
    'Gujarat': 'IN-GJ',
    'Haryana': 'IN-HR',
    'Himachal Pradesh': 'IN-HP',
    'Jammu And Kashmir': 'IN-JK',
    'Jharkhand': 'IN-JH',
    'Karnataka': 'IN-KA',
    'Kerala': 'IN-KL',
    'LAKSHADWEEP': 'IN-LD',
    'Madhya Pradesh': 'IN-MP',
    'Maharashtra': 'IN-MH',
    'Manipur': 'IN-MN',
    'Meghalaya': 'IN-ML',
    'Mizoram': 'IN-MZ',
    'Nagaland': 'IN-NL',
    'Nct Of Delhi': 'IN-DL',
    'Pondicherry': 'IN-PY',
    'Punjab': 'IN-PB',
    'Rajasthan': 'IN-RJ',
    'Sikkim': 'IN-SK',
    'Tamil Nadu': 'IN-TN',
    'Telangana': 'IN-TG',
    'Tripura': 'IN-TR',
    'Uttar Pradesh': 'IN-UP',
    'Uttarakhand': 'IN-UT',
    'West Bengal': 'IN-WB',
    'Orissa': 'IN-OR',
    'Andhra Pradesh': 'IN-AP'
}

gc_base = shapegeocode.geocoder("local_reverse_geocoder_india/States/Admin2.shp")
gc_base_1 = shapegeocode.geocoder("local_reverse_geocoder_india/Igismap/Indian_States.shp")
gc_base_2 = shapegeocode.geocoder("local_reverse_geocoder_india/India_SHP/INDIA.shp")

#shape_file = shapefile.Reader("./States/Admin2.shp")
#print(shape_file.records())
def geocode(latitude, longitude, code_name_only = True, fast=True):
    if(fast):
        try:
            state_name = gc_base_1.geocode(latitude, longitude)['st_nm']
            state_code_name = state_code_mapper_v1[state_name]
            if(code_name_only):
                return state_code_name
            else:
                return state_name
        except:
            try:
                print("using different geocoder...")
                state_name = gc_base_2.geocode(latitude, longitude)['ST_NAME']
                state_code_name = state_code_mapper_v2[state_name]
                if(code_name_only):
                    return state_code_name
                else:
                    return state_name
            except:
                state_code_name = "UNKNOWN"
                return state_code_name
    else:
        if(not code_name_only):
            result =  gc_base.geocode(latitude, longitude)
            if(result):
                return result["ST_NM"]
            else:
                return "UNKNOWN"
        else:
            result =  gc_base.geocode(latitude, longitude)
            if(result):
                return state_code_mapper[result["ST_NM"]]
            else:
                return "UNKNOWN"

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
