var page = require('./page')

var mainPage = Object.create(page, {

    loggedUser: {  get: function () { return browser.element('#topbar-user-name'); } },
    sendButton: {  get: function () { return browser.element('#chat-input > div > div.n-chat-input-submit > a'); } },
    msgBox: {  get: function () { return browser.element('#chat-input > div > textarea'); } },
    logoutButton: {  get: function () { return browser.element('body > div.topbar > div.topbar-right > a.topbar-element.topbar-logout'); } },
    resizeInboxPanel: {  get: function () { return browser.element('#inbox-menu > div > div.n-inbox-header > div'); } },
    inboxPanelTitle: {  get: function () { return browser.element('#inboxName'); } },
    firstConv: {  get: function () { return browser.element('#conversations > div > div:nth-child(1) > div.n-list-item-details > div.n-list-item-name'); } } ,
    firstConvMenu: { value: function (index) { return browser.element('#conversations > div > div:nth-child(1) > div.n-list-item-details > div:nth-child(4) > select > option:nth-child('+index+')'); } },
    inboxName: {  value: function (index) { return browser.element('#inbox-menu > div > div.n-data-wrapper.n-data-wrapper-active > div > div:nth-child('+index+')'); } },
    rightPanelName: {  get: function () { return browser.element('#user-info > div > div.n-info-wrapper > div > div > div.n-info-title'); } },
    rightPanelRightArrow: {  get: function () { return browser.element('#user-info > div > div.n-info-controls > button.icon-btn.n-info-control.n-info-control-right.flex-next > i'); } },
    rightPanelLeftArrow: {  get: function () { return browser.element('#user-info > div > div.n-info-controls > button.icon-btn.n-info-control.n-info-control-left.flex-prev > i'); } },

    open: { 
        value: function() {
            page.open.call(this, '/inboxes');
        }
    }
});

module.exports = mainPage