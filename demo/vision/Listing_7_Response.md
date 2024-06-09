# Car Rental System

This document contains the C# implementation for the Car Rental System based on the provided class diagram. The class diagram illustrates the structure and interactions between different classes in the system.

## Class Diagram

![Car Rental System Class Diagram](CarRentalSystem.jpg)

## Implementation

```csharp
// ErrorHandler.cs
public class ErrorHandler
{
    public void HandleError(Exception exception)
    {
        // Handle the exception
    }
}

// SecurityManager.cs
public class SecurityManager
{
    public string Encrypt(string data)
    {
        // Implementation for encryption
    }

    public string Decrypt(string data)
    {
        // Implementation for decryption
    }

    public bool Authorize(string user, string permission)
    {
        // Implementation for authorization
    }
}

// AuthenticationManager.cs
public class AuthenticationManager
{
    public bool Login(string username, string password)
    {
        // Implementation for login
    }

    public void Logout()
    {
        // Implementation for logout
    }
}

// MessageHandler.cs
public class MessageHandler
{
    public void Log(string message)
    {
        // Implementation for logging
    }

    public void ShowMessage(string message)
    {
        // Implementation for showing message
    }
}

// DataManager.cs
public enum EntityType
{
    CUSTOMER,
    CAR,
    TRANSACTION
}

public enum DataType
{
    CSV,
    JSON
}

public class DataManager
{
    public void ReadData(EntityType entityType, DataType dataType)
    {
        // Implementation for reading data
    }

    public void WriteData(EntityType entityType, DataType dataType)
    {
        // Implementation for writing data
    }
}

// CarRentalSystem.cs
public class CarRentalSystem
{
    public List<Customer> Customers { get; set; }
    public List<Car> AvailableCars { get; set; }
    public List<Car> RentedCars { get; set; }
    public List<Transaction> Transactions { get; set; }

    public void RegisterCustomer()
    {
        // Implementation for registering customer
    }

    public void RentCar()
    {
        // Implementation for renting car
    }

    public void ReturnCar()
    {
        // Implementation for returning car
    }

    public void ListAvailableCars()
    {
        // Implementation for listing available cars
    }

    public void ListRentedCars()
    {
        // Implementation for listing rented cars
    }

    public void ListCustomerTransactions()
    {
        // Implementation for listing customer transactions
    }
}

// Customer.cs
public class Customer
{
    public string Id { get; set; }
    public string Name { get; set; }
    public string PhoneNumber { get; set; }
    public string Address { get; set; }
    public string Email { get; set; }
    public List<Car> RentedCars { get; set; }

    public void RentCar()
    {
        // Implementation for renting a car
    }

    public void ReturnCar()
    {
        // Implementation for returning a car
    }

    public List<Car> ListRentedCars()
    {
        // Implementation for listing rented cars
    }

    public string Serialize(DataType dataType)
    {
        // Implementation for serialization
    }

    public void Deserialize(string data, DataType dataType)
    {
        // Implementation for deserialization
    }
}

// Transaction.cs
public class Transaction
{
    public string Id { get; set; }
    public Customer Customer { get; set; }
    public Car Car { get; set; }
    public DateTime RentDate { get; set; }
    public DateTime ReturnDate { get; set; }
    public double TotalPrice { get; set; }

    public double CalculateTotalPrice()
    {
        // Implementation for calculating total price
    }

    public string Serialize(DataType dataType)
    {
        // Implementation for serialization
    }

    public void Deserialize(string data, DataType dataType)
    {
        // Implementation for deserialization
    }
}

// Car.cs
public class Car
{
    public string Id { get; set; }
    public string Make { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }
    public double DailyPrice { get; set; }
    public bool Rented { get; set; }

    public void Rent()
    {
        // Implementation for renting car
    }

    public void Return()
    {
        // Implementation for returning car
    }

    public string Serialize(DataType dataType)
    {
        // Implementation for serialization
    }

    public void Deserialize(string data, DataType dataType)
    {
        // Implementation for deserialization
    }
}
```

## Usage

To use the Car Rental System, create objects of the classes and invoke the respective methods as per your requirements. Below is a sample usage:

```csharp
var carRentalSystem = new CarRentalSystem();
carRentalSystem.RegisterCustomer();
carRentalSystem.RentCar();
carRentalSystem.ReturnCar();
```

Ensure you have the necessary dependencies and configurations to manage exceptions, handle security, authenticate users, and manage data.

Happy coding!