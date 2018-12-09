import json

# General data structure
class Account():

    def __init__(self, name, street_address, city, post_code):
        self.name=name
        self.address={"street_address": street_address, "city": city, "post_code": post_code}
        self.cards=[]

    def add_cards(self,number,valid):
        if not any(c["number"] == number for c in self.cards):
            self.cards.append({"number": number, "valid": valid, "operations": []})
        else:
            print("WARNING: Card don't added. Card with number "+ number +" exist.")

    def add_operations(self, number, date, amount, type):
        if any(c["number"] == number for c in self.cards):
            index_card = next((index for (index, d) in enumerate(self.cards) if d["number"] == number), None)
            operations = self.cards[index_card]['operations']

            # 5 last operations (!)
            if len(operations) < 5:
                operations.append({"date": date, "amount": amount, "type": type})
            else:
                del operations[0] # FIFO
                operations.append({"date": date, "amount": amount, "type": type})
        else:
            print("WARNING: Operation (" + date + ", " + amount + ", " + type + ") failed. Card number "+ number +" not found.")

    # get JSON format
    def get_result(self):
        return json.dumps(vars(self), indent=2)

# Created Account() through JSON
def json_to_account(data):
    jdata = json.loads(data)

    for key, value in jdata.iteritems():
        if key == "name":
            name = value
        elif key == "address":
            address = value
        elif key == "cards":
            cards = value

    result=Account(name, address["street_address"], address["city"], address["post_code"])

    for c in cards:
        result.add_cards(c["number"],c["valid"])
        for o in c["operations"]:
            result.add_operations(c["number"], o["date"], o["amount"], o["type"])

    return result

##################################################
# Create new Account
##################################################
andrey=Account("Andrey Alekseevich Petrov","Raduzhnaya ulitsa, 3","Moscow","142784")
andrey.add_cards("5555 5678 9012 3456","12/2020")
# andrey.add_cards("5555 5678 9012 3456","12/2020") # WARNING
andrey.add_cards("1234 5678 9012 3456","12/2020")
andrey.add_operations("1234 5678 9012 3456","09.10.2018","170","income")
andrey.add_operations("1234 5678 9012 3456","10.10.2018","80","outcome")
andrey.add_operations("1234 5678 9012 3456","12.10.2018","1200","income")
andrey.add_operations("1234 5678 9012 3456","15.10.2018","315","income")
andrey.add_operations("1234 5678 9012 3456","20.10.2018","500","outcome")
andrey.add_operations("1234 5678 9012 3456","22.10.2018","700","income")
andrey.add_operations("1234 5678 9012 3456","25.10.2018","200","income")
# andrey.add_operations("1234 5678 9012 0000","30.10.2018","750","income") # WARNING
print(andrey.get_result())

print("#####################")

##################################################
# Create new Account through JSON-format
##################################################
string_json = '''{
  "address": {
    "city": "Saint Petersburg",
    "post_code": "190121",
    "street_address": "Sadovaya Street, 82"
  },
  "cards": [
    {
      "number": "5412 3456 7890 1234",
      "operations": [],
      "valid": "12/2018"
    },
    {
      "number": "5412 3456 1234 7890",
      "operations": [
        {
          "amount": "2200",
          "date": "20.08.2018",
          "type": "income"
        },
        {
          "amount": "300",
          "date": "05.09.2018",
          "type": "outcome"
        },
        {
          "amount": "800",
          "date": "12.09.2018",
          "type": "income"
        },
        {
          "amount": "750",
          "date": "25.09.2018",
          "type": "income"
        },
        {
          "amount": "920",
          "date": "20.10.2018",
          "type": "outcome"
        },
        {
          "amount": "1560",
          "date": "24.10.2018",
          "type": "income"
        },
        {
          "amount": "410",
          "date": "28.10.2018",
          "type": "outcome"
        }
      ],
      "valid": "04/2022"
    }
  ],
  "name": "Aleksandr Sergeevich Klimov"
}
'''

aleksander = json_to_account(string_json)
print(aleksander.get_result())
