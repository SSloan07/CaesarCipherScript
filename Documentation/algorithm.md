# Caesar Cipher Algorithm

The encryption and decryption functions process the message one character at a time. Supported characters are shifted within the selected alphabet, while spaces, numbers, punctuation, and other unsupported characters are preserved.

```mermaid
flowchart TD
    start([Start]) --> normalize["Convert message to lowercase"]
    normalize --> remaining{"Are there characters remaining?"}
    remaining -- "No" --> result([Return transformed message])
    remaining -- "Yes" --> membership{"Is the character in the selected alphabet?"}
    membership -- "No" --> preserve["Append character unchanged"]
    preserve --> remaining
    membership -- "Yes" --> index["Find character index"]
    index --> shift["Add key for encryption or subtract key for decryption"]
    shift --> wrap["Apply modulo alphabet length"]
    wrap --> append["Append transformed character"]
    append --> remaining
```

For an alphabet of length `N`, the transformed index is calculated as follows:

- Encryption: `(index + key) % N`
- Decryption: `(index - key) % N`

This modular operation makes the shift circular. For example, shifting the last character of an alphabet moves back to its first character.
