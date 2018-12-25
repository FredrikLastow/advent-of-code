from datetime import datetime
from datetime import timedelta

def main():
  entries = []
  with open('input.txt') as f:
    for line in f:
      date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
      action = line[19:-1]

      entries.append([date, action])

  entries.sort(key=lambda entryDate: entryDate[0])


  guardsSleep = generateSleepDict(entries)
  #part1(guardsSleep)
  part2(guardsSleep)


def part1(guardsSleep):
  guardId = mostSleepyGuard(guardsSleep)

  minutes = guardsSleep[guardId]["timeSlept"]
  sleptCount = 0
  mostSleptMin = -1
  for m in minutes:
    mCount = minutes.count(m)
    if mCount > sleptCount:
      sleptCount = mCount
      mostSleptMin = m

  print(guardId, mostSleptMin)

def part2(guardsSleep):
  minuteCounts = []
  minuteGuards = []
  for i in range(61):
    curMinuteCount = 0
    curGuardId = -1
    for guardId, values in guardsSleep.items():
      sleepMinutes = values["timeSlept"]
      sleepCount = sleepMinutes.count(i)

      if sleepCount > curMinuteCount:
        curMinuteCount = sleepCount
        curGuardId = guardId

    minuteCounts.append(curMinuteCount)
    minuteGuards.append(curGuardId)

  mostSleptMin = minuteCounts.index(max(minuteCounts))
  guardId = minuteGuards[mostSleptMin]
  print(guardId, mostSleptMin)

def generateSleepDict(entries):
  guardsSleep = {}
  currentGuardId = ""
  sleepTime = datetime.today()

  for entry in entries:
    action = entry[1]
    date = entry[0]

    if action == "falls asleep":
      sleepTime = date
    elif action == "wakes up":
      dtMin = int((date - sleepTime).total_seconds()/60)

      guardsSleep[currentGuardId]["totSleep"] += dtMin
      for i in range(dtMin):
        sleepDate = sleepTime + timedelta(minutes=i)
        guardsSleep[currentGuardId]["timeSlept"].append(sleepDate.minute)

    else:
      currentGuardId = action.split(' ')[1]
      if not currentGuardId in guardsSleep:
        guardsSleep[currentGuardId] = {"totSleep": 0, "timeSlept": []}

  return guardsSleep


def mostSleepyGuard(guardsSleep):
  mostSlept = 0
  mostSleptId = -1

  for guardId, values in guardsSleep.items():
    totSleep = values["totSleep"]
    if totSleep > mostSlept:
      mostSlept = totSleep
      mostSleptId = guardId

  return mostSleptId

if __name__ == '__main__':
  main()
