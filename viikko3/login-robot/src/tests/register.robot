*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pakkanep  patrik1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    input Credentials  pa  patrik1234
    Output Should Contain  Username has to consist of 3 characters minimum

Register With Enough Long But Invalid Username And Valid Password
    input Credentials  pakkanep1  patrik1234
    Output Should Contain  Username has to consist of 3 characters minimum

Register With Valid Username And Too Short Password
    input Credentials  pakkanep1  pa1234
    Output Should Contain  Password has to be atleast 8 characters long and consist atleast 1 number

Register With Valid Username And Long Enough Password Containing Only Letters
    input Credentials  pakkanep1  paaaaaaaaa
    Output Should Contain  Password has to be atleast 8 characters long and consist atleast 1 number

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command