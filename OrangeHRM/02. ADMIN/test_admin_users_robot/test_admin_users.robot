*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String

*** Variables ***
${loginUrl}                 https://opensource-demo.orangehrmlive.com/
${usersUrl}                 https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers            
${txtUsername}              id = txtUsername
${txtPassword}              id = txtPassword
${btnSubmit}                id = btnLogin
${validUsername}            admin
${validPassword}            admin123

${txtSrcUsename}            id = searchSystemUser_userName
${cmbSrcUserRole}           id = searchSystemUser_userType
${txtSrcEmpName}            id = searchSystemUser_employeeName_empName
${cmbSrcStatus}             id = searchSystemUser_status
${btnSearch}                id = searchBtn

${btnAdd}                   Add
${btnEdit}                  Edit
${btnSave}                  Save
${btnDelete}                Delete
${btnDeleteOk}              id = dialogDeleteBtn

${cmbFormUserRole}          id = systemUser_userType
${txtFormEmpName}           id = systemUser_employeeName_empName
${txtFomUsername}           id = systemUser_userName
${cmbFormStatus}            id = systemUser_status
${txtFormPassword}          id = systemUser_password
${txtFormPasswordConfirm}   id = systemUser_confirmPassword

${chkUsers}                 name = chkSelectRow[]

${aMenuAdmin}               id = menu_admin_viewAdminModule
${aSubMenuUsermanagement}   id = menu_admin_UserManagement
${aSubMenuUsers}            id = menu_admin_viewSystemUsers


*** Keywords ***
Open page
    Open Browser    ${loginUrl}    chrome

User Login
    Open page
    Input Text      ${txtUsername}    ${validUsername}
    Input Text      ${txtPassword}    ${validPassword}
    Click Button    ${btnSubmit}

Generate Random Username
    ${randUname} =

Users Page
    User Login
    Mouse Over      ${aMenuAdmin}
    Mouse Over      ${aSubMenuUsermanagement}
    Click Link      ${aSubmenuUsers}

*** Test Cases ***
View User Page
    Users Page
    Location Should Be         ${usersUrl}
    Capture Page Screenshot    EMBED
    Close Browser

Search Users Data
    Users Page
    Input Text                    ${txtSrcUsename}    Aaliyah.Haq
    Select From List By Label     ${cmbSrcUserRole}   ESS
    Input Text                    ${txtSrcEmpName}    Aaliyah Haq
    Select From List By Label     ${cmbSrcStatus}     Enabled
    Click Button                  ${btnSearch}
    Sleep                         2
    Capture Page Screenshot       EMBED
    Close Browser

Add Users Data
    Users Page
    ${randUname} =    Generate Random String    7    [LETTERS]
    Click Button                    ${btnAdd}
    Wait Until Page Contains        Add User
    Select From List By Label       ${cmbFormUserRole}            Admin
    Input Text                      ${txtFormEmpName}             Aaliyah Haq
    Input Text                      ${txtFomUsername}             ${randUname}
    Select From List By Label       ${cmbFormStatus}              Disabled
    Input Text                      ${txtFormPassword}            admin123
    Input Text                      ${txtFormPasswordConfirm}     admin123
    Click Button                    ${btnSave}
    Sleep                           2
    Wait Until Page Contains        Successfully Saved
    Capture Page Screenshot         EMBED
    Close Window

Edit Users Data
    Users Page
    Click Link                      Jacqueline W
    Wait Until Page Contains        Edit User
    Click Button                    ${btnEdit}
    Select From List By Label       ${cmbFormStatus}              Disabled
    Click Button                    ${btnSave}
    Sleep                           2
    Wait Until Page Contains        Successfully Updated
    Capture Page Screenshot         EMBED
    Close Window

Delete Users Data
    Users Page
    Select Checkbox                ${chkUsers}
    Click Button                   ${btnDelete}
    Element Should Be Visible      ${btnDeleteOk}
    Click Button                   ${btnDeleteOk}
    Wait Until Page Contains       Successfully Deleted
    Capture Page Screenshot        EMBED
    Close Window