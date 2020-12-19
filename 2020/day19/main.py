import sys
import regex as re
from ast import literal_eval
from tqdm import tqdm

def main():
  unsolved_rules = dict()
  solved_rules = dict()
  messages = list()

  with open("input.txt") as f:
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

  while(len(unsolved_rules.keys()) > 0):
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

  combinations = solved_rules["0"]
  valid_count = 0

  for msg in tqdm(messages):
    valid_count += msg in combinations

  print(valid_count)

def get_rule_ids(rule):
  if rule.count("|") > 0:
    rule_a, rule_b = rule.split("|")

    return rule_a.strip().split(" ") + rule_b.strip().split(" ")
  else:
    return rule.split(" ")



if __name__ == '__main__':
  main()
