import json


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, complex):
            return {"__type__": "complex", "real": o.real, "imag": o.imag}
        elif isinstance(o, range):
            return {"__type__": "range", "start": o.start, "stop": o.stop, "step": o.step}
        return super().default(o)


class MyJSONDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        def hook(obj):
            if "__type__" in obj:
                if obj["__type__"] == "complex":
                    return complex(obj["real"], obj["imag"])
                elif obj["__type__"] == "range":
                    return range(obj["start"], obj["stop"], obj["step"])
            return obj
        super().__init__(**kwargs, object_hook=hook)


def my_dumps(obj, **kwargs):
    # Wrapper around json.dumps with additional options if needed.
    return json.dumps(obj, cls=MyJSONEncoder, **kwargs)


def my_loads(s, **kwargs):
    # Wrapper around json.loads with additional options if needed.
    return json.loads(s, cls=MyJSONDecoder, **kwargs)
