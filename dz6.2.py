

a=1900800
days=a//86400
hours=a//3600-(days*24)
mins=a//60-days*(24*60)-(hours*60)
sec=a-((days*24*3600)+(hours*3600)+(mins*60))

string_hours=str(hours)
string_mins=str(mins)
string_sec=str(sec)

padded_hours=string_hours.zfill(2)
padded_mins=string_mins.zfill(2)
padded_sec=string_sec.zfill(2)


if 5<=days<=19 or str(days).endswith("0"):
    print(str(days)+" днів,",padded_hours+":"+padded_mins+":"+padded_sec)
elif str(days).endswith("2"):
    print(str(days)+" дні,",padded_hours+":"+padded_mins+":"+padded_sec)
elif str(days).endswith("1") and days!="11":
    print(str(days)+" день,",padded_hours+":"+padded_mins+":"+padded_sec)
else:
    print(str(days) + " днів,",padded_hours+":"+padded_mins+":"+padded_sec)



