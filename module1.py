worker_data = [[], []]

def show_workers():
    print("Current data:")
    print("Worker   | Year")
    print("_" * 20)
    for i in range(len(worker_data[0])):
        print(f"{worker_data[0][i]:<8} - {worker_data[1][i]}")
    print("_" * 20)

def add_workers(amount):
    for _ in range(amount):
        try:
            name = str(input("Enter Name: "))
            year = int(input("Enter Year: "))
            worker_data[0].append(name)
            worker_data[1].append(year)
            print("New worker added:")
            print(f"{name:<8} - {year}")
            print("_" * 25)
        except:
            print("Error")

def average_age():
    from datetime import datetime
    current_year = datetime.now().year
    years = [int(y) for y in worker_data[1]]
    avg_age = sum(current_year - y for y in years) / len(years)
    print(f"Average age: {avg_age:.1f} years")

def list_oldest_youngest():
    from datetime import datetime
    current_year = datetime.now().year

    combined = list(zip(worker_data[0], worker_data[1]))
    combined.sort(key=get_year)
    combined.sort(key=get_year)

    print("\n10 youngest workers:")
    for name, year in combined[-10:]:
        print(f"{name:<8} - {year}")

    print("\n10 oldest workers:")
    for name, year in combined[:10]:
        print(f"{name:<8} - {year}")

    print("_" * 25)
def get_year(z):
    return int(z[1])
def find_by_age(target_age):
    from datetime import datetime
    current_year = datetime.now().year
    target_year = current_year - target_age
    found = False
    for i in range(len(worker_data[0])):
        if int(worker_data[1][i]) == target_year:
            print(f"Found: {worker_data[0][i]} - {worker_data[1][i]}")
            found = True
    if not found:
        print("No employee found with that age.")

def remove_worker(name):
    if name in worker_data[0]:
        index = worker_data[0].index(name)
        removed_name = worker_data[0].pop(index)
        removed_year = worker_data[1].pop(index)
        print(f"Removed: {removed_name} - {removed_year}")
    else:
        print("Worker not found.")