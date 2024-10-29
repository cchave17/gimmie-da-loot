import re 

def reference_filtering(answer, references, field="id"):
  if not references or len(references) == 0:
      return references

  ids=[]
  match = re.search(r"(usedIds: (.*))", answer)
  if match and match.group(2):
    ids=[x.strip().lower() for x in match.group(2).split(',')]

  filtered=[]
  for reference in references:
    if str(reference[field]).lower() in ids:
      del reference[field]
      filtered.append(reference)

  return filtered

def reference_filtering_location(answer, references):
    if not references or len(references) == 0:
        return references

    classes = []
    match = re.search(r"(usedClassNames: (.*))", answer)
    if match and match.group(2):
        classes = [x.strip().lower() for x in match.group(2).split(",")]

    filtered = []
    for reference in references:
        if reference["name"].lower() in classes:
            filtered.append(reference)

    return filtered

def reference_filtering_scheduling(answer, references):
    if not references or len(references) == 0:
        return references

    ids = []
    match = re.search(r"(usedIds: (.*))", answer)
    if match and match.group(2):
        ids = [x.strip().lower() for x in match.group(2).split(",")]

    filtered = []
    for reference in references:
        if reference["id"].lower() in ids:
            del reference["id"]
            filtered.append(reference)

    return filtered
