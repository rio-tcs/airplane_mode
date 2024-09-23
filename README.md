# Airplane Mode

This repository contains my **final project** for the **Frappe Framework Certification Training**. The project demonstrates several key features of the **Frappe Framework**, including airline and airport management functionalities, custom development, report generation, and validation logic. The project serves as a showcase of my **skills and knowledge of Frappe development**.

## Project Overview

**Airplane Mode** is a custom Frappe app designed to manage various aspects of airline and airport operations. The project handles functionalities related to airlines, airplanes, flights, crew members, tickets, and airport shops. Additionally, it includes logic for managing lease contracts, generating financial reports, and sending notifications.

### Key Features:
1. **Airline and Flight Management**: 
   - Custom **DocTypes** for managing airlines, airplanes, and flights.
   - Complex logic such as gate assignment, flight validation, and handling crew and passenger management.
   
2. **Airport Shop and Lease Management**:
   - Handling leases for airport shops, including contract creation, validation, and managing payments and renewals.
   - Built-in notifications for expiring contracts and shop availability.
   
3. **Custom Reports**:
   - Financial reports such as `Revenue by Airline`, which aggregates data across airlines and flights to generate insights.
   - Other reports like `Add-On Popularity` and `Shops per Airport`, showcasing report customization and chart generation in Frappe.
   
4. **Web Forms and Notifications**:
   - Implemented web forms for user-friendly data entry, such as flight booking and shop lease forms.
   - Automated notifications for lease renewals and flight updates.

### Skills Demonstrated:

This project showcases several important aspects of **Frappe development**:
- **Custom DocTypes**: I created multiple custom DocTypes to manage data models for airlines, flights, tickets, shops, and leases, highlighting my understanding of database design within the Frappe ecosystem.
  
- **Server-Side Logic and Validations**: Using Frappe’s server-side scripting, I implemented business logic to ensure data integrity, such as flight gate assignment and validation for shop leases.
  
- **Report Building**: Developed detailed financial and operational reports using **Frappe’s report builder**, SQL queries, and chart generation, demonstrating my ability to extract and visualize business insights.

- **Custom Notifications**: I created notification systems that automatically alert users of flight and lease contract updates, demonstrating Frappe’s event-driven architecture.
  
- **Web Forms**: Developed web forms for managing flights and shop leases, providing a simple interface for external users to interact with the system.

## Installation and Setup

To install and run the project, you need to have **Frappe Framework** installed. If you don’t have it installed, please refer to the official **[Frappe Installation Guide](https://frappeframework.com/docs/user/en/installation)**.

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/rio-tcs/airplane_mode.git
cd airplane_mode
```

### 2. Install the App on Your Frappe Site

Once you’ve cloned the repository, install the app on your existing Frappe site:

```bash
bench get-app airplane_mode ./airplane_mode
bench --site [your-site-name] install-app airplane_mode
```

### 3. Start the Frappe Bench

After installing the app, start the Frappe development server:

```bash
bench start
```

Once running, you can access the site through your browser at `http://localhost:8000`.

## Running the Application

1. Log in as an administrator to explore the **Airplane Mode** features.
2. Manage airlines, airplanes, flights, crew, and tickets through custom DocTypes.
3. Utilize the **airport shop module** to manage shop leases, payments, and notifications.
4. Generate and analyze financial reports, such as **Revenue by Airline** and **Shops per Airport**.
5. Use the provided web forms for data entry related to flight bookings and shop leases.

## Credits

This project was developed by **Rio Pramana** as a final project for the **Frappe Framework Certification Training**. It serves as a demonstration of my proficiency in Frappe development, custom app creation, and advanced business logic implementation.

## License

This project is licensed under the [MIT License](LICENSE).
