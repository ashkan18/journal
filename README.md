<p align="center" margin=0 padding=0>
  <img src="docs/journalist.png" width=100 margin=0 padding=0/>
</p>

# Journalists [![PyPI version](https://badge.fury.io/py/journalists.svg)](https://badge.fury.io/py/journalists)
Command-line based personal journal tool. 

## Install
```
pip install journalists
```

## Usage

### Help
```
> journalists --help
Usage: journalists [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  append   Append to today's journal
  end      End today's journal
  version
```


### Append to your today's journal

```
➜  journalists append
## 2020_05_22

### Pick an item type.
1) ✅ = Accomplishment
2) 🚢 = Shipped it
3) 🗑 = Trashed it
4) 🧻 = WIP
5) 👀 = Reviewed
6) 📚 = Learning
7) 🎉 = Celebration
8) 💡 = Idea
9) 🥩 = Meeting
10) 🤔 = Puzzling/Challenging
11) 😐 = Mmmm...
12) 💩 = Not great
12 + 1) 🤷‍♀️ = Other
9
What?
Standup with Highlights

- 📚 Python's format method
- 👀 PR #143
- 🚢 New release of journal app
- 🥩 Standup with Highlights
```

## End your day
```
journalists end
## 2020-05-22
- 📚 Python's format method
- 👀 PR #143
- 🚢 New release of journal app
- 🥩 Standup with Highlights

### How was your day?
5) 🍾 AMAZING!
4) 🍷 Pretty Decent
3) 🍺 OK
2) ☕️ hmm
1) 🥃 Horrible
4
Anything to add?
Felt productive
- 📚 Python's format method
- 👀 PR #143
- 🚢 New release of journal app
- 🥩 Standup with Highlights

# ------------------------🍷 Pretty Decent Felt productive------------------------
```

# Credits
Based on @hansencc original script.
