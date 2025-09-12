def book_seat(total_seats, booked_seats, seat_to_book):
    if seat_to_book < 1 or seat_to_book > total_seats:
        return "Invalid seat number"
    if seat_to_book in booked_seats:
        return f"Seat {seat_to_book} is already booked"
    booked_seats.append(seat_to_book)
    return f"Seat {seat_to_book} booked successfully"

def cancel_seat(booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
        return f"Seat {seat_to_cancel} cancellation successful"
    else:
        return f"Seat {seat_to_cancel} is not booked"
    
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

total_seats = 10
booked_seats = [2, 5, 7]
seat_to_book = 3
seat_to_cancel = 5

book_seat(total_seats, booked_seats, seat_to_book)
cancel_seat(booked_seats, seat_to_cancel)

print("Available seats :", available_seats(total_seats, booked_seats))
