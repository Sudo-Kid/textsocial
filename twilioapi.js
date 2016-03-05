var config = require('./config.js');

cfg.accountSid = config.sid;
cfg.authToken = config.authToken;
cfg.sendingNumber = config.sendingNumber;

var client = require('twilio')(cfg.accountSid, cfg.authToken);

var requiredConfig = [cfg.accountSid, cfg.authToken, cfg.sendingNumber];
var isConfigured = requiredConfig.every(function(configValue) {
  return configValue || false;
});

if (!isConfigured) {
  var errorMessage =
    'TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_NUMBER must be set.';

  throw new Error(errorMessage);
}

sendSms = function(to, message) {
  client.messages.create({
    body: message,
    to: to,
    from: cfg.sendingNumber
  }, function(err, data) {
    if (err) {
      console.error('Could not notify administrator');
      console.error(err);
    } else {
      console.log('Administrator notified');
    }
  });
};

client.messages.list(function(err, data) {
    data.messages.forEach(function(message) {
        console.log(message.body);
    });
});

twilioClient.sendSms(phoneNumber, messageToSend);
