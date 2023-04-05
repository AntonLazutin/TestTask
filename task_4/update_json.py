from datetime import datetime


example_json = {
	"id": "0001",
	"type": "donut",
	"updated": "Cake",
	"ppu": 0.55,
	"field": {
			"updated": None,
    },
    "new_field" : 
        {"some_field" : 
    			{
    			"updated" : "the most nested guy",
                "inner_child": {
						"updated": None,
						"inner_child": {
									"updated": None,
                                    "inner_child": {
												"updated": None,
                                                "inner_child": {
															"updated": None,
												},
									},
						},
				},
				}
        },
}

def update_json(some_json):
    for key, value in some_json.items():  
        if isinstance(value, dict):
            update_json(value)
        elif key == "updated":
            some_json[key] = datetime.now().isoformat()


if __name__ == "__main__":
    print(example_json)
    update_json(example_json)
    print(example_json)
