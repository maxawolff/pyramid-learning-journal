"""Place to hold the raw data for learning journal entries."""
from datetime import datetime

FMT = '%m/%d/%Y'

entries = [{'id': 1, 'title': 'Day 1', 'creation_date': datetime.strptime('10/16/2017', FMT), 'body': 'some words and some text'},
           {'id': 2, 'title': 'Day 2', 'creation_date': datetime.strptime('10/17/2017', FMT), 'body': 'some words and some text'},
           {'id': 3, 'title': 'Day 3', 'creation_date': datetime.strptime('10/18/2017', FMT), 'body': 'some words and some text'},
           {'id': 4, 'title': 'Day 4', 'creation_date': datetime.strptime('10/19/2017', FMT), 'body': 'some words and some text'},
           {'id': 5, 'title': 'Day 5', 'creation_date': datetime.strptime('10/20/2017', FMT), 'body': 'some words and some text'},
           {'id': 6, 'title': 'Day 6', 'creation_date': datetime.strptime('10/23/2017', FMT), 'body': 'some words and some text'},
           {'id': 7, 'title': 'Day 7', 'creation_date': datetime.strptime('10/24/2017', FMT), 'body': 'some words and some text'},
           {'id': 8, 'title': 'Day 8', 'creation_date': datetime.strptime('10/25/2017', FMT), 'body': 'some words and some text'},
           {'id': 9, 'title': 'Day 9', 'creation_date': datetime.strptime('10/26/2017', FMT), 'body': 'some words and some text'},
           {'id': 10, 'title': 'Day 10', 'creation_date': datetime.strptime('10/27/2017', FMT), 'body': "Some good news and some bad news today. We finished our work for day 3, our server works as expected, sending back the file that we asked for, passing all of our tests. However we had a problem with our gevent server which was giving us an OS error that none of the TA's could figure out, (though they were all awesome and really tried to help!). Anyways I'm feeling pretty good about the class so far, though this was a bit frustrating. The code review session today was very helpful, it emphasized the importance of writing tests."},
           {'id': 11, 'title': 'Day 11', 'creation_date': datetime.strptime('10/30/2017', FMT), 'body': "Today we walked through how to use pyramid to host our own sites. I think this is the proper terminology for this, we can serve up our html files, give them custom routes and even more probably. It doesn't sound like a lot but there is a lot to it and was not easy to do. However it is much easier than trying to write our own servers and handle all possible edge cases. I also worked on deploying a site to heroku again, only this time in python instead of javascript. Always a few issues there but thankfully it went up without too much trouble."},
           {'id': 12, 'title': 'Day 12', 'creation_date': datetime.strptime('10/31/2017', FMT), 'body': "Today was interesting. We spent most of our time working on our binary heap, which was harder than I thought it would be. We tried using nodes at first but eventually we ran into a bunch of problems with this. Once we switched over to using a list it was easier but we still took a while to figure out exactly what should happen, right before we were going to switch to the learning journal though we got our push method working. Working with pyramid has been ... interesting? It doesn't seem too hard, though I haven't quite finished it, but I also don't totally understand it yet. I'm sure I will eventually though."}]
