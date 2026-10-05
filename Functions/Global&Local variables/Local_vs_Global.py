# Global variable
counter = 0
def show_local():
    # Local variable with the same name
    counter = 10
    print("Local counter:", counter)
show_local()
# Global variable
print("Global counter:", counter)
#output:
Local counter: 10
Global counter: 0

