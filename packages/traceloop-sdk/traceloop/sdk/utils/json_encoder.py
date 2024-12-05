import dataclasses
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, dict) and "callbacks" in o:
                del o["callbacks"]
                return o

            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)

            if hasattr(o, "to_json"):
                return o.to_json()

            if hasattr(o, "json"):
                return o.json()

            return super().default(o)
        except:
            return str(o)
