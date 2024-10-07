# Residential Autonomous Air Ventilation Control (RAAVC)

## Project Overview
The **Residential Autonomous Air Ventilation Control (RAAVC)** project optimizes airflow in residential spaces using custom motorized 3D-printed air vent covers and wall-mounted sensors (temperature, humidity, and occupancy). Paired with Google Nest, the system dynamically adjusts air distribution based on local conditions, aiming to improve efficiency by reducing HVAC runtime, saving energy, and lowering costs. It also utilizes machine learning to enhance control over time, directing air where it’s needed most.


<div style="text-align: center;">
  <img src="/images/cad_design.png" alt="CAD Design Side" style="width: 50%; object-fit: cover;" />
  <br>
  <img src="/images/airvent.gif" alt="Air Vent Operating" style="width: 50%; height: auto; object-fit: cover;" />
</div>


## Table of Contents
- [Overview](#project-overview)
- [Motivation](#motivation)
- [Problem and Solution](#problem-and-solution)
- [Learnings](#learnings)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Team and Credits](#team-and-credits)
- [Funding](#funding)

## Motivation
Inspired by the climate control challenges of split-level and long ranch-style homes, the **RAAVC** system addresses heating and cooling imbalances commonly faced in these living spaces. The system optimizes airflow by mechanically controlling vent openings based on real-time conditions, counteracting air sinkage and temperature imbalances while improving overall comfort and energy efficiency.

## Problem and Solution
**Problem:** Managing temperature effectively across different floors in split-level and long ranch-style homes presents significant challenges. In split-level homes, the basement can be too cold in summer while the top floors become overheated, leading to discomfort and inefficient HVAC operation. Similarly, in ranch homes, southern spaces may become excessively hot while central locations, housing the thermostat, indicate a satisfied temperature threshold.

**Solution:** The **RAAVC** employs custom motorized vent covers and wall-mounted sensors to regulate airflow dynamically based on localized temperature, humidity, and occupancy data. By adjusting vent positions in real-time, the system optimally directs climate-controlled air to where it’s needed most, enhancing comfort and energy efficiency while reducing HVAC runtime and costs.

## Learnings
Throughout the development of the **RAAVC** system, we gained valuable insights and skills in:
- **CAD Assembly and 3D Printing Optimization:** Designing components for efficient 3D printing.
- **Bluetooth and Wi-Fi Signal Processing:** Ensuring effective data transfer between devices.
- **Raspberry Pi GPIO Control:** Seamless control of hardware components.
- **Software Development:** Enhancing coding and problem-solving skills for data collection and processing.
- **Machine Learning for System Optimization:** Exploring self-improving models to optimize airflow management.

## Features
The **RAAVC** system includes several innovative features designed to enhance home climate control:
- **Custom Motorized Vent Covers:** 3D-printed covers that open and close automatically based on real-time data.
- **Wall-Mounted Sensors:** Each room is equipped with sensors measuring temperature, humidity, and occupancy for localized data.
- **Real-Time Airflow Regulation:** Dynamic vent adjustments optimize airflow throughout the home.
- **Google Nest Integration:** Seamless compatibility with Google Nest thermostats for efficient HVAC control.
- **Universal Performance Data Visualization Dashboard:** A user-friendly interface for monitoring temperatures, tracking system runtime, and calculating potential energy savings.
- **Machine Learning Optimization:** Continuous learning from data improves performance for optimal airflow management.
- **Bluetooth and Wi-Fi Connectivity:** Reliable communication between devices for coordinated operation and data transfer.

## Installation
To set up the **RAAVC** system, follow these steps:
1. **Gather Required Components:** Custom vent covers, wall-mounted sensors, Raspberry Pi units, Google Nest thermostat, and necessary wiring.
2. **Install Vent Covers:** Replace existing covers with custom motorized ones, ensuring each is connected to its Raspberry Pi.
3. **Set Up Wall-Mounted Sensors:** Install sensors at appropriate heights for accurate measurement and connect to Raspberry Pi units.
4. **Connect Raspberry Pi Units:** Power on each unit, connect to a monitor, and manually input Wi-Fi credentials on one unit.
5. **Power On All Devices:** After configuring one Raspberry Pi, power on all other devices to auto-pair and connect to Wi-Fi.
6. **Google Nest Integration:** Log into the Google account associated with the Nest thermostat on the master vent Raspberry Pi for API access.
7. **Visualization Dashboard Setup:** Configure the dashboard for performance data visualization, with scripts provided for integration with Tableau Online or Google Sheets.
8. **Testing and Calibration:** Test system operations, ensuring sensors provide accurate readings, and make necessary adjustments.

## How to Use
Using the **RAAVC** system is straightforward:
1. **Initial Setup:** Ensure all components are installed and connected, then power on Raspberry Pi units.
2. **Access the Visualization Dashboard:** Open the designated dashboard in your web browser and log in to access performance metrics.
3. **Monitor Room Conditions:** Use the dashboard to view real-time data on temperatures, humidity, and occupancy status.
4. **Adjust Settings as Needed:** Manually override settings via the dashboard for rooms that are too hot or cold.
5. **Automatic Operation:** The system will autonomously adjust vent positions based on real-time data, learning and adapting over time for optimal performance.
6. **Regular Maintenance:** Periodically check sensors and vent covers for dust and update Raspberry Pi software as necessary.

## Team and Credits
The **RAAVC** project is a collaborative effort by:
- **Griffin McKnight, Graduate Research Assistant:** Conceptualization, Methodology, Formal Analysis, Machine Learning Optimization, Hardware and Software Design and Development.
- **Malachi Swindler, Undergraduate Research Assistant:** Electrical Engineering, Signal Processing, Software Development.
- **Jon Mari McKinley, Undergraduate Research Assistant:** Hardware Production and Assembly, Signal Processing, Electrical Engineering.
- **Issa AlHmoud, Postdoc Lab Manager:** Supervisor, System Deployment Lead.
- **Balakrishna Gokaraju, Primary Investigator:** Conceptualization, Methodology, Funding Acquisition.

## Funding
We thank the following agencies for their support:
1. The United States Department of Commerce (USDOC), Economic Development Administration Good Jobs Challenge Awardee, STEPs4GROWTH (ED22HDQ3070099).
2. National Centers of Academic Excellence in Cybersecurity Grant (H98230-21-1-0326).
3. National Science Foundation’s Engineering Research Center (NSF-ERC) Hybrid Autonomous Manufacturing Moving from Evolution to Revolution (HAMMER) (Award No.: 2133630).
