def string_with_arrows(text, pos_start, pos_end):
    result = ''

    # Calculate indices
    inx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', inx_start + 1)
    if idx_end < 0: idx_end = len(text)

    #generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        #calculate line columns
        line_content = text[inx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line_content) - 1

        #Append to result

        result += line_content + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)

        #recalculate indices
        inx_start = idx_end
        idx_end = text.find('\n', inx_start + 1)
        if idx_end < 0: idx_end = len(text)

    return result.replace('\t', '')