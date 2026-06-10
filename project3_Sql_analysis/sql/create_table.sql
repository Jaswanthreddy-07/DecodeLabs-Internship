CREATE TABLE dataset (
    OrderID TEXT PRIMARY KEY,
    Date DATE,
    CustomerID TEXT,
    Product TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    ShippingAddress TEXT,
    PaymentMethod TEXT,
    OrderStatus TEXT,
    TrackingNumber TEXT,
    ItemsInCart INTEGER,
    CouponCode TEXT,
    ReferralSource TEXT,
    TotalPrice REAL
);
