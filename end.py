#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
import os

now = datetime.datetime.now()

levels_dict = {
    "5" : "🍾 AMAZING!",
    "4" : "🍷 Pretty Decent",
    "3" : "🍺 OK",
    "2" : "☕️ hmm",
    "1" : "🥃 Horrible"
}

level_str = "\n".join([ x + ") " + y for x, y in levels_dict.items()])

typeQuestion = """## {}

### How was your day?
{}
""".format(now.strftime("%Y-%m-%d"), level_str)

def dayString(day_level, desc):
    selection = levels_dict[day_level]
    return "{:^80}".format(selection + " " + desc + " ").replace("  ", "--")

if __name__ == '__main__':
    day_level = input(typeQuestion)
    anythingToAdd = input("Anything to add? \n")
    item = dayString(day_level, anythingToAdd)
    fn = "{}/{}.md".format("days", now.strftime("%Y_%m_%d"))
    f = open(fn, "a+")
    f.write("\n")
    f.write("# " + item)
    f.close()
    os.system("cat " + fn)
