countries = [
    {"name":"COUNTRIES", "population": "POPULATION"},
    {"name":"Poland", "population":"38000000"},
    {"name":"USA", "population":"312000000"},
    {"name":"Germany", "population":"82000000"},
    {"name":"Japan", "population":"120000000"},
    {"name":"Czechia", "population":"8000000"},
]

for item in countries:
    print(item["name"], item["population"])