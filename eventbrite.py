import json
import requests


main_url = "https://www.eventbriteapi.com/v3/users/me/organizations/"
payload = ""
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer Z3MMSXNHS64V5XEIAJ67",
    }
response = requests.request("GET", main_url, data=payload, headers=headers)
my_string = json.loads(response.text)
new_dict = my_string["organizations"]
dictionary = new_dict[0]
main_id = dictionary["id"]


create_event_url = "https://www.eventbriteapi.com/v3/organizations/{key}/events/".format(key=main_id)
payload1 = {"event": {
            "name": {
                "html": "Relinn's Party"
            },
            "start": {
                "timezone": "America/Los_Angeles",
                "utc": "2019-04-25T02:00:00Z"
            },
            "end": {
                "timezone": "America/Los_Angeles",
                "utc": "2019-05-25T05:00:00Z"
            },
            "currency": "USD"
        }
}
response1 = requests.request("POST", create_event_url, data=json.dumps(payload1), headers=headers)
create_event_string = json.loads(response1.text)
event_id = create_event_string["id"]

view_events_url = "https://www.eventbriteapi.com/v3/organizations/{key}/events/".format(key=main_id)
response_view_events = requests.request("GET", view_events_url, data=payload, headers=headers)
view_events_string = json.loads(response_view_events.text)
new_dict1 = view_events_string["events"]
my_dict = new_dict1[1]
event_id = 0
for k, v in my_dict.items():
    if k == "id":
        event_id = v
        break

update_event_url = "https://www.eventbriteapi.com/v3/events/{key}/".format(key=event_id)
payload2 = {
    "event": {
                "capacity": 55
             }
}
response2 = requests.request("POST", update_event_url, data=json.dumps(payload2), headers=headers)
update_event_string = json.loads(response2.text)
# print(update_event_string)



ticket_classes_url = "https://www.eventbriteapi.com/v3/events/{key}/ticket_classes/".format(key=event_id)
payload3 = {"ticket_class": {
                                "name": "VIP",
                                "quantity_total": 15,
                                "cost": "USD,50000"
                            }
           }

response3 = requests.request("POST", ticket_classes_url, data=json.dumps(payload3), headers=headers)
ticket_classes_string = json.loads(response3.text)
# print(ticket_classes_string)


publish_url = "https://www.eventbriteapi.com/v3/events/{key}/publish/".format(key=event_id)
response4 = requests.request("POST", publish_url, headers=headers)
publish_string = json.loads(response4.text)
for k, v in publish_string.items():
    print(f"{k}: {v}")

find_event_url = "https://www.eventbriteapi.com/v3/users/me/events/"
response5 = requests.request("GET", url=find_event_url, data=payload, headers=headers)
temp = json.loads(response5.text)
temp1 = temp["events"]
for i in temp1:
    events_data = i
    for k, v in events_data.items():
        if k == "id":
            d = events_data["name"]
            print(d["text"], end=": ")
            print(f"{v}")
            break
    print()
category_url = "https://www.eventbriteapi.com/v3/categories/"


