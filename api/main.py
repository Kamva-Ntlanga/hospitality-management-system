from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import List

from factories.repository_factory import RepositoryFactory, StorageType
from services.room_service import RoomService
from services.guest_service import GuestService
from services.booking_service import BookingService
from services.housekeeping_service import HousekeepingService
from services.service_request_service import ServiceRequestService
from api.room_routes import router as room_router
from api.guest_routes import router as guest_router
from api.booking_routes import router as booking_router
from api.housekeeping_routes import router as housekeeping_router
from api.service_request_routes import router as service_request_router

# Global service instances
room_service = None
guest_service = None
booking_service = None
housekeeping_service = None
service_request_service = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup - initialize services with in-memory repositories
    global room_service, guest_service, booking_service, housekeeping_service, service_request_service
    
    room_repo = RepositoryFactory.create_room_repository(StorageType.MEMORY)
    guest_repo = RepositoryFactory.create_guest_repository(StorageType.MEMORY)
    booking_repo = RepositoryFactory.create_booking_repository(StorageType.MEMORY)
    service_request_repo = RepositoryFactory.create_service_request_repository(StorageType.MEMORY)
    
    room_service = RoomService(room_repo)
    guest_service = GuestService(guest_repo)
    booking_service = BookingService(booking_repo, room_repo, guest_repo)
    housekeeping_service = HousekeepingService()
    service_request_service = ServiceRequestService(service_request_repo)
    
    yield
    
    # Shutdown - cleanup if needed
    pass

# Create FastAPI app
app = FastAPI(
    title="HotelHub API",
    description="REST API for Hospitality Management System",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(room_router, prefix="/api/rooms", tags=["Rooms"])
app.include_router(guest_router, prefix="/api/guests", tags=["Guests"])
app.include_router(booking_router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(housekeeping_router, prefix="/api/housekeeping", tags=["Housekeeping"])
app.include_router(service_request_router, prefix="/api/service-requests", tags=["Service Requests"])

@app.get("/")
async def root():
    return {"message": "Welcome to HotelHub API", "docs": "/docs"}

# Dependency functions to get services
def get_room_service() -> RoomService:
    return room_service

def get_guest_service() -> GuestService:
    return guest_service

def get_booking_service() -> BookingService:
    return booking_service

def get_housekeeping_service() -> HousekeepingService:
    return housekeeping_service

def get_service_request_service() -> ServiceRequestService:
    return service_request_service