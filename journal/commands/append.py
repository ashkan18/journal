#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
import click

date_str = datetime.datetime.now().strftime("%Y_%m_%d")

typesDict = {
    "1" : "✅ = Accomplishment",
    "2" : "🚢 = Shipped it",
    "3" : "🗑 = Trashed it",
    "4" : "🧻 = WIP",
    "5" : "👀 = Reviewed",
    "6" : "📚 = Learning",
    "7" : "🎉 = Celebration",
    "8" : "💡 = Idea",
    "9" : "🥩 = Meeting",
    "10" : "🤔 = Puzzling/Challenging",
    "11" : "😐 = Mmmm...",
    "12" : "💩 = Not great",
    "12 + 1" : "🤷‍♀️ = Other"
}

types_str = "\n".join([ x + ") " + y for x, y in typesDict.items()])

type_question = """## {}

### Pick an item type.
{}
""".format(date_str, types_str)

def item_string(item_type, item_text):
    selection = typesDict[item_type]
    return "- " + selection.split(" = ")[0] + " " + item_text

if __name__ == '__main__':
    item_type = input(type_question)
    item_text = input("What?\n")
    item = item_string(item_type, item_text)
    fn = "{}/{}.md".format("days", date_str)
    f = open(fn, "a+")
    f.write("\n" + item)
    f.close()
    os.system("cat " + fn)
