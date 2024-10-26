# Real-Time OS Performance Dashboard

A web-based dashboard that monitors system performance in real-time, displaying CPU, memory, and disk usage with interactive graphs. Built with Python, Flask, and Chart.js, this project is ideal for visualizing system performance data dynamically and exploring full-stack development.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [License](#license)

## Overview

This project provides a real-time, web-based dashboard for monitoring your computer's performance. It uses Flask to create a lightweight web server, `psutil` to gather system metrics, and Chart.js to display data as dynamic, interactive graphs. Users can toggle between light and dark modes and view updates every 5 seconds.

## Features

- **Real-time system performance monitoring**: Displays CPU, memory, and disk usage with automatic updates.
- **Interactive, animated charts**: Charts update every few seconds, showing historical data.
- **Dark mode toggle**: Easily switch between light and dark themes.
- **Responsive design**: Accessible and visually appealing across all devices.

## Technologies

- **Python**: Used for backend server and data collection
- **Flask**: Serves the web interface and provides data via JSON
- **psutil**: Gathers system performance data (CPU, memory, disk)
- **Chart.js**: Creates interactive, animated charts
- **HTML, CSS, Bootstrap**: Designs the web interface

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/real-time-os-performance-dashboard.git
   cd real-time-os-performance-dashboard
