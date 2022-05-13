from email import message
import modules, utils

from utils import colors, messages

""" Command handeling for FiveTux """

def commands():

    try:

        utils.clear_with_banner()

        while True:

            try:

                user_data = input(f"[ {colors.yellow}{colors.bold}FiveTux{colors.unbold}{colors.white} ] {messages.arrow}  ")

                if 'clear' in user_data.lower():
                    utils.clear_with_banner()

                elif 'info' in user_data.lower():
                    utils.basic_help()

                elif 'modules' in user_data.lower():
                    utils.modules_show()

                elif 'get-ip' in user_data.lower():
                    cfxcode = user_data.split(' ')[1]
                    modules.receive_ip(cfxcode)
                    
                elif 'get-handles' in user_data.lower():
                    modules.get_handles()

            

                elif 'exit' in user_data.lower() or 'quit' in user_data.lower():
                    exit(f"\n{messages.title} Ses en anden god gang ;')\n")

            except TypeError:
                print(f"\n{messages.title} Failed..- Read modules again!\n")

    except KeyboardInterrupt:
        exit()
