#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2
import sys
import re


con = None

try:

    class puppy_route(object):

        def __init__(self,dbname,user):
            self.connStr = "dbname=%s user=%s" % (dbname,user)
            self.con = psycopg2.connect(self.connStr)
            self.cur = self.con.cursor()

        def routeTimes(self):
            # Getting the unique dog ids from the route_stop table
            self.cur.execute("SELECT distinct dog_info_id FROM route_stop;")
            rows = self.cur.fetchall()
            routeTimeDict = {}
            # Getting each dog's pickup time and drop-off time putting that in dictionary
            for row in rows:
                dogID = int(''.join(map(str,row)))
                cur1 = self.cur
                cur1.execute("SELECT id FROM route_stop WHERE dog_info_id = (%s);", row)
                dogRoutes = cur1.fetchall()
                routeTime = []
                for routeID in dogRoutes:
                    cur2 = self.cur
                    cur2.execute("SELECT recorded_timestamp FROM route_stop_time WHERE route_stop_id = (%s);", routeID)
                    rt = cur2.fetchall()
                    routeTime.append(rt)
                    routeTime.sort(reverse=True)
                    if (len(routeTime) == 2):
                        routeTimeDict[dogID]=routeTime
            return routeTimeDict

        def maxNumOfDogs(self):
            cur5 = self.cur
            # Getting unique dog walker ids from route_stop table
            cur5.execute("SELECT distinct dog_walker_id FROM route_stop;")
            rows = self.cur.fetchall()
            maxDogsPerWalker = {}
            # Getting dogsPerWalker count and comparing with maxDogsPerWalker current maximum number of dogs
            for dogWalkerID in rows:
                maxDogsPerWalker[dogWalkerID] = 0
                dogsPerWalker = {}
                cur6 = self.cur
                cur6.execute("SELECT is_pickup FROM route_stop WHERE dog_walker_id = (%s) ORDER BY id asc;", dogWalkerID)
                isPickup = self.cur.fetchall()
                count = 0
                for val in isPickup:
                    val = ''.join(map(str,val))
                    if count == 0 and val == 'True':
                        dogsPerWalker[dogWalkerID] = 0
                        dogsPerWalker[dogWalkerID] += 1
                        count += 1
                    elif count == 0 and val == 'False':
                        dogsPerWalker[dogWalkerID] = 0
                        count += 1
                    elif val == 'True':
                        dogsPerWalker[dogWalkerID] += 1
                    else:
                        dogsPerWalker[dogWalkerID] -= 1


                    if dogsPerWalker[dogWalkerID] > maxDogsPerWalker[dogWalkerID]:
                        maxDogsPerWalker[dogWalkerID] = dogsPerWalker[dogWalkerID]
            maxNumDogs = max(maxDogsPerWalker.values())
            return maxNumDogs


        def timeElasped(self,routeTimeDict):
            # Updating the dictionary to have the dogID with its time outside as the value
            for key in routeTimeDict.keys():
                firstVal = routeTimeDict[key][0][0]
                secondVal = routeTimeDict[key][1][0]
                routeTimeDict[key] = int(''.join(map(str,firstVal))) - int(''.join(map(str,secondVal)))
            return routeTimeDict

        def breedDog(self,routeTimeDict):
            breedDict = {}
            for key, val in routeTimeDict.items():
                cur4 = self.cur
                cur4.execute("SELECT distinct breed FROM dog_info WHERE id = (%s);", [key])
                dogB = cur4.fetchall()
                dogBreed = ''.join(map(str,dogB))
                breedDict[dogBreed] = val
                try:
                    if (len(breedDict[dogBreed]) == 2):
                        breedDict[dogBreed] = sum(breedDict[dogBreed])
                except TypeError:
                    continue
            return breedDict

        def maxValueID(self, routeTimeDict):
            maxVal = max(routeTimeDict.values())
            # If they have two or more dogs that have the maximum value. Store both
            ######### COME BACK TO THIS!! ##############
            puppyID = []
            for key, val in routeTimeDict.items():
                if (val == maxVal):
                    puppyID.append(key)
            return puppyID

        def dogName(self,puppyID):
            cur3 = self.cur
            dogList = []
            for i in puppyID:
                cur3.execute("SELECT name FROM dog_info WHERE id = (%s);", [i])
                dogName = cur3.fetchall()
                dogList.append(dogName)
            return ' '.join(map(str,dogList))

        def breedName(self,puppyID):
            return ''.join(map(str,puppyID))



    # Replace the below two arguments with the Database Name and Username you are going to use.
    puppy = puppy_route(sys.argv[1],sys.argv[2])

    # Answer 1
    # Getting the dog that was outside the longest
    dogsRouteTimes = puppy.routeTimes()
    dogsTimeOutside = puppy.timeElasped(dogsRouteTimes)
    dogID = puppy.maxValueID(dogsTimeOutside)
    dogName = puppy.dogName(dogID)
    regex = re.compile('[^a-z A-Z]')
    print("Dog outside the longest: " + regex.sub('', dogName))

    # Answer 2
    # Getting the breed that was outside the longest
    dogsRouteTimes = puppy.routeTimes()
    dogsTimeOutside = puppy.timeElasped(dogsRouteTimes)
    breedDict = puppy.breedDog(dogsTimeOutside)
    breedID = puppy.maxValueID(breedDict)
    breedName = puppy.breedName(breedID)
    regex = re.compile('[^a-z A-Z]')
    bName = regex.sub(' ', breedName)
    print("Breed outside longest: " + bName.strip())

    # Answer 3
    # Maximum number of dogs any walker has at any time
    maxNumDogs = puppy.maxNumOfDogs()
    print("Most dogs any walker has: " + str(maxNumDogs))


except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)


finally:

    if con:
        con.close()
