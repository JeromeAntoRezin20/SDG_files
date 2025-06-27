from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date

app = FastAPI()


DATABASE_URL = "sqlite:///./service_center.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ServiceBooking(Base):
    __tablename__ = "service_bookings"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    vehicle_number = Column(String, nullable=False)
    service_type = Column(String, nullable=False)
    booking_date = Column(Date, nullable=False)


Base.metadata.create_all(bind=engine)


class ServiceBookingCreate(BaseModel):
    customer_name: str = Field(..., example ='Test User')
    vehicle_number: str = Field(..., example = 'TN051234')
    service_type: str = Field(..., example = 'Oil change')
    booking_date: date = Field(..., example = '2025-06-05')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bookings/", status_code=status.HTTP_201_CREATED)
def create_booking(booking: ServiceBookingCreate, db: SessionLocal = Depends(get_db)):
    if booking.booking_date < date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Booking date cannot be in the past."
        )
    new_booking = ServiceBooking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@app.get("/bookings/", status_code=status.HTTP_200_OK)
def get_all_bookings(db: SessionLocal = Depends(get_db)):
    bookings = db.query(ServiceBooking).all()
    return bookings

@app.get("/bookings/{booking_id}", status_code=status.HTTP_200_OK)
def get_booking_by_id(booking_id: int, db: SessionLocal = Depends(get_db)):
    booking = db.query(ServiceBooking).filter(ServiceBooking.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found."
        )
    return booking

@app.put("/bookings/{booking_id}", status_code=status.HTTP_200_OK)
def update_booking(booking_id: int, updated_booking: ServiceBookingCreate, db: SessionLocal = Depends(get_db)):
    booking = db.query(ServiceBooking).filter(ServiceBooking.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found."
        )
    if updated_booking.booking_date < date.today():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Booking date cannot be in the past."
        )
    for key, value in updated_booking.dict().items():
        setattr(booking, key, value)
    db.commit()
    db.refresh(booking)
    return booking

@app.delete("/bookings/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(booking_id: int, db: SessionLocal = Depends(get_db)):
    booking = db.query(ServiceBooking).filter(ServiceBooking.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found."
        )
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully."}

