*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  paavo
    Set Password  paavo1234
    Set Password Confirmation  paavo1234
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pa
    Set Password  paavo1234
    Set Password Confirmation  paavo1234
    Click Button  Register
    Register Should Fail with Message  Username has to consist of 3 characters minimum

Register With Valid Username And Invalid Password
    Set Username  pekka
    Set Password  pekka
    Set Password Confirmation  pekka
    Click Button  Register
    Register Should Fail with Message  Password has to be atleast 8 characters long and consist of letters and atleast 1 number

Register With Nonmatching Password And Password Confirmation
    Set Username  pertti
    Set Password  pertti1
    Set Password Confirmation  pertti2
    Click Button  Register
    Register Should Fail with Message  Given passwords do not match

Login After Successful Registration
    Set Username  petteri
    Set Password  petteri1234
    Set Password Confirmation  petteri1234
    Click Button  Register
    Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  petteri
    Set Password  petteri1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  pa
    Set Password  paavo1234
    Set Password Confirmation  paavo1234
    Click Button  Register
    Register Should Fail with Message  Username has to consist of 3 characters minimum
    Click Link  Login
    Login Page Should Be Open
    Set Username  pa
    Set Password  paavo1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  Login

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open