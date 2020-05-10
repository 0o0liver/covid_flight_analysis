import pandas as pd
import os

keep_col = ["callsign","number","icao24","registration","typecode","origin","destination","firstseen","lastseen","day"]

for f in os.listdir("./flight"):
	df = pd.read_csv("flight/"+f)
	new_df = df[keep_col]
	new_df.to_csv("flight/cleaned_"+f, index=False)
	os.remove("flight/"+f)