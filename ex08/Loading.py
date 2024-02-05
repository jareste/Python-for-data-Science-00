def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        if i+1 != total:
            print(f"\r{int((i+1)/total*100)}%|[{'='*int((i+1)/total*20 - 1)}>\
                  {' '*(19-int((i+1)/total*20))}]| {i+1}/{total}", end="")
        else:
            print(f"\r{int((i+1)/total*100)}%|[{'='*int((i+1)/total*20)}\
                  {' '*(20-int((i+1)/total*20))}]| {i+1}/{total}", end="")
        yield item
    print()
