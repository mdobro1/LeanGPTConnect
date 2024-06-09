# Car Rental System

This README provides an overview of the Car Rental System classes as represented in the class diagram and includes the generated C# code for each class.

## Class Diagram

The class diagram showcases the relationships and operations among the following classes:

- `CarRentalSystem`
- `Customer`
- `Transaction`
- `Car`
- `ErrorHandler`
- `SecurityManager`
- `AuthenticationManager`
- `MessageHandler`
- `DataManager`

## C# Code

Here is the generated C# code based on the class diagram:

### CarRentalSystem.cs

```csharp
using System;
using System.Collections.Generic;

public class CarRentalSystem
{
    public List<Customer> customers;
    public List<Car> availableCars;
    public List<Car> rentedCars;
    public List<Transaction> transactions;

    public void registerCustomer() { }
    public void rentCar() { }
    public void returnCar() { }
    public void listAvailableCars() { }
    public void listRentedCars() { }
    public void listCustomerTransactions() { }
}
```

### Customer.cs

```csharp
using System;
using System.Collections.Generic;

public class Customer
{
    public string id;
    public string name;
    public string phoneNumber;
    public string address;
    public string email;
    public List<Car> rentedCars;

    public void rentCar() { }
    public void returnCar() { }
    public void listRentedCars() { }
    public string serialize(DataType dataType) { return string.Empty; }
    public void deserialize(string data, DataType dataType) { }
}
```

### Transaction.cs

```csharp
using System;

public class Transaction
{
    public string id;
    public Customer customer;
    public Car car;
    public DateTime rentalDate;
    public DateTime returnDate;
    public double totalPrice;

    public double calculateTotalPrice() { return 0.0; }
    public string serialize(DataType dataType) { return string.Empty; }
    public void deserialize(string data, DataType dataType) { }
}
```

### Car.cs

```csharp
using System;

public class Car
{
    public string id;
    public string make;
    public string model;
    public int year;
    public double dailyPrice;
    public bool rented;

    public void rent() { }
    public void return() { }
    public string serialize(DataType dataType) { return string.Empty; }
    public void deserialize(string data, DataType dataType) { }
}
```

### ErrorHandler.cs

```csharp
using System;

public class ErrorHandler
{
    public void handleError(Exception exception) { }
}
```

### SecurityManager.cs

```csharp
using System;

public class SecurityManager
{
    public string encrypt(string data) { return string.Empty; }
    public string decrypt(string data) { return string.Empty; }
    public bool authorize(User user, string permission) { return true; }
}
```

### AuthenticationManager.cs

```csharp
using System;

public class AuthenticationManager
{
    public bool login(string username, string password) { return true; }
    public void logout() { }
}
```

### MessageHandler.cs

```csharp
using System;

public class MessageHandler
{
    public void log(string message) { }
    public void showMessage(string message) { }
}
```

### DataManager.cs

```csharp
using System;

public class DataManager
{
    public void readData(EntityType entityType, DataType dataType) { }
    public void writeData(EntityType entityType, DataType dataType) { }
}
```

### EntityType.cs

```csharp
public enum EntityType
{
    CUSTOMER,
    CAR,
    TRANSACTION
}
```

### DataType.cs

```csharp
public enum DataType
{
    CSV,
    JSON
}
```

## Usage

These classes form the foundation of the Car Rental System. Each class is associated with specific responsibilities, and the methods provided offer essential functionalities for managing the car rental operations.

### Example

An instance of the `CarRentalSystem` class can be used to register customers, handle car rentals, and manage transactions.

```csharp
CarRentalSystem system = new CarRentalSystem();
system.registerCustomer();
system.rentCar();
system.returnCar();
system.listAvailableCars();
system.listRentedCars();
system.listCustomerTransactions();
```

This example demonstrates how you might interact with the Car Rental System to perform common operations.