import config
import pandas as pd
import matplotlib.pyplot as plt
from bob_telegram_tools.bot import TelegramBot

key = config.key_sales_bot
user_id = config.user_id
bot = TelegramBot(key, user_id)

sheet_url = 'https://docs.google.com/spreadsheets/d/1UVjkHJAwH6S5LjOSeXSnV6amIrp4TnJL8gsRfqWeNmw/edit#gid=0'
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
df = pd.read_csv(url_1)
# print(df)
df = df[1:14]
print(df)

x = df['BO NAME']
y = df['Haryanto']

plt.bar(x, y,
        width=0.8)
plt.xticks(rotation=90)
bot.send_plot(plt)
