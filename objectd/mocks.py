from django.http import Http404


class Objectd():
    OBJECTDS =[
    {'id':1,'title':'first image','body':'sdfjodfj podjflsd'},
    {'id':2,'title':'fsecode image','body':'sdfjodfj podjflsd'},
    {'id':3,'title':'first image','body':'sdfjodfj podjflsd'},
    ]

    @classmethod
    def all(cls):
        return cls.OBJECTDS 
    @classmethod
    def find(cls,id):
        try:
            return cls.OBJECTDS[int(id)-1]
        except:
            raise Http404('Sorry, objet #{} not found'.format(id))