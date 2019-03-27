import sys
import wikipedia as wiki

# get
query = input("What are you thinking about?\n")
result = wiki.page(title=query)
# write
file = open(result.title + ".txt", 'w')
file.write(result.content)
file.close()
