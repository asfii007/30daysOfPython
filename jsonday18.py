#coverting python objects into JSON string(json.dumps)
import json
data={
"name":"asfiya",
'age': 20,
"is_student":True,
"college":"gist"
}
print("python dict: data")
print (data)
print("converting dict to json string")
jsonstring=json.dumps(data)
print(jsonstring)