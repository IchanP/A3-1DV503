from view.ui import ui

def handle_forward_pagination(view: ui, offset, is_next_page, amount):
    if is_next_page:
        return offset + amount 
    else:
        view.print_header("No next page")
        return offset  

def handle_backwards_pagination(view: ui, offset, amount):
    if offset-amount< 0:
        view.print_header("No Previous Page")
        return 0
    else:
        return offset-2