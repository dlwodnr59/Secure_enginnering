import tweepy
import logging
import logstash


#트위터에 연결돼있을시 이전에 연결할려던것을 지우고 새로 룰 생성


BEARER_TOKEN = "BEAER_TOKEN"

class IDPrinter(tweepy.StreamingClient):
    def on_connect(self):
        if self.get_rules().data != None:
            for rule in self.get_rules().data:
                self.delete_rules(rule.id)
        self.add_rules(tweepy.StreamRule("수능"))

    def on_tweet(self, tweet):
        tlogger = logging.getLogger('Twitter Crawler')
        if len(tlogger.handlers) ==0:
            tlogger.setLevel(logging.INFO)
            tlogger.addHandler(logstash.LogstashHandler('localhost', 5959, version=1))
        try:
            tlogger.info(tweet.text)
            print(tweet.text)
        except :
            None

    def on_errors(self, errors):
        print(f"Received error code {errors}")
        self.disconnect()
        return False

printer = IDPrinter(BEARER_TOKEN)
printer.filter()