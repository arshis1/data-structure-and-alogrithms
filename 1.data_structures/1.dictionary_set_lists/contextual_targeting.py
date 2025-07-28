#Content categories
#Tags
import random

class Contents:
    def __init__(self, title, c_types):
        self.title = title
        self.c_types = c_types
        self.id = random.randint(1,100000000)
        self.tags = set([])

    def addTags(self,c_tag):
        for x in c_tag:
            self.tags.add(x)

class Tags:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(100000001,200000000)
        self.contents = set([])

    def addContents(self,c_content):
        for x in str(c_content):
            self.contents.add(x)

x1 = Contents("Harry Potter", "Movies")
x2 = Contents("Friends", "TV Show")
x3 = Contents("Harry Potter 2", "Movies")
x4 = Contents("Dark", "TV Show")
x5= Contents("House of Cards", "TV Show")
x6= Contents("X Factor", "TV Show")


contentDict = {}
contentDict[x1.title] = x1
contentDict[x2.title] = x2
contentDict[x3.title] = x3
contentDict[x4.title] = x4
contentDict[x5.title] = x5
contentDict[x6.title] = x6
# print(contentDict)

y1 = Tags("action")
y2 = Tags("thriller")
y3 = Tags("male_demo")
y4 = Tags("female_demo")
y5 = Tags("drama")
y6 = Tags("comedy")

tagDict = {}
tagDict[y1.name] = y1
tagDict[y2.name] = y2
tagDict[y3.name] = y3
tagDict[y4.name] = y4
tagDict[y5.name] = y5
tagDict[y6.name] = y6
# print(tagDict)

x1.addTags([y2.id,y3.id,y4.id])
y2.addContents(x1.id)
y3.addContents(x1.id)
y4.addContents(x1.id)

x2.addTags([y5.id,y3.id,y4.id])
y5.addContents(x2.id)
y3.addContents(x2.id)
y4.addContents(x2.id)

x3.addTags([y5.id,y3.id,y4.id, y1.id])
y5.addContents(x3.id)
y3.addContents(x3.id)
y4.addContents(x3.id)
y1.addContents(x3.id)

x4.addTags([ y3.id ])
y3.addContents(x4.id)

x4.addTags([ y5.id,y3.id,y4.id, y1.id, y2.id ])
y5.addContents(x4.id)
y3.addContents(x4.id)
y4.addContents(x4.id)
y1.addContents(x4.id)
y2.addContents(x4.id)

#I want all drama content
print(tagDict["drama"].id)
