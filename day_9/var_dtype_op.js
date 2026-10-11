///1. Variable & Data types

const customerName = "Vignesh"; // cannot be change
const itemInCart = 3; // cannot be change
let accountBalance = 100.65; //can be change
let coupenApplied = null; //Null
let isPremiumMember = false; //Boolean
let checkoutError; //Undefined 

//object holding structured data
const storeSettings = {
    taxRate: 0.08,
    freeShippingMin: 50.00
}

//arithmetic and assignment operator
const itemPrice = 25.0;
const subtotal = itemPrice * itemInCart;
const tax = subtotal * storeSettings.taxRate;

let totalCost = subtotal + tax;

//assignment operator (discount)
totalCost -= 10;

const qualifiesForFreeShipping = totalCost >= storeSettings.freeShippingMin;

const showSpecialBadge = isPremiumMember || qualifiesForFreeShipping;

accountBalance -= totalCost;
const isBalanceExactlyZero = accountBalance === 0;

console.log("Customer :"+ customerName);
console.log("Final total : $"+totalCost);
console.log("Free Shipping? :",qualifiesForFreeShipping)
console.log("Remaining Balance : $",accountBalance);