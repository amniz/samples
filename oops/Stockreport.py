# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:program to create a Stockreport
import json


class StockReport:
    # function to calculate the Stock_value and total Stock value and prints it
    @staticmethod
    def stock():
        with open('stock.json', 'r') as file:
            file_content = file.read()  # this function is used to read json file
            file.close()  # closing the file
        main_file = json.loads(file_content)  # using loads() convert json data into python data
        total_share_value = 0
        for i in range(len(main_file['stock'])):
            # print(main_file['stock'][i], end="")
            number_of_share = main_file['stock'][i]['number of share']  # getting the number of share for each share
            share_price = main_file['stock'][i]['share price']  # getting the share price for each share
            share_value = share_price * number_of_share  # calculating the share value
            total_share_value += share_value  # calculating the total share value
            print("share value of ", main_file['stock'][i]['stock name'], "=", share_value)
        print("total share value ", total_share_value)


if __name__ == '__main__':
    StockReport.stock()
