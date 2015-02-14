import abc

""" All Rules should Implement this interface """
class RuleInterface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def itemRead(self, item):
        """ This Method should be called if a item has been read
            To  update the database and apply ML
        """
        return