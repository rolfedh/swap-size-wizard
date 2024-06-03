# Swap Size Recommendation Wizard for Red Hat Platforms

This repository contains a command-line "wizard" style application that helps determine the recommended swap size for Red Hat platforms based on user inputs. The script is designed to guide users through a series of prompts to gather relevant information and provide an appropriate swap size recommendation.

## Features

- Interactive command-line interface
- Calculates swap size based on Red Hat's guidelines
- Takes into account:
  - Amount of RAM installed
  - Hibernation requirement
  - Number of logical processors
  - Whether the system is a virtual guest

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/swap-size-wizard.git
    cd swap-size-wizard
    ```

2. Ensure you have Python 3.x installed on your system.

## Usage

1. Run the script:

    ```sh
    python swap_size_wizard.py
    ```

2. Follow the prompts:
    - Enter the amount of RAM installed (in GB).
    - Specify if hibernation is required (yes/no).
    - Enter the number of logical processors.
    - Indicate if this is a virtual guest (yes/no).

3. The script will output the recommended swap size based on your inputs.

## Example

```sh
$ python swap_size_wizard.py

Swap Size Recommendation Wizard for Red Hat Platforms

Enter the amount of RAM installed (in GB): 16
Is hibernation required? (yes/no): no
Enter the number of logical processors: 4
Is this a virtual guest? (yes/no): yes

Recommended swap size: 4 GB.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## Author

- [Your Name](https://github.com/your-username)

## Note

- This is unofficial. Use at your own risk.
- This code and the output it generates is based on my personal interpretation of the information in [Red Hat Solution](https://access.redhat.com/solutions/15244) and does not represent Red Hat. For Red Hat's response on this matter, contact Red Hat support.

---

*IMPORTANT: This solution is based on Red Hat's guidelines for swap space allocation. For specific requirements, please refer to the official Red Hat documentation or consult with Red Hat support.*
