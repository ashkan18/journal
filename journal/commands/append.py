import os
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

@click.command(short_help="Append to today's journal")
@click.option('--type', default="9", prompt=type_question, help=type_question)
@click.option('--desc', default="", prompt="What?")
def append(type, desc):
    item = item_string(type, desc)
    fn = "{}/{}.md".format("days", date_str)
    f = open(fn, "a+")
    f.write("\n" + item)
    f.close()
    os.system("cat " + fn)
