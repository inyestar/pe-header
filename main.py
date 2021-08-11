import os

from module.viewer import Viewer
import logging


def logo():
    logo ="""
    ######  #######    #     #                                       #     #                               
    #     # #          #     # ######   ##   #####  ###### #####     #     # # ###### #    # ###### #####  
    #     # #          #     # #       #  #  #    # #      #    #    #     # # #      #    # #      #    # 
    ######  #####      ####### #####  #    # #    # #####  #    #    #     # # #####  #    # #####  #    # 
    #       #          #     # #      ###### #    # #      #####      #   #  # #      # ## # #      #####  
    #       #          #     # #      #    # #    # #      #   #       # #   # #      ##  ## #      #   #  
    #       #######    #     # ###### #    # #####  ###### #    #       #    # ###### #    # ###### #    # 
    """
    print("=" * 110)
    print(logo)
    print("=" * 110)


def set_env():
    os.environ['APP_TEMP_DIR'] = './temp'


def main():
    logo()
    logging.basicConfig(filename='./log/myapp.log', level=logging.INFO)
    logging.info("started")
    set_env()
    app = Viewer()
    app.mainloop()


if __name__ == '__main__':
    main()

