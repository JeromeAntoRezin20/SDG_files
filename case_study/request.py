import requests

BASE_URL = "http://127.0.0.1:8089"

def create_booking(customer_name, vehicle_number, service_type, booking_date):
    url = f"{BASE_URL}/bookings/"
    booking_data = {
        "customer_name": customer_name,
        "vehicle_number": vehicle_number,
        "service_type": service_type,
        "booking_date": booking_date
    }
    try:
        response = requests.post(url, json=booking_data)
        response.raise_for_status() 
        print("Booking created successfully:", response.json())
    except requests.exceptions.RequestException as err:
        print(f"Error creating booking: {err}")

def get_all_bookings():
    url = f"{BASE_URL}/bookings/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("All bookings:", response.json())
    except requests.exceptions.RequestException as err:
        print(f"Error fetching bookings: {err}")

def get_booking_by_id(booking_id):
    url = f"{BASE_URL}/bookings/{booking_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Booking {booking_id} details:", response.json())
    except requests.exceptions.RequestException as err:
        print(f"Error fetching booking {booking_id}: {err}")

def update_booking(booking_id, customer_name, vehicle_number, service_type, booking_date):
    url = f"{BASE_URL}/bookings/{booking_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        current_booking = response.json()

        updated_data = {
            "customer_name": customer_name if customer_name.strip() else current_booking["customer_name"],
            "vehicle_number": vehicle_number if vehicle_number.strip() else current_booking["vehicle_number"],
            "service_type": service_type if service_type.strip() else current_booking["service_type"],
            "booking_date": booking_date if booking_date.strip() else current_booking["booking_date"]
        }

        response = requests.put(url, json=updated_data)
        response.raise_for_status()
        print(f"Booking {booking_id} updated successfully:", response.json())
    except requests.exceptions.RequestException as err:
        print(f"Error updating booking {booking_id}: {err}")

def delete_booking(booking_id):
    url = f"{BASE_URL}/bookings/{booking_id}"
    try:
        response = requests.delete(url)
        if response.status_code == 204:
            print(f"Booking {booking_id} deleted successfully.")
        else:
            print(f"Failed to delete booking {booking_id}: {response.json()}")
    except requests.exceptions.RequestException as err:
        print(f"Error deleting booking {booking_id}: {err}")

def menu():
    while True:
        print("\nVehicle Service Center Management System")
        print("1. Create a new booking")
        print("2. View all bookings")
        print("3. Fetch booking by ID")
        print("4. Update booking")
        print("5. Delete booking")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                customer_name = input("Enter customer name: ")
                vehicle_number = input("Enter vehicle number: ")
                service_type = input("Enter service type: ")
                booking_date = input("Enter booking date (YYYY-MM-DD): ")
                create_booking(customer_name, vehicle_number, service_type, booking_date)

            elif choice == "2":
                get_all_bookings()

            elif choice == "3":
                booking_id = int(input("Enter booking ID: "))
                get_booking_by_id(booking_id)

            elif choice == "4":
                booking_id = int(input("Enter booking ID: "))
                customer_name = input("Enter customer name: ")
                vehicle_number = input("Enter vehicle number: ")
                service_type = input("Enter service type: ")
                booking_date = input("Enter booking date (YYYY-MM-DD): ")
                update_booking(booking_id, customer_name, vehicle_number, service_type, booking_date)

            elif choice == "5":
                booking_id = int(input("Enter booking ID: "))
                delete_booking(booking_id)

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    menu()
