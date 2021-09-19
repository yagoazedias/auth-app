# Super class for all types of authorizes,
# it prevents, for example, the subclasses from defining the same constructor
# It also tells the subclasses to implement the 'review_operation' method
# In order to force the return of it on the interface layer
class Authorizer:

    def __init__(self):
        self.result = {
            "account": {},
            "violations": []
        }

    def review_operation(self, operation):
        pass
