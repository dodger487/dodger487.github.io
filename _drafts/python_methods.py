class Foo(object):
  def __init__(self):
    self.foo = 'foo'

  def __add__(self, other):
    print "add"
    return self

class Bar(object):
  def __init__(self):
    self.foo = 'bar'

  def __radd__(self, other):
    print "radd"
    return self