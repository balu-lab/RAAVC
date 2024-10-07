# Residential Autonomous Air Ventilation Control (RAAVC)

## Project Overview
The **Residential Autonomous Air Ventilation Control (RAAVC)** project is designed to optimize airflow in residential spaces using custom motorized 3D-printed air vent covers and wall-mounted sensors (temperature, humidity, and occupancy). Paired with Google Nest, the system dynamically adjusts air distribution based on local conditions, aiming to improve efficiency by reducing HVAC runtime, saving energy, and lowering costs. The system will also utilize machine learning to enhance control over time, offering better climate control in homes by directing air where it's needed most.

![CAD Design](./cad_image.png)
![Vent Operation](./vent_action.gif)

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
Inspired by the climate control challenges of a split-level home, the **Residential Autonomous Air Ventilation Control (RAAVC)** system was designed to address the heating and cooling imbalances commonly faced in multi-story living spaces. The system was created to optimize airflow by mechanically controlling air vent openings and closings based on real-time conditions in each room. This targeted airflow management counters issues like air sinkage, uneven temperature distribution, and inefficient HVAC use, ultimately improving comfort and energy efficiency throughout the home.

## Problem and Solution
**Problem:** In split-level and long ranch-style homes, effectively managing temperature across different floors and spaces presents significant challenges. In split-level homes, the basement often remains too cold in summer while the top floor bedrooms can become overheated, leading to discomfort and inefficient HVAC operation. Similarly, in ranch homes, southern spaces (in the northern hemisphere) can become excessively hot while more centralized locations housing the thermostat, such as a living room or foyer, may indicate a satisfied temperature threshold.

**Solution:** The **Residential Autonomous Air Ventilation Control (RAAVC)** system employs custom motorized 3D-printed vent covers and wall-mounted sensors to dynamically regulate airflow based on localized temperature, humidity, and occupancy data. By adjusting vent positions in real-time, the system optimally directs climate-controlled air to where it’s needed most, enhancing overall comfort and energy efficiency while reducing HVAC runtime and costs.


## Learnings
Throughout the development of the **Residential Autonomous Air Ventilation Control (RAAVC)** system, we have gained valuable insights and skills in various areas, including:
- **CAD Assembly and 3D Printing Optimization:** Learning to design and optimize components for efficient 3D printing has been crucial in creating the custom vent covers and sensor housings.
- **Bluetooth and Wi-Fi Signal Processing:** Understanding the intricacies of wireless communication has enabled effective data transfer between devices within the system.
- **Raspberry Pi GPIO Control:** Gaining proficiency in using Raspberry Pi GPIO pins has allowed us to control hardware components seamlessly.
- **Software Development:** Developing the necessary software for data collection, processing, and system control has enhanced our coding and problem-solving skills.
- **Machine Learning for System Optimization:** We are continuing to explore self-improving machine learning models to further optimize airflow management and enhance energy efficiency in HVAC operations.

## Features
The **Residential Autonomous Air Ventilation Control (RAAVC)** system includes several innovative features designed to enhance home climate control:
- **Custom Motorized Vent Covers:** 3D-printed vent covers that can open and close automatically based on real-time data.
- **Wall-Mounted Sensors:** Each room is equipped with sensors that measure temperature, humidity, and occupancy to provide localized environmental data.
- **Real-Time Airflow Regulation:** The system adjusts vent positions dynamically to optimize airflow throughout the home, ensuring comfort in all spaces.
- **Integration with Google Nest:** Seamless compatibility with Google Nest thermostats for efficient HVAC control.
- **Universal Performance Data Visualization Dashboard:** A user-friendly interface for monitoring room-by-room temperatures, tracking system runtime, and calculating potential energy savings.
- **Machine Learning Optimization:** The system continuously learns from data to improve its performance, ensuring optimal airflow management over time.
- **Bluetooth and Wi-Fi Connectivity:** Reliable communication between devices for coordinated system operation and data transfer.

## Installation

To set up the **Residential Autonomous Air Ventilation Control (RAAVC)** system, follow these steps:

1. **Gather Required Components:**
   - Custom motorized 3D-printed vent covers.
   - Wall-mounted sensors for temperature, humidity, and occupancy.
   - Raspberry Pi units for each vent cover and sensor pair.
   - Google Nest thermostat.
   - Required wiring and power supplies.
