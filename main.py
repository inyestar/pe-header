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


def main():
    logo()
    logging.basicConfig(filename='./log/myapp.log', level=logging.INFO)
    logging.info("started")
    app = Viewer()
    #app.mainloop()


if __name__ == '__main__':
    main()

