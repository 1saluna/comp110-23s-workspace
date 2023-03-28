"""Value exists."""

__author__: "730572303"

def value_exists(value: dict[str, int], elem: int) -> bool:
    exists: bool = False
    for i in value: 
        if value[i] == elem:
            exists = True
    return exists
