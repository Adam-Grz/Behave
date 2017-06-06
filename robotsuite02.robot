*** Settings ***
Library    RequestsLibrary

*** Variables ***
${HOMEPAGE}    https://cakesolutions.github.io/cake-qa-test/#/

*** Test Cases ***
Session
    Create Session    CakeQA    ${HOMEPAGE}

Send GET to page and receive 200
    ${resp}    Get Request    CakeQA    /
    Should Be Equal As Strings    ${resp.status_code}    200

Navigate to page and verify header
    ${headers}    Head Request    CakeQA    /
    Should Be Equal As Strings    ${headers.headers['server']}    GitHub.com
