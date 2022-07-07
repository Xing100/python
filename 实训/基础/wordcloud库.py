import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud by python")
c.to_file("pywordcloud.png")