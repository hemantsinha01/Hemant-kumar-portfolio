result = []
    visitedFrom = [-1] * len(edges)
    for startCell in range(0, len(edges)):
        cells = []
        cell = startCell
        while cell > -1 and visitedFrom[cell] == -1:
            visitedFrom[cell] = startCell
            cells.append(cell)
            cell = edges[cell]
        if cell > -1 and visitedFrom[cell] == startCell:
            cells_idx = cells.index(cell)
            cells = cells[cells_idx:]
            if len(cells) > len(result):
                result = cells

    return result, len(result)