Welcome to the guide-automator-mobile wiki!

GuideAutomator was proposed by professor Rodrigo Souza and originally implemented by Allan Oliveira as part of his Bachelor's thesis. The project is being developed in the context of aSide, a research group at the Federal University of Bahia specialized in software design and evolution.

Related publications:
* [GuideAutomator: Continuous Delivery of End User Documentation](https://rodrigorgs.github.io/files/icse-nier2017-rodrigo.pdf) -- paper accepted at [ICSE 2017, NIER Track](http://icse2017.gatech.edu/?q=nier) (New Ideas and Emerging Results)
* [GuideAutomator: Automated User Manual Generation with Markdown](https://repositorio.ufba.br/ri/bitstream/ri/20947/1/monografia-allan-versao-final.pdf) -- Allan Oliveira's bachelor thesis
* [GuideAutomator: Automated User Manual Generation with Markdown](https://rodrigorgs.github.io/files/cbsoft2016-tools.pdf) -- paper presented at CBSoft 2016 (Tools Track)

## Instalation
* Python
* * https://www.python.org/downloads/source/
* Python Libraries
* * pytest, IPython.
* Appium Desktop
* * https://github.com/appium/appium-desktop/releases
* Jupyter notebook
* * https://jupyter.org/install
* ADB
* * https://developer.android.com/studio/command-line/

## Getting Started
Description: GuideAutomatorMobile use the code blocks from jupyter notebook to process and generate manual form the app to be documents. You need to connect with your phone using appium in order do generate the document.
**Exemple:**

![Captura de tela de 2019-03-09 20-40-55](https://user-images.githubusercontent.com/8061594/54078797-58512880-42ad-11e9-9f01-a77295ca8d5d.png)

Appium selector: You need to take  the selectors from Appium to use then in you script.

Jupyter notebook with the selectors from Appium.

![Captura de tela de 2019-03-09 20-42-00](https://user-images.githubusercontent.com/8061594/54078806-774fba80-42ad-11e9-9056-ac53ee86f1e2.png)

In the part number one you can see the markdown part created, in the number 2 is a function from GuideAutomatorMobile using the selectors from Appium and the number 3 is the output image process by the GuideAutomator Mobile.

## Commands
Basic commands from GuideAutomator Mobile
* **init()** - Initializes a new session on the target smartphone using Appium.
* **clickById(id)** - Click an element on the screen of the through the 'id' selector..
* **clickByAccessibilityId(accessibilityId)** - Click an element on the screen through the 'accessibilityId' selector.
* **clickByXPath(xpath)** - Click an element on the screen through the 'xpath' selector.
* **sendKeysById(id, text)** - It finds a text field through the 'id' selector and fills it with the value of the 'text' parameter.
* **sendKeysByAccessibilityId(accessibilityId, text)** - Finds a text field through the 'accessibilityId' selector and fills it with the value of the 'text' parameter.
* **getTextById(id)** - Retrieves the text of a label through its 'id' attribute.
* **getTextByAccessibilityId(accessibilityId)** - Retrieves the text of a label through its 'accessibilityId' attribute.
* **getTextByXpath(xpath)** - Swipe the screen to the desired element via its 'xpath' attribute.
* **scrolltoElementById(id)** - Swipe the screen to the desired element via its 'id' attribute.
* **scrolltoElementByAccessibilityId(accessibilityId)** - Swipe the screen to the desired element via its 'accessibilityId' attribute.
* **scrolltoElementByXpath(xpath)** - Swipe the screen to the desired element via its 'xpath' attribute.
* **quit()** - Ends the GuideAutomator session with Appium.

You can find the list with all commands of the GuideAutomator Mobile in the source code in the repository.
