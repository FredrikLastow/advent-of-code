import sys
import regex as re
from ast import literal_eval
from tqdm import tqdm

def main():
  unsolved_rules = dict()
  solved_rules = dict()
  messages = list()

  with open("input2.txt") as f:
    isRules = True

    for line in f:
      if line == "\n":
        isRules = False
      elif isRules:
        rule_id, rule = line.strip().split(":")

        if rule.count("\"") > 0:
          solved_rules[rule_id] = rule[2:-1]
        else:
          unsolved_rules[rule_id] = rule[1:]

      else:
        messages.append(line.strip())

  unsolved_rules = dict(sorted(unsolved_rules.items()))
  solved_rules = dict(sorted(solved_rules.items()))

  while(len(unsolved_rules.keys()) > 3):
    newly_solved = dict()
    
    for rid, rule in unsolved_rules.items():
      solved = True
      ids = get_rule_ids(rule)

      for rules_id in ids:
        if rules_id not in solved_rules:
          solved = False
          break
      if solved:
        solved_rule = list()
        for sub_rule in rule.split("|"):
          srids = sub_rule.strip().split(" ")

          if len(srids) > 1:
            solved_rule += [m1+m2 for m1 in solved_rules[srids[0]] for m2 in solved_rules[srids[1]]]
          else:
            solved_rule += solved_rules[srids[0]]

        solved_rules[rid] = solved_rule
        newly_solved[rid] = solved_rule

    for rid, rule in newly_solved.items():
      unsolved_rules.pop(rid, None)
      solved_rules[rid] = rule

  valid_count = 0
  for msg in messages:
    valid_count += find_match(msg, False, solved_rules, 0)

  print(valid_count)
  
def find_match(msg, done_42, solved_rules, found42s):
  if len(msg) == 0 and done_42:
    return True

  matches = list()
  if not done_42:
    matches = solved_rules["42"]
  else:
    matches = solved_rules["31"]

  match_found = False
  for match in matches:
    if msg[0:len(match)] == match and (len(match) != len(msg) or done_42):
      if not done_42:
        match_found = find_match(msg[len(match):], done_42, solved_rules, found42s+1)
      elif found42s > 1:
        match_found = find_match(msg[len(match):], done_42, solved_rules, found42s-1)

      if match_found:
        return True

  if done_42:
    return False
  else:
    done_42 = True
    match_found = find_match(msg, done_42, solved_rules, found42s)
    return match_found

def get_rule_ids(rule):
  if rule.count("|") > 0:
    rule_a, rule_b = rule.split("|")

    return rule_a.strip().split(" ") + rule_b.strip().split(" ")
  else:
    return rule.split(" ")

if __name__ == '__main__':
  main()
