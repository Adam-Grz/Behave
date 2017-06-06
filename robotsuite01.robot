*** Settings ***
Library    Selenium2Library
Suite Setup    Open Browser    ${HOMEPAGE}    ${BROWSER}
Test Setup    Go To    ${HOMEPAGE}
Suite Teardown    Close All Browsers

*** Variables ***
${HOMEPAGE}    https://cakesolutions.github.io/cake-qa-test/#/
${BROWSER}    chrome
${url}    https://cakesolutions.github.io/cake-qa-test/#/
${title}    Cake Soloptions FED Test

*** Test Cases ***
Navigate to page and verify url
    Location Should Be    ${url}

Navigate to page and verify title
    Title Should Be    ${title}
