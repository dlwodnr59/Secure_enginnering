 
 #트위터에 연결돼있을시 이전에 연결할려던것을 지우고 새로 룰 생성
 def on_connect(self):
    if self.get_rules().data != None:
        for rule in self.get_rules().data:
            self.delete_rules(rule.id)
    self.add_rules(tweepy.StreamRule("수능"))



#트위터에서 로그스테시로 port 5959를 사용하여 로그 스테시로 전송후 결과 출력
def on_tweet(self, tweet):
    tlogger = logging.getLogger('Twitter Crawler')
    if len(tlogger.handlers) == 0:
        tlogger.setLevel(logging.INFO)
        tlogger.addHandler(logstash.LogstashHandler('localhost', 5959, version=1))
    try:
        tlogger.info(tweet.text)
        print(tweet.text)
    except:
        None


 
 #에러코드
 def on_errors(self, errors):
        print(f"Received error code {errors}")
        self.disconnect()
        return False