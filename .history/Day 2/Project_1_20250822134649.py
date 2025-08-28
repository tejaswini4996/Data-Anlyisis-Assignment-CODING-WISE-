def roadmap(exp,fresher,experienced):
    if exp== "fresher":
        if fresher == "web dev":
            return "learn html,css,js,python,django"
        elif fresher == "app dev":
            return "learn java+ dsa+ built projects"
        elif fresher == "DS, ML, AI ":
            return "Learn python, matchs, R"
    if exp == "experienced":
        if experienced == "Data analytics":
            return "learn py , excel, powerBI"
        elif experienced == "Cloud computing":
             return "Learn devops, python for automation"
        elif experienced == "Front-end":
            return "Learn python, django for backend"
            


print(roadmap("fresher","web dev",""))
print(roadmap("experienced", "","Data analytics"))


