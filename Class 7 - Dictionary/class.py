from typing import Dict,Union,Any

Key = Union[str,int,tuple] # Creating Custom Data Type
Value = Union[int,str,list,dict,tuple,set] # Creating Custom Data Type
data : Dict[Key,Value] = {"fname":"Suhail",
                        "name":"Azfar",
                        "occupation":"Student",
                        100:"Pakistan",
                        (1,2,3):"Hello",
                        'asd':{"a":1,"b":2}
                        }
print(data["asd"]["b"])