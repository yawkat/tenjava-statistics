To download all repos to the `repos/` folder, run `./download.py`. If you want to pull any changes run `./pull.py`.

To collect cloc stats, install cloc and run `./collect_cloc_stats.py`. This will save statistics in the `cloc.json` file.

To view stats, run `./list_cloc.py <language> <type> [reverse]`, for example `./list_cloc.py Java code`. Values are sorted with the most lines of code at the bottom (or top if `reverse` is specified)
