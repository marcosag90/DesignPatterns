from abc import ABC, abstractmethod

class Topic(object):
    def __init__(self):
        self.subscribers = []
    def register(self, observer):
        self.subscribers.append(observer)
    def unregister(self, observer):
        self.subscribers.remove(observer)
    def NotifyObservers(self):
        for susbscriber in self.subscribers:
            susbscriber.update()




class Observer(ABC):
    def setSubject(self, Topic):
        Topic.register(self)
    @abstractmethod
    def update(self):
        pass



class PhoneFeed(Topic):
    def __init__(self, name):
        Topic.__init__(self)
        self.name = name
        self.message = None
    def newMessage(self, message):
        self.message = message
        self.NotifyObservers()



class Regularcustomer(Observer):
    def update(self):
        print("Need to buy one of those")

class CorporateCustomer(Observer):
    def update(self):
        print("My company would benefit from this!")


if __name__ == "__main__":
    iphoneFeed = PhoneFeed("Iphone")
    androidFeed = PhoneFeed("Android")
    john = Regularcustomer()
    john.setSubject(iphoneFeed)
    Ann = CorporateCustomer()
    Ann.setSubject(androidFeed)

    androidFeed.newMessage("New Samsumg out!")

    iphoneFeed.newMessage("Iphone upgrade!")
