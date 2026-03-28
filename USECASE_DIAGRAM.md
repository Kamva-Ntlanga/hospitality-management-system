# Use Case Diagram - Hospitality Management System

```mermaid
graph TB
    subgraph Actors["<b>ACTORS</b>"]
        direction LR
        Guest["🏨 Hotel Guest"]
        FrontDesk["📋 Front Desk Staff"]
        Housekeeping["🧹 Housekeeping Staff"]
        Manager["📊 Hotel Manager"]
        ITAdmin["💻 IT Administrator"]
        Finance["💰 Finance Department"]
        Marketing["📢 Marketing Team"]
        RestaurantMgr["🍽️ Restaurant Manager"]
    end

    subgraph SystemBoundary["<b>HOTELHUB SYSTEM BOUNDARY</b>"]
        
        subgraph BookingMgmt["📅 BOOKING MANAGEMENT"]
            UC1["🔍 Search Rooms"]
            UC2["📝 Book Room"]
            UC3["❌ Cancel Booking"]
            UC4["📜 View Booking History"]
        end
        
        subgraph GuestServices["👤 GUEST SERVICES"]
            UC5["✅ Online Check-in"]
            UC6["🚪 Online Check-out"]
            UC7["🛎️ Request Service"]
            UC8["💳 Make Payment"]
            UC17["👤 Manage Guest Profile"]
        end
        
        subgraph Operations["⚙️ OPERATIONS"]
            UC9["🧹 Manage Housekeeping Tasks"]
            UC10["🚶 Process Walk-in Check-in"]
            UC11["🔧 Manage Maintenance Requests"]
            UC12["📈 Generate Reports"]
        end
        
        subgraph AdminMgmt["👔 ADMINISTRATION"]
            UC13["👥 Manage Staff Accounts"]
            UC14["📊 View Dashboard"]
            UC15["🔌 Manage OTA Integration"]
            UC16["🎯 Create Promotions"]
            UC18["🔔 Manage Notifications"]
        end
    end

    %% Guest Connections
    Guest --> UC1
    Guest --> UC2
    Guest --> UC3
    Guest --> UC4
    Guest --> UC5
    Guest --> UC6
    Guest --> UC7
    Guest --> UC8
    Guest --> UC17
    
    %% Front Desk Connections
    FrontDesk --> UC7
    FrontDesk --> UC8
    FrontDesk --> UC9
    FrontDesk --> UC10
    FrontDesk --> UC14
    FrontDesk --> UC17
    
    %% Housekeeping Connections
    Housekeeping --> UC9
    Housekeeping --> UC11
    
    %% Manager Connections
    Manager --> UC12
    Manager --> UC14
    Manager --> UC16
    
    %% IT Admin Connections
    ITAdmin --> UC13
    ITAdmin --> UC14
    ITAdmin --> UC18
    
    %% Finance Connections
    Finance --> UC8
    Finance --> UC12
    
    %% Marketing Connections
    Marketing --> UC15
    Marketing --> UC16
    
    %% Restaurant Manager Connections
    RestaurantMgr --> UC7
    
    %% Include Relationships (mandatory dependencies)
    UC2 -.->|<<include>>| UC1
    UC5 -.->|<<include>>| UC8
    UC6 -.->|<<include>>| UC8
    
    %% Extend Relationships (optional extensions)
    UC7 -.->|<<extend>>| UC11
    UC2 -.->|<<extend>>| UC18
    UC5 -.->|<<extend>>| UC18
    UC7 -.->|<<extend>>| UC18
