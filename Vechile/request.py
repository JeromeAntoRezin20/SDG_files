import requests

BASE_URL = "http://127.0.0.1:8060"  # Replace with your FastAPI server URL

def create_booking(customer_name, vehicle_number, service_type, booking_date):
    url = f"{BASE_URL}/bookings/"
    booking_data = {
        "customer_name": customer_name,
        "vehicle_number": vehicle_number,
        "service_type": service_type,
        "booking_date": booking_date
    }
    response = requests.post(url, json=booking_data)
    if response.status_code == 201:
        print("Booking created successfully:", response.json())
    else:
        print("Failed to create booking:", response.json())

def get_all_bookings():
    url = f"{BASE_URL}/bookings/"
    response = requests.get(url)
    if response.status_code == 200:
        print("All bookings:", response.json())
    else:
        print("Failed to fetch bookings:", response.json())

def get_booking_by_id(booking_id):
    url = f"{BASE_URL}/bookings/{booking_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Booking {booking_id} details:", response.json())
    else:
        print(f"Failed to fetch booking {booking_id}:", response.json())

def update_booking(booking_id, customer_name, vehicle_number, service_type, booking_date):
    url = f"{BASE_URL}/bookings/{booking_id}"

    # Fetch the current booking details
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch booking {booking_id}: {response.json()}")
        return

    current_booking = response.json()

    # Use current values if the user provides no input
    updated_data = {
        "customer_name": customer_name if customer_name.strip() else current_booking["customer_name"],
        "vehicle_number": vehicle_number if vehicle_number.strip() else current_booking["vehicle_number"],
        "service_type": service_type if service_type.strip() else current_booking["service_type"],
        "booking_date": booking_date if booking_date.strip() else current_booking["booking_date"]
    }

    # Send the update request
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print(f"Booking {booking_id} updated successfully:", response.json())
    else:
        print(f"Failed to update booking {booking_id}:", response.json())

def delete_booking(booking_id):
    url = f"{BASE_URL}/bookings/{booking_id}"
    response = requests.delete(url)
    if response.status_code == 204:
        print(f"Booking {booking_id} deleted successfully.")
    else:
        print(f"Failed to delete booking {booking_id}:", response.json())

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

# Run the menu
if __name__ == "__main__":
    menu()
