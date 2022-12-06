fig, ax = plt.subplots(1, 5, figsize = (15, 3), sharey = True)
colors = ["blue", "yellow", "green", "orange", "purple"]
axis_index = [0,1,2,3,4]
index = 0
for continent, df_continent in gapminder.groupby(['continent']):



 # run this code to understand what's happening
 # print(continent, df_continent.shape)


 for country, df_country in df_continent.groupby(['country']):
 # some plotting code here

 ax[axis_index[index]].plot(df_country['year'], df_country['lifeExp'],
 color = colors[index], linewidth=0.25)
 ax[axis_index[index]].title.set_text(continent)
 # run this code to understand what's happening
 # print(country, df_country.shape)

 index += 1
