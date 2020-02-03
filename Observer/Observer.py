from abc import ABC, abstractmethod

class Topic(ABC):
    @abstractmethod
    def __init__(self):
        self.subscribers = []
    @abstractmethod
    def register(self, observer):
        self.subscribers.append(observer)
    @abstractmethod
    def unregister(self, observer):
        self.subscribers.remove(observer)
    @abstractmethod
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
        self.name == name



class Regularcustomer(Observer):
    def update(self):
        print("Need to buy one of those")

class CorporateCustomer(Observer):
    def update(self):
        print("My company would benefit from this!")


if __name__ == "__main__":
    iphoneFeed = PhoneFeed("Iphone")
    androidFeer = PhoneFeed("Android")
    john = Regularcustomer()
    john.setSubject(iphoneFeed)
    Ann = CorporateCustomer()
    Ann.setSubject(androidFeer)