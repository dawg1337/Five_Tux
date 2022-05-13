from utils import messages

def basic_help():
    print(
        f"""
{messages.title} clear              Clears your screen.
{messages.title} modules            shows available modules.
{messages.title} info               information.
        """)


def modules_show():
    print(
        f"""
{messages.title} get-ip            Receive Server IP Adress Using CFX ID.
{messages.title} get-handles       Shows current blacklisted server handles.
        """)
