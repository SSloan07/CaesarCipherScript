# Input Validation Flow

The application validates menu options and numeric input before performing an operation. Invalid input is rejected and the corresponding prompt is shown again.

```mermaid
flowchart TD
    start([Receive input]) --> integerCheck{"Is the input an integer?"}
    integerCheck -- "No" --> integerError["Display integer error"]
    integerError --> start
    integerCheck -- "Yes" --> inputType{"What type of input is being validated?"}
    inputType -- "Menu option" --> optionCheck{"Is the option available?"}
    optionCheck -- "No" --> optionError["Display invalid option"]
    optionError --> start
    optionCheck -- "Yes" --> validOption["Accept option"]
    inputType -- "Key" --> positiveCheck{"Is the key greater than zero?"}
    positiveCheck -- "No" --> positiveError["Display positive-key error"]
    positiveError --> start
    positiveCheck -- "Yes" --> validKey["Accept key"]
    validOption --> continue([Continue application])
    validKey --> continue
```

The key validation is strict: `0` and negative integers are rejected. Positive keys greater than the alphabet length are accepted and normalized by the modulo operation inside the cipher core.
