"""
  Module documentation goes here
"""
def inherits_from(obj, a_class):
   if isinstance(obj, a_class) or issubclass(obj, a_class):
      return True
   
   return False