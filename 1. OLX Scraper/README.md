> [!Note]
> I first tried using `requests`, but OLX uses anti-scraping measures that block access unless a valid cookie header is included. I could have hardcoded the cookie, yet it would eventually expire, which would defeat the purpose of the app. Because of this, I switched to `Playwright`, which lets us launch a browser in headless mode to simulate a real visit and retrieve the data reliably.  
> I was also unable to fetch the description through the initial search results link since it does not provide that field. To get descriptions, we would need to open each listing page individually. This would slow the app down quite a bit and increase the chance of getting blocked unless we are very careful.
## Result:

```bash
(venv) [deba@potato 1. OLX Scraper]$ python scraper.py 
Navigating to https://www.olx.in/items/q-car-cover?isSearchCall=true...
Waiting for page to load and listings to appear...
Listings found. Getting page content.
Searching for listings with attribute data-aut-id='itemBox3'...
Found 40 listings. Extracting data...

Successfully extracted the following data:
+------------------------------------------------------------------------+---------------+
| Title                                                                  | Price         |
+========================================================================+===============+
| Flats/house 2BHK for rental available with covered secured car parking | ₹ 8,500       |
+------------------------------------------------------------------------+---------------+
| 2BHK 896Sq. ft. flat  with covered car parking,  for sale in Eden Lake | ₹ 36,00,000   |
+------------------------------------------------------------------------+---------------+
| Car Cover for Renault Kwid – Perfect Fit  Neodrift  Excel Condition    | ₹ 2,500       |
+------------------------------------------------------------------------+---------------+
| 3 BHK RERA APPROVE 70.90 LAKH WITH COVER CAR PARKING                   | ₹ 70,90,000   |
+------------------------------------------------------------------------+---------------+
| Car seat cover                                                         | ₹ 2,000       |
+------------------------------------------------------------------------+---------------+
| 2 BHK Flat with Covered Car Parking and Store                          | ₹ 68,50,000   |
+------------------------------------------------------------------------+---------------+
| 2 BHK Flat with Store and Covered Car Parking                          | ₹ 70,00,000   |
+------------------------------------------------------------------------+---------------+
| Wagon R Car Cover – Good Condition                                     | ₹ 700         |
+------------------------------------------------------------------------+---------------+
| READY TO MOVE 2BHK FLATS WITH COVERED CAR PARKING & LIFT KOVILAMBAKKAM | ₹ 66,90,000   |
+------------------------------------------------------------------------+---------------+
| 1620 Sq.ft 3 BHK water view flat,covered car parking,Marinedrive Kochi | ₹ 1,15,00,000 |
+------------------------------------------------------------------------+---------------+
| 3bhk MICL With 1 Alloted covered car park                              | ₹ 1,90,00,000 |
+------------------------------------------------------------------------+---------------+
| One covered car parking is available for rent with EV charging point   | ₹ 2,000       |
+------------------------------------------------------------------------+---------------+
| Back water view 3 BHK luxury flat,covered car parking,Marine drive EKM | ₹ 1,15,00,000 |
+------------------------------------------------------------------------+---------------+
| 2 BHK with Covered Car Parking in Luxurious Society with all Amenities | ₹ 52,00,000   |
+------------------------------------------------------------------------+---------------+
| Car Cover for Eon Alto                                                 | ₹ 600         |
+------------------------------------------------------------------------+---------------+
| 3BHK SUPER SPACIOUS VERY BIG FLAT FOR SALE WITH 2 COVERED CAR PARKING  | ₹ 1,99,00,000 |
+------------------------------------------------------------------------+---------------+
| A well maintained Flat including one covered car parking available     | ₹ 48,00,000   |
+------------------------------------------------------------------------+---------------+
| Brembo brake caliper covers all colours available for all cars         | ₹ 699         |
+------------------------------------------------------------------------+---------------+
| Renault Captur car cover                                               | ₹ 1,300       |
+------------------------------------------------------------------------+---------------+
| 1 BHK independent kothi with covered car parking inside                | ₹ 8,000       |
+------------------------------------------------------------------------+---------------+
| 1 BHK WITH COVERED CAR PARKING FOR URGENT SALE                         | ₹ 28,51,000   |
+------------------------------------------------------------------------+---------------+
| 1BHK For rent with cover car parking ,Nere Panvel                      | ₹ 6,000       |
+------------------------------------------------------------------------+---------------+
| New Swift Dzire car cover hle us v ni kita hoya                        | ₹ 500         |
+------------------------------------------------------------------------+---------------+
| 2 bhk semi furnished with covered car parking.                         | ₹ 42,00,000   |
+------------------------------------------------------------------------+---------------+
| 2 Bhk independent builder floor with cover car parking for sale        | ₹ 27,00,000   |
+------------------------------------------------------------------------+---------------+
| Hatchback car universal seat cover                                     | ₹ 2,750       |
+------------------------------------------------------------------------+---------------+
| One room with attached toilet 6500 + covered car parking rent 4500     | ₹ 6,500       |
+------------------------------------------------------------------------+---------------+
| 2 bhk furnished flat in gated society with covered car parking         | ₹ 42,00,000   |
+------------------------------------------------------------------------+---------------+
| Ignis wheel cover 3 no's and ignis car cover                           | ₹ 1,800       |
+------------------------------------------------------------------------+---------------+
| CAR BODY COVER FOR HYUNDAI I10                                         | ₹ 800         |
+------------------------------------------------------------------------+---------------+
| Thar roxx car cover                                                    | ₹ 1,000       |
+------------------------------------------------------------------------+---------------+
| 2BHK ready to move with covered car parking available for sale.        | ₹ 42,52,000   |
+------------------------------------------------------------------------+---------------+
| T.Nagar fully furnished and covered car parking only 35k               | ₹ 35,000      |
+------------------------------------------------------------------------+---------------+
| 2BHK flat with covered car parking sale in Orchard at Godrej Se7en     | ₹ 43,00,000   |
+------------------------------------------------------------------------+---------------+
| Fully furnished 2 bhk flat with store, covered car parking             | ₹ 79,99,999   |
+------------------------------------------------------------------------+---------------+
| Newly build 75 Sq yards home with covered car parking                  | ₹ 35,00,111   |
+------------------------------------------------------------------------+---------------+
| 75 Gaj newly constructed home with covered car parking                 | ₹ 35,00,001   |
+------------------------------------------------------------------------+---------------+
| AFFORDABLE 3BHK FLATS WITH LIFT,CCTV,COVERED CAR PARKING NEAR JJ PARK  | ₹ 77,22,100   |
+------------------------------------------------------------------------+---------------+
| 5 BHK Duplex (with attic ) with covered car parking                    | ₹ 1,55,00,000 |
+------------------------------------------------------------------------+---------------+
| NEW BRAND 3BHK FLATS WITH LIFT AND CCTV WITH COVERED CAR PARKING       | ₹ 76,84,900   |
+------------------------------------------------------------------------+---------------+
```
