from core.app_manager import init_day_page, select_day

selected_day, module = select_day(__file__.split('.')[0].split("_")[-1])
init_day_page(selected_day, module)
