# User Workflow Sequence

The following sequence shows the successful path for both encryption and decryption. The selected operation determines which core function receives the message.

```mermaid
sequenceDiagram
    title Caesar cipher user workflow
    participant User
    participant CLI
    participant Validator
    participant Alphabet
    participant CipherEngine

    User->>CLI: Start the application
    CLI-->>User: Display operation menu
    User->>CLI: Select encryption or decryption
    CLI->>Validator: Validate operation option
    Validator-->>CLI: Return valid option
    CLI-->>User: Display language menu
    User->>CLI: Select English or Spanish
    CLI->>Alphabet: Load selected alphabet
    Alphabet-->>CLI: Return alphabet mappings
    CLI-->>User: Request message and key
    User->>CLI: Enter message and positive key
    CLI->>Validator: Validate key
    Validator-->>CLI: Return valid key
    CLI->>CipherEngine: Process message with operation and key
    CipherEngine-->>CLI: Return transformed message
    CLI-->>User: Display final result
```

The decryption workflow uses the same interaction sequence, but applies the inverse shift to recover the original message.
