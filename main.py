import os
from module.viewer import Viewer
import logging
from module import parser


def logo():
    title = """
    ######  #######    #     #                                       #     #                               
    #     # #          #     # ######   ##   #####  ###### #####     #     # # ###### #    # ###### #####  
    #     # #          #     # #       #  #  #    # #      #    #    #     # # #      #    # #      #    # 
    ######  #####      ####### #####  #    # #    # #####  #    #    #     # # #####  #    # #####  #    # 
    #       #          #     # #      ###### #    # #      #####      #   #  # #      # ## # #      #####  
    #       #          #     # #      #    # #    # #      #   #       # #   # #      ##  ## #      #   #  
    #       #######    #     # ###### #    # #####  ###### #    #       #    # ###### #    # ###### #    # 
    """
    print("=" * 110)
    print(title)
    print("=" * 110)


def set_env():
    temp_dir = './temp'
    if not os.path.exists(temp_dir) or not os.path.isdir(temp_dir):
        os.mkdir(temp_dir)
    os.environ['APP_TEMP_DIR'] = temp_dir


def main():
    logo()
    logging.basicConfig(filename='./log/myapp.log', level=logging.INFO)
    logging.info("started")
    set_env()
    app = Viewer()
    app.mainloop()


if __name__ == '__main__':
    # main()
    parser.convert('temp/96a6c4c6-02e1-4023-9205-ef6a33baba45.exe')
