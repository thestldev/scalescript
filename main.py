import os

import full_json_generate
import json
import colorama

CACHED_TABLE = {}
CACHED_RESULTS = {}


sys_def_pref = colorama.Back.GREEN + colorama.Fore.BLACK
sys_err_pref = colorama.Back.RED + colorama.Fore.WHITE
sys_war_pref = colorama.Back.YELLOW + colorama.Fore.BLACK


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# msg_type can be: default, error, warning
def sys_msg(msg: str | list | tuple, msg_type: str = "default") -> None:
    pref = sys_def_pref

    match msg_type:
        case "error":
            pref = sys_err_pref
        case "warning":
            pref = sys_war_pref
        case _:
            pass

    if isinstance(msg, (list, tuple)):
        for line in msg:
            print(pref + line + colorama.Style.RESET_ALL)
    else:
        print(pref + msg + colorama.Style.RESET_ALL)


def sys_input(msg: str, do_clear_styles: bool = False) -> str:
    if do_clear_styles:
        return input(sys_def_pref + msg + colorama.Style.RESET_ALL)
    return input(sys_def_pref + msg)


def clear_style():
    print(colorama.Style.RESET_ALL)


def cache_table_from_file():
    global CACHED_TABLE, CACHED_RESULTS
    try:
        with open("fl_scales.json", "r") as f:
            CACHED_TABLE = json.loads(f.read())

    except FileNotFoundError:
        full_json_generate.main()
        cache_table_from_file()

    try:
        with open("results.json", "r") as f:
            CACHED_RESULTS = json.loads(f.read())
    except FileNotFoundError:
        pass


def dump_results():
    with open("results.json", "w") as f:
        json.dump(CACHED_RESULTS, f, indent=2, ensure_ascii=False)


def clear_cache():
    global CACHED_TABLE, CACHED_RESULTS
    CACHED_TABLE = {}
    CACHED_RESULTS = {}
    dump_results()


def help_menu():
    pass


def main():
    clear()
    cache_add = sys_input("Enter 4 notes(separate it by a comma): ", True)

    if cache_add not in CACHED_RESULTS:
        notes = cache_add.split(",")

        tables = []

        for index, note in enumerate(notes):
            note = note.strip()
            tables.append(CACHED_TABLE[note])

        for index, table in enumerate(tables):
            tables[index] = set(table)

        intersection = set.intersection(*tables)

        CACHED_RESULTS[cache_add] = list(intersection)

        # sys_msg(CACHED_RESULTS[cache_add])
        #
        # sys_input("Press enter to continue...")
        # clear()
        # return

    sys_msg(CACHED_RESULTS[cache_add])
    sys_input("Press enter to continue...")
    clear()

    return


def lobby():
    clear()

    sys_msg(["[     Scale Finder    ]",
             "| Enter work mode:    |",
             "| — 0. Exit           |",
             "| — 1. Search         |",
             "| — 2. Clear cache    |",
             "| - 3. Debug info     |",
             ])
    mode = int(sys_input("| — >> "))

    if mode == 0:
        clear()
        sys_input("Bye! Press enter to exit...")

    elif mode == 1:
        main()
        lobby()
    elif mode == 2:
        clear_cache()
        sys_msg("Cleared!")
        sys_input("Press enter to continue...")
        lobby()
    elif mode == 3:
        clear()
        sys_msg(f"{CACHED_TABLE=}")
        sys_msg(f"{CACHED_RESULTS=}")
        sys_input("Press enter to continue...")
        lobby()


if __name__ == "__main__":
    cache_table_from_file()
    lobby()
    clear_style()
    dump_results()
