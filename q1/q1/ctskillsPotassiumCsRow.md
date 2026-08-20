# Computational Thinking Exercise: Smart Vending Machine

## Step 1: Identify the Big Problem

The vending machine's overall system is unreliable—it mishandles transactions (wrong change and wrong item selection), fails to manage inventory, and cannot process multiple users efficiently.

## Step 2: Identify Three to Four Sub-Problems

1. Incorrect change calculation
2. No inventory/stock monitoring
3. Input/selection errors
4. Slow processing with multiple users

## Step 3: Computational Thinking Approaches

| Sub-Problem | CT Skill | Example Solution |
|-------------|-----------|------------------|
| Incorrect change calculation | Algorithm Design | Create a step-by-step process to calculate and dispense change. |
| No inventory monitoring | Abstraction | Represent stock using simple variables and alert staff when stock is low. |
| Input errors | Pattern Recognition | Add a confirmation step before dispensing items. |
| Slow processing | Decomposition | Divide transactions into smaller tasks for faster processing. |

## Step 4: Pseudocode

```
BEGIN
    INPUT itemPrice
    INPUT amountInserted

    IF amountInserted < itemPrice THEN
        DISPLAY "Insufficient payment"
    ELSE
        changeDue = amountInserted - itemPrice
        DISPENSE item

        IF changeDue > 0 THEN
            coinValues = [20,10,5,1]

            FOR EACH coin IN coinValues
                WHILE changeDue >= coin
                    DISPENSE coin
                    changeDue = changeDue - coin
                END WHILE
            END FOR
        END IF

        DISPLAY "Transaction complete"
    END IF
END
```

## Reflection

Breaking the vending machine problem into smaller parts made each issue easier to solve. Decomposition, abstraction, pattern recognition, and algorithm design helped transform a large problem into specific and manageable solutions.
