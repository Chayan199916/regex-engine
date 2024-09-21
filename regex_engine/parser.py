from typing import List


def parse(regex: str) -> List[str]:
    j = 0
    pattern = []
    while j < len(regex):
        if regex[j: j + 2] in ("\\d", "\\w"):
            pattern.append(regex[j:j+2])
            j += 2
        elif regex[j: j + 2] == "[^" and "]" in regex[j:]:
            end = regex.index("]", j) + 1
            pattern.append(regex[j:end])
            j = end
        elif regex[j] == "[" and "]" in regex[j:]:
            end = regex.index("]", j) + 1
            pattern.append(regex[j:end])
            j = end
        else:
            pattern.append(regex[j])
            j += 1
    return pattern
