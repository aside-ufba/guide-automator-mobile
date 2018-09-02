const wdio = require('webdriverio');


const opts = {
    port: 4723,
    desiredCapabilities: {
      platformName: "Android",
      platformVersion: "7.1.1",
      deviceName: "192.168.57.101:5555",
      app: "/home/afonso/Documentos/UFBA/TCC/appium/ApiDemos.apk",
      automationName: "UiAutomator2",
      "noReset": "true",
      "full-reset": "false"
    }
  };
  
  const client = wdio.remote(opts);
  
  client
  .init()
  .click("~App")
  .click("~Alert Dialogs")
  .back()
  .back()
  .end();
