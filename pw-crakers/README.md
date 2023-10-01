# pw-crackers
# hashcrack.py
To use the script:
python -m pip install hashlib
cd /in/to/directory/pw-crackeers
python hashcrack.py

This script only supports cracking MD5 hashes see the hashlib module at https://docs.python.org/3/library/hashlib.html
for adding other hashes to crack
<br />
1.You can practice with the templates privided -or-
2.Create your own MD5 Hash and Dictionary text.

METHOD 1.
Password is Welcome
-Copy the hash in the welcome-md5.txt file and paste it to the hash entry
-Type in the path to file where the welcome.txt is created in this case
it's in the same directory type in welcome.txt
-And viola it worked!

METHOD 2
Create your own md5hash and text
-$echo -n yourpassword | md5sum
-copy the hash for later or save the hash to a text file
-create a text file with how evermany lines of passwords you want as long
as it's not too big so you computer doesn't have a heart attack.
Also it's a simple script it doesn't have memory manipulation
ex:
  $echo -n whaaaaaatuup! | md5sum
  44a1819c9618be3c0001ae0f2bf010e9
  $touch password.txt
  $mousepad password.txt
  -type in whatever you want just include the password
      asdAwR4rw$ <br/>
      war#q$wws  <br/>
      sdwr$we    <br/>
      welcom <br/>
      (#R$HNKSDN<br/>
      SDHL#id<br/>
      S_Di33<br/>
      SD(#*REHFC<br/>
      D*E#RH<br/>
      asdasdu738hr<br/>
      adsfffaueir7<br/>
      3947ryehkaf<br/>
      asd<br/>
      afseerr05u8<br/>
      asdfjaiol3ehu<br/>
      asfiealyl9<br/>
      KEVI<br/>
      EIRHHNC<br/>
      LSJDRE#UR<br/>
      JNCXCSOII<br/>
      OELURJIELKDJ<br/>
      ESCh93<br/>
      erfdksuE<br/>
      SDJIOELDJUE<br/>
      Welcome<br/>

![alt text](https://github.com/dirtybrie/ditched-n-fixed-py3/blob/base/pw-crakers/hashcrack.png?raw=true)
