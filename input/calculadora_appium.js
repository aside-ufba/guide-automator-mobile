const wdio = require('webdriverio');


const opts = {
    port: 4723,
    desiredCapabilities: {
	  "platformName": "Android",
	  "platformVersion": "7.0",
	  "deviceName": "0023048519",
	  "automationName": "UiAutomator2",
	  "appPackage": "com.android.calculator2",
  	  "appActivity": "com.android.calculator2.Calculator",
	  "noReset": "true",
	  "full-reset": "false"
	
	}
};
  
// sleep time expects milliseconds
function sleep (time=1000) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
 
const driver = wdio.remote(opts);

driver.init()		
		.click('//android.widget.LinearLayout[@content-desc="Números e operações básicas"]/android.view.ViewGroup[1]/android.widget.Button[8]')		
		.element("~mais")
		.click()
		.element('//android.widget.LinearLayout[@content-desc="Números e operações básicas"]/android.view.ViewGroup[1]/android.widget.Button[8]')
		.click()
		.element("~igual")
		.click()
		.screenshot().saveScreenshot('./snapshot.png')
		//.screenshot().saveScreenshot('./snapshot.png')
		.end();

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
