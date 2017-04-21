# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: henrypj
# Collaborators: None
# Time: x:xx

import feedparser
import string
import time
import threading
import re
import sys
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewStory object
                
        guid (string): A globally unique identifier for this news story
        
        title (string): The news story's headline
        
        description (string): A paragraph or so summarizing the news story
        
        link (string): A link to a website with the entire story
        
        pubdate (datetime): Date the news was published 

        A NewsStory object has two attributes:
            self.guid (string, determined by input text)
            self.title (string, determined by input text)
            self.description (string, determined by input text)
            self.link (string, determined by input text)
            self.pubdate (datetime, determined by input text)
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
        
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link

    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate

    

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    """
    An abstract class
    """
    def __init__(self, phrase):
        '''
        Initializes a PhraseTrigger object
                
        phrase (string): some text of one or more words separated by space or punctuation
        
        A NewsStory object has two attributes:
            self.phrase (string, determined by input text)
        '''
        self.phrase = phrase.lower()
    
    def is_phrase_in(self, text):
        '''
        Used to determine if the entire phrase self.phrase is present in text.
        Case is ignored.
                
        Returns: True if self.phrase is present in self.txt or False otherwise
        '''
        # Remove punctuations, multiple spaces from text and convert to lower case
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        newtext = regex.sub(' ', text)
        newtext = ' '.join(newtext.split()).lower()
        
        if self.phrase in newtext:
            x = newtext.find(self.phrase)
            y = len(self.phrase) + x
            # Check to see if next char after phrase is a letter, if so, return False
            if y < len(newtext) and newtext[len(self.phrase) + x].isalpha():
                return False
            else:
                return True
        else:
            return False     

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    """
    An subclass of PhraseTrigger that fires when a news item's ​title contains a given phrase
    """
    def __init__(self, phrase):
        '''
        Initializes a TitleTrigger object
                
        phrase (string): some text of one or more words separated by space or punctuation
        '''
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in(story.get_title())
    
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    """
    An subclass of PhraseTrigger that fires when a news item's description contains a given phrase
    """
    def __init__(self, phrase):
        '''
        Initializes a DescriptionTrigger object
                
        phrase (string): some text of one or more words separated by space or punctuation
        '''
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in(story.get_description())


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    """
    An abstract subclass of Trigger
    """
    def __init__(self, testdate):
        '''
        Initializes a TimeTrigger object
                
        time (string): time that story was published as EST in format "3 Oct 2016 17:00:10"
        
        A TimeTrigger object has one attributes:
            self.time (datetime, determined by input text)
        '''
        self.testdate = datetime.strptime(testdate, '%d %b %Y %H:%M:%S')
        self.testdate = self.testdate.replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """
    A subclass of TimeTrigger that fires when a news story is published before the time trigger
    """
    def __init__(self, testdate):
        '''
        Initializes a BeforeTrigger object
                
        '''
        TimeTrigger.__init__(self, testdate)
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated for the given news item
        becuase it was published before the time trigger, or False otherwise.
        """
        return self.testdate > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    """
    A subclass of TimeTrigger that fires when a news story is published after the time trigger
    """
    def __init__(self, testdate):
        '''
        Initializes a BeforeTrigger object
                
        '''
        TimeTrigger.__init__(self, testdate)
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated for the given news item
        becuase it was published after the time trigger, or False otherwise.
        """
        return self.testdate < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    """
    An abstract class
    """
    def __init__(self, T):
        '''
        Initializes a NotTrigger object
                
        T (Trigger): A trigger
        
        '''
        self.T = T
        
    def evaluate(self, story):
        """
        Returns the invert output of another trigger.
        """
        return not self.T.evaluate(story)
    

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    """
    An abstract class
    """
    def __init__(self, T1, T2):
        '''
        Initializes a AndTrigger object
                
        T1 (Trigger): A trigger
        T2 (Trigger): A trigger
        
        '''
        self.T1 = T1
        self.T2 = T2
        
    def evaluate(self, story):
        """
        Returns the invert output of another trigger.
        """
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    """
    An abstract class
    """
    def __init__(self, T1, T2):
        '''
        Initializes a OrTrigger object
                
        T1 (Trigger): A trigger
        T2 (Trigger): A trigger
        
        '''
        self.T1 = T1
        self.T2 = T2
        
    def evaluate(self, story):
        """
        Returns the invert output of another trigger.
        """
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break
    return filtered_stories

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_list = []
    trigger_dict = {}
    for line in lines:
        element = line.split(",")
        if element[0] == "ADD":
            for trig in element:
                if trig != "ADD":
                    trigger_list.append(trigger_dict[trig])
        else:
            if element[1] == "TITLE":
                trigger_dict[element[0]] = TitleTrigger(element[2])
            elif element[1] == "DESCRIPTION":
                trigger_dict[element[0]] = DescriptionTrigger(element[2])
            elif element[1] == "AFTER":
                trigger_dict[element[0]] = AfterTrigger(element[2])
            elif element[1] == "BEFORE":
                trigger_dict[element[0]] = BeforeTrigger(element[2])
            elif element[1] == "AND":
                trigger_dict[element[0]] = AndTrigger(trigger_dict[element[2]], trigger_dict[element[3]])
            elif element[1] == "OR":
                trigger_dict[element[0]] = OrTrigger(trigger_dict[element[2]], trigger_dict[element[3]])
            elif element[1] == "NOT":
                trigger_dict[element[0]] = NotTrigger(trigger_dict[element[2]])
    
    return trigger_list                
    #print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Aaron Hernandez")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Russia")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    #sys.setrecursionlimit(5000)
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

