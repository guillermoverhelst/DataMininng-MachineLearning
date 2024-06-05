import requests
import re
import databaseConf

url = 'http://localhost/dashboard/recipes/Recipe'
con = databaseConf.Database()


def getSourceCode(id):
    r = requests.get(url + str(id) + ".html")
    return r.text


def getUsers():
    users = []
    for i in range(1, 10):
        source_code = getSourceCode(i)
        for match in re.findall('<p id="userId">([0-9]+)', source_code):
            if match not in users:
                users.append(match)
                databaseConf.Database.insert(con, "insert into users (userName) values ({0});".format(match))
    return users


def getRecipes():
    recipes = []
    for i in range(1, 10):
        source_code = getSourceCode(i)
        for match in re.findall('<title>(.*)</title>', source_code):
            if match not in recipes:
                recipes.append(match)
                databaseConf.Database.insert(con, "insert into recipe (recipeName) values ('{0}');".format(match))
    return recipes


def getRatings():
    ratings = []
    for i in range(1, 10):
        found_ratings = []
        j = 0
        source_code = getSourceCode(i)
        for match in re.findall('<p id="rating">([0-9]+)',source_code):
            found_ratings.append(match)

        for match in re.findall('<p id="userId">([0-9]+)', source_code):
            ratings.append([found_ratings[j], match, i])
            databaseConf.Database.insert(con, "insert into rating (rating, Users_idUsers, Recipe_idRecipe) "
                                              "values ('{0}', (select idUsers from users where userName = '{1}') , "
                                              "'{2}');"
                                         .format(found_ratings[j], match, i))
            j += 1

    return ratings
