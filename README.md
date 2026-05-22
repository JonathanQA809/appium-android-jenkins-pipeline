# Appium Android Jenkins Pipeline

Mobile automation testing project using Appium, Python, PyTest, Android Emulator, and Jenkins CI/CD concepts.

## Project Overview

This project demonstrates basic Android mobile automation testing using Appium with Python.  
The automated test launches the Android Settings application on an emulator and verifies that the application opens successfully.

The project was created to practice:
- Mobile automation testing
- Android emulator testing
- Appium framework setup
- PyTest automation
- CI/CD workflow concepts using Jenkins

---

## Tools & Technologies

- Python
- Appium
- PyTest
- Selenium WebDriver
- Android Studio Emulator
- Jenkins
- GitHub
- VS Code

---

## Project Structure

```text
appium-android-jenkins-pipeline/
│
├── test/
│   └── test_android_settings.py
│
├── requirements.txt
├── Jenkinsfile
├── README.md
```

---

## Test Scenario

The automated test performs the following steps:

1. Connects to the Android emulator
2. Starts an Appium session
3. Launches the Android Settings application
4. Waits for the application to become active
5. Verifies the Settings app launched successfully
6. Closes the Appium session

---

## Running the Test

### Start the Android Emulator

Open Android Studio and start the emulator.

---

### Start Appium Server

```bash
appium
```

---

### Run the Test

```bash
pytest -v
```

---

## Jenkins CI/CD

This project also includes a basic Jenkins pipeline configuration using a `Jenkinsfile`.

The pipeline:
- Installs project dependencies
- Runs PyTest automation tests

Example Jenkins stages:

```groovy
stage('Install Dependencies')
stage('Run Appium Tests')
```

---

## Skills Demonstrated

- Mobile automation testing
- Android emulator configuration
- Appium automation framework
- Selenium/Appium waits
- Assertions and validations
- PyTest test execution
- CI/CD workflow concepts
- Troubleshooting automation environments

---

## Future Improvements

- Add additional mobile test scenarios
- Integrate reporting
- Add real device testing
- Expand Jenkins pipeline automation
- Add Page Object Model structure