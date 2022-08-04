*** Settings ***
Library          SeleniumLibrary
Library          OperatingSystem

*** Variables ***
${url}              https://opensource-demo.orangehrmlive.com/
${txtUsername}      id = txtUsername
${txtPassword}      id = txtPassword
${btnSubmit}        id = btnLogin
${errField}         id = spanMessage
${validUsername}    admin
${validPassword}    admin123
${invalidUsername}  falsemin
${invalidPassword}  falsepass

*** Keywords ***
Open page
    Open Browser    ${url}    chrome

*** Test Cases ***
Valid Login
    Open page
    Input Text                 ${txtUsername}    ${validUsername}
    Input Text                 ${txtPassword}    ${validPassword}
    Click Button               ${btnSubmit}
    Capture Page Screenshot    EMBED
    Close Browser

Invalid Login
    Open page
    Input Text                ${txtUsername}     ${invalidUsername}
    Input Text                ${txtPassword}     ${invalidPassword}
    Click Button              ${btnSubmit}
    Element Text Should Be    ${errField}        Invalid credentials
    Capture Page Screenshot   EMBED
    Close Browser

Empty Username Login
    Open page
    Click Button                ${btnSubmit}
    Element Text Should Be      ${errField}        Username cannot be empty
    Capture Page Screenshot     EMBED
    Close Browser

Empty Password Login
    Open page
    Input Text                  ${txtUsername}     ${validUsername}
    Click Button                ${btnSubmit}
    Element Text Should Be      ${errField}        Password cannot be empty
    Capture Page Screenshot     EMBED
    Close Browser