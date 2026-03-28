# Use Case Diagram - Hospitality Management System

```mermaid
graph TB
    subgraph Actors
        Guest[Hotel Guest]
        FrontDesk[Front Desk Staff]
        Housekeeping[Housekeeping Staff]
        Manager[Hotel Manager]
        ITAdmin[IT Administrator]
        Finance[Finance Department]
        Marketing[Marketing Team]
        RestaurantMgr[Restaurant Manager]
    end

    subgraph SystemBoundary[HotelHub System]
        
        subgraph BookingManagement
            UC1[Search Rooms]
            UC2[Book Room]
            UC3[Cancel Booking]
            UC4[View Booking History]
        end
        
        subgraph GuestServices
            UC5[Online Check-in]
            UC6[Online Check-out]
            UC7[Request Service]
            UC8[Make Payment]
        end
        
        subgraph Operations
            UC9[Manage Housekeeping Tasks]
            UC10[Process Walk-in Check-in]
            UC11[Manage Maintenance Requests]
            UC12[Generate Reports]
        end
        
        subgraph StaffManagement
            UC13[Manage Staff Accounts]
            UC14[View Dashboard]
        end
        
        subgraph Marketing
            UC15[Manage OTA Integration]
            UC16[Create Promotions]
        end
    end

    Guest --> UC1
    Guest --> UC2
    Guest --> UC3
    Guest --> UC4
    Guest --> UC5
    Guest --> UC6
    Guest --> UC7
    Guest --> UC8
    
    FrontDesk --> UC9
    FrontDesk --> UC10
    FrontDesk --> UC7
    FrontDesk --> UC8
    
    Housekeeping --> UC9
    Housekeeping --> UC11
    
    Manager --> UC12
    Manager --> UC14
    Manager --> UC16
    
    ITAdmin --> UC13
    ITAdmin --> UC14
    
    Finance --> UC12
    Finance --> UC8
    
    Marketing --> UC15
    Marketing --> UC16
    
    RestaurantMgr --> UC7
    
    UC2 -.->|<<include>>| UC1
    UC5 -.->|<<include>>| UC8
    UC6 -.->|<<include>>| UC8
    UC7 -.->|<<extend>>| UC11
