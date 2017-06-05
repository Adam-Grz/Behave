var fs = require('fs');
var files = fs.readdirSync('./test/specs');
var SpecReporter = require('/usr/lib/node_modules/jasmine-spec-reporter').SpecReporter;
var DisplayProcessor = require('/usr/lib/node_modules/jasmine-spec-reporter').DisplayProcessor;

function TimeProcessor(configuration) {
}
function getTime() {
    var now = new Date();
    return now.getHours() + ':' +
           now.getMinutes() + ':' +
           now.getSeconds()
}
TimeProcessor.prototype = new DisplayProcessor();
TimeProcessor.prototype.displaySuite = function (suite, log) {
  return getTime() + ' - ' + log;
};
TimeProcessor.prototype.displaySuccessfulSpec = function (spec, log) {
  return getTime() + ' - ' + log;
};
TimeProcessor.prototype.displayFailedSpec = function (spec, log) {
  return getTime() + ' - ' + log;
};
TimeProcessor.prototype.displayPendingSpec = function (spec, log) {
  return getTime() + ' - ' + log;
};

var reporter = new SpecReporter({
    customProcessors: [TimeProcessor]
});

exports.config = {
  framework: 'jasmine2',
    onPrepare: function () {
  jasmine.getEnv().addReporter(reporter);
  },
//  seleniumAddress: 'http://127.0.0.2:4444/wd/hub',
  specs: ['./test/specs/test_*.js'],
  jasmineNodeOpts: {
    showColors: true,
  },
  multiCapabilities: [{
        browserName: 'firefox',
        shardTestFiles: true,
        maxInstances: files.length,
    }]
};