2. **Install Vent Covers:**
   - Remove existing vent covers and replace them with the custom motorized ones.
   - Ensure each vent cover is properly connected to its respective Raspberry Pi.
3. **Set Up Wall-Mounted Sensors:**
   - Install the sensors in each room at an appropriate height to accurately measure environmental conditions.
   - Connect the sensors to their corresponding Raspberry Pi units.
4. **Connect Raspberry Pi Units:**
   - Power on each Raspberry Pi and connect them to a monitor.
   - Manually input your Wi-Fi username and password on one of the Raspberry Pi units.
5. **Power On All Devices:**
   - After configuring one Raspberry Pi, power on all other devices in the system.
   - The devices will automatically pair over Bluetooth and connect to Wi-Fi.
6. **Google Nest Integration:**
   - Log into the Google account associated with your Google Nest thermostat on the master vent Raspberry Pi.
   - Allow authentication for API access to enable control of the thermostat.
7. **Visualization Dashboard Setup:**
   - Configure the dashboard for performance data visualization, which can be written to Tableau Online or Google Sheets.
   - Additional scripts for programmatic data production will be provided to facilitate this setup.
8. **Testing and Calibration:**
   - Test the system by observing the vent operations and ensuring that the sensors are providing accurate readings.
   - Make any necessary adjustments to optimize performance.

Once the installation is complete, the system will begin to operate autonomously, optimizing airflow based on real-time data inputs.

## How to Use

Using the **Residential Autonomous Air Ventilation Control (RAAVC)** system is designed to be straightforward. Follow these steps to get the most out of your system:
1. **Initial Setup:**
   - Ensure that all components are installed and connected as per the installation instructions.
   - Power on all Raspberry Pi units and ensure they are connected to your Wi-Fi network.
2. **Access the Visualization Dashboard:**
   - Open the designated dashboard for performance data visualization (Tableau Online or Google Sheets) using your preferred web browser.
   - Log in with the provided credentials to access the performance metrics.
3. **Monitor Room Conditions:**
   - Use the dashboard to view real-time data on room temperatures, humidity levels, and occupancy status.
   - Identify rooms that may require additional climate control based on their current conditions.
4. **Adjust Settings as Needed:**
   - If you notice certain rooms are consistently too hot or cold, you can manually override the system settings via the dashboard to adjust vent positions.
   - Use the dashboard to set preferences for specific rooms based on occupancy patterns or personal comfort levels.
5. **Automatic Operation:**
   - Once configured, the system will autonomously adjust vent positions based on real-time data inputs, ensuring optimal airflow and temperature regulation.
   - The system learns and adapts over time, improving its efficiency in managing airflow and minimizing HVAC runtime.
6. **Regular Maintenance:**
   - Periodically check the sensors and vent covers for dust and debris to ensure optimal performance.
   - Update the Raspberry Pi software as necessary to incorporate improvements and new features.

By following these steps, you can effectively utilize the RAAVC system to enhance comfort and efficiency in your home.

## Team and Credits
The **Residential Autonomous Air Ventilation Control (RAAVC)** project is a collaborative effort by a dedicated team of individuals:
- **Griffin McKnight, Graduate Research Assistant:** Conceptualization, Methodology, Formal Analysis, Machine Learning Optimization, Hardware and Software Design and Development.
- **Malachi Swindler, Undergraduate Research Assistant:** Electrical Engineering, Signal Processing, Software Development.
- **Jon Mari McKinley, Undergraduate Research Assistant:** Hardware Production and Assembly, Signal Processing, Electrical Engineering.
- **Issa AlHmoud, Postdoc Lab Manager:** Supervisor, System Deployment Lead.
- **Balakrishna Gokaraju, Primary Investigator:** Conceptualization, Methodology, Funding Acquisition.

## Funding
The RAAVC team would like thank the following agencies for their partial support:
1. The United States Department of Commerce (USDOC), Economic Development Administration Good Jobs Challenge Awardee, STEPs4GROWTH (ED22HDQ3070099)
2. National Centers of Academic Excellence in Cybersecurity Grant (H98230-21-1-0326)
3. National Science Foundation’s – Engineering Research Center (NSF-ERC) Hybrid Autonomous Manufacturing Moving from Evolution to Revolution (HAMMER) (Award No.: 2133630).![image](https://github.com/user-attachments/assets/73b63a5f-37ab-498d-ab28-0087f35c08ff)






