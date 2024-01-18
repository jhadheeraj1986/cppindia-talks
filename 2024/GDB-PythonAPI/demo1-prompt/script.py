import gdb
import time

def my_prompt_hook(current_prompt):
    now_str = time.strftime("%H:%M:%S")

    try:
        frame = gdb.selected_frame().name()
    except gdb.error:
        frame = "(no frame)"

    return f"[{now_str}] {frame} >"

gdb.prompt_hook = my_prompt_hook