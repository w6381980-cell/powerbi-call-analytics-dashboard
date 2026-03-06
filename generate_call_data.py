import pandas as pd
import random

types = ["Incoming","Outgoing","Missed"]
category = ["Personal","Work","Spam","Unknown"]

data = []

for i in range(1000):
    number = "9"+str(random.randint(100000000,999999999))
    t = random.choice(types)
    dur = random.randint(5,900)
    cat = random.choice(category)

    data.append([number,t,dur,cat])

df = pd.DataFrame(data, columns=["Number","Type","Duration","Category"])

df.to_csv("call_logs.csv", index=False)

print("Dataset generated successfully!")