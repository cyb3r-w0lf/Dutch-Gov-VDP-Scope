# Dutch-Government-VDP-Scope
This repo consists of an automated way to extract the In-Scope Targets of the Dutch(Netherland) Government Vulnerability Disclosure Program using a **python** script.<br>

**Requirements**

```
requests
pyexcel_ods3
bs4
```

**Usage Example** <br>
Download the **run.py** file and run the below commmands.
```
pip install -r requirements.txt
python run.py
```

This command will automatically download the **.ods** source file which is provided in the offical Netherland Government website and extract only the domains.


## Reference Links: 
**Program Page** - https://english.ncsc.nl/contact/reporting-a-vulnerability-cvd <br>
**Report Form** - https://english.ncsc.nl/contact/reporting-a-vulnerability-cvd/cvd-report-form <br>
**Domains Source** - https://www.communicatierijk.nl/vakkennis/r/rijkswebsites/verplichte-richtlijnen/websiteregister-rijksoverheid <br>

Good Luck with finding a 🪲! Happy Hunting :sunglasses: !