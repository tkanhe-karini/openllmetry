import dataclasses
import inspect
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
                json_method = o.json
                if callable(json_method) and not inspect.iscoroutinefunction(json_method):
                    result = json_method()
                    if not inspect.iscoroutine(result):
                        return result
                    result.close()

            if hasattr(o, "__class__"):
                return o.__class__.__name__

            return super().default(o)

        except:
            return str(o)
