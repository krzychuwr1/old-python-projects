import traceback


def read_exception(e):
    print(e)
    print("Do you want to read the traceback of the error? Write 'yes' to read the cause, anything else to quit.")
    reply = input()
    if reply == 'yes':
        traceback.print_exc()
