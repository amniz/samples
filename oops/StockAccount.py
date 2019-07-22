class Stock:
    total_number_shares=1000
    value_per_share=1678
    # create a new account from file
    def StockAccount(file_name):
        try:
            file=open(file_name,"r")  # opening the file in the read mode
        except FileNotFoundError as e:
            print("file not found",e)
        file_contents=file.read()
        stock_object=Stock()
    @staticmethod
    def valueOf():
        return

