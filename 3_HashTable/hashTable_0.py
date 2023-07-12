scores = {
    "math" : 97,
    "eng" : 97,
    "kor" : 89
}

scores["math"]

scores["math"] = 45
print(scores["math"])

scores["sci"] = 100
print(scores["sci"])

if "music" in scores:
    print(scores["music"])
else:
    scores["music"] = 0
