def row_col_select(cell_index):
    row_number = cell_index // 9
    col_number = cell_index % 9

     
    row_indices = [row_number * 9 + i for i in range(9)]
    col_indices = [col_number + 9 * i for i in range(9)]

     
    block_row = row_number // 3
    block_col = col_number // 3
    block_indices = []
    for r in range(3):
        for c in range(3):
            block_index = (block_row * 3 + r) * 9 + (block_col * 3 + c)
            block_indices.append(block_index)

    return row_indices, col_indices, block_indices

def is_puzzle_incomplete(all_cells):
    return any(c.text().strip() == "" for c in all_cells)

     


     

     
     
     
    




     
     
    
     
 
