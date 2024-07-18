# High-Interaction Honeypot

This project is a high-interaction honeypot implemented using Python and Flask. It captures detailed information about attackers, including IP addresses, attack patterns, and potentially malware uploads. The honeypot is designed to mimic real services, attract attackers, and log their activities for analysis.

## Features

- Captures IP addresses and attack patterns.
- Logs HTTP methods and paths visited by attackers.
- Captures headers and POST data.
- Allows file uploads to capture potential malware.
- Logs all activities for further analysis.

## Prerequisites

- Python 3.x
- Flask
- Requests
- Scapy (optional, for advanced packet manipulation)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nasirfaraj671/high-interaction-honeypot.git
   cd high-interaction-honeypot
