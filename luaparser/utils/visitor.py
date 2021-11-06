# A couple helper functions first


class VisitorException(Exception):
    def __init__(self, message):
        self.message = message


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[: name.rfind(".")]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    if (_qualname(type(self)), type(arg)) in _methods:
        method = _methods[(_qualname(type(self)), type(arg))]
        return method(self, arg)
    else:
        # if no visitor method found for this arg type,
        # search in parent arg type:
        arg_parent_type = arg.__class__.__bases__[0]
        while arg_parent_type != object:
            if (_qualname(type(self)), arg_parent_type) in _methods:
                method = _methods[(_qualname(type(self)), arg_parent_type)]
                return method(self, arg)
            else:
                arg_parent_type = arg_parent_type.__bases__[0]
    raise VisitorException("No visitor found for class " + str(type(arg)))


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator
