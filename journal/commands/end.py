import datetime
import os
import click

now = datetime.datetime.now()

levels_dict = {
    "5" : "🍾 AMAZING!",
    "4" : "🍷 Pretty Decent",
    "3" : "🍺 OK",
    "2" : "☕️ hmm",
    "1" : "🥃 Horrible"
}

level_str = "\n".join([ x + ") " + y for x, y in levels_dict.items()])

day_level_question = """## {}

### How was your day?
{}
""".format(now.strftime("%Y-%m-%d"), level_str)

def dayString(day_level, desc):
    selection = levels_dict[day_level]
    return "{:^80}".format(selection + " " + desc + " ").replace("  ", "--")

@click.command(short_help="End today's journal")
@click.option('-t', default="9", prompt=day_level_question, help=day_level_question)
@click.option('-n', default="", prompt="Anything to add?")
def end(day_level, note):
    fn = "{}/{}.md".format("days", now.strftime("%Y_%m_%d"))
    f = open(fn, "a+")
    os.system("cat " + fn)
    item = dayString(day_level, note)
    f.write("\n")
    f.write("# " + item)
    f.close()
    os.system("cat " + fn)
